#!/usr/bin/env python

import os
import pickle
import sys

edirectdir = sys.argv[1]

def get_name(idd):
    command = "sh %sesearch -db gene -query %s | sh %sefetch -format docsum | %sxtract.Linux -pattern DocumentSummary -element Name"%(edirectdir,idd,edirectdir,edirectdir)
    name=os.popen(command).read().strip()
    return name

def build_dict():
    dictt={}
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if file.endswith("fasta"):
            dictt[file.split(".fasta")[0]]=get_name(file.split(".fasta")[0])
    a_file = open("names.pkl", "wb")
    pickle.dump(dictt, a_file)
    a_file.close()

build_dict()

print(" --> Dictionary created.")


