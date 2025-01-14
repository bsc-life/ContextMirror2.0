#!/bin/bash

mkdir -p my_runs

for d in */orthologue_results/*.fasta #for every orthologue file
do
echo "$d" >> ortho_file.txt #get the name and path and write to a file
done

treedir="tree_results/" #create a directory to store the results of the comparisons

mkdir -p $treedir

