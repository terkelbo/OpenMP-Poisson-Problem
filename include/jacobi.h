#ifndef __JACOBI_H
#define __JACOBI_H

void jacobi(int n, double h, double **restrict u_old, double **restrict u_new, double **restrict f);

#define CHECK_FLOP 7
#endif
