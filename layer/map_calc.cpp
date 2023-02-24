#include <cstdio>
#include <cstdlib>

int map_calc_init_check = 0;
long double *map_new_x;


void map_calc_init(int dim){
    if (map_calc_init_check == 0){
        map_new_x = (long double*)malloc(dim * sizeof(long double));
        map_calc_init_check = 1;
        return ;
    }
    else
        return ;
}

void map_calc(int dim, long double curr_t, long double delta_t, 
          long double *curr_x, long double *para,
          void (*f)(long double*, long double*, long double, long double*))
{
    map_calc_init(dim);
    f(map_new_x, curr_x, curr_t, para);
    for(int i = 0; i < dim; i ++)       curr_x[i] = map_new_x[i];
}

