#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import math
import os
import sys
from scipy import stats
import numpy as np
from itertools import product

#read files
TTmatrix_file="tree_results/tree_tree_matrix.csv"
TTmatrix=pd.read_csv(TTmatrix_file, index_col=0)
PPmatrix_file="tree_results/profile_profile_matrix.csv"
PPmatrix=pd.read_csv(PPmatrix_file,index_col=0)
pair_file="all_pairs.txt"

#create a dataframe (1 row x len(proteome) columns) per each possible pair (df folder previously created)
os.system('mkdir -p df/')

# assign directory
directory = 'tree_results/'
pairs=[]
# iterate over files in that directory
with open(pair_file, "r") as f:
    a=f.read().splitlines()
    for i in a:
        pairs.append((i[13:].split("_vs_")[0],i[13:].split("_vs_")[1]))

        
third_prot=list(PPmatrix.columns)

#create partial correlation matrix dataframe
empty_df=np.zeros((len(pairs),len(third_prot)))
partial_corr_matrix=pd.DataFrame(empty_df,columns=third_prot,index=pairs)
partial_corr_matrix.replace(0, np.nan, inplace=True)



#split dataframe into 1 row dataframes
n=0
m=1
#while m<=len(pairs):
#    partial_corr_matrix[n:m].to_csv("df/pair_"+str((partial_corr_matrix[n:m].index[0][0]))+"_"+str((partial_corr_matrix[n:m].index[0][1]))+"_dataframe.csv")
#    n+=1
#    m+=1 
    
while m <= len(pairs):
    # Extract pair names and replace unsafe characters
    pair_1 = str(partial_corr_matrix[n:m].index[0][0]).replace('/', '_')
    pair_2 = str(partial_corr_matrix[n:m].index[0][1]).replace('/', '_')
    filename = f"df/pair_{pair_1}_{pair_2}_dataframe.csv"
    
    # Save the dataframe
    partial_corr_matrix[n:m].to_csv(filename)
    n += 1
    m += 1

