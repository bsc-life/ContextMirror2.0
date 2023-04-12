#!/usr/bin/env python

import Bio
import sys
import dendropy
from numpy import *
from Bio import Phylo
from Bio.Phylo.Consensus import *
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

tree_file1=sys.argv[1]
tree_file2=sys.argv[2]

#Load the consensus tree, get the patristic distance matrix out of it
def get_DM_from_CONSENSUS_TREE(consensus_tree):
    tree = dendropy.Tree.get(path=consensus_tree, schema="newick")
    pdc = tree.phylogenetic_distance_matrix()
    #save the distance matrices because i cannot do it withour idk why
    pdc.as_data_table().write_csv(consensus_tree+'_PATRISTIC_DISTANCES.csv')


get_DM_from_CONSENSUS_TREE(tree_file1)
get_DM_from_CONSENSUS_TREE(tree_file2)
