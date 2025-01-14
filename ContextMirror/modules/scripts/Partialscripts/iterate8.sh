#!/bin/bash

currentdir="$PWD"

#create subdirs with 10000 csv files in each
n=0
for f in $(find df -maxdepth 1 -type f); do
    d="df/subdir_$((n++ / 10000))"
    mkdir -p "$d"
    mv -- "$f" "$d"
done

        
for i in df/subdir*; do
echo "bash ../ContextMirror/modules/scripts/Partialscripts/stack_subdir.sh" $i >> ${currentdir}'/'my_runs_subdir.txt
done

cat ${currentdir}'/'my_runs_subdir.txt | parallel

mv ${currentdir}'/'my_runs_subdir.txt ${currentdir}'/my_runs/'
