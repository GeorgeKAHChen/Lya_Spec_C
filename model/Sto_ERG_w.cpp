/*=========================================
    
    Sto_ERG_w.cpp

    Stochastic Extend Rossler (after Generation) (rand_4-d)   

=========================================*/

#include<cstdio>
#include<cmath>

/*General Parameter*/
int dim = 4;
int rand_dim = 1;
int para_size = 4;
int rand_para_size = 1;
int this_is_map = 0;

long double min_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.023, 1};
long double max_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.023, 1};
int  group_size[] = {              1,           1,           1,          1,     1, 1, 1,     1, 1};


char model_name[] = "ExtendedRossler(Generalized, sto W)";

/*Dot f function - for ode4 or Euler part of EM algorithm*/
void f(long double *result, long double *state, long double t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    long double w = state[3];

    long double para_a = para[0];
    long double para_b = para[1];
    long double para_c = para[2];
    long double para_mu = para[3];

    result[0] = -(y+z);
    result[1] = x+para_a*y+w;
    result[2] = para_b+x*z-para_c*z;
    result[3] = -para_mu*(10*z-w);
    return ;
}


/*dW_t - for maruyama part of EM algorithm*/
void rand_f(long double *result, long double *state, long double t, long double *random_value, long double *rand_para, long double delta_t){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    long double w = state[3];

    //printf("%lf, %lf\n", para_epsilon * random_val, result[2]);
    result[0] = result[0];
    result[1] = result[1];
    result[2] = result[2];
    result[3] = result[3] + sqrt(delta_t) * rand_para[0] * random_value[0];
    return ;
}


/*Iteration Jacobian Matrix*/
void Jf(long double *result, long double *state, long double delta_t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    long double w = state[3];
        
    long double para_a = para[0];
    long double para_b = para[1];
    long double para_c = para[2];
    long double para_mu = para[3];

    result[0] = 1.0;
    result[1] = -delta_t;
    result[2] = -delta_t;
    result[3] = 0.0;

    result[4] = delta_t;
    result[5] = 1+para_a*delta_t;
    result[6] = 0.0;
    result[7] = delta_t;

    result[8] = z*delta_t;
    result[9] = 0.0;
    result[10] = 1+(x-para_c)*delta_t;
    result[11] = 0.0;

    result[12] = 0.0;
    result[13] = 0.0;
    result[14] = -10*para_mu*delta_t;
    result[15] = 1+para_mu*delta_t;

    return ;
}


