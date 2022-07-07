import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.elements.BulletList):
        text = '\n'.join(pf.stringify(item) for item in elem.content)
        text = text.split('\n')
        text = ''.join('\n    ' + row for row in text)
        text = '\n\\begin{itemize}' + text + '\n\\end{itemize}'

        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.ListItem) and isinstance(elem.parent, pf.BulletList):
        text = r'\item ' + pf.stringify(elem)
        return pf.ListItem(pf.Plain(pf.Str(text)))

    elif isinstance(elem, pf.Header):
        text = f"\\{'sub'*(elem.level-1)}section{{{pf.stringify(elem)}}}"
        return pf.Plain(pf.Str(text))

    elif isinstance(elem, pf.Code):
        # inline code
        text = f"\\mintinline{{text}}{{{pf.stringify(elem)}}}"
        return pf.Code(text)
    
    elif isinstance(elem, pf.CodeBlock):
        language = elem.classes[0]
        caption = "test"
        label = "test"
        code = pf.stringify(elem).split('\n')
        code = [code[0]] + [" " * 8 + f"{line}" for line in code[1:]]
        code = "\n".join(code)
        text = (f"\\begin{{listing}}[H]\n"
        f"    \\begin{{minted}}[gobble=12]{{{language}}}\n"
        f"        {code}\n"
        f"    \\end{{minted}}\n"
        f"\\end{{listing}}\n")

        return pf.Plain(pf.Str(text))

def main(doc=None):
    return pf.run_filter(action, doc = doc)

def debug():
    with open("test.md") as fs:
        markdown = fs.read()

    doc = pf.convert_text(markdown, standalone=True)
    doc.walk(action)

if __name__ == "__main__":
    main()
    #debug()

