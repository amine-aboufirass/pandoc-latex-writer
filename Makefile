SHELL=powershell.exe

generate_pdf: pandoc_write latex_compile

latex_compile:
	latexmk --lualatex test.tex

pandoc_write:
	pandoc test.md -t custom_writer.lua --template custom_template.latex -o test.tex

pandoc_native:
	pandoc test.md -t native    

pandoc_json_clip:
	pandoc test.md -t json | clip

compare_files:
	compare-object (get-content test.md) (get-content ref.md)
