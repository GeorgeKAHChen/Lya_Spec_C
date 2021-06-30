#include <stdio.h>
#include <stdlib.h>

#include "gene_rand.c"

int maruyama_init = 0;
double *new_x;
double random_value;

void maruyama_init_check(int dim){
    if (maruyama_init == 0){
        new_x = malloc(2 * dim * sizeof(double));
        maruyama_init = 1;
        return ;
    }
    else
        return ;
}



void maruyama(int dim, double curr_t, double delta_t, 
          double *curr_x, double rand_para,
          void (*f)(double*, double*, double))
{
    /*Initialization*/
    maruyama_init_check(dim);
    f(new_x, curr_x, curr_t);

    random_value = gene_rand(rand_para);
    //printf("%lf, %lf, %lf, %lf, %lf, %lf\n", new_x[0], new_x[1], new_x[2], new_x[3], new_x[4], new_x[5]);
    //printf("%lf, %lf, %lf, %lf, %lf\n", curr_x[0], curr_x[1], curr_x[2], curr_x[3], random_value);
    for (int i = 0; i < dim; i ++){
        curr_x[i] = curr_x[i] + new_x[i] * delta_t + new_x[dim+i] * random_value;
    }
    //printf("%lf, %lf, %lf, %lf\n", curr_x[0], curr_x[1], curr_x[2], curr_x[3]);
    //int tmp;
    //scanf("%d", &tmp);
    curr_x[dim] = curr_x[dim] + random_value;
    return ;
}

