#!/bin/bash


for d in tree_results/*/; do
	for f in "${d}*.csv"; do
		echo "python3 ../ContextMirror/modules/scripts/MT2scripts/pearson_corr.py" $f $d >> my_runs_corr.txt
	done
done

cat my_runs_corr.txt | parallel
