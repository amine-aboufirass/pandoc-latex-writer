import panflute as pf
import os
from pathlib import Path

if __name__ == "__main__":
    with open("test.bib") as fs:
        markdown = fs.read()

    doc = pf.convert_text(
        markdown, 
        input_format='bibtex',
        standalone=True
    )

    print(doc.metadata.content['references'])
