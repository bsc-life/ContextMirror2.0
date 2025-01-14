#!/bin/bash

currentdir="$PWD"

for d in tree_results/*/corr_*; do
echo $d >> "${currentdir}/corr_files.txt"
done

python3 ../ContextMirror/modules/scripts/PPscripts/fill_tree_tree_matrix.py "${currentdir}/tree_results/tree_tree_matrix.csv" "${currentdir}/corr_files.txt"
