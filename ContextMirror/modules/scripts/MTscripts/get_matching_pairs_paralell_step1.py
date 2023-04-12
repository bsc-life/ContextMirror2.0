#!/usr/bin/env python
# coding: utf-8
import os
import Bio
import sys
import numpy as np
import pandas as pd
from itertools import combinations

#we will create the tree_tree_matrix with the ortho_file and the tree_results directory
ortho_file=sys.argv[1]
treedir=sys.argv[2]

with open(ortho_file, "r") as f:
    m=[]
    c=[]
    for line in f:
        m.append(line.strip("\n"))
        c.append(line.strip("\n").split("/")[-1].split("orthologues_")[-1].split(".fasta")[0])
        
all_combinations=list(combinations(m, 2))
with open("all_combinations.txt", 'w') as fp:
   fp.write('\n'.join('{} {}'.format(x[0],x[1]) for x in all_combinations))

all_combinations2=list(combinations(c,2))
cnames=all_combinations2
cnames2=[]
for i in cnames:
    if i[0] not in cnames2:
        cnames2.append(i[0])
    if i[1] not in cnames2:
        cnames2.append(i[1])

df = pd.DataFrame(columns=cnames2, index=cnames2)
df.to_csv(treedir+"tree_tree_matrix.csv")
