#!/bin/bash

input_file=$1
target_taxid=$2 #taxonomy identifier of the target species that we are studying (the species where the sequences in the input file come from
blastdir=$3
edirectdir=$4
dbdir=$5
currentdir="$PWD/.."

bash $currentdir/ContextMirror/modules/scripts/setupscripts/split_multifasta.sh $input_file
echo " --> Multifasta file splitted."

bash $currentdir/ContextMirror/modules/scripts/setupscripts/create_my_runs.sh ContextMirror.sh $input_file $blastdir $dbdir my_runs.txt

#INTERNET CONEXION NEEDED FOR THIS PART
python $currentdir/ContextMirror/modules/scripts/setupscripts/build_dictionary.py $edirectdir
bash $currentdir/ContextMirror/modules/scripts/setupscripts/get_taxids.sh $target_taxid
echo " --> Taxonomy identifiers retrieved."
#INTERNET CONNECTION NO LONGER NECESSARY

bash $currentdir/ContextMirror/modules/scripts/setupscripts/build_target_db.sh $input_file $target_taxid $blastdir
echo " --> Target databse created."
