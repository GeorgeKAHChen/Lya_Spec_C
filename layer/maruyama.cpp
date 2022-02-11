#include <cstdio>
#include <cstdlib>
#include <random>

int maruyama_init = 0;
double *maruyama_x;
double *random_value;
std::random_device rd{};
std::mt19937 rand_gen{rd()};
std::normal_distribution<> gauss_dis{0,1};

double random_value_generator(){
    return gauss_dis(rand_gen);
}


void maruyama_init_check(int dim, int rand_dim){
    if (maruyama_init == 0){
        maruyama_x = (double*)malloc(2 * dim * sizeof(double));
        random_value = (double*)malloc(rand_dim * sizeof(double));
        maruyama_init = 1;
        return ;
    }
    else
        return ;
}

void maruyama(int dim, int rand_dim, double curr_t, double delta_t, 
          double *curr_x, double *para, double *rand_para,
          void (*f)(double*, double*, double, double*),
          void (*rand_f)(double*, double*, double, double*, double*))
{
    /*Initialization*/
    maruyama_init_check(dim, rand_dim);
    f(maruyama_x, curr_x, curr_t, para);
    for (int i = 0; i < rand_dim; i ++)
        random_value[i] = random_value_generator();
    
    for (int i = 0; i < dim; i ++)
        maruyama_x[i] = curr_x[i] + maruyama_x[i] * delta_t;
    rand_f(maruyama_x, curr_x, curr_t, random_value, rand_para);
    for (int i = 0; i < dim; i ++)
        curr_x[i] = maruyama_x[i];
    return ;
}