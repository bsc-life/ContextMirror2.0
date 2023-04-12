#!/bin/bash


for d in tree_results/*/; do
	for f in "${d}*_CONSENSUS_TREE.tree"; do
		echo "python3 ../ContextMirror/modules/scripts/MT2scripts/build_dm.py" $f >> my_runs_dm.txt
	done
done

cat my_runs_dm.txt | parallel
