#!/bin/bash

common_species_threshold=$1
currentdir="$PWD"

cat all_combinations.txt | awk -F" " '{print "python3 ../ContextMirror/modules/scripts/MTscripts/get_matching_pairs_paralell_step2.py "$0" tree_results/ '$common_species_threshold'"}' > my_runs_pairs.txt

