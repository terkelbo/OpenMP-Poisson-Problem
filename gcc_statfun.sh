#!/bin/bash

#BSUB -q hpcintro
#BSUB -J MFlopfig_gcc
#BSUB -n 24
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 3GB
#BSUB -W 02:00
#BSUB -N
#BSUB -oo MFlopfig_gcc.out
#BSUB -eo MFlopfig_gcc.err

module load studio

make -f Makefile.gcc clean
make -f Makefile.gcc


THREADS="1 2 4 8 16"
N="10 20 30 50 100 150 200 250 500 1000 1250 1500 2000 2500 2830"
IMPLEMENTATIONS="poisson_ccnuma"
bind="spread"
place="sockets"

for impl in $IMPLEMENTATIONS
do
	rm -f data/gcc_statfun_$impl.dat
	echo "Making data file containing stats - see data/gcc_statfun_$impl.dat"
	for t in $THREADS
		do 
		for rows in $N
			do
			echo "OMP_PROC_BIND=$bind OMP_PLACES=$place OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ./$impl $rows"
			output=$(OMP_PROC_BIND=$bind OMP_PLACES=$place OMP_WAIT_POLICY=active OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,8 ./$impl $rows)
			echo "$t $output $rows" >> data/gcc_statfun_$impl.dat
		done
	done
done
echo "File is done"

exit 0

