#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <math.h>

#include "inittools.h"
#include "jacobi.h"
#include "gaussseidel.h"
#include <omp.h>

#define CACHE_LINE_SIZE 64

int
main( int argc, char *argv[] ){

	int i, j, n, k, max_it = 5000;
	char * algo, * test;
	double u_start = 0.0, d = 100000.0, threshold = 0.001;
	double memory, te, mflops;
	double * u_old, * u_new, * f;
	double * sol;

	if(argc >= 2){
		n = atoi(argv[1]);
	}
	else{
		n = 100;
	}
	double h = 2.0/(n + 1);
	if(argc >= 3){
		algo = argv[2];
	}
	else{
		algo = "jacobi";
	}
	if(argc >= 4){
		test = argv[3];
	}
	else{
		test = "notest";
	}

	

	/* Allocate memory for all arrays */
	u_old = memalign(0x40, (n + 2)*(n + 2)* sizeof(double *));
	u_new = memalign(0x40, (n + 2)*(n + 2)* sizeof(double *)); 
	f = memalign(0x40, (n + 2)*(n + 2)* sizeof(double *));
	if (u_old == NULL || u_new == NULL | f == NULL) {
	    fprintf(stderr, "Memory allocation error...\n");
	    exit(EXIT_FAILURE);
	}

	/* Initialize arrays */
	if(strcmp(test,"test")==0){
		sol = memalign(0x40, (n + 2)*(n + 2)* sizeof(double *));
		init_u_test(n, u_old, u_new);
		init_f_test(n, h, f);
		init_sol(n, h, sol);
	}
	else{
		init_u(n, u_start, u_old, u_new);
		init_f(n, h, f);
	}
	
	te = omp_get_wtime();	
	/* Start the time loop */
	#pragma omp parallel default(none) shared(n,h,u_old,u_new,f,max_it,algo) private(k,i,j)
	{
	//while(d > threshold && k < max_it){
	for(k = 0; k < max_it; k++){
		//solve one timestep using jacobi
		if(strcmp(algo,"jacobi")==0){
			jacobi(n, h, u_old, u_new, f); 	
		}
		else{
			gaussseidel(n, h, u_old, u_new, f);
		}
		
		//calculate 2-norm between old and new
		//d = euclidian_norm(n, u_old, u_new);

		//now that the values are updated we copy new values into the old array
		#pragma omp for schedule(runtime)
		for(i = 0; i < (n + 2); i++){
			for(j = 0; j < (n + 2); j++){
				u_old[i*(n + 2) + j] = u_new[i*(n + 2) + j];
			}
		}

	}
	}
	te = omp_get_wtime() - te;
	mflops   = 1.0e-06*n*n*max_it*CHECK_FLOP/te;
	memory = 8*n*n/1000; // in Kbytes

	if(strcmp(test,"test")==0){
		d = euclidian_norm(n, sol, u_new);
		printf("Mean euclidian norm between sol and approximation is %f \n", d/(n*n));
	}

	printf("%10.2lf %10.2lf %le %le\n", 
	   max_it, memory, mflops, te);
	
	//printf("Number of iterations run was %i \n", k);
	//print final array
	/*
	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			printf("%f ", u_new[i][j]);
		}
		printf("\n");
	}
	*/

	free(u_old);
	free(u_new);
	free(f);
	if(strcmp(test,"test")==0){
		free(sol);
	}
}
