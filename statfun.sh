#!/bin/bash

#BSUB -q hpcintro
#BSUB -J MFlopfig
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo MFlopfig.out
#BSUB -eo MFlopfig.err

module load studio


THREADS="1 2 4 8 16"
N="10 20 30 50 100 150 200 250 500 1000 1250 1500 2000 2800"

rm -f data/statfun.dat

echo "Making data file containing stats - see data/statfun.dat"
for t in $THREADS
	do 
	for rows in $N
		do
		echo "OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ./poisson_openmp1 $rows"
		output=$(OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ./poisson_openmp1 $rows)
		echo "$t $output $rows" >> data/statfun.dat
	done
done

echo "File is done"

exit 0

