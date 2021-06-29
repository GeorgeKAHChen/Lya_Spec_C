#include <stdio.h>
#include <stdlib.h>

int ode4_init = 0;
double *k1;
double *k2;
double *k3;
double *k4;
double *new_x;

double new_t;


void ode4_init_check(int dim){
    if (ode4_init == 0){
        k1 = malloc(dim * sizeof(double));
        k2 = malloc(dim * sizeof(double));
        k3 = malloc(dim * sizeof(double));
        k4 = malloc(dim * sizeof(double));
        new_x = malloc(dim * sizeof(double));

        ode4_init = 1;
        return ;
    }
    else
        return ;
}



void ode4(int dim, double curr_t, double delta_t, 
          double *curr_x, 
          void (*f)(double*, double*, double))
{
    /*Initialization*/
    ode4_init_check(dim);

    return ;
}

