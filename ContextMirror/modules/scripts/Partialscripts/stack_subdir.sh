#!/bin/bash

dir=$1
subdir=$(basename $dir)

csvstack $dir/*_dataframe.csv > df/out_$subdir.csv

csvstack df/out_subdir* > df/partial_correlation_matrix_merged.csv
