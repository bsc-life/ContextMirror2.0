#!/bin/bash

#We will build phylogenetic trees from msas and we will bootstrap these trees 1000 times. for this, for speed reasons we will use FastTree instead of ClustalW

msa_file1=$1
msa_file2=$2

#FastTree -fastest -gamma -quiet -boot 1000 -nj $1 > "${1}_CONSENSUS_TREE.tree"
FastTree -fastest -gamma -quiet -boot 1000 -nj "$1" > "${1}_CONSENSUS_TREE.tree" 2>/dev/null

#FastTree -fastest -gamma -quiet -boot 1000 -nj $2 > "${2}_CONSENSUS_TREE.tree"
FastTree -fastest -gamma -quiet -boot 1000 -nj "$2" > "${2}_CONSENSUS_TREE.tree" 2>/dev/null

#this will save a tree file for every msa in the corresponding folder and will end in _CONSENSUS_TREE
