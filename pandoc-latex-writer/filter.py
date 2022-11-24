import panflute as pf
import os
from pathlib import Path
import bib_conversions as bc

def action(elem, doc):
    
    if isinstance(elem, pf.Doc):
        meta = elem.get_metadata()
        generate_bib = meta['bibliography']

        if generate_bib:
            references = meta['references']
            pf.debug("generating bibliography from scratch")
            with open("bibliography.bib", "w", encoding='utf8') as bib_file:
                for reference in references:
                    f = getattr(bc, reference['type'].replace('-', "_"))
                    formatted_text = f(reference)
                    bib_file.write(formatted_text)

  
    elif isinstance(elem, pf.CodeBlock):
        language = elem.classes[0]
        caption = elem.attributes["caption"]
        label = "test"
        
        if language in ["plantuml", "graphviz"]:
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
            
            return pf.Para(pf.Image(
                pf.Str(caption),
                identifier = elem.identifier,
                url = f"images/{filename}.png",
                attributes = {
                    "scale": elem.attributes["scale"]   
                    }
                ))


        return elem


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

