#include <cstdio>
#include <cstdlib>
#include <random>
#include <iostream>

int rand_map_init = 0;
long double *map_euler_x;
long double *map_random_value;
std::random_device rdm{};
std::mt19937 rand_genm{rdm()};
std::uniform_real_distribution<> uni_dis(0, 1.0);


long double gen_uni_dis(){
    return uni_dis(rand_genm);
}


void rand_init_check(int dim, int rand_dim){
    if (rand_map_init == 0){
        map_euler_x = (long double*)malloc(2 * dim * sizeof(long double));
        map_random_value = (long double*)malloc(rand_dim * sizeof(long double));
        rand_map_init = 1;
        return ;
    }
    else
        return ;
}


void rand_map_calc(int dim, int rand_dim, long double curr_t, long double delta_t, 
          long double *curr_x, long double *para, long double *rand_para,
          void (*f)(long double*, long double*, long double, long double*),
          void (*rand_f)(long double*, long double*, long double, long double*, long double*, long double))
{
    /*Initialization*/
    rand_init_check(dim, rand_dim);
    
    /*Euler Step*/
    f(map_euler_x, curr_x, curr_t, para);               // = dot x
    
    /*Maruyama Step*/
    //long double min_rand = -rand_para[0];
    long double min_rand = -rand_para[0];
    long double max_rand = rand_para[0];
    for (int i = 0; i < rand_dim; i ++)
        map_random_value[i] = gen_uni_dis(); // Random value generator
    rand_f(map_euler_x, curr_x, curr_t, map_random_value, rand_para, delta_t);
    for (int i = 0; i < dim; i ++)
        curr_x[i] = map_euler_x[i];
    return ;
}
