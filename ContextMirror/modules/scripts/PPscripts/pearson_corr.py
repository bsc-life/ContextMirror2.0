#!/usr/bin/env python

import sys
import numpy as np
from numpy import *
import pandas as pd
from scipy import stats # For in-built method to get PCC

dm_file1=sys.argv[1]
dm_file2=sys.argv[2]
orthomatching_dir=sys.argv[3]

#define the correlation function (it's trickier than before)
def updated_corr(dm1file,dm2file):
    #read the DMs
    dm1=pd.read_csv(dm1file,index_col=0)
    dm2=pd.read_csv(dm2file,index_col=0)
    #get the dm to a upper triangular dm
    new_dm1=pd.DataFrame(np.triu(dm1),columns=dm1.columns)
    new_dm1.index=dm1.index

    new_dm2=pd.DataFrame(np.triu(dm2),columns=dm2.columns)
    new_dm2.index=dm2.index
    #store distances of every distance matrix into a list of tuples
    distances_dm1 = []
    for i in range(len(new_dm1.columns)):
        for j in range(i+1, len(new_dm1.columns)):
            distances_dm1.append((new_dm1.columns[i].split(" ")[2], new_dm1.columns[j].split(" ")[2], new_dm1.iloc[i,j]))

    distances_dm2 = []
    for i in range(len(new_dm2.columns)):
        for j in range(i+1, len(new_dm2.columns)):
            distances_dm2.append((new_dm2.columns[i].split(" ")[2], new_dm2.columns[j].split(" ")[2], new_dm2.iloc[i,j]))
            
    #get this information into a three column dataframe
    distance_dm1=pd.DataFrame(distances_dm1, columns=['protA','protB','distance'])
    distance_dm2=pd.DataFrame(distances_dm2, columns=['protA','protB','distance'])

    #NO NEED TO FIND THE INTERSECTION SINCE THESE ARE ALREADY MATCHING SPECIES (IT IS REDUCED)
    merged = pd.merge(distance_dm1, distance_dm2, on=['protA','protB'], how='inner')

    #get the distances into vectors
    vector1 = merged['distance_x'].tolist()

    vector2 = merged['distance_y'].tolist()
    
    r, pvalue = stats.pearsonr(vector1,vector2)
    
    with open(orthomatching_dir+"corr_coef_"+dm1file.split("/")[-1].split("orthologues_")[-1]+"_vs_"+dm2file.split("/")[-1].split("orthologues_")[-1]+".txt", "w") as o:
        o.write(str(r)+"\n"+str(pvalue))
    
    return r, pvalue


updated_corr(dm_file1,dm_file2)
