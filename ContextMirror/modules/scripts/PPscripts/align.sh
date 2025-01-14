#!/bin/bash


ortho_matching_file=$1

#mafft --auto --clustalout $ortho_matching_file > "${ortho_matching_file}.aln"

mafft --auto --anysymbol --quiet $ortho_matching_file > "${ortho_matching_file}_ALIGNMENT.fasta" #no --clustalout tag since I need fasta formatted msas

