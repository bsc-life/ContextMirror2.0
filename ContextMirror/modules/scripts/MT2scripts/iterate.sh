#!/bin/bash

#remove the orthomatching files WITHOUT taxid

for i in tree_results/*/*matching.fasta; do rm $i; done

#gather the files WITH taxid

for f in tree_results/*/*_matching.fasta_TAXID.fasta; do
echo "bash ../ContextMirror/modules/scripts/MT2scripts/align.sh" $f >> my_runs_aln.txt
done

cat my_runs_aln.txt | parallel

