/*=========================================
    
    ExtRoss.c

    Extend Rossler model (4-d)   

=========================================*/

#include<stdio.h>

int STOCHASTIC_DIFFERENTIAL_EQUATION = 0;

/*General Parameter*/
int dim = 4;
int size_state = 4;

double initial_val[4] = {-10.0, -6.0, 0.0, 10.0};
char model_name[] = "ExtRoss";

/*Model Parameter*/
double para_a = 0.25;
double para_b = 3.0;
double para_c = 0.5;
double para_d = 0.05;



/*Dot f function*/
void f(double *result, double *state, double t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];
    result[0] = -y-z;
    result[1] = x+para_a*y+w;
    result[2] = para_b+x*z;
    result[3] = -para_c*z+para_d*w;
    return ;
}



/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];
    
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
    result[14] = -para_c*delta_t;
    result[15] = 1+para_d*delta_t;

    return ;
}



/*Model Information*/
void call_info(){
    printf("%s\n", model_name);
    printf("(a, b, c, d) = (%lf, %lf, %lf, %lf)\n", para_a, para_b, para_c, para_d);
}