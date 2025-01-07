#!/bin/bash

mkdir custom_db/
cd custom_db/

echo '''ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.00.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.01.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.02.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.03.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.04.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.05.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.06.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.07.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.08.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.09.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.10.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.11.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.12.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.13.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.14.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.15.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.16.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.17.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.18.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.19.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.20.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.21.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.22.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.23.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.24.tar.gz
ftp://ftp.ncbi.nlm.nih.gov/blast/db/refseq_select_prot.25.tar.gz''' > list.txt

sudo apt-get install aria2

#download files
aria2c -x 16 -j 16 -i list.txt 

#uncompress
parallel 'tar -xzvf {}' ::: *.tar.gz

#check database
cd ../
blastdbcmd -db custom_db/refseq_select_prot -info
