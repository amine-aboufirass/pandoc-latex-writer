$tex_files = get-childitem -recurse -filter *.bib -path ../
$global:files_of_interest = new-object System.Collections.ArrayList

foreach ($tex_file in $tex_files)
{
    $content = get-content $tex_file | select-string "href"
    if ($content)
    {
        $files_of_interest.add($tex_file)
    }
}
