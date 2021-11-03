/*=========================================
    
    ExtRoss.c

    Extend Rossler model (4-d)   

=========================================*/

#include<stdio.h>

/*General Parameter*/
int dim = 4;
int para_size = 6;
int rand_para_size = 0;

// STD Extended Rossler
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 1.0, 3.0, 0.0, 0.5, 0.05};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 1.0, 3.0, 0.0, 0.5, 0.05};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   1,   1,   1,    1};

// STD Rossler
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, -5.7, 0.0, 0.0};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, -5.7, 0.0, 0.0};
//int group_size[]  = {    1,    1,   1,    1,   1,   1,   1,    1,   1,   1};

// R+ER 
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 1.0, 0.2, -5.7, 0.5, 0.05};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 1.0, 0.2, -5.7, 0.5, 0.05};
//int group_size[]  = {    1,    1,   1,    1,   1,   1,   1,    1,   1,    1};

// R+ER 
//double min_para[] = {-10.0, -4.0, 0.0, 12.0,  0.2, 1.0, 0.2, -5.7, 0.5, 0.05};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 1.0,   3,  0.0, 0.5, 0.05};
//int group_size[]  = {    1,    1,   1,    1,    6,   1,   5,    4,   1,    1};

// ER -> R
//double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 0.0, 0.2, -5.7, 0.0, 0.0};
//double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.25, 0.0, 3.0,  0.0, 0.0, 0.0};
//int group_size[]  = {    1,    1,   1,    1,    1,   1,   5,    4,   1,   1};

// ER -> R
double min_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, -1.5, 0.0, 0.0};
double max_para[] = {-10.0, -4.0, 0.0, 12.0, 0.2, 0.0, 0.2, -1.0, 0.0, 0.0};
int group_size[]  = {    1,    1,   1,    1,   1,   1,   1,    1,   1,   1};

char model_name[] = "ExtendedRossler(Generalized)";

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
    double para_e = para[4];
    double para_f = para[5];

    result[0] = -y-z;
    result[1] = x+para_a*y+para_b*w;
    result[2] = para_c+x*z+para_d*z;
    result[3] = -para_e*z+para_f*w;
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
    double para_e = para[4];
    double para_f = para[5];

    result[0] = 1.0;
    result[1] = -delta_t;
    result[2] = -delta_t;
    result[3] = 0.0;

    result[4] = delta_t;
    result[5] = 1+para_a*delta_t;
    result[6] = 0.0;
    result[7] = para_b*delta_t;

    result[8] = z*delta_t;
    result[9] = 0.0;
    result[10] = 1+(x+para_d)*delta_t;
    result[11] = 0.0;

    result[12] = 0.0;
    result[13] = 0.0;
    result[14] = -para_e*delta_t;
    result[15] = 1+para_f*delta_t;

    return ;
}


