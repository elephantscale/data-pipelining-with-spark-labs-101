#!/bin/bash

rm -rf output *.out *.zip
mkdir -p output/docx  output/pdf  output/html output/tmp
cp -r images/   output/html/
cp -r assets/   output/html/

for md in *.md
do
    basename=${md%\.*}

    sed 's/\.md/\.docx/g'  < "$md"  > output/tmp/$md.1.md
    pandoc "output/tmp/$md.1.md" -o  "output/docx/${basename}.docx"

    sed 's/\.md/\.pdf/g'  < "$md"  > output/tmp/$md.1.md
    pandoc "output/tmp/$md.1.md" -o  "output/pdf/${basename}.pdf"


    sed 's/\.md/\.html/g'  < "$md"  > output/tmp/$md.1.md
    pandoc "output/tmp/$md.1.md" -o  "output/html/${basename}.html"
done

rm -rf output/tmp

mv output effective-spark.out
zip -q effective-spark.zip -r effective-spark.out
