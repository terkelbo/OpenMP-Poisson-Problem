#!/bin/bash

#BSUB -q hpcintro
#BSUB -J statsfun
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo statsfun.out
#BSUB -eo statsfun.err

module load studio


THREADS="1 2 4 8 16"
pixelsize="250 500 750 1000 1250 1500 2000 2500 3000 3500 4000"

rm -f data/statfun.dat

echo "Making data file containing stats - see data/statfun.dat"
for t in $THREADS
	do 
	for rows in $pixelsize
		do
		output=$(OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,50 ./mandelbrot $rows)
		echo "$t $output $rows" >> data/statfun.dat
	done
done									

echo "File is done"
									
exit 0
