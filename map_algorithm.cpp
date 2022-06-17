#include <cstdio>
#include <cstdlib>

#include "setting_parameters.cpp"

void map_algorithm(struct PARAMETERS *parameters)
{


    /*Define Parameter*/
        long long int curr_t;                // Time parameter(during the iteration)
        long long int t_after;               // Lyapunov Spectrum time average use

        long double *curr_x;                 // current x vector
        long double *spectrum;               // current spectrum vector

        long double *para;                   // Parameter vector
        long double *rand_para;              // Random parameter vector

    /*Memory Initialization*/
        curr_x = (long double*) malloc(parameters->dim * sizeof(long double));
        spectrum = (long double*) malloc(parameters->dim * sizeof(long double));

        para = (long double*) malloc(parameters->para_size * sizeof(long double));
        rand_para = (long double*) malloc(parameters->rand_para_size * sizeof(long double));

    /*Value Initialization*/
        curr_t = 0;
        t_after = 0;

        for (int i = 0; i < parameters->dim; i ++){
            curr_x[i] = parameters->group_data[i];
            spectrum[i] = 0;
        }
        for (int i = 0; i < parameters->para_size; i ++)
                                        para[i] = parameters->group_data[dim + i];
        for (int i = 0; i < parameters->rand_para_size; i ++)
                                        rand_para[i] = parameters->group_data[dim + parameters->para_size + i];


    /*Main Loop*/
    long long int print_mark_t = 0;

                printf("StartValue ");
    for (int i = 0; i < parameters->dim; i ++)  
                printf("%Le ", curr_x[i]);
                printf("Parameter ");
    for (int i = 0; i < parameters->para_size; i ++)      
                printf("%Le ", para[i]);
                printf("RandParameter ");
    for (int i = 0; i < parameters->rand_para_size; i ++)      
                printf("%Le ", rand_para[i]);
    if (print_every_values != 1 && print_every_LyaSpec != 1)
                printf("MainVals ");
        else    printf("MainVals\n");


    while (1){
        if (curr_t > step_max)          break;
        if (curr_x[0] > 1000000 || curr_x[0] < -1000000)         
                                        break;          //Overflow break
                                      
        /*Map computation*/  
        parameters->f(curr_x, curr_x, curr_t, para);
        /*if (parameters->rand_para_size == 0 || parameters->rand_dim == 0){
            parameters->rand_f(curr_x, curr_x, curr_t, para);
        }*/

        curr_t += 1;
        print_mark_t += 1;

        /*Output and Print*/
        if (curr_t > step_mark){
            if (print_mark_t >= print_delta_s){
                print_mark_t = 0;
                if (print_every_values >= 1 || print_every_LyaSpec == 1){
                    printf("%lld %lld ", curr_t, step_max); 
                    //printf("%Le ", curr_x[2] - last_z);
                    if (print_every_values == 1)
                        for (int i = 0; i < parameters->dim; i ++)  
                                        printf("%Le ", curr_x[i]);
                    if (print_every_LyaSpec == 1)
                        for (int i = 0; i < parameters->dim; i ++)  
                                        printf("%Le ", spectrum[i]);
                    printf("\n");
                }
            }

        }
        else{
            if (print_mark_t >= print_delta_s){
                print_mark_t = 0;
                if (print_every_values == 2){
                    printf("%lld %lld ", curr_t, step_max); 
                    for (int i = 0; i < parameters->dim; i ++)  
                                        printf("%Le ", curr_x[i]);
                    printf("\n");
                }
            }
        }

    }
    printf("%lld %lld ", curr_t, step_max); 
    for (int i = 0; i < parameters->dim; i ++)  printf("%Le ", curr_x[i]);
                                    
    if (print_every_LyaSpec == 1 || print_final_LyaSpec == 1){
        for (int i = 0; i < parameters->dim; i ++)  
                                    printf("%Le ", spectrum[i]);
    }
    printf("\n");
}
