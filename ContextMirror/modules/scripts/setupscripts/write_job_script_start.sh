#!/bin/bash

tracking=$(date +%F)

var=$(cat my_runs.txt | wc -l)

if [ "$var" -gt 750 ]; then # if there are more than 750 tasks (max n1 of tasks allowed in MN4)
    n="$((var / 8))" #number of tasks per file
    
    echo "#!/bin/bash
#SBATCH --job-name my_runs.txt
#SBATCH -o ../debug/output_%A.txt
#SBATCH -e ../debug/errors_%A.txt
#SBATCH --ntasks $n
#SBATCH --cpus-per-task=2
#SBATCH --constraint=highmem
#SBATCH --time=24:00:00
#SBATCH --qos=bsc_ls

#Greasy log file
#######################################################################
export GREASY_LOGFILE=../debug/CM-1_${tracking}.log
#######################################################################
# Run greasy
#######################################################################

module load greasy

greasy my_runs.txt" > job_script_start.cmd

fi
