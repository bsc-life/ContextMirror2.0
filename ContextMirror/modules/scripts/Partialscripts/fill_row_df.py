#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import math
import os
import sys
from scipy import stats
import numpy as np
import pingouin as pg
from itertools import product

# Suppress divide-by-zero warnings
np.seterr(divide='ignore', invalid='ignore')


TTmatrix_file="tree_results/tree_tree_matrix.csv"
TTmatrix=pd.read_csv(TTmatrix_file, index_col=0)
PPmatrix_file="tree_results/profile_profile_matrix.csv"
PPmatrix=pd.read_csv(PPmatrix_file,index_col=0)
row_df_file=sys.argv[1]

def partial_corrcoef(protA,protB,protN,PPmatrix):
    rAB=PPmatrix.loc[protA][protB]
    rAN=PPmatrix.loc[protA][protN]
    rBN=PPmatrix.loc[protB][protN]
    if np.isnan(rAB)==False and np.isnan(rAN)==False and np.isnan(rBN)==False: #make sure the pearsoncorrcoef from PPmatrix exists (we need significant correlation values)
        rAB_N = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['r'][0]
        pval = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['p-val'][0]
        return ((protA,protB), protN, rAB_N, pval)

#def partial_correlation_final(protA,protB,protN,PPmatrix):
#    # Clean the protein identifiers by removing "/" or other invalid characters
#    protA = protA.strip().replace('/', '')  # Remove "/" and strip any whitespace
#    protB = protB.strip().replace('/', '')  # Remove "/" and strip any whitespace
#    protN = protN.strip().replace('/', '')  # Remove "/" and strip any whitespace
#    rAB=PPmatrix.loc[protA][protB]
#    rAN=PPmatrix.loc[protA][protN]
#    rBN=PPmatrix.loc[protB][protN]
#    try:
#        if np.isnan(rAB)==False and np.isnan(rAN)==False and np.isnan(rBN)==False: #make sure the pearsoncorrcoef from PPmatrix exists (we need significant correlation values)
#            rAB_N = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['r'][0]
#            print(rAB_N)
#            pval = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['p-val'][0]
#            
#            return ((protA,protB), protN, rAB_N, pval)
#    except:
#        return None    
 
def partial_correlation_final(protA, protB, protN, PPmatrix):
    # Clean the protein identifiers by removing "/" or other invalid characters
    protA = protA.strip().replace('/', '')  # Remove "/" and strip any whitespace
    protB = protB.strip().replace('/', '')  # Remove "/" and strip any whitespace
    protN = protN.strip().replace('/', '')  # Remove "/" and strip any whitespace
    
    # Print the cleaned identifiers to ensure they are correct
    #print(f"Checking: protA={protA}, protB={protB}, protN={protN}")
    
    # Check if the protein identifiers exist in the PPmatrix
    if protA not in PPmatrix.index or protB not in PPmatrix.columns or protN not in PPmatrix.columns:
        #print(f"One or more proteins not found in PPmatrix: {protA}, {protB}, {protN}")
        return None
    
    # Get the Pearson correlation values
    rAB = PPmatrix.loc[protA][protB]
    rAN = PPmatrix.loc[protA][protN]
    rBN = PPmatrix.loc[protB][protN]

    # Print the correlation values to check if they are valid
    #print(f"rAB={rAB}, rAN={rAN}, rBN={rBN}")
    
    try:
        # Validate sample size
        subset_data = PPmatrix.loc[[protA, protB, protN]]
        nx = len(subset_data)
        if nx < 3:
            #print(f"Skipping: Insufficient data for partial correlation involving {protA}, {protB}, {protN}")
            return None
            
        # Ensure that all correlations are valid (not NaN)
        if not (np.isnan(rAB) or np.isnan(rAN) or np.isnan(rBN)):
            # Perform the partial correlation
            #print(f"Calculating partial correlation between {protA} and {protB}, controlling for {protN}")
            #rAB_N = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['r'][0]
            #pval = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN)['p-val'][0]
            rAB_N = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN).iloc[0]['r']
            #print(rAB_N)
            pval = pg.partial_corr(data=PPmatrix, x=protA, y=protB, covar=protN).iloc[0]['p-val']
            #print(f"Partial correlation rAB_N={rAB_N}, p-value={pval}")
            return ((protA, protB), protN, rAB_N, pval)
    except Exception as e:
    #    print(f"Error in partial correlation: {e}")
        return None    
    
    return None

row_df=pd.read_csv(row_df_file,index_col=0)
a=row_df.index[0]
b=list(row_df.columns)

#get identifiers
protA=a[1:-1].split(",")[0][1:-1]
protB=a[1:-1].split(",")[1][2:-1]
protA = protA.strip().replace('/', '')  # Remove "/" and strip any whitespace
protB = protB.strip().replace('/', '')  # Remove "/" and strip any whitespace

#fill the df
for i in b:
    result=partial_correlation_final(protA,protB,i,PPmatrix)
    if result!=None:
        #row_df.at[a,result[1]]=f"{result[2]}, {result[3]}"
        row_df = row_df.astype(str)
        row_df.at[a, result[1]] = f"{result[2]}, {result[3]}"

row_df.to_csv(row_df_file)
