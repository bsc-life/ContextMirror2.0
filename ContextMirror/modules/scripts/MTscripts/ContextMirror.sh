#!/bin/bash

currentdir="$PWD"

db=$1
blastdir=$2
input_file=$3
input_dir="${input_file}"
outdir="output_${input_file//.fasta}/"
refdb=$currentdir"/targetdb/targetdb"
mkdir -p $outdir

outfile="${outdir}fwd_results.tab"
taxids="bacteria_species_no_strains_no_target.txids" 

#FORWARD BLAST

n_aa=$(cat $input_file | grep -v "^>" | tr -d '\n' | wc -m)

if [ "$n_aa" -gt 30 ]; then 
echo " --> {$input_file} is blasted with the blastp algorithm"
$blastdir/blastp -query $input_dir -out $outfile -max_target_seqs 10000 -evalue 1e-5 -num_threads 4 -db $db -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -taxidlist $taxids

else #utilizamos blastp-short para secuencias de menos de 30aa
echo " --> {$input_file} is blasted with the blastp-short algorithm"
$blastdir/blastp  -task blastp-short -query $input_dir -out $outfile -max_target_seqs 10000 -evalue 1e-5 -num_threads 4 -db $db -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -taxidlist $taxids

fi

fwd_uniq="${outdir}fwd_uniq_hits.tab"

#APPLY FILTERS: KEEP ONE SEQUENCE PER TAX_ID ; %ID >= 30% ; QCOVERAGE >= 60% ; LENGTH/QUERY LENGTH >= 0.7 
awk -F"\t" '$2 ~ /^ref/' $outfile | sort -t $'\t' -k1,1 -k3,3 -k5,5nr | awk -F"\t" '!seen[$1, $3]++' | sort -t$'\t' -k1,1 -k3,3 | awk '{-F"\t"; if($5>=30)print$0}' | awk '{-F"\t"; if($7>=60)print$0}' | awk '{-F"\t"; if($15/$9>=0.7)print$0}' > $fwd_uniq 

#DOWNLOAD FILTERED SEQUENCES FROM THE FWD HITS
awk -F"\t" '{print $2}' $fwd_uniq | cut -d "|" -f 2 | while IFS= read -r acc; do $blastdir/blastdbcmd -db $db -entry "$acc" > "${outdir}${acc}.fasta"; done

#RECIRPROCAL BLAST
reciprocaldir="${outdir}reciprocal_blast/"
mkdir -p $reciprocaldir

for f in "${outdir}"*.fasta; do
queryacc="$(cut -d'/' -f2 <<< $f)"
#echo $queryacc
reciprocalfile="${reciprocaldir}rev_results_${queryacc}.tab"
$blastdir/blastp -query $f -db $refdb -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -evalue 10e-5 -max_target_seqs 1000 -num_threads 4 -out $reciprocalfile
done

#KEEP ONLY UNIQ SEQUENCES
rev_uniq="${reciprocaldir}rev_uniq_results.tab"

for r in "${reciprocaldir}"*.tab
do
awk -F"\t" '$2 ~ /^ref/' $r | awk 'FNR <= 1' >> $rev_uniq
done

#ORTHOLOG DETECTION
orthodir="${outdir}orthologue_results/"
mkdir -p $orthodir 

python3 $currentdir/../ContextMirror/modules/scripts/MTscripts/find_orthologues.py $input_dir $fwd_uniq $rev_uniq $orthodir $outdir

#BUILD INDEX
i="${orthodir}orthologues_${input_file}"
bash $currentdir/..//ContextMirror/modules/scripts/MTscripts/build_index.sh $fwd_uniq $i

rm "${outdir}"*.fasta
rm "${reciprocaldir}"rev_results*
