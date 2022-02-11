/*=========================================
    
    2dSERS.cpp

    SERS 2-dim simplify

=========================================*/


#include<cstdio>

/*General Parameter*/

int dim = 3;
int rand_dim = 0;
int para_size = 4;
int rand_para_size = 0;

///*                 x_0, z_0, w_0, y_0, b, c,    mu, sigma2
double min_para[] = {-10,   0,  12,  -4, 3, 0, 0.025, 0.0000};
double max_para[] = {-10,   0,  12,  -4, 3, 0, 0.025, 0.0000};
int  group_size[] = {  1,   1,   1,   1, 1, 1,     1,      1};
//*/

char model_name[] = "2DSERS";

/*Dot f function - for ode4 or Euler part of EM algorithm*/
void f(double *result, double *state, double t, double *para){
    double x = state[0];
    double z = state[1];
    double w = state[2];

    double para_y0 = para[0];
    double para_b = para[1];
    double para_c = para[2];
    double para_mu = para[3];
    
    result[0] = -(para_y0+z);
    result[1] = para_b+x*z-para_c*z;
    result[2] = -para_mu*(10*z-w);
    return ;
}


/*dW_t - for maruyama part of EM algorithm*/
void rand_f(double *result, double *state, double t, double *random_value, double *rand_para){
    double x = state[0];
    double z = state[1];
    double w = state[2];

    //printf("%lf\n", rand_para[1] * random_value[0]);
    result[0] = result[0] + rand_para[0] * random_value[0];
    result[1] = result[1];
    result[2] = result[2];
    return ;
}


/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t, double *para){
    double x = state[0];
    double z = state[1];
    double w = state[2];
        
    double para_y0 = para[0];
    double para_b = para[1];
    double para_c = para[2];
    double para_mu = para[3];

    result[0] = 1.0;
    result[1] = -delta_t;
    result[2] = 0.0;

    result[3] = z*delta_t;
    result[4] = 1+(x-para_c)*delta_t;
    result[5] = 0.0;

    result[6] = 0.0;
    result[7] = -10*para_mu*delta_t;
    result[8] = 1+para_mu*delta_t;

    return ;
}


