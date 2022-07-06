SHELL=powershell.exe

generate_pdf: pandoc_write latex_compile

latex_compile:
	latexmk -lualatex test.tex -jobname=out test.tex

pandoc_write:
	pandoc -F write.py --template custom_template.latex -t plain -o test.tex test.md


