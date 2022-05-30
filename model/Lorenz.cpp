/*=========================================
    
    Lorenz.c

    Lorenz model (3-d)   

=========================================*/


#include<cstdio>

/*General Parameter*/

int dim = 3;
int rand_dim = 0;
int para_size = 3;
int rand_para_size = 0;

/* 3 - 2 - 1 - (3) - 2 */
///*                 x_0,  y_0, z_0  sigma    rho   beta
double min_para[] = {-0.1, 0.1, 0.1,  10.0,   0.0,   8/3};
double max_para[] = { 0.1, 0.1, 0.1,  10.0,  30.0,   8/3};
int  group_size[] = {   2,   1,   1,     1,    31,     1};
//*/

char model_name[] = "Lorenz";



/*Dot f function*/
void f(double *result, double *state, double t, double *para){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    result[0] = para[0] * (y - x);
    result[1] = x * (para[1] - z) - y;
    result[2] = x * y - para[2] * z;

    return ;
}



/*dW_t - for maruyama part of EM algorithm*/
void rand_f(double *result, double *state, double t, double *random_value, double *rand_para){
    double x = state[0];
    double y = state[1];
    double z = state[2];

    //printf("%lf, %lf\n", para_epsilon * random_val, result[2]);
    result[0] = result[0];
    result[1] = result[1];
    result[2] = result[2];
    return ;
}




/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t, double *para){
    double x = state[0];
    double y = state[1];
    double z = state[2];

    result[0] = 1.0 - delta_t * para[0];
    result[1] = delta_t * para[0];
    result[2] = 0.0;

    result[3] = delta_t * (para[1] - z);
    result[4] = 1.0 - delta_t;
    result[5] = -delta_t * x;

    result[6] = delta_t * y;
    result[7] = delta_t * x;
    result[8] = 1.0 - delta_t * para[2];

    return ;
}

