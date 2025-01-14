#!/bin/bash

currentdir="$PWD"

#remove the orthomatching files WITHOUT taxid

for i in tree_results/*/*matching.fasta; do rm $i; done

#gather the files WITH taxid

for f in tree_results/*/*_matching.fasta_TAXID.fasta; do
echo "bash ../ContextMirror/modules/scripts/PPscripts/align.sh" $f >> ${currentdir}'/'my_runs_aln.txt
done

cat ${currentdir}'/'my_runs_aln.txt | parallel

mv ${currentdir}'/'my_runs_aln.txt ${currentdir}'/my_runs/'
