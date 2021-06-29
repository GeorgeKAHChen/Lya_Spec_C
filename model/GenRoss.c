/*=========================================
    
    GenRoss.c

    Extend Rossler model (4-d)   

=========================================*/

#include<stdio.h>
#include <stdlib.h>
#include <string.h>

int STOCHASTIC_DIFFERENTIAL_EQUATION = 0;

/*General Parameter*/
int dim = 10;
//double initial_val[] = {0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75};
//double initial_val[] = {0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5};
//double initial_val[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
double initial_val[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char model_name[] = "ExtRoss";

/*Model Parameter*/
double para_a = 0.3;
//double para_a = 0.3;
double para_b = 4;
double para_d = 2;
double para_eps = 0.1;

/*Initial model*/
int init_gene_ross = 0;
double *pre_jaco;


void init_gene_ross_check(double delta_t){
    if (init_gene_ross == 0){
        pre_jaco = malloc(dim * dim * sizeof(double));
        pre_jaco[0] = para_a*delta_t + 1;
        pre_jaco[1] = -delta_t;
        for (int i = 1; i < dim - 1; i ++){
            pre_jaco[i * dim + i - 1] = delta_t;
            pre_jaco[i * dim + i    ] = 1;
            pre_jaco[i * dim + i + 1] = - delta_t;
        }
        init_gene_ross = 1;
        return ;
    }
    else
        return ;
}



/*Dot f function*/
void f(double *result, double *state, double t){
    result[0] = (para_a * state[0] - state[1]);
    for (int i = 1; i < dim - 1; i ++)          result[i] = state[i-1] - state[i+1];
    result[dim-1] = (para_eps + para_b * state[dim - 1]*(state[dim - 2] - para_d));
        
    return ;
}

/*Iteration Jacobian Matrix*/
void Jf(double *result, double *state, double delta_t){
    init_gene_ross_check(delta_t);
    memcpy(result, pre_jaco, dim * dim * sizeof(double));
    result[(dim - 1) * dim + dim - 2] = para_b * state[dim - 1] * delta_t;
    result[(dim - 1) * dim + dim - 1] = (para_b * state[dim - 2] - para_d*para_b) * delta_t + 1;
    return ;
}



/*Model Information*/
void call_info(){
    printf("%s\n", model_name);
    printf("(dim, a, b, d, eps) = (%d, %lf, %lf, %lf, %lf)\n", dim, para_a, para_b, para_d, para_eps);
    printf("(");
    for (int i = 0; i < dim; i ++) printf("%lf\t", initial_val[i]);
    printf(")\n");
}