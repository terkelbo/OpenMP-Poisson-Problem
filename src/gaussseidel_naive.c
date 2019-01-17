#include "gaussseidel_naive.h"

void
gaussseidel(int n, double h, double **restrict u, double **restrict f){

	int i, j;

	for(i = 1; i < (n + 1); i++){
		for(j = 1; j < (n + 1); j++){
			u[i][j] = 0.25*(u[i-1][j] + u[i+1][j] + u[i][j-1] + u[i][j+1] + h*h*f[i][j]);
		}
	}
}
