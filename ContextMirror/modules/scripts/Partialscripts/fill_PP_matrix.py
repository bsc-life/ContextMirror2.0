#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import math
import os
import sys
from scipy import stats
import numpy as np
import pickle


matrix_file="tree_results/tree_tree_matrix.csv"
matrix=pd.read_csv(matrix_file,index_col=0)
PPmatrix=pd.DataFrame().reindex_like(matrix)

#this shouldnt be done here, but in the previous step (compute_PP_pearson_parallel_updtaed.py), but because I dont want to wait, I will just flter out here
non_nan_cells=[]
for c in matrix.columns:
    a=matrix[c].to_dict()
    for i in a:
        if np.isnan(a[i])==False:
            non_nan_cells.append(tuple((c,i)))  

# assign directory
directory = './'
list_coev_prof_corr=[]

def merge_pkl(file):
    with open(file, "rb") as f:
        a=pickle.load(f)
    return a

# iterate over files in that directory
for filename in os.scandir(directory):
    if filename.name.endswith("pearson.pkl"):
        #print(filename.name)
        for i in merge_pkl(filename):
            list_coev_prof_corr.append(i)            
            
for l in list_coev_prof_corr:
    if (l[0],l[3]) in non_nan_cells or (l[3],l[0]) in non_nan_cells:
#        if float(l[2])<0.00001:
#no pvalue filtereing in this step because since we are using the controlled input, the pvalues are too high
         PPmatrix.at[l[0],l[3]]=l[1]#asigno los valores
#        PPmatrix.at[l[3],l[0]]=l[1]
#solo asigno valores a las parejas que: 1) están correlacionadas en la primera matriz, tienen un pvalue < 10-5 


PPmatrix.to_csv("tree_results/profile_profile_matrix.csv")
