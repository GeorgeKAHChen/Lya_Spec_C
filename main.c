//#include "model/Lorenz.c"
//#include "model/Rossler.c"
#include "model/ExtRoss.c"
//#include "model/GenRoss.c"
//#include "model/Sto_Lorenz.c"

#include <stdlib.h>
#include "main_algorithm.c"


int main(int argc, char const *argv[])
{

    /*Group property initialization*/
    double *total_group;

    int sum_group = 1;
    int para_group = 0;
    int group_dim = dim + para_size + rand_para_size;

    int *para_mark;
    int *para_mod;
    double *all_para_vals;
    para_mark = malloc(group_dim * sizeof(int));
    para_mod = malloc(group_dim * sizeof(int));
    
    for (int i = 0; i < group_dim; i ++){
        sum_group *= group_size[i];
        para_group += group_size[i];
        para_mark[i] = 0;
        for(int j = 0; j < i; j ++)     para_mark[i] += group_size[j];
        if (i == 0)                     para_mod[i] = group_size[i];
        else                            para_mod[i] = para_mod[i - 1] * group_size[i];
    }

    total_group = malloc(sum_group * group_dim * sizeof(double));
    all_para_vals = malloc(para_group * sizeof(double));

    for (int i = 0; i < group_dim; i ++){
        if (group_size[i] != 1){
            double delta_val = (max_para[i] - min_para[i]) / (group_size[i] - 1);
            all_para_vals[para_mark[i]] = min_para[i];
            for(int j = 1 ; j < group_size[i] - 1; j ++){
                all_para_vals[para_mark[i] + j] = all_para_vals[para_mark[i] + j - 1] + delta_val;
            }
            all_para_vals[para_mark[i] + group_size[i] - 1] = max_para[i];
        }
        else
            all_para_vals[para_mark[i]] = min_para[i];
    }

    for (int i = 0; i < sum_group; i ++){
        for (int j = 0; j < group_dim; j ++){
            int mark_all_para_vals = para_mark[j];
            if (j == 0)     mark_all_para_vals += i % group_size[j];
            else            mark_all_para_vals += (int)(i / para_mod[j - 1]) % group_size[j];
            total_group[i * group_dim + j] = all_para_vals[mark_all_para_vals];
        }
    }

    /* Main computation*/
    for (int i = 0; i < sum_group; i ++){
        double *group_data;
        group_data = malloc(group_dim * sizeof(double));
        memcpy(group_data, total_group + i * group_dim, group_dim * sizeof(double));

        main_algorithm(group_data, dim, para_size, rand_para_size, f, Jf);
    }

    return 0;

}