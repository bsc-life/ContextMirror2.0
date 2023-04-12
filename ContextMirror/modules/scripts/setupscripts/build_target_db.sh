#!/bin/bash
#SBATCH -o /gpfs/scratch/bsc08/bsc08092/debug/output_%A.txt
#SBATCH -e /gpfs/scratch/bsc08/bsc08092/debug/errors_%A.txt
#SBATCH -J down
#SBATCH --qos=debug
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=48
#SBATCH --constraint=highmem

export PATH=$PATH:$PWD

#keep virtual memory unlimited to perform the blast search
export BLASTDB_LMDB_MAP_SIZE=100000000
ulimit -s unlimited

proteome=$1
taxid=$2
blastdir=$3
title="targetdb"

$blastdir/makeblastdb -in $proteome -dbtype prot -parse_seqids -input_type fasta -taxid $taxid -title $title -out $title/$title -max_file_sz "4GB" -blastdb_version 5
