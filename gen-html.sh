#!/bin/bash

## convert ipynb --> html

me=$(basename $0)

echo "    $me : converting ipynb files --> html"
input_files=$(find . -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" )
for input_file in $input_files
do
    output_file="${input_file%\.*}.html"
    # only convert newer files
    if [ "$input_file" -nt "$output_file" ] ; then
        #echo "$input_file --> $output_file"
        jupyter nbconvert --log-level WARN "${input_file}" --to html
        # convert all md links to html links
        sed 's/\.ipynb/\.html/g'  < "$output_file"  > a.html
        mv -f a.html  "$output_file"
    fi
done

## convert md files to html
#echo "=============== converting md files --> html=============== "
echo "    $me : converting md files --> html"
input_files=$(find . -type f -name "*.md" | grep -v ".ipynb_checkpoints" )
for input_file in $input_files
do
    output_file="${input_file%\.*}.html"

    # only convert newer files
    if [ "$input_file" -nt "$output_file" ] ; then
        #echo "$input_file --> $output_file"
        pandoc "$input_file" -f markdown -t html -o  "$output_file"
        # convert all md links to html links
        sed 's/\.md/\.html/g' < "$output_file"  | sed 's/\>md\</\>html\</g'  > a.html
        mv -f a.html  "$output_file"
    fi
done

## cleanup orphan html files
#echo "=============== removing orphan htmls =================="
echo "    $me : removing orphan htmls"
html_files=$(find . -type f -name "*.html" | grep -v ".ipynb_checkpoints" )
for html_file in $html_files
do
    src_file1="${html_file%\.*}.md"
    src_file2="${html_file%\.*}.ipynb"

    #echo $src_file1
    #echo $src_file2

    if [ -f "$src_file1" ] || [ -f "$src_file2" ] ; then
         :
    else
        #echo "removing orphan html : $html_file"
        rm -f "$html_file"
    fi
done
