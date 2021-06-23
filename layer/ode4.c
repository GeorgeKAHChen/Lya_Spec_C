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
    
    /*k1 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i];
    new_t = curr_t;
    f(k1, new_x, new_t);

    /*k2 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * 0.5 * k1[i];
    new_t = curr_t + delta_t * 0.5;
    f(k2, new_x, new_t);

    /*k3 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * 0.5 * k2[i];
    new_t = curr_t + delta_t * 0.5;
    f(k3, new_x, new_t);
    
    /*k4 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * k3[i];
    new_t = curr_t + delta_t;
    f(k4, new_x, new_t);

    /*Summary part*/
    for(int i = 0; i < dim; i ++)       curr_x[i] = curr_x[i] + delta_t * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6;

    return ;
}

