#!/bin/sh

ALGO=$1
THREADS=$2
N="100 200 300 400 500 600 700 800 900 1000 1200 1400 1700 2000 2300 2600 2800"
N="100 200 300 400"

/bin/rm -rf data/$ALGO.$THREADS.dat

OMP_NUM_THREADS=$THREADS
for m in $N
do
    ./poisson $m $ALGO | grep -v CPU >> data/$ALGO.$THREADS.dat
done
    
exit 0
    
