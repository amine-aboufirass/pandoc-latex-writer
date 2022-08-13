import panflute as pf
import os
from pathlib import Path

def action(elem, doc):
    if isinstance(elem, pf.elements.BulletList):
        text = '\n'.join(pf.stringify(item) for item in elem.content)
        text = text.split('\n')
        text = ''.join('\n    ' + row for row in text)
        text = '\n\\begin{itemize}' + text + '\n\\end{itemize}'

        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.elements.OrderedList):
        text = '\n'.join(pf.stringify(item) for item in elem.content)
        text = text.split('\n')
        text = ''.join('\n    ' + row for row in text)
        text = '\n\\begin{enumerate}' + text + '\n\\end{enumerate}'

        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.ListItem) and isinstance(elem.parent, pf.BulletList):
        text = r'\item ' + pf.stringify(elem)
        return pf.ListItem(pf.Plain(pf.Str(text)))

    elif isinstance(elem, pf.ListItem) and isinstance(elem.parent, pf.OrderedList):
        text = r'\item ' + pf.stringify(elem)
        return pf.ListItem(pf.Plain(pf.Str(text)))

    elif isinstance(elem, pf.Header):
        text = (f"\\{'sub'*(elem.level-1)}section{{{pf.stringify(elem)}}}\n"
            f"\\label{{{elem.identifier}}}\n")

        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.Code):
        # inline code
        text = f"\\mintinline{{text}}{{{pf.stringify(elem)}}}"
        return pf.Str(text)
    
    elif isinstance(elem, pf.CodeBlock):
        language = elem.classes[0]
        caption = elem.attributes["caption"]
        label = "test"
        
        if "linenos" in elem.attributes.keys():
            linenos = elem.attributes['linenos']
        else:
            linenos = 'true'

        if "filename" in elem.attributes.keys():
            filename = elem.attributes['filename']
            firstline = elem.attributes['firstline']
            lastline = elem.attributes['lastline']
            gobble = elem.attributes['gobble']

            text = (f"\\begin{{listing}}[H]\n"
            f"    \\inputminted\n"
            f"        [\n"
            f"            breaklines,\n"
            f"            mathescape,\n"
            f"            firstline={{{firstline}}},\n" 
            f"            lastline={{{lastline}}},\n" 
            f"            linenos={{{linenos}}},\n"
            f"            gobble={gobble},\n"
            f"        ]\n"
            f"        {{{language}}}\n"
            f"        {{{filename}}}\n"
            f"    \\caption{{{caption}}}\n"
            f"    \\label{{{elem.identifier}}}\n"
            f"\\end{{listing}}\n")
        
        elif language in ["plantuml", "graphviz"]:
            code = pf.stringify(elem).split('\n')
            code = "\n".join(code)
            filename = elem.identifier.split(":")[-1]
            caption = elem.attributes["caption"]
            
            with open(f"{language}-diagrams/{filename}.txt", 'w') as fs:
                    fs.write(code)

            if language == 'plantuml':
                command = f"plantuml -o ../images {language}-diagrams/{filename}.txt"
            else:
                command = f"dot -Tpng -o images/{filename}.png " + \
                    f"{language}-diagrams/{filename}.txt" 

            os.system(command)
            
            return pf.Plain(pf.Image(
                pf.Str(caption),
                identifier = elem.identifier,
                url = f"images/{filename}.png",
                attributes = {
                    "scale": elem.attributes["scale"]   
                    }
                ))

        else:
            gobble = elem.attributes["gobble"]
            code = pf.stringify(elem).split('\n')
            code = [code[0]] + [" " * 8 + f"{line}" for line in code[1:]]
            code = "\n".join(code)
            text = (f"\\begin{{listing}}[H]\n"
            f"    \\begin{{minted}}[breaklines, mathescape, gobble={gobble}, linenos={{{linenos}}}]{{{language}}}\n"
            f"        {code}\n"
            f"    \\end{{minted}}\n"
            f"    \\caption{{{caption}}}\n"
            f"    \\label{{{elem.identifier}}}\n"
            f"\\end{{listing}}\n")

        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.Div):
        
        # DEFINITION LISTS
        if isinstance(elem.content[0], pf.DefinitionList):           
            if "glossary" in elem.classes:
                text = ""
                for definition_item in elem.content[0].content:
                    term = pf.stringify(definition_item.term)
                    definition = pf.stringify(definition_item.definitions[0])
                    text += (f"\\newglossaryentry{{{term}}}\n{{\n"
                    f"    name={term},\n"
                    f"    description={{{definition}}}\n}}\n\n")
            if "acronyms" in elem.classes:
                text = ""
                for definition_item in elem.content[0].content:
                    term = pf.stringify(definition_item.term)
                    definition = pf.stringify(definition_item.definitions[0])
                    text += (f"\\newacronym\n"
                    f"    {{{term}}}\n"
                    f"    {{{term}}}\n"
                    f"    {{{definition}}}\n"
                    )
        
        # TABLES
        elif isinstance(elem.content[0], pf.Table):
            table = elem.content[0]
            head = table.head
            rows = table.content[0].content
            colnames = [pf.stringify(item)for item in head.content[0].content]
                
            caption = pf.stringify(table.caption)
            text = (
                "\\begin{table}[h]\n"
                f"    \\caption{{{caption}}}\n"
                f"    \\label{{{elem.identifier}}}\n"
                "    \\centering\n"
                "    \\begin{tabular}{"
            )
            
            ## column widths
            for i, (alignment, colwidth) in enumerate(table.colspec):
                # ignore alignment for now
                if colnames[i] in elem.attributes.keys():
                    text += f"|p{{{elem.attributes[colnames[i]]}}}" 
                else:
                    if colwidth=="ColWidthDefault":
                        text += "|c"
                    else:
                        text += f"|p{{\\dimexpr{str(round(colwidth,2))}\\textwidth-2\\tabcolsep}}"
                          
            text += "|}\n        \\hline\n        "
            
            ## header content
            colnames = [f"\\bfseries{{{item}}}" for item in colnames]
            text += " &\n        ".join(colnames)
            text += (
                " \\\\\n"
                "        \\hline\n"
            )

            for row in rows:
                cells = [pf.stringify(item) for item in row.content]
                text += "        " 
                text += " &\n        ".join(cells)
                text += (
                    " \\\\\n"
                    "        \\hline\n"
                )

            text += "    \\end{tabular}\n\\end{table}"
                
        else:
            pass
        
        return pf.Plain(pf.Str(text))
        
       
    elif isinstance(elem, pf.Span):
        if "glossary" in elem.classes:
            return pf.Str(f"\\gls{{{pf.stringify(elem)}}}")

        if "acronyms" in elem.classes:
            return pf.Str(f"\\gls{{{pf.stringify(elem)}}}")

        if "figure" or "table" or "listing" in elem.classes:
            return pf.Str(f"\\ref{{{pf.stringify(elem)}}}")
        
        if "line" in elem.classes:
            return pf.Str(f"\\ref{{{pf.stringify(elem)}}}")
        
        if "section" in elem.classes:
            return pf.Str(f"\\ref{{{pf.stringify(elem)}}})")

    elif isinstance(elem, pf.Image):
        caption = pf.stringify(elem)
        scale = float(elem.attributes["scale"])
        text = (
            f"\\begin{{figure}}[H]\n"
            f"    \\centering\n"
            f"    \\includegraphics[scale={scale}]{{{elem.url}}}\n"
            f"    \\caption{{{caption}}}\n"
            f"    \\label{{{elem.identifier}}}\n"
            f"\\end{{figure}}\n"
            )
        return pf.Str(text)

    elif isinstance(elem, pf.Emph):
        text = f"\\textit{{{pf.stringify(elem)}}}"
        return pf.Str(text)

    elif isinstance(elem, pf.Strong):
        text = f"\\textbf{{{pf.stringify(elem)}}}"
        return pf.Str(text)

def main(doc=None):
    return pf.run_filter(action, doc = doc)

def debug():
    with open("test.md") as fs:
        markdown = fs.read()

    doc = pf.convert_text(markdown, standalone=True, extra_args=['--columns', '72'])
    doc.walk(action)

if __name__ == "__main__":
    main()
    #debug()

