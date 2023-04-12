#!/bin/bash

#this scripts creates n individual fasta files out of a n-entry multifasta input file

multifasta_file=$1

cat $1 | awk -v RS='' -v FS='[> ]' '{f=($2 ".fasta"); print >> f; close(f)}'
