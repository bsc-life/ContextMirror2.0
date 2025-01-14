#!/bin/bash

currentdir="$PWD"
for d in tree_results/*/; do
    files=()
    for f in "${d}"*.csv; do
        files+=("$f")  # Add each CSV file path to the array
    done
    # Check if there are two CSV files
    if [ ${#files[@]} -eq 2 ]; then
        echo "python3 ../ContextMirror/modules/scripts/PPscripts/pearson_corr.py" "${files[@]}" "$d" >> "${currentdir}/my_runs_corr.txt"
    fi
done

cat ${currentdir}'/'my_runs_corr.txt | parallel

mv ${currentdir}'/'my_runs_corr.txt ${currentdir}'/my_runs/'
