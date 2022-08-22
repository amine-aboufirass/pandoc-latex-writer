generate_pdf: pandoc_write latex_compile
generate_pdf_q: pandoc_write latex_compile_q

latex_compile:
	latexmk -lualatex --shell-escape -jobname=out $(name).tex

latex_compile_q:
	latexmk -lualatex --quiet --shell-escape -jobname=out $(name).tex 

pandoc_write:
	pandoc -F filter.py -F write.py -F write.py --template template.latex -t plain -o $(name).tex $(name).md


