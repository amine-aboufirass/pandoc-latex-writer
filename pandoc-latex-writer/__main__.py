from . import write as w
from . import filter as f

from panflute import *

if __name__=="__main__":
    
    pandoc_args = [
        "--template=template.latex",
        "--metadata=bibliography:true"
    ]

    with open("test.md") as fs:
        doc = convert_text(
            fs.read(),
            standalone=True,
            extra_args=pandoc_args
        )

    actions = [f.action, w.action, w.action]
    
    doc = run_filters(actions, doc=doc)

    result = convert_text(
        doc,
        input_format="panflute",
        output_format="plain",
        standalone=True,
        extra_args= ["--output=test.tex"]
    )
