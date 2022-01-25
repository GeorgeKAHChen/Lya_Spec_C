/*=========================================
    
    Sto_ERG.cpp

    Stochastic Extend Rossler (after Generation) (rand_4-d)   

=========================================*/

#include<cstdio>

/*General Parameter*/
int dim = 4;
int rand_dim = 1;
//int rand_dim = 4;
int para_size = 4;
//int para_size = 5;
int rand_para_size = 1;
//int rand_para_size = 4;

// SERG_main
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 1.0, 3.0, -0.5, 0.5, -0.05, 0.000, 0.000, 0.000, 0.000};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 1.0, 3.0,    0, 0.5, -0.05, 0.000, 0.000, 0.000, 0.000};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,    6,   1,    1,     1,     1,     1,     1};

//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, 5.7,  0.05, 0.005, 0.000, 0.000, 0.000, 0.000};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, 5.7,  0.05, 0.005, 0.000, 0.000, 0.000, 0.000};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,  1,     1,    1,     1,     1,     1,     1};

//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.20, 1,  2.2, 0,  0.1, -0.001, 0.000, 0.000, 0.000, 0.000};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.20, 1,  2.2, 0,  0.1, -0.01, 0.000, 0.000, 0.000, 0.000};
//int group_size[]  = {    1,    1,   1,    1,    1, 1,    1, 1,   1,    10,     1,     1,     1,     1};

// SERS
//           name =      x     y    z     w    a     b    c      mu   sigma 
double min_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2,   3,   0, 0.032,  0.013};
double max_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2,   3,   0, 0.032,  0.015};
int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,     1,     21};

// ERSS
//           name =      x     y    z     w    a     b    c     mu   sigma 
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25,   3,   0,  0.05,     0};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25,   3,   0,  0.05,     0};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,     1,     1};


char model_name[] = "ExtendedRossler(Generalized, sto Z)";

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
    result[0] = result[0];
    result[1] = result[1];
    result[2] = result[2];
    result[3] = result[3] + rand_para[0] * random_value[0];
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


