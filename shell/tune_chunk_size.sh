#!/bin/bash

#BSUB -q hpcintro
#BSUB -J Chunksizefig
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo Chunksizefig.out
#BSUB -eo Chunksizefig.err

module load studio


THREADS="8"
N=1000
CHUNKSIZE="1 2 4 8 16 32 64 128 256 512 1024"
SCHEDULETYPE="static dynamic guided"

rm -f ../data/chunksize.dat

echo "Making data file containing stats - see data/chunksize.dat"
for type in $SCHEDULETYPE
	do 
	for chunks in $CHUNKSIZE
		do
		output=$(OMP_WAIT_POLICY=active OMP_NUM_THREADS=$THREADS OMP_SCHEDULE=$type,$chunks ../poisson_openmp1 $N)
		echo "$THREADS $type $chunks $output" >> ../data/chunksize.dat
	done
done

echo "File is done"

exit 0

Ver > nul
