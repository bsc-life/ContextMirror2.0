#!/bin/bash

#export BLASTDB=$db
#export BLASTDB_LMDB_MAP_SIZE=100000000
#ulimit -s unlimited

currentdir="$PWD"

db=$1
blastdir=$2
input_file=$3
input_dir="${input_file}"
outdir="output_${input_file}/"
refdb="${currentdir}/targetdb/targetdb"
mkdir -p $outdir

outfile="${outdir}fwd_results.tab"
taxids="bacteria_species_no_strains_no_target.txids" 

#FORWARD BLAST

n_aa=$(cat $input_file | grep -v "^>" | tr -d '\n' | wc -m)

if [ "$n_aa" -gt 30 ]; then 
#echo -e "\n{$input_file} is blasted with the blastp algorithm"
$blastdir/blastp -query $input_dir -out $outfile -max_target_seqs 1000 -evalue 1e-5 -db $db -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -taxidlist $taxids

else #utilizamos blastp-short para secuencias de menos de 30aa
#echo -e "\n{$input_file} is blasted with the blastp-short algorithm"
$blastdir/blastp  -task blastp-short -query $input_dir -out $outfile -max_target_seqs 1000 -evalue 1e-5 -db $db -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -taxidlist $taxids

fi

#if the fwd blast output is empty or non existeng
if [ ! -s "$outfile" ]; then
    echo -e "\n$input_file failed\n"  # Print failure message
    #rm -r $outdir
    exit 1  # Exit if no results are found
fi

fwd_uniq="${outdir}fwd_uniq_hits.tab"

#APPLY FILTERS: KEEP ONE SEQUENCE PER TAX_ID ; %ID >= 30% ; QCOVERAGE >= 60% ; LENGTH/QUERY LENGTH >= 0.7 

awk -F"\t" '!seen[$3]++ && $5 >= 30 && $7 >= 60 && $15/$9 >= 0.7' $outfile > $fwd_uniq

#if the fwd unique output is empty or non existeng
if [ ! -s "$fwd_uniq" ]; then
    echo -e "\n$input_file failed\n"  # Print failure message
    #rm -r $outdir
    exit 1  # Exit if no results are found
fi

#DOWNLOAD FILTERED SEQUENCES FROM THE FWD HITS

awk -F"\t" '{print $2}' $fwd_uniq | cut -d "|" -f 2 | while IFS= read -r acc; do
    # Debugging: Print the value of $acc to make sure it's correct
#    echo "Processing accession: $acc" 
    # Now use $acc with blastdbcmd
    blastdbcmd -db $db -entry "$acc" > "${outdir}${acc}.fasta"
#    echo "download ok"
done


#RECIRPROCAL BLAST
reciprocaldir="${outdir}reciprocal_blast/"
mkdir -p $reciprocaldir

for f in "${outdir}"*.fasta; do
queryacc="$(cut -d'/' -f2 <<< $f)"
#echo $queryacc
reciprocalfile="${reciprocaldir}rev_results_${queryacc}.tab"
$blastdir/blastp -query $f -db $refdb -outfmt "6 qseqid sseqid staxid evalue pident bitscore qcovs sallseqid qlen slen qstart qend sstart send length nident qseq sseq" -evalue 10e-5 -max_target_seqs 1000 -out $reciprocalfile
done

#KEEP ONLY UNIQ SEQUENCES
rev_uniq="${reciprocaldir}rev_uniq_results.tab"

for r in "${reciprocaldir}"*.tab
do
awk -F"\t" '$2 ~ /^ref/' $r | awk 'FNR <= 1' >> $rev_uniq
done

awk -F"\t" '{print $1}' "$rev_uniq" | while IFS= read -r acc; do
    blastdbcmd -db "$db" -entry "$acc" > "${outdir}${acc}.fasta"
done

#ORTHOLOG DETECTION
orthodir="${outdir}orthologue_results/"
mkdir -p $orthodir 

python3 $currentdir/../ContextMirror/modules/scripts/MTscripts/find_orthologues.py $input_dir $fwd_uniq $rev_uniq $orthodir $outdir

#BUILD INDEX
i="${orthodir}orthologues_${input_file}"
bash $currentdir/../ContextMirror/modules/scripts/MTscripts/build_index.sh $fwd_uniq $i

mkdir -p ${currentdir}/sequences/
mv $input_file ${currentdir}/sequences/
#rm "${outdir}"*.fasta
#rm "${reciprocaldir}"rev_results*
