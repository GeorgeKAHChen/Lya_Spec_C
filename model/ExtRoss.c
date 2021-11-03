/*=========================================
    
    ExtRoss.c

    Extend Rossler model (4-d)   

=========================================*/

#include<stdio.h>

/*General Parameter*/
int dim = 4;
int para_size = 4;
int rand_para_size = 0;

// X_start - 1d
//double min_para[] = { -10.0, 5.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
//double max_para[] = { -10.0, 20.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
//int group_size[] =  {   1,    601,   1,    1,    1,    1,   1,   1};

// X_start Space - 4d
//double min_para[] = { -30.0, -20.0, -50.0,  0.0, 0.25, 3.0, 0.5, 0.05};
//double max_para[] = {  30.0,  20.0,  55.0,  0.0, 0.25, 3.0, 0.5, 0.05};
//int group_size[] =  {   11,      9,    11,      1,    1,   1,   1,   1};

// Parameter - 1d
//double min_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2, 2.0, 0.2, 0.48};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.26, 9.0, 0.6, 0.66};
//int group_size[]  = {    1,    1,   1,    1,  101, 101, 101,  101};

//Sample = {-10.0, -4.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,   1};

double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 3.0, 0.5, 0.05};
int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,   1};

char model_name[] = "ExtRoss";

/*Dot f function*/
void f(double *result, double *state, double t, double *para){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    double w = state[3];

    double para_a = para[0];
    double para_b = para[1];
    double para_c = para[2];
    double para_d = para[3];

    result[0] = -y-z;
    result[1] = x+para_a*y+w;
    result[2] = para_b+x*z;
    result[3] = -para_c*z+para_d*w;
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
    double para_d = para[3];

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


