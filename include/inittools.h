#ifndef __INITTOOLS_H
#define __INITTOOLS_H

void init_u(int n, double u_start, double ** restrict u_old, double ** restrict u_new);

void init_u_test(int n, double ** restrict u_old, double ** restrict u_new);

void init_f(int n, double h, double ** restrict f);

void init_f_test(int n, double h, double ** restrict f);

void init_sol(int n, double h, double ** restrict sol);

double euclidian_norm(int n, double ** restrict u_old, double ** restrict u_new);

double ** malloc_2d(int m, int n);

void free_2d(double **A);
#endif
