currentdir="$PWD"

for f in tree_results/*/*_matching.fasta; do
echo "python3 ../ContextMirror/modules/scripts/PPscripts/add_taxid.py" $f >> ${currentdir}'/'my_runs_taxid.txt
done

cat ${currentdir}'/'my_runs_taxid.txt | parallel

mv ${currentdir}'/'my_runs_taxid.txt ${currentdir}'/my_runs/'
