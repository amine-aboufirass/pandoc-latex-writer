SHELL=powershell.exe

generate_pdf: pandoc_write latex_compile
test_pandoc: compile_pandoc_test compare_files

latex_compile:
	latexmk --lualatex test.tex

pandoc_write:
	pandoc -F write.py --template custom_template.latex -o test.tex test.md
