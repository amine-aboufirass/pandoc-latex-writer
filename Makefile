SHELL=powershell.exe

generate_pdf: pandoc_write latex_compile
test_pandoc: compile_pandoc_test compare_files

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
 
compile_pandoc_test:
	pandoc -t new-style-writer-example.lua -o test.md test.json
