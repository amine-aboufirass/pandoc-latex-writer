generate_pdf: pandoc_write latex_compile

generate_pdf_bib: pandoc_write_bib latex_compile

latex_compile:
	latexmk -lualatex --shell-escape -jobname=out $(name).tex

pandoc_write_bib:
	pandoc -F write.py -F write.py --template template.latex --metadata bibliography=true -t plain -o $(name).tex $(name).md

pandoc_write:
	pandoc -F write.py -F write.py --template template.latex --metadata bibliography=false -t plain -o $(name).tex $(name).md
