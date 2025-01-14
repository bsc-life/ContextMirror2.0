#!/bin/bash

currentdir="$PWD"

for d in tree_results/*/; do
	for f in "${d}*ALIGNMENT.fasta"; do
		echo "bash ../ContextMirror/modules/scripts/PPscripts/build_tree.sh" $f >> ${currentdir}'/'my_runs_build_tree.txt
	done
done

cat ${currentdir}'/'my_runs_build_tree.txt | parallel

mv ${currentdir}'/'my_runs_build_tree.txt ${currentdir}'/my_runs/'
