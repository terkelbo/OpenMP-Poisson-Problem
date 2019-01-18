#!/bin/bash

#BSUB -q hpcintro
#BSUB -J Scheduletypefig
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo Scheduletypefig.out
#BSUB -eo Scheduletypefig.err

module load studio


THREADS="8"
N="10 20 30 50 100 150 200 250 500 1000 1250 1500 2000 2800"
CHUNKSIZE="8"
SCHEDULETYPE="static dynamic guided"

rm -f ../data/scheduletype.dat

echo "Making data file containing stats - see data/scheduletype.dat"
for type in $SCHEDULETYPE
	do 
	for rows in $N
		do
		echo "Starting with $rows, $type, $CHUNKSIZE and $t threads"
		output=$(OMP_WAIT_POLICY=active OMP_NUM_THREADS=$THREADS OMP_SCHEDULE=$type,$CHUNKSIZE ../poisson_openmp1 $rows)
		echo "$THREADS $type $output" >> ../data/scheduletype.dat
	done
done

echo "File is done"

exit /b 0
