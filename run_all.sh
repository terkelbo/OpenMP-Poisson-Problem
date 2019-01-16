#!/bin/sh

CC=${1-"gcc"}
OPT=$2
NUMBER_ROWS="50 100 180 200 220 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 2000 2500"
LOOPS=1000
LOGEXT=$CC.dat

/bin/rm -rf data/${CC}/${OPT}/nat.${OPT}.$LOGEXT data/${CC}/${OPT}/blk.${OPT}.$LOGEXT data/${CC}/${OPT}/lib.${OPT}.$LOGEXT data/${CC}/${OPT}/knm.${OPT}.$LOGEXT data/${CC}/${OPT}/kmn.${OPT}.$LOGEXT data/${CC}/${OPT}/mkn.${OPT}.$LOGEXT data/${CC}/${OPT}/mnk.${OPT}.$LOGEXT data/${CC}/${OPT}/nkm.${OPT}.$LOGEXT data/${CC}/${OPT}/nmk.${OPT}.$LOGEXT

for m in $NUMBER_ROWS
do
    ./matmult_c.${CC} nat $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/nat.${OPT}.$LOGEXT
    ./matmult_c.${CC} lib $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/lib.${OPT}.$LOGEXT
    ./matmult_c.${CC} knm $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/knm.${OPT}.$LOGEXT
    ./matmult_c.${CC} kmn $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/kmn.${OPT}.$LOGEXT
    ./matmult_c.${CC} mkn $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/mkn.${OPT}.$LOGEXT
    ./matmult_c.${CC} mnk $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/mnk.${OPT}.$LOGEXT
    ./matmult_c.${CC} nkm $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/nkm.${OPT}.$LOGEXT
    ./matmult_c.${CC} nmk $m $m-10 $m-30 | grep -v CPU >> data/${CC}/${OPT}/nmk.${OPT}.$LOGEXT
	./matmult_c.${CC} blk $m $m-10 $m-30 1000 | grep -v CPU >> data/${CC}/${OPT}/blk.${OPT}.$LOGEXT
done

exit 0    	    					
    	    					
