echo "#thrds wall user sys"; for t in 1 2 4 8 16; \
do echo -n " $t "; OMP_NUM_THREADS=$t OMP_SCHEDULE=dynamic,50 \
OMP_NUM_THREADS=$t time -f "%e %U %S" mandelbrot ; done
exit 0
