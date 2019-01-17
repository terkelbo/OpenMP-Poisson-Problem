#!/bin/bash

ALGO="jacobi gauss"

rm -f convergence.dat
for algo in $ALGO
do
	output=$(./poisson_writefiles 150 $algo test)
	echo "$output" >> convergence.dat
done
