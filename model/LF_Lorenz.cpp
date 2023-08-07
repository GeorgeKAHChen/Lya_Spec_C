/*=========================================
    
    Lorenz.c

    Lorenz model (3-d)   

=========================================*/


#include<cstdio>
#include<cmath>

/*General Parameter*/
int dim = 3;
int rand_dim = 0;
int para_size = 3;
int rand_para_size = 0;
int this_is_map = 0;

/* 3 - 2 - 1 - (3) - 2 */
///*                       x_0,  y_0, z_0  sigma    rho   beta

long double min_para[] = { -0.1, -0.1, -0.1,  10.0,      0.0,   8.0/3.0};
long double max_para[] = {  0.1, -0.1, -0.1,  10.0,    300.0,   8.0/3.0};
int  group_size[] = {        1,   1,   1,     1,         301,         1};
//*/

void model_initialization(){
    return ;
}

/*Dot f function*/
void f(long double *result, long double *state, long double t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    result[0] = para[0] * (y - x);
    result[1] = x * (para[1] - z) - y;
    result[2] = x * y - para[2] * z;

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


long double *last_vals;
long double *last_last_vals;

int ps_f(long double *state, int ps_print, long double *ps_return){

    if (ps_print == -1){
        last_vals = (long double*) malloc(dim * sizeof(long double));
        last_last_vals = (long double*) malloc(dim * sizeof(long double));
    }

    //if (ps_print != -1 && last_vals[1] > 0 && state[1] < 0){
    if (ps_print != -1 && last_vals[2] > last_last_vals[2] && last_vals[2] > state[2]){
        ps_print = 1;
        ps_return[0] = last_vals[0];
        ps_return[1] = last_vals[1];
        ps_return[2] = last_vals[2];

        last_last_vals[0] = last_vals[0];
        last_last_vals[1] = last_vals[1];
        last_last_vals[2] = last_vals[2];

        last_vals[0] = state[0];
        last_vals[1] = state[1];
        last_vals[2] = state[2];

        return 1;
    }

    last_last_vals[0] = last_vals[0];
    last_last_vals[1] = last_vals[1];
    last_last_vals[2] = last_vals[2];

    last_vals[0] = state[0];
    last_vals[1] = state[1];
    last_vals[2] = state[2];
    return 0;
}

