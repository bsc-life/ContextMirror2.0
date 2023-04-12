#!/bin/bash/

#this script takes 3 arguments (name of the program, input file (multifasta) and name of the output file (my_runs.txt) and creates a file compatible with greasy

program=$1
multifasta_file=$2
blastdir=$3
dbdir=$4
output_file=$5
currentdir="$PWD"

len=$(cat $2 | grep "^>" | wc -l)

yes 'bash '${currentdir}'/../ContextMirror/modules/scripts/MTscripts/'$program $dbdir $blastdir 2>/dev/null | head -n $len > lines.txt

yes .fasta 2>/dev/null | head -n $len > fas.txt

cat $2 | grep "^>" | awk -F" " '{print $1}' | cut -c 2- > acc.txt

paste acc.txt fas.txt | tr -d "\t"  > sequences.txt

paste lines.txt sequences.txt | tr "\t" " " > $output_file

rm lines.txt fas.txt sequences.txt acc.txt

