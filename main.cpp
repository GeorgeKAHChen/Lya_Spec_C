//HF: Henon family
#include "model/HF_N_RGHM.cpp"
//#include "model/HF_2_Henon.cpp"

//LF: Lorenz family
//#include "model/LF_Lorenz.cpp"
//#include "model/LF_SLS.cpp"

//LGF: Logistic family
//#include "model/LGF_Logistic.cpp"
//#include "model/LGF_RL.cpp"

//RF: Rossler family
//#include "model/RF_3_Rossler.cpp"
//#include "model/RF_4_FDRS.cpp"
//#include "model/RF_4_FDSRS.cpp"

//RF: Belousov-Zhabotinsky reaction model
//#include "model/bz.cpp"



#include <cstdlib>
//#include <cpthread>

#include "main_algorithm.cpp"
#include "map_algorithm.cpp"
#include "setting_parameters.cpp"


int main(int argc, char const *argv[])
{   
    /* Initizal model files */
    model_initialization();



    /* Group property initialization */
        // Define
        long double *total_group;

        int sum_group = 1;
        int para_group = 0;
        int group_dim = dim + para_size + rand_para_size;

        int *para_mark;
        int *para_mod;
        long double *all_para_vals;
        para_mark = (int*)malloc(group_dim * sizeof(int));
        para_mod = (int*)malloc(group_dim * sizeof(int));
    

        // Calculate group size
        for (int i = 0; i < group_dim; i ++){
            sum_group *= group_size[i];
            para_group += group_size[i];
            para_mark[i] = 0;
            for(int j = 0; j < i; j ++)     para_mark[i] += group_size[j];
            if (i == 0)                     para_mod[i] = group_size[i];
            else                            para_mod[i] = para_mod[i - 1] * group_size[i];
        }

        // Define
        total_group = (long double*)malloc(sum_group * group_dim * sizeof(long double));
        all_para_vals = (long double*)malloc(para_group * sizeof(long double));

        for (int i = 0; i < group_dim; i ++){
            if (group_size[i] != 1){
                long double delta_val = (max_para[i] - min_para[i]) / (group_size[i] - 1);
                all_para_vals[para_mark[i]] = min_para[i];
                for(int j = 1 ; j < group_size[i] - 1; j ++){
                    all_para_vals[para_mark[i] + j] = all_para_vals[para_mark[i] + j - 1] + delta_val;
                }
                all_para_vals[para_mark[i] + group_size[i] - 1] = max_para[i];
            }
            else
                all_para_vals[para_mark[i]] = min_para[i];
        }

        // group / para init
        for (int i = 0; i < sum_group; i ++){
            for (int j = 0; j < group_dim; j ++){
                int mark_all_para_vals = para_mark[j];
                if (j == 0)     mark_all_para_vals += i % group_size[j];
                else            mark_all_para_vals += (int)(i / para_mod[j - 1]) % group_size[j];
                total_group[i * group_dim + j] = all_para_vals[mark_all_para_vals];
            }
        }
        if (rand_init_val == 1){
            long double *rand_init_vals;
            rand_init_vals = (long double*)malloc(dim * sizeof(long double));
            for(int i = 0; i < sum_group; i ++){
                gen_init_val(rand_init_vals);
                for (int j = 0; j < dim; j ++){
                //for (int j = 0; j < dim; j ++){
                    total_group[i * group_dim + j] = rand_init_vals[j];
                }
            }
        }
    


    struct PARAMETERS parameters;
    parameters.group_data = (long double*)malloc(group_dim * sizeof(long double));
    parameters.dim = dim;
    parameters.rand_dim = rand_dim;
    parameters.para_size = para_size;
    parameters.rand_para_size = rand_para_size;
    parameters.this_is_map = this_is_map;
    parameters.f = f;
    parameters.Jf = Jf;
    parameters.rand_f = rand_f;
    parameters.ps_f = ps_f;
    
    if (this_is_map == 0)
        for (int i = 0; i < sum_group; i ++){
            memcpy(parameters.group_data, total_group + i * group_dim, group_dim * sizeof(long double));
            main_algorithm(&parameters);
        }
    else
        for (int i = 0; i < sum_group; i ++){
            memcpy(parameters.group_data, total_group + i * group_dim, group_dim * sizeof(long double));
            map_algorithm(&parameters);
        }
    return 0;

}
