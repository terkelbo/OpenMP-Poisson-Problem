#!/bin/bash

ALGO="jacobi gauss"

rm -f ../data/convergence.dat
for algo in $ALGO
do
	output=$(../poisson_writefiles 150 $algo test)
	echo "$output" >> ../data/convergence.dat
done
