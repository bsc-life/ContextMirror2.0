import os
import pandas as pd
import sys
from Bio import SeqIO
import subprocess

currentdir=os.getcwd()

def add_taxid():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate0.sh'%(currentdir),shell=True)

def align():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate.sh'%(currentdir),shell=True)

def tree():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate2.sh'%(currentdir),shell=True)

def dm():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate3.sh'%(currentdir),shell=True)

def corr():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate4.sh'%(currentdir),shell=True)
    
def fill_tt():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/PPscripts/iterate5.sh'%(currentdir),shell=True)
