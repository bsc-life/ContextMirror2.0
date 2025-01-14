#!/bin/bash

currentdir="$PWD"

commonthreshold=$1

bash ${currentdir}'/../ContextMirror/modules/scripts/MTscripts/get_ortho_file.sh'

python3 ${currentdir}'/../ContextMirror/modules/scripts/MTscripts/get_matching_pairs_paralell_step1.py' ortho_file.txt tree_results/

bash ${currentdir}'/../ContextMirror/modules/scripts/MTscripts/find_pairs_paralell.sh' $commonthreshold
