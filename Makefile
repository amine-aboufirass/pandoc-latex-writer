generate_pdf: pandoc_write latex_compile

latex_compile:
	latexmk -lualatex --shell-escape test.tex -jobname=out test.tex

pandoc_write:
	pandoc -F write.py --template template.latex -t plain -o test.tex test.md


