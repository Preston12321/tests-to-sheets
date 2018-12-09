#!/bin/bash

# Runs a series of tests using the run_a_test.sh script

# Author: Libby Shoop
#  (With modifications by Preston Locke)

# Usage:
#          bash ./run_tests.sh 4 kj2l3k2h34l5kh3ljlkhk2gh34 R11:V75
#    will run each problem size set below 4 times using a variety of thread counts

# Note: you can set the number of time you want to run each test
#       by including it on the command line
num_times=$1
spreadsheet_id=$2
spreadsheet_range=$3

file_name=values.txt

rm -f $file_name

# Note: you should set the problem sizes that you want to run-
#        the following are very poor problem sizes
for problem_size in 1048576 2097152 8388608 16777216 33554432
do

  for num_threads in 1 2 4 8 12 16
  do
    bash ./run_a_test.sh $problem_size $num_threads $num_times >> $file_name
    printf "\n" >> $file_name
  done

done

python upload_test.py $file_name $num_times $spreadsheet_id $spreadsheet_range
