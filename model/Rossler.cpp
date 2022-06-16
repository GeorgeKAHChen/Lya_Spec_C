/*=========================================
    
    Rossler.c

    Rossler model (3-d)   

=========================================*/

#include<stdio.h>
#include<cmath>

/*General Parameter*/

int dim = 3;
int rand_dim = 0;
int para_size = 3;
int rand_para_size = 0;

/* 3 - 2 - 1 - (3) - 2 */
///*                       x_0,  y_0, z_0   a    b    c
long double min_para[] = {-1.0, 0.0, -1.0, 0.2, 0.2, 5.7};
long double max_para[] = {-1.0, 0.0, -1.0, 0.2, 0.2, 5.7};
int  group_size[] = {        1,   1,    1,   1,   1,   1};
//*/

char model_name[] = "Rossler";



/*Dot f function*/
void f(long double *result, long double *state, long double t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    result[0] = - y - z;
    result[1] = x + para[0] * y;
    result[2] = para[1] + z * (x - para[2]);
    return ;
}



/*dW_t - for maruyama part of EM algorithm*/
void rand_f(long double *result, long double *state, long double t, long double *random_value, long double *rand_para, long double delta_t){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];

    //printf("%lf, %lf\n", para_epsilon * random_val, result[2]);
    result[0] = result[0];
    result[1] = result[1];
    result[2] = result[2];
    return ;
}



/*Iteration Jacobian Matrix*/
void Jf(long double *result, long double *state, long double delta_t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];

    result[0] = 1.0;
    result[1] = -delta_t;
    result[2] = -delta_t;

    result[3] = delta_t;
    result[4] = para[0] * delta_t + 1;
    result[5] = 0.0;

    result[6] = delta_t * z;
    result[7] = 0.0;
    result[8] = (x - para[2]) * delta_t + 1;

    return ;
}

