/*=========================================
    
    gene_rand.c

    Gaussian Distribution Random Value Generator (3-d)   

=========================================*/

#include <math.h>

double gene_rand(double sigma){
    double val1 = (double)rand() / 0x7fffffff;
    double val2 = (double)rand() / 0x7fffffff;
    
    return sigma * sqrt(-2 * log(val1)) * cos(2 * 3.1415926535897932384626 * val2);
}
// https://doi.org/10.4236/jamp.2019.711185