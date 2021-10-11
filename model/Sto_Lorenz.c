/*=========================================
    
    Sto_Lorenz.c

    Stochastic Lorenz model (3-d)   

=========================================*/

#include<stdio.h>

int STOCHASTIC_DIFFERENTIAL_EQUATION = 1;

/*General Parameter*/
int dim = 3;
int size_state = 4;

double initial_val[3] = {1.0, 1.0, 1.0};
char model_name[] = "Lorenz";

/*Model Parameter*/
double para_rho = 28.0;
double para_sigma = 10.0;
double para_beta = 8.0/3.0;
double sto_para_sigma = 0.1;
double rand_para = 0.1;

/*Dot f function*/
void f(double *result, double *state, double t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double last_w = state[3];

    /*Normal part*/
    result[0] = para_sigma * (y - x);
    result[1] = x * (para_rho - z) - y;
    result[2] = x * y - para_beta * z;
    /*Stochastic Vector*/
    result[3] = sto_para_sigma * x;
    result[4] = sto_para_sigma * y;
    result[5] = sto_para_sigma * z;
    return ;
}



/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t){
    double x = state[0];
    double y = state[1];
    double z = state[2];

    result[0] = 1.0 - delta_t * para_sigma;
    result[1] = delta_t * para_sigma;
    result[2] = 0.0;

    result[3] = delta_t * (para_rho - z);
    result[4] = 1.0 - delta_t;
    result[5] = -delta_t * x;

    result[6] = delta_t * y;
    result[7] = delta_t * x;
    result[8] = 1.0 - delta_t * para_beta;

    return ;
}



/*Model Information*/
void call_info(){
    printf("%s\n", model_name);
    printf("(rho, sigma, beta) = (%lf, %lf, %lf)\n", para_rho, para_sigma, para_beta);
    printf("%lf * (x,y,z)^T * N(0, %lf)\n", sto_para_sigma, rand_para);
}
