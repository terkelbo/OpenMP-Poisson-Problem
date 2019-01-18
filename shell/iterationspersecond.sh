#!/bin/bash

ALGO="jacobi gauss"
N="10 20 30 50 100 150 200 250 500 1000 1250 1500 2000 2500 2830"

rm -f ../data/iterationpersecond.dat
for algo in $ALGO
do
	for rows in $N
	do
		output=$(../poisson_openmp1 $rows $algo)
		echo "$algo $output" >> ../data/iterationspersecond.dat
	done
done
