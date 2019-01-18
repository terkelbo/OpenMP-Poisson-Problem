#!/bin/bash

#BSUB -q hpcintro
#BSUB -J NumaCC_MFlopfig
#BSUB -n 24
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo NumaCC_MFlopfig.out
#BSUB -eo NumaCC_MFlopfig.err

module load studio


THREADS="1 2 4 8 16"
N="10 20 30 50 100 150 200 250 500 1000 1250 1500 2000 2500 2830"
BINDS="true spread close"
PLACES="cores sockets"

for place in $PLACES
do
	for bind in $BINDS
	do
		rm -f ../data/statfun_ccnuma-$place-$bind.dat
		echo "Making data file containing stats - see data/statfun_ccnuma-$place-$bind.dat"
		for t in $THREADS
			do 
			for rows in $N
				do
				echo "OMP_PROC_BIND=$bind OMP_PLACES=$place OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ../poisson_ccnuma $rows"
				output=$(OMP_PROC_BIND=$bind OMP_PLACES=$place OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ../poisson_ccnuma $rows)
				echo "$t $output $rows" >> ../data/statfun_ccnuma-$place-$bind.dat
			done
		done
	done
done
echo "File is done"

exit 0

