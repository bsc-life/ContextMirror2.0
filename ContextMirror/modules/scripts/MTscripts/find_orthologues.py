#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd
from Bio import SeqIO

input_file=sys.argv[1]#name of the multifasta input file
fwd_uniq_hits=sys.argv[2]#name of the fwd uniq hits file
rev_uniq_hits=sys.argv[3]#name of the rev uniq hits file
orthodir=sys.argv[4]#directory for the orthologue file
outdir=sys.argv[5]#directory with fasta files

forward_results = pd.read_csv(fwd_uniq_hits, sep="\t", header=None)
headers = ['query', 'subject', 'taxid', 'e_value', 'pc_identity','bitscore', 'query_coverage', 'all_subject_seqids', 'qlen', 'slen', 'qstart', 'qend', 'sstart', 'send', 'length', 'nident', 'qseq', 'sseq']

# Assign headers
forward_results.columns = headers

rev_results = pd.read_csv(rev_uniq_hits, sep="\t", header=None)

# Assign headers
rev_results.columns = headers


queries=[]
for record in SeqIO.parse(input_file,"fasta"):
    queries.append(record.format("fasta"))

fwd_BH=[]
querr=[]
for i,j in zip(forward_results['query'],forward_results['subject']):
    if i not in querr:
        querr.append(i)
    fwd_BH.append(j.split("|")[1])

for x,n in zip(querr,range(len(querr))):
    with open(orthodir+"orthologues_"+x+".fasta", "w") as f:
        f.write(queries[n])#first we write the query sequence
        for i in range(len(rev_results)):
            if rev_results.iloc[i]['subject']=="ref|"+x+"|":
                orthologue=rev_results.iloc[i]['query']
                s=open(outdir+orthologue+".fasta","r")
                f.write(s.read().strip("\n")+"\n")
                s.close()

