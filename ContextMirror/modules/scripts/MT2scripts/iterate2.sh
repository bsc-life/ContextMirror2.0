#!/bin/bash

for d in tree_results/*/; do
	for f in "${d}*ALIGNMENT.fasta"; do
		echo "bash ../ContextMirror/modules/scripts/MT2scripts/build_tree.sh" $f >> my_runs_build_tree.txt
	done
done

cat my_runs_build_tree.txt | parallel
