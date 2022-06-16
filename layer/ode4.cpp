#include <cstdio>
#include <cstdlib>

int ode4_init = 0;
long double *k1;
long double *k2;
long double *k3;
long double *k4;
long double *new_x;

long double new_t;


void ode4_init_check(int dim){
    if (ode4_init == 0){
        k1 = (long double*)malloc(dim * sizeof(long double));
        k2 = (long double*)malloc(dim * sizeof(long double));
        k3 = (long double*)malloc(dim * sizeof(long double));
        k4 = (long double*)malloc(dim * sizeof(long double));
        new_x = (long double*)malloc(dim * sizeof(long double));

        ode4_init = 1;
        return ;
    }
    else
        return ;
}



void ode4(int dim, long double curr_t, long double delta_t, 
          long double *curr_x, long double *para,
          void (*f)(long double*, long double*, long double, long double*))
{
    /*Initialization*/
    ode4_init_check(dim);
    
    /*k1 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i];
    new_t = curr_t;
    f(k1, new_x, new_t, para);

    /*k2 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * 0.5 * k1[i];
    new_t = curr_t + delta_t * 0.5;
    f(k2, new_x, new_t, para);

    /*k3 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * 0.5 * k2[i];
    new_t = curr_t + delta_t * 0.5;
    f(k3, new_x, new_t, para);
    
    /*k4 part*/
    for(int i = 0; i < dim; i ++)       new_x[i] = curr_x[i] + delta_t * k3[i];
    new_t = curr_t + delta_t;
    f(k4, new_x, new_t, para);

    /*Summary part*/
    for(int i = 0; i < dim; i ++)       curr_x[i] = curr_x[i] + delta_t * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6;

    return ;
}

