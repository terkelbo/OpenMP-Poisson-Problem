#ifndef __GAUSSSEIDEL_NAIVE_H
#define __GAUSSSEIDEL_NAIVE_H

void gaussseidel(int n, double h, double **restrict u, double **restrict f);

#define CHECK_FLOP 7
#endif
