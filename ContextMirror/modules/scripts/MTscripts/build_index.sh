#!/bin/bash

fwd_uniq_hits=$1
orthologue_file=$2

taxindex_orth="${orthologue_file}_tax.index"

awk -F"\t" '{print $2}' $fwd_uniq_hits | cut -d "|" -f 2 > a | awk -F"\t" '{print $3}' $fwd_uniq_hits > b #retrieve the subject sequence (-f2) and the taxid (-f3)
paste a b > tax.index #paste them to get a file with all of the fwd hits and their taxid

cat $orthologue_file | grep "^>" | cut -d" " -f1 | cut -d">" -f2 > c #filter this file to only keep the protein acc and the taxid of the orthologues that we found

awk 'FNR==NR{a[$1]=$1; next}; $1 in a {print $0;}' c tax.index > $taxindex_orth #this code prints the line of tax_index.txt if there is a match between the column 1 of c and the column 1 of tax_index.txt and stores the output in a file called orthologue_tax_index.txt

rm a b c tax.index
