#!/usr/bin/env python
# coding: utf-8
'''
import os
import Bio
import sys
import numpy as np
from numpy import *
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo.Consensus import *
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

ortho_file1=sys.argv[1]
ortho_file2=sys.argv[2]
treedir=sys.argv[3]
threshold=int(sys.argv[4])

def get_matching_tax(taxindex1,taxindex2):#arguments= tax index files
    seqs1=[]
    seqs2=[]
    d1={line.split("\t")[0] : line.split("\t")[1].strip("\n") for line in open(taxindex1)} #get tax index information into a dictionary
    d2={line.split("\t")[0] : line.split("\t")[1].strip("\n") for line in open(taxindex2)}
    d1set=set(d1.values())
    d2set=set(d2.values())
    common_values=d1set&d2set #find the intersection (matching values) between both dictionaries --> matching tax ids (speceies)
    for i in common_values: #for every common value
        seqs1.append(list(d1.keys())[list(d1.values()).index(i)]) #retrieve the sequence acc in dict1 for the shared species
        seqs2.append(list(d2.keys())[list(d2.values()).index(i)]) #retrieve the sequence acc in dict2 for the shared species
    return seqs1, seqs2


def redo_orthologues(input_file,coinciding_taxindex,treedir):
    recs=[]
    for rec in SeqIO.parse(open(input_file),"fasta"):
        if rec.id in coinciding_taxindex:
            recs.append(rec)
    return SeqIO.write(recs, treedir+"orthologues_"+input_file.split("/")[-1].split("orthologues_")[-1]+"_matching.fasta", "fasta")


def create_dir(file1,file2,threshold):
    index1=file1+"_tax.index"
    index2=file2+"_tax.index"
    if len(get_matching_tax(index1,index2)[0])==len(get_matching_tax(index1,index2)[1])>=threshold:
        subdirectory=(treedir+file1.split("/")[-1].split("orthologues_")[-1].split(".fasta")[0]+"_vs_"+file2.split("/")[-1].split("orthologues_")[-1].split(".fasta")[0]+"/")
        os.makedirs(subdirectory, exist_ok=True)
        ortho1=redo_orthologues(file1,get_matching_tax(index1,index2)[0],subdirectory)
        ortho2=redo_orthologues(file2,get_matching_tax(index1,index2)[1],subdirectory)
        return ortho1, ortho2

create_dir(ortho_file1,ortho_file2,threshold)
'''
import os
import sys
import subprocess
from Bio import SeqIO

ortho_file1 = sys.argv[1]
ortho_file2 = sys.argv[2]
treedir = sys.argv[3]
threshold = int(sys.argv[4])

def get_matching_tax(taxindex1, taxindex2):
    seqs1 = []
    seqs2 = []
    d1 = {line.split("\t")[0]: line.split("\t")[1].strip("\n") for line in open(taxindex1)} 
    d2 = {line.split("\t")[0]: line.split("\t")[1].strip("\n") for line in open(taxindex2)}
    d1set = set(d1.values())
    d2set = set(d2.values())
    common_values = d1set & d2set 
    for i in common_values:
        seqs1.append(list(d1.keys())[list(d1.values()).index(i)]) 
        seqs2.append(list(d2.keys())[list(d2.values()).index(i)]) 
    return seqs1, seqs2


def redo_orthologues(input_file, coinciding_taxindex, treedir):
    recs = []
    for rec in SeqIO.parse(open(input_file), "fasta"):
        if rec.id in coinciding_taxindex:
            recs.append(rec)
    return SeqIO.write(recs, treedir+"orthologues_"+input_file.split("/")[-1].split("orthologues_")[-1]+"_matching.fasta", "fasta")


def create_dir(file1, file2, threshold):
    index1 = file1 + "_tax.index"
    index2 = file2 + "_tax.index"
    if len(get_matching_tax(index1, index2)[0]) == len(get_matching_tax(index1, index2)[1]) >= threshold:
        subdirectory = (treedir + file1.split("/")[-1].split("orthologues_")[-1].split(".fasta")[0] + "_vs_" + file2.split("/")[-1].split("orthologues_")[-1].split(".fasta")[0] + "/")
        os.makedirs(subdirectory, exist_ok=True)
        ortho1 = redo_orthologues(file1, get_matching_tax(index1, index2)[0], subdirectory)
        ortho2 = redo_orthologues(file2, get_matching_tax(index1, index2)[1], subdirectory)
        
        # Example of running clustalw using subprocess
        # You can replace this part with whatever other external tools you are running
        # subprocess.run(["clustalw", "-infile=" + subdirectory + "orthologues_" + file1.split("/")[-1]], check=True)

        return ortho1, ortho2


# Call create_dir to execute your logic
create_dir(ortho_file1, ortho_file2, threshold)

