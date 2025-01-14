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
pair_file=sys.argv[1]
pairs=[]
with open(pair_file, "r") as f:
    a=f.read().splitlines()
    for i in a:
        pairs.append((i[13:].split("_vs_")[0],i[13:].split("_vs_")[1]))

#print(matrix)
#print(pairs)
def coev_prof_corr(tuplee):
    prot1=tuplee[0]
    prot2=tuplee[1]
    matrix=pd.read_csv(matrix_file,index_col=0)
    A=matrix.loc[prot1]# cone sto tengo el coevolutionary profile de NP_414543.1
    B=matrix.loc[prot2]
    #esto lo añado porque creo que va a funcionar, pero podría ser que no (lo he añadido en la nc15)
    c = np.vstack([A,B]) #me guardo los dos vectores (con sus respectivos NaN) en un array
    d = c[:,~np.any(np.isnan(c), axis=0)]#elimino las columnas (de los dos vectores) si en alguno de ellos hay un valor NaN
    #la idea es que así si hay NaN en una familia porteica, aunque en el otro vector sí tenga valor, no lo usaré
    #de esta dorma, como la diagonal está con valres NaN cuando hago la correlación de A contra B estoy excluyendo la correlación entre A con su propio árbol y con el de B y viceversa
    if d.shape[1] >= 2:  # Check if at least two columns remain after filtering
        rAB, p_value = stats.pearsonr(d[0], d[1])
        return (prot1, rAB, p_value, prot2)
    else:
        #print(f"\nInsufficient data for {prot1} and {prot2}. Skipping...")
        return (prot1, None, None, prot2)
    
    #rAB, p_value = stats.pearsonr(d[0], d[1]) #d[0] es la primera fila de la matriz, que es el vector A sin las columnas NaN de A o de B
    #return (prot1,rAB,p_value,prot2)

non_nan_cells=[]
for c in matrix.columns:
    a=matrix[c].to_dict()
    for i in a:
        if np.isnan(a[i])==False:
            non_nan_cells.append(tuple((c,i)))  

list_coev_prof_corr=[]
#for i in pairs:
#    if i in non_nan_cells:
#        print(i)
#            list_coev_prof_corr.append(coev_prof_corr(i))
#        except:
#            pass

for i in non_nan_cells:
    list_coev_prof_corr.append(coev_prof_corr(i))
    
#print(list_coev_prof_corr)
with open(pair_file+"_pearson.pkl", "wb") as f:
    pickle.dump(list_coev_prof_corr,f)
    
    #print(pair_file+"_pearson.pkl")
