/*=========================================
    
    Rossler.c

    Rossler model (3-d)   

=========================================*/

#include<stdio.h>

int STOCHASTIC_DIFFERENTIAL_EQUATION = 0;

/*General Parameter*/
int dim = 3;
double initial_val[3] = {-1.0, 0.0, -1.0};
char model_name[] = "Rossler";

/*Model Parameter*/
double para_a = 0.2;
double para_b = 0.2;
//double para_c = 6.0;    //Rossler1
double para_c = 5.7;    //Rossler2



/*Dot f function*/
void f(double *result, double *state, double t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    result[0] = - y - z;
    result[1] = x + para_a * y;
    result[2] = para_b + z * (x - para_c);
    return ;
}



/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t){
    double x = state[0];
    double y = state[1];
    double z = state[2];

    result[0] = 1.0;
    result[1] = -delta_t;
    result[2] = -delta_t;

    result[3] = delta_t;
    result[4] = para_a * delta_t + 1;
    result[5] = 0.0;

    result[6] = delta_t * z;
    result[7] = 0.0;
    result[8] = (x - para_c) * delta_t + 1;

    return ;
}



/*Model Information*/
void call_info(){
    printf("%s\n", model_name);
    printf("(a, b, c) = (%lf, %lf, %lf)\n", para_a, para_b, para_c);
}