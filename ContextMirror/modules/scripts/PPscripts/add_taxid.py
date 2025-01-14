import os
import dendropy
import sys
import pandas as pd
from scipy import stats
import numpy as np
import csv
from Bio import SeqIO

orthomatching_file1=sys.argv[1]
id=orthomatching_file1.split("/")[2].split('orthologues_')[1].split('_matching.fasta')[0]

#Get the tax id for each ncbi id (i already have them in the taxonomy index file) into a dictionary
def get_tax_dic(taxindex_file):
    with open(taxindex_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        taxindex = {rows[0]:rows[1] for rows in reader}
    return taxindex

#Write the NCBI ID followed by the _taxid
def add_taxid(ortho_matching_file,taxindex):
    with open(ortho_matching_file, "r") as handle, open(ortho_matching_file+"_TAXID.fasta", "w") as out_handle:
        for record in SeqIO.parse(handle, "fasta"):
            identifier = record.id
            taxonomy_id = taxindex.get(identifier, "")
            new_identifier = identifier + '_' + taxonomy_id
            record.id = new_identifier
            record.name = ""
            record.description = ""
            SeqIO.write(record, out_handle, "fasta")
            
            
#add_taxid(orthomatching_file1,get_tax_dic('output_'+id.split('.fasta')[0]+'/orthologue_results/orthologues_'+id+'_tax.index'))
add_taxid(orthomatching_file1,get_tax_dic('output_'+id+'/orthologue_results/orthologues_'+id+'_tax.index'))
