currentdir="$PWD"

for t in tree_results/*/; do
echo $t >> ${currentdir}'/all_pairs.txt'
done

python3 ${currentdir}'/../ContextMirror/modules/scripts/Partialscripts/compute_PP_pearson_parallel_updated.py' ${currentdir}'/all_pairs.txt'

#mv ${currentdir}'/all_pairs.txt' ${currentdir}'/my_runs/'
