#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import numpy as np

matrix_file=sys.argv[1]# tree_results/tree_tree_matrix.csv
corr_files_file=sys.argv[2]

files=[] #list of every corr_coeff file
with open(corr_files_file, "r") as f:
    for line in f:
        files.append(line.strip("\n"))
        
list_pairs=[]
for file in files:
    with open(file, "r") as f:
        q1=file.split("/")[-1].split("corr_coef_")[1].split("_matching")[0].split(".fasta")[0]
        q2=file.split("/")[-1].split("vs_")[1].split("_matching")[0].split(".fasta")[0]
        corr_coeff=f.readline().strip()
        p_value=f.readline().strip()
        list_pairs.append((q1,corr_coeff,p_value,q2))
        
matrix=pd.read_csv(matrix_file,index_col=0)

for l in list_pairs:
    if float(l[2])<0.00001: #only pvaleues < 10e-5
        matrix.at[l[0],l[3]]=float(l[1])
        matrix.at[l[3],l[0]]=float(l[1])
    
matrix.to_csv(matrix_file)
