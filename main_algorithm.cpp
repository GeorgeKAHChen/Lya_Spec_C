#include <cstdio>
#include <cstdlib>

#include "layer/ode4.cpp"
#include "layer/lya_spec.cpp"
#include "layer/maruyama.cpp"
#include "setting_parameters.cpp"

void main_algorithm(struct PARAMETERS *parameters)
{
    /*Define Parameter*/
        long double curr_t;                  // Time parameter(during the iteration)
        long double t_after;                 // Lyapunov Spectrum time average use

        long double *curr_x;                 // current x vector
        long double *spectrum;               // current spectrum vector
        long double *eye;                    // Lyapunov Spectrum iteration matrix

        long double *para;                   // Parameter vector
        long double *rand_para;              // Random parameter vector



    /*Memory Initialization*/
        curr_x = (long double*) malloc(parameters->dim * sizeof(long double));
        spectrum = (long double*) malloc(parameters->dim * sizeof(long double));
        eye = (long double*) malloc(parameters->dim * parameters->dim * sizeof(long double));

        para = (long double*) malloc(parameters->para_size * sizeof(long double));
        rand_para = (long double*) malloc(parameters->rand_para_size * sizeof(long double));

    

    //printf("delta = %Le, T_max = %Le, T_mark = %Le\n", delta_t, T_max, T_mark);

    /*Value Initialization*/
        curr_t = 0;
        t_after = 0;

        for (int i = 0; i < parameters->dim; i ++){
            curr_x[i] = parameters->group_data[i];
            spectrum[i] = 0;
            for (int j = 0; j < parameters->dim; j ++){
                if (i == j)             eye[i*parameters->dim + j] = 1;
                else                    eye[i*parameters->dim + j] = 0;
            }
        }
        for (int i = 0; i < parameters->para_size; i ++)
                                        para[i] = parameters->group_data[dim + i];
        for (int i = 0; i < parameters->rand_para_size; i ++)
                                        rand_para[i] = parameters->group_data[dim + parameters->para_size + i];


    /*Main Loop*/
    long double print_mark_t = 0;

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
        if (curr_t > T_max)             break;
        if (curr_x[0] > 1000000 || curr_x[0] < -1000000)         
                                        break;          //Overflow break
                                    
        /*Runge-Kutta Calculator*/
        if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                        ode4(parameters->dim, curr_t, delta_t, curr_x, para, parameters->f);
        else                            maruyama(parameters->dim, parameters->rand_dim, curr_t, delta_t, curr_x, para, rand_para, parameters->f, parameters->rand_f);
    
        /*Lya_Spec Calculator*/
        if (curr_t > T_mark){
            if (print_every_LyaSpec != 0 || print_final_LyaSpec != 0)
                                        t_after = lya_spec(parameters->dim, curr_x, delta_t, parameters->Jf, eye, spectrum, t_after, para);
        }

        curr_t += delta_t;
        print_mark_t += delta_t;

        /*Output and Print*/
        if (curr_t > T_mark){
            if (print_mark_t >= print_delta_t){
                print_mark_t = 0;
                if (print_every_values >= 1 || print_every_LyaSpec == 1){
                    printf("%Le %Le ", curr_t, T_max); 
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
            if (print_mark_t >= print_delta_t){
                print_mark_t = 0;
                if (print_every_values == 2){
                    printf("%Le %Le ", curr_t, T_max); 
                    for (int i = 0; i < parameters->dim; i ++)  
                                        printf("%Le ", curr_x[i]);
                    printf("\n");
                }
            }
        }
        //{printf("[%Le, ", curr_t); for (int i = 0; i < dim; i ++)  printf("%Le, ", curr_x[i]);printf("], ");}
        //if (kase % 100000 == 0)                         {printf("%Le / %Le:\t", curr_t, T_max); for (int i = 0; i < dim; i ++)  printf("%Le ", curr_x[i]);printf("\r");}
        //if (kase % 100000 == 0)                         printf("%Le / %Le:\t", curr_t, T_max);
        //if (curr_t > T_mark && kase % 100000 == 0)      {for (int i = 0; i < dim; i ++)  printf("%Le ", spectrum[i]);printf("\r");}
        //else                                            printf("\r");
    }
    printf("%Le %Le ", curr_t, T_max); 
    for (int i = 0; i < parameters->dim; i ++)  printf("%Le ", curr_x[i]);
                                    
    if (print_every_LyaSpec == 1 || print_final_LyaSpec == 1){
        for (int i = 0; i < parameters->dim; i ++)  
                                    printf("%Le ", spectrum[i]);
    }
    printf("\n");
}