#include "jacobi.h"

void
jacobi(int n, double h, double **restrict u_old, double **restrict u_new, double **restrict f){

	int i, j;

	#pragma omp parallel default(none) shared(n,h,u_new,f,u_old) private(i,j)
	{
	#pragma omp for schedule(runtime)
	for(i = 1; i < (n + 1); i++){
		for(j = 1; j < (n + 1); j++){
			u_new[i][j] = 0.25*(u_old[i-1][j] + u_old[i+1][j] + u_old[i][j-1] + u_old[i][j+1] + h*h*f[i][j]);
		}
	}
	}
}
