#!/bin/bash

## cleanup html
#find . -name "*.html" -print0 | xargs -0 rm -f

me=$(basename $0)

curr_dir_name=$(basename `pwd`)
echo "$me : packaging $curr_dir_name ($(pwd))..."


SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

# copy every thing to output dir

OUTPUT_DIR1="output"
OUTPUT_DIR2="effective-spark-lesson"
OUTPUT_DIR3="${OUTPUT_DIR1}/${OUTPUT_DIR2}"
rm -rf $OUTPUT_DIR1; mkdir -p $OUTPUT_DIR3

rsync -a  --exclude OUTPUT_DIR1  --exclude '*.out' --exclude '.*' --exclude '__pycache__' --exclude '*.zip'  .  $OUTPUT_DIR3/

## convert ipynb notebooks into HTML
#echo "=============== converting ipynb files --> html=============== "
echo "    $me : converting ipynb files --> html"
input_files=$(find $OUTPUT_DIR3 -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" )
for input_file in $input_files
do
    output_file="${input_file%\.*}.html"
    # only convert newer files
    if [ "$input_file" -nt "$output_file" ] ; then
        #echo "$input_file --> $output_file"
        jupyter nbconvert --log-level WARN --to html "${input_file}"
        # convert all md links to html links
        sed 's/\.ipynb/\.html/g'  < "$output_file"  > a.html
        mv -f a.html  "$output_file"
    fi
done

## convert md files to html
#echo "=============== converting md files --> html=============== "
echo "    $me : converting md files --> html"
input_files=$(find $OUTPUT_DIR3 -type f -name "*.md" | grep -v ".ipynb_checkpoints" )
for input_file in $input_files
do
    output_file="${input_file%\.*}.html"

    # only convert newer files
    if [ "$input_file" -nt "$output_file" ] ; then
        #echo "$input_file --> $output_file"
        pandoc "$input_file" -f markdown -t html -o  "$output_file"
        # convert all md links to html links
        cat "$output_file"  | sed 's/\.md/\.html/g'  | sed 's/\>md\</\>html\</g'   > a.html
        #cat "$output_file"  | sed 's/\.md/\.html/g'  | sed 's/\>md\</\>html\</g' | sed 's/\.ipynb/\.html/g'  > a.html
        mv -f a.html  "$output_file"
    fi
done


## remove MD files from output
find $OUTPUT_DIR3 -type f -name '*.md' -print0 | xargs -0 rm


# create a zipfile
#echo "=============== creating  the zip file bundle  =================="
echo "    $me : creating  the zip file bundle"
#curr_dir_name=$(basename `pwd`)
rm -f *.zip
#cd .. && rm -rf *.zip &&  zip -q -x '*target/*'  -x '*.DS_Store*'  -x "*.log" -x "*out/*" -x '*.git*'  -x '*zip*'  -x '*metastore_db*' -x '*out' -x '*.ipynb_checkpoints*' -x '*not-using*' -r "${curr_dir_name}.zip"  "$curr_dir_name"    && mv "${curr_dir_name}.zip"   "${curr_dir_name}" &&  cd -

cd $OUTPUT_DIR1; zip -qr "${OUTPUT_DIR2}.zip"  $OUTPUT_DIR2


IFS=$SAVEIFS
