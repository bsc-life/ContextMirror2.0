import os
import pandas as pd
import sys
from Bio import SeqIO
import subprocess

currentdir=os.getcwd()

def tree_tree_matrix(my_runs_file, commonsp_threshold,my_runs_pairs):
    subprocess.call('cat %s | parallel'%(my_runs_file),shell=True)
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MTscripts/ContextMirror-2.sh %s'%(currentdir,commonsp_threshold),shell=True)
    subprocess.call('cat %s | parallel'%(my_runs_pairs),shell=True)
