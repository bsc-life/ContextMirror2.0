#!/usr/bin/env python

import Bio
import sys
import dendropy
from numpy import *
from Bio import Phylo
from Bio.Phylo.Consensus import *
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import pandas as pd
import numpy as np

tree_file1=sys.argv[1]
#tree_file2=sys.argv[2]

#Load the consensus tree, get the patristic distance matrix out of it
def get_DM_from_CONSENSUS_TREE(consensus_tree):
    tree = dendropy.Tree.get(path=consensus_tree, schema="newick")
    pdc = tree.phylogenetic_distance_matrix()
    #pdc.
    datatable=pdc.as_data_table()
    df=pd.DataFrame(datatable._data)
    df=df.round(4)
    distance_matrix=df.to_csv(consensus_tree+'_PATRISTIC_DISTANCES.csv') 
    return distance_matrix

get_DM_from_CONSENSUS_TREE(tree_file1)
#get_DM_from_CONSENSUS_TREE(tree_file2)
