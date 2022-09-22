generate_pdf: pandoc_write latex_compile
generate_pdf_q: pandoc_write latex_compile_q
generate_pdf_bib: pandoc_write_bib latex_compile
generate_pdf_bib_q: pandoc_write_bib latex_compile_q

latex_compile:
	latexmk -lualatex --shell-escape -jobname=out $(name).tex

pandoc_write_bib:
	pandoc -F filter.py -F write.py -F write.py --template template.latex --metadata bibliography=true -t plain -o $(name).tex $(name).md

pandoc_write:
	pandoc -F filter.py -F write.py -F write.py --template template.latex --metadata bibliography=false -t plain -o $(name).tex $(name).md

latex_compile_q:
	latexmk -lualatex --quiet --shell-escape -jobname=out $(name).tex 



