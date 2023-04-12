import os
import pandas as pd
import sys
from Bio import SeqIO
import subprocess

currentdir=os.getcwd()

def add_taxid():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MT2scripts/iterate0.sh'%(currentdir),shell=True)

def align():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MT2scripts/iterate.sh'%(currentdir),shell=True)

def tree():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MT2scripts/iterate2.sh'%(currentdir),shell=True)

def dm():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MT2scripts/iterate3.sh'%(currentdir),shell=True)

def corr():
    subprocess.call('bash %s/../ContextMirror/modules/scripts/MT2scripts/iterate4.sh'%(currentdir),shell=True)
