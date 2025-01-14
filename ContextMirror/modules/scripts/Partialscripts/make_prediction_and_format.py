import pandas as pd
import scipy
import requests
import numpy as np
import pickle
import ast
import sys
from tqdm import tqdm

pMatrix_file=sys.argv[1]
ppMatrix_file=sys.argv[2]
partial_evalue=float(sys.argv[3])
third_prot_correction_threshold=int(sys.argv[4])


def str_to_tuple(string):
    A=string.replace("(","").replace(")","").replace("'","").split(",")[0].strip()
    B=string.replace("(","").replace(")","").replace("'","").split(",")[1].strip()
    C=tuple((A,B))
    return C

#get tha names dictionary
#dic_file="names.pkl"
#with open(dic_file, 'rb') as handle:
#    trans_dic = pickle.load(handle)
    
def score_pairs(partialmatrix, ppmatrix):
    partialmatrix_vectors = {}

    for i in partialmatrix.index:
        row_values = partialmatrix.loc[i].dropna().values
        third_proteins = []

        for value in row_values:
            if isinstance(value, str):
                numeric_value, pvalue = map(float, value.split(','))
                third_proteins.append([partialmatrix.columns[row_values.tolist().index(value)],numeric_value,pvalue])
        partialmatrix_vectors[i] = (third_proteins)

    pairs_and_score_and_count = []

    for i, key in enumerate(partialmatrix_vectors.keys()):
        pair = str_to_tuple(key)

        prot1=pair[0].strip().replace('/', '') 
        prot2=pair[1].strip().replace('/', '') 
        
        value = partialmatrix_vectors[key]
        
        if np.isnan(ppmatrix.at[prot1, prot2]):
            pairs_and_score_and_count.append(
                (prot1, prot2, value, 'no')
            )
        else:
            pairs_and_score_and_count.append(
                (prot1, prot2, value, ppmatrix.at[prot1, prot2])
            )
      
    df = pd.DataFrame(
        pairs_and_score_and_count,
        columns=['interactorA', 'interactorB', 'third_protein_info', 'PPcorrelation']
    )

    return df


def safe_literal_eval(x):
    try:
        return ast.literal_eval(x)
    except ValueError:
        return []


#load matrices

pMatrix=pd.read_csv(pMatrix_file,index_col=0)
ppMatrix=pd.read_csv(ppMatrix_file,index_col=0)

info_df_average_informative=score_pairs(pMatrix,ppMatrix)
info_df_average_informative['third_protein_info'] = info_df_average_informative['third_protein_info'].apply(
    lambda x: x if isinstance(x, list) and len(x) > 0 else []
)

#calculate all the relevant information
filtered_data2 = []
for index, row in info_df_average_informative.iterrows():

    # Convert 'third_protein_info' column from string to list of lists
    #third_protein_info_list = ast.literal_eval(row['third_protein_info'])
    third_protein_info_list = row['third_protein_info']
    # Filter the sublists based on the correlation_threshold and pvalue_threshold
    third_proteins = [x[0] for x in third_protein_info_list]
    partial_corrs = [round(x[1],4) for x in third_protein_info_list]
    
    # Create a new row with the filtered data
    new_row = row.copy()
    new_row['third_proteins'] = third_proteins
    new_row['third_proteins_len'] = len(third_proteins)
    new_row['av_partial'] = float(sum(partial_corrs) / len(partial_corrs)) if len(partial_corrs) != 0 else np.nan
    new_row['interactor_pair'] = '-'.join(sorted([row['interactorA'], row['interactorB']]))
    if new_row['PPcorrelation']!='no':
        new_row['combined_score'] = float(new_row['av_partial']) + float(new_row['PPcorrelation'])
    else:
        new_row['combined_score'] = np.nan
        #Add the new row to the filtered_data list
    filtered_data2.append(new_row)

#add 50-protein threshold correction

def calculate_re_combined_score(row, subset):
    if row['third_proteins_len'] <= int(subset):
        penalty = 0.1 - (0.1 - 0.002) * (row['third_proteins_len'] - 1) / int(int(subset)-1) 
        return row['combined_score'] - penalty
    else:
        return row['combined_score']

info_df_filtered_sumarised = pd.DataFrame(filtered_data2)

info_df_filtered_sumarised['interaction_score'] = info_df_filtered_sumarised.apply(calculate_re_combined_score, axis=1, subset=third_prot_correction_threshold)
final_df=info_df_filtered_sumarised.sort_values(by=['interaction_score'], ascending=False)

final_df.to_csv("info_df.csv")
