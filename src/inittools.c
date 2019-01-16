#include <stdlib.h>
#include <math.h>
#include "inittools.h"

#define M_PI 3.14159265358979323846

void
init_u(int n, double u_start, double * restrict u_old, double * restrict u_new){

	int i, j;

	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			if(j == (n + 1) || i == 0 || i == (n + 1)){
				u_old[i*(n + 2) + j] = 20.0;
				u_new[i*(n + 2) + j] = 20.0;
			} 
			else if(j == 0){
				u_old[i*(n + 2) + j] = 0.0;
				u_new[i*(n + 2) + j] = 0.0;
			}
			else{
				u_old[i*(n + 2) + j] = u_start;
				u_new[i*(n + 2) + j] = u_start;
			}
		}
	}
}

void
init_u_test(int n, double * restrict u_old, double * restrict u_new){

	int i, j;

	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			u_old[i*(n + 2) + j] = 0.0;
			u_new[i*(n + 2) + j] = 0.0;
		}
	}
}

void
init_f(int n, double h, double * restrict f){

	int i, j;

	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			if((double)(-1 + i*h) >= 0.0 && (double)(-1 + i*h) <= 0.33 && (double)(-1 + j*h) >= -0.66 && (double)(-1 + j*h) <= -0.33){
				f[i*(n + 2) + j] = 200;
			}
			else{
				f[i*(n + 2) + j] = 0;
			}
		}
	}
}

void
init_f_test(int n, double h, double * restrict f){

	int i, j;
	double x, y;

	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			x = -1 + h*i;
			y = -1 + h*j;
			f[i*(n + 2) + j] = 2*M_PI*M_PI*sin(M_PI*x)*sin(M_PI*y);
		}
	}
}

void
init_sol(int n, double h, double * restrict sol){

	int i, j;
	double x, y;

	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			x = -1 + h*i;
			y = -1 + h*j;
			if(x == -1 || y == -1 || x == 1 || y == 1){
				sol[i*(n + 2) + j] = 0.0;
			}
			else{
				sol[i*(n + 2) + j] = sin(M_PI*x)*sin(M_PI*y);				
			}
		}
	}
}

/* Routine for calculating two norm differences between two arrays */
double
euclidian_norm(int n, double * restrict u_old, double * restrict u_new){
	int i, j;
	double sum = 0, diff;
	
	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			diff = (u_new[i*(n + 2) + j] - u_old[i*(n + 2) + j]);
			sum += diff*diff;
		}
	}
	sum = sqrt(sum);
	return(sum);
} 

/* Routine for allocating two-dimensional array */
double **
malloc_2d(int m, int n)
{
    int i;

    if (m <= 0 || n <= 0)
	return NULL;

    double **A = malloc(m * sizeof(double *));
    if (A == NULL)
	return NULL;

    A[0] = malloc(m*n*sizeof(double));
    if (A[0] == NULL) {
	free(A);
	return NULL;
    }
    for (i = 1; i < m; i++)
	A[i] = A[0] + i * n;

    return A;
}

void
free_2d(double **A) {
    free(A[0]);
    free(A);
}

