#!/bin/bash

currentdir="$PWD"

for i in df/*_dataframe.csv; do
echo "python3 ../ContextMirror/modules/scripts/Partialscripts/fill_row_df.py" $i >> ${currentdir}'/'my_runs_df.txt
done

cat ${currentdir}'/'my_runs_df.txt | parallel

mv ${currentdir}'/'my_runs_df.txt ${currentdir}'/my_runs/'
