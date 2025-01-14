#!/bin/bash

currentdir="$PWD"
for d in tree_results/*/; do
    for f in "$d"*_CONSENSUS_TREE.tree; do
        echo "python3 ../ContextMirror/modules/scripts/PPscripts/build_dm.py" "$f" >> "${currentdir}/my_runs_dm.txt"
    done
done


cat ${currentdir}'/'my_runs_dm.txt | parallel

mv ${currentdir}'/'my_runs_dm.txt ${currentdir}'/my_runs/'
