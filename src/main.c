#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "inittools.h"
#include "jacobi.h"
#include "gaussseidel.h"

int
main( int argc, char *argv[] ){

	int i, j, n, k, max_it = 5000;
	char * algo, * test;
	double u_start = 0.0, d = 100000.0, threshold = 0.001;
	double ** u_old, ** u_new, ** f;
	double ** sol;

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
	u_old = malloc_2d(n + 2, n + 2);
	u_new = malloc_2d(n + 2, n + 2); 
	f = malloc_2d(n + 2, n + 2);
	if (u_old == NULL || u_new == NULL | f == NULL) {
	    fprintf(stderr, "Memory allocation error...\n");
	    exit(EXIT_FAILURE);
	}

	/* Initialize arrays */
	if(strcmp(test,"test")==0){
		sol = malloc_2d(n + 2, n + 2);
		init_u_test(n, u_old, u_new);
		init_f_test(n, h, f);
		init_sol(n, h, sol);
	}
	else{
		init_u(n, u_start, u_old, u_new);
		init_f(n, h, f);
	}
	
	k = 0;
	/* Start the time loop */
	while(d > threshold && k < max_it){
		//solve one timestep using jacobi
		if(strcmp(algo,"jacobi")==0){
			jacobi(n, h, u_old, u_new, f); 	
		}
		else{
			gaussseidel(n, h, u_old, u_new, f);
		}
		
		//calculate 2-norm between old and new
		d = euclidian_norm(n, u_old, u_new);

		//now that the values are updated we copy new values into the old array
		for(i = 0; i < (n + 2); i++){
			for(j = 0; j < (n + 2); j++){
				u_old[i][j] = u_new[i][j];
			}
		}

		//increment k
		k += 1;

	}

	if(strcmp(test,"test")==0){
		d = euclidian_norm(n, sol, u_new);
		printf("Mean euclidian norm between sol and approximation is %f \n", d/(n*n));
	}

	printf("Number of iterations run was %i \n", k);
	//print final array
	/*
	for(i = 0; i < (n + 2); i++){
		for(j = 0; j < (n + 2); j++){
			printf("%f ", u_new[i][j]);
		}
		printf("\n");
	}
	*/

	free_2d(u_old);
	free_2d(u_new);
	free_2d(f);
}
