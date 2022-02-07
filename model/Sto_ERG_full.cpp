/*=========================================
    
    Sto_ERG_full.cpp

    Stochastic Extend Rossler (after Generation) (rand_4-d)   

=========================================*/


#include<cstdio>

/*General Parameter*/

int dim = 4;
int rand_dim = 1;
int para_size = 4;
int rand_para_size = 4;

/* 3 - 2 - 1 - (3) - 2 */
///*                        x_0,         y_0,          z_0        w_0    a  b  c     mu  sigma1  sigma2  sigma3  sigma4
double min_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936, 0.2, 3, 0, 0.025,      0,      0,      0, 0.0010};
double max_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936, 0.2, 3, 0, 0.025,      0,      0,      0, 0.0010};
int  group_size[] = {         1,           1,            1,         1,   1, 1, 1,     1,      1,      1,      1,     10};
//*/

char model_name[] = "ExtendedRossler(4-d noise)";

/*Dot f function - for ode4 or Euler part of EM algorithm*/
void f(double *result, double *state, double t, double *para){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];

    double para_a = para[0];
    double para_b = para[1];
    double para_c = para[2];
    double para_mu = para[3];

    result[0] = -(y+z);
    result[1] = x+para_a*y+w;
    result[2] = para_b+x*z-para_c*z;
    result[3] = -para_mu*(10*z-w);
    return ;
}


/*dW_t - for maruyama part of EM algorithm*/
void rand_f(double *result, double *state, double t, double *random_value, double *rand_para){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];

    //printf("%lf, %lf\n", para_epsilon * random_val, result[2]);
    result[0] = result[0] + rand_para[0] * random_value[0];
    result[1] = result[1] + rand_para[1] * random_value[0];
    result[2] = result[2] + rand_para[2] * random_value[0];
    result[3] = result[3] + rand_para[3] * random_value[0];
    return ;
}


/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t, double *para){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];
        
    double para_a = para[0];
    double para_b = para[1];
    double para_c = para[2];
    double para_mu = para[3];

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


