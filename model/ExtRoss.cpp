/*=========================================
    
    ExtRoss.c

    Extend Rossler model (4-d)   

=========================================*/

#include<stdio.h>
#include<cmath>

/*General Parameter*/
int dim = 4;
int rand_dim = 0;
int para_size = 4;
int rand_para_size = 0;
int this_is_map = 0;

/*ERS - From 2020's paper*/
long double min_para[] = {-4, -6, 40, 24, 0.25,  11.0, 0.0, 0.05};
long double max_para[] = {-4, -6, 40, 24, 0.25,  11.0, 0.0, 0.05};
int group_size[]  = {      1,  1,  1,  1,    1,     6,   1,    1};


char model_name[] = "4-dim Rossler System";

/*Dot f function*/
void f(long double *result, long double *state, long double t, long double *para){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    long double w = state[3];

    long double para_a = para[0];
    long double para_b = para[1];
    long double para_c = para[2];
    long double para_d = para[3];

    result[0] = -y-z;
    result[1] = x+para_a*y+w;
    result[2] = para_b+x*z-para_c*z;
    result[3] = -para_d*(10*z-w);
    return ;
}


/*dW_t - for maruyama part of EM algorithm*/
void rand_f(long double *result, long double *state, long double t, long double *random_value, long double *rand_para, long double delta_t){
    long double x = state[0];
    long double y = state[1];
    long double z = state[2];
    long double w = state[3];

    result[0] = result[0];
    result[1] = result[1];
    result[2] = result[2];
    result[3] = result[3];
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
    long double para_d = para[3];

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
    result[10] = 1+x*delta_t;
    result[11] = 0.0;

    result[12] = 0.0;
    result[13] = 0.0;
    result[14] = -10*para_d*delta_t;
    result[15] = 1+para_d*delta_t;

    return ;
}

/*Poincare section y = 0*/
long double *last_vals;

int ps_f(long double *state, int ps_print, long double *ps_return){
    if (ps_print == -1){
        last_vals = (long double*) malloc(dim * sizeof(long double));
    }

    if (ps_print != -1 && last_vals[1] > 0 && state[1] < 0){
        ps_print = 1;

        ps_return[0] = (last_vals[1] * state[0] - last_vals[0] * state[1])/(last_vals[1] - state[1]);
        ps_return[1] = 0;
        ps_return[2] = (last_vals[1] * state[2] - last_vals[2] * state[1])/(last_vals[1] - state[1]);
        ps_return[3] = (last_vals[1] * state[3] - last_vals[3] * state[1])/(last_vals[1] - state[1]);
        
        last_vals[0] = state[0];
        last_vals[1] = state[1];
        last_vals[2] = state[2];
        last_vals[3] = state[3];

        return 1;
    }

    last_vals[0] = state[0];
    last_vals[1] = state[1];
    last_vals[2] = state[2];
    last_vals[3] = state[3];
    return 0;
}


/*Poincare section dot y = 0
long double *last_vals;
long double *last_vals;
last_vals = (long double*) malloc(dim * sizeof(long double));
last_vals = (long double*) malloc(dim * sizeof(long double));

void ps_f(long double *state, int ps_print){
    
}
*/

void call_info(long double *para){
    return ;
}
