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

// Here the parameter of random value is random value * delta t (sigma * delta_t)

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
//           name =            x            y         z           w    a     b    c     mu   sigma 
//double min_para[] = {-227.691998, -194.679932, 0.013127, 176.027075,  0.2,   3,   0, 0.032,  0.008}; //0.014
//double max_para[] = {-227.691998, -194.679932, 0.013127, 176.027075,  0.2,   3,   0, 0.032,  0.008};
//int group_size[]  = {          1,           1,        1,          1,    1,   1,   1,     1,    100};

// start value (-10, -4, 0, 12) have initial value (90000.999670/100000.000000)
// (-227.691998, -194.679932, 0.013127, 176.027075)


// ERS - check parameter interval between 2-3-dim chaos
//           name =      x     y    z     w     a    b    c     mu sigma 
//double min_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2,   3,   0, 0.001,  0.0}; //0.014
//double max_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2,   3,   0, 0.050,  0.0};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,    10,    1};


/* Stochastic Extended Rossler System - Parameter mu - sigma figure*/
/* Here the start value is (-10, -4, 0, 12), to accelerate the algorithm, we use 
the value after t_max  = 100000(Delta t = 1e-4) as the initial value.*/
/* (2) - 3*/
/*
double min_para[] = {-31.402973,   28.286854,    0.098552,  27.326078,   0.2, 3, 0, 0.016, 0.013};
double max_para[] = {-31.402973,   28.286854,    0.098552,  27.326078,   0.2, 3, 0, 0.016, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/

/* 3 - (2) */
/*
double min_para[] = {-29.144808,   -21.497397,   0.100538,  27.28628,    0.2, 3, 0, 0.017, 0.013};
double max_para[] = {-29.144808,   -21.497397,   0.100538,  27.28628,    0.2, 3, 0, 0.017, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/

/* (3) - 2 - 1 - 3 - 2 */
/*
double min_para[] = {-46.31808,    -40.664952,   0.063617,  37.545777,   0.2, 3, 0, 0.022, 0.013};
double max_para[] = {-46.31808,    -40.664952,   0.063617,  37.545777,   0.2, 3, 0, 0.022, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 3 - (2) - 1 - 3 - 2 */
/*
double min_para[] = {-53.23819,    19.408075,    0.056752,  34.50442,    0.2, 3, 0, 0.023, 0.013};
double max_para[] = {-53.23819,    19.408075,    0.056752,  34.50442,    0.2, 3, 0, 0.023, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 3 - 2 - (1) - 3 - 2 */
/*
double min_para[] = {-0.426018,    4.221228,     1.742067,  42.344296,   0.2, 3, 0, 0.024, 0.013};
double max_para[] = {-0.426018,    4.221228,     1.742067,  42.344296,   0.2, 3, 0, 0.024, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 3 - 2 - 1 - (3) - 2 */
///*
double min_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.023, 0.0100};
double max_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.023, 0.0100};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,    100};
//*/
/*
double min_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.025, 0.000};
double max_para[] = {-13.333874,   -6.043156,    14.617957, 36.531936,   0.2, 3, 0, 0.025, 0.000};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/

/* 3 - 2 - 1 - 3 - (2) */
/*
double min_para[] = {6.017988,     -100.579058,  0.619902,  132.219147,  0.2, 3, 0, 0.026, 0.013};
double max_para[] = {6.017988,     -100.579058,  0.619902,  132.219147,  0.2, 3, 0, 0.026, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* (2) - 3 */
/*
double min_para[] = {-282.572987,  -20.851666,   0.010614,  135.823654,  0.2, 3, 0, 0.029, 0.013};
double max_para[] = {-282.572987,  -20.851666,   0.010614,  135.823654,  0.2, 3, 0, 0.029, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 2 - (3) */
/*
double min_para[] = {-288.848176,  -85.936736,   0.010375,  151.10536,   0.2, 3, 0, 0.030, 0.013};
double max_para[] = {-288.848176,  -85.936736,   0.010375,  151.10536,   0.2, 3, 0, 0.030, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* (3) - 1 - 2 */
/*
double min_para[] = {-66.642032,   -296.438048,  1.101436,  1332.867646, 0.2, 3, 0, 0.044, 0.013};
double max_para[] = {-66.642032,   -296.438048,  1.101436,  1332.867646, 0.2, 3, 0, 0.044, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 3 - (1) - 2 */
/*
double min_para[] = {-1311.330838,  1910.116861, 0.00229,   1785.068858, 0.2, 3, 0, 0.045, 0.013};
double max_para[] = {-1311.330838,  1910.116861, 0.00229,   1785.068858, 0.2, 3, 0, 0.045, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/


/* 3 - 1 - (2) */
/*
double min_para[] = {-1110.499644, -4234.53565,  0.002692,  3698.616852, 0.2, 3, 0, 0.046, 0.013};
double max_para[] = {-1110.499644, -4234.53565,  0.002692,  3698.616852, 0.2, 3, 0, 0.046, 0.013};
int  group_size[] = {         1,           1,           1,          1,     1, 1, 1,     1,     1};
*/



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


