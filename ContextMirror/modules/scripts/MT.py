import os
import pandas as pd
import sys
from Bio import SeqIO
import subprocess

#currentdir=os.getcwd()
currentdir=os.path.dirname('../')

def tree_tree_matrix(my_runs_file, commonsp_threshold,my_runs_pairs):
    subprocess.call('cat %s | parallel'%(my_runs_file),shell=True)
    subprocess.call('mv %s my_runs/'%(my_runs_file),shell=True)
    subprocess.call('bash %s/ContextMirror/modules/scripts/MTscripts/ContextMirror-2.sh %s'%(currentdir,commonsp_threshold),shell=True)
    #os.system('bash %s'%(my_runs_pairs))
    subprocess.call('cat %s | parallel'%(my_runs_pairs),shell=True)
    #subprocess.call(f'cat {my_runs_pairs} | parallel --jobs 16', shell=True)
    subprocess.call('mv %s my_runs/'%(my_runs_pairs),shell=True)
