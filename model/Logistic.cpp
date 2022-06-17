/*=========================================
    
    Logistic.c

    Lorenz model (3-d)   

=========================================*/


#include<cstdio>
#include<cmath>

/*General Parameter*/
int dim = 1;
int rand_dim = 0;
int para_size = 1;
int rand_para_size = 0;
int this_is_map = 1;

/* 3 - 2 - 1 - (3) - 2 */
///*                        x_0,   a
long double min_para[] = { 0.33, 3.5};
long double max_para[] = { 0.33, 3.5};
int  group_size[] = {         1,   1};
//*/

char model_name[] = "Logistic";



/*Dot f function*/
void f(long double *result, long double *state, long double t, long double *para){
    long double x = state[0];
    result[0] = para[0] * x * (1 - x);

    return ;
}



/*dW_t - for maruyama part of EM algorithm*/
void rand_f(long double *result, long double *state, long double t, long double *random_value, long double *rand_para, long double delta_t){
    long double x = state[0];

    result[0] = state[0];
    return ;
}




/*Iteration Jacobian Matrix*/
void Jf(long double *result, long double *state, long double delta_t, long double *para){
    long double x = state[0];

    result[0] = para[0] - 2*para[0]*x;


    return ;
}

