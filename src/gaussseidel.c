#include "gaussseidel.h"

void
gaussseidel(int n, double h, double ** restrict u_old, double ** restrict u_new, double ** restrict f){

	int i, j;

	for(i = 1; i < (n + 1); i++){
		for(j = 1; j < (n + 1); j++){
			u_new[i][j] = 0.25*(u_new[i-1][j] + u_old[i+1][j] + u_new[i][j-1] + u_old[i][j+1] + h*h*f[i][j]);
		}
	}
}