import os
import pandas as pd
import sys
import subprocess

currentdir=os.getcwd()


def pp_matrix():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/Partialscripts/iterate6.sh'%(currentdir),shell=True)        
    subprocess.call('python3 %s/../ContextMirror/modules/scripts/Partialscripts/fill_PP_matrix.py'%(currentdir),shell=True)        
        
def partial_matrix():
    subprocess.call('python3 %s/../ContextMirror/modules/scripts/Partialscripts/create_row_df.py'%(currentdir),shell=True)        
    subprocess.call('bash %s/../ContextMirror/modules/scripts/Partialscripts/iterate7.sh'%(currentdir),shell=True)        
    subprocess.call('bash %s/../ContextMirror/modules/scripts/Partialscripts/iterate8.sh'%(currentdir),shell=True)        

def ranked_lists(partial_matrix, pp_matrix, partial_evalue, third_prot_correction_threshold):
    subprocess.call('python3 %s/../ContextMirror/modules/scripts/Partialscripts/make_prediction_and_format.py %s %s %s %s'%(currentdir, partial_matrix, pp_matrix, partial_evalue, third_prot_correction_threshold),shell=True)        
    subprocess.call('mkdir %s/misc'%(currentdir),shell=True)
    subprocess.call('mv  %s/*txt %s/*pkl %s/*txids %s/misc'%(currentdir, currentdir, currentdir, currentdir),shell=True)        
