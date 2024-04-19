#!/bin/bash
# Bash script to zip the whole project in order to make it deriverable
# please make sure zip and texlive are installed

set -e  # exit on error

OUTFILE=../p1_arnaiz_casais.zip
[ -e $OUTFILE ] && rm $OUTFILE  # remove if exists already

# compile the report (and save it to root folder)
echo "Compiling the report..."

latexmk -cd -shell-escape -pdf report/report.tex 

cp report/report.pdf .

cp results/output_test.csv .

# zip it (excluding useless stuff)
echo "Zipping..."
zip -r $OUTFILE . -x zip.sh report/\* \*.git\* img/\* data/\* .venv/\* README.md LICENSE requirements.txt results/\*

# cleanup
echo "Cleaning up..."
rm report.pdf output_test.csv
