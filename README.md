# pandoc-latex-writer

Custom writer for rapid note taking in markdown using panflute.

Dependencies:
- `make`
- `pandoc`
- working Python installation with `panflute` installed

Compile as follows:

`pandoc -F write.py --template custom_template.latex test.md`
