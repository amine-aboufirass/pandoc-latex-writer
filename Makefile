generate_pdf: pandoc_write latex_compile

latex_compile:
	latexmk -lualatex --shell-escape -jobname=out $(name).tex

pandoc_write:
	pandoc -F write.py --template template.latex -t plain -o $(name).tex $(name).md


