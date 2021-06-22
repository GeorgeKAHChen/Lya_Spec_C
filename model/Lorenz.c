#include<stdio.h>

int dim = 3;
double rho = 28.0;
double sigma = 10.0;
double beta = 8.0/3.0;
double initial_val[3] = {1.0, 1.0, 1.0};
char model_name[] = "Lorenz";

void f(double *result, double *state, double t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    result[0] = sigma * (y - x);
    result[1] = x * (rho - z) - y;
    result[2] = x * y - beta * z;

    return ;
}

void Jf(double *result, double *state, double delta_t){
    double x = state[0];
    double y = state[1];
    double z = state[2];
    result[0] = 1.0 - delta_t * sigma;
    result[1] = delta_t * sigma;
    result[2] = 0.0;
    result[3] = delta_t * (rho - z);
    result[4] = 1.0 - delta_t;
    result[5] = -delta_t * x;
    result[6] = delta_t * y;
    result[7] = delta_t * x;
    result[8] = 1.0 - delta_t * beta;

    return ;
}

void call_info(){
    printf("%s\n", model_name);
    printf("(rho, sigma, beta) = (%lf, %lf, %lf)\n", rho, sigma, beta);
}


//For test model
/*
int main(int argc, char const *argv[])
{
    double result1[3];
    double result2[9];
    f(result1, initial_val, 0);
    Jf(result2, initial_val, 1e-3);
    printf("%lf, %lf, %lf\n", result1[0], result1[1], result1[2]);
    for(int i = 0; i < dim*dim; i ++) {printf("%lf, ", result2[i]);printf("\n");}

    call_info();

    return 0;
}

*/