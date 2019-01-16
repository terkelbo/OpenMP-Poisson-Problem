#include <stdio.h>
#include <stdlib.h>
#include "mandel.h"
#include "writepng.h"
#include <omp.h>

int
main(int argc, char *argv[]) {

    int   width, height;
    int	  max_iter;
    int   *image;
	double memory, te;
	
    width    = 2601;
    height   = 2601;
    max_iter = 5000;

    // command line argument sets the dimensions of the image
    if ( argc == 2 ) width = height = atoi(argv[1]);

    image = (int *)malloc( width * height * sizeof(int));
    if ( image == NULL ) {
       fprintf(stderr, "memory allocation failed!\n");
       return(1);
    }
	
	te = omp_get_wtime();
	#pragma omp parallel default(none) shared(width,height, max_iter,image)
	{
    mandel(width, height, image, max_iter);
	} // end of paralization
	te = omp_get_wtime() - te;	
	
	memory = sizeof(int)*width*height/1000; // Kbytes
	
	printf("%10.2li %10.2lf %le\n", 
	   max_iter, memory, te);
	
    //writepng("mandelbrot.png", image, width, height);

    return(0);
}
