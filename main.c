//#include "model/Lorenz.c"
//#include "model/Rossler.c"
//#include "model/ExtRoss.c"
#include "model/GenRoss.c"

#include <stdio.h>
#include <stdlib.h>

#include "layer/ode4.c"
#include "layer/Lya_Spec.c"


double delta_t = 1e-4;
double T_max = 100000;
double T_mark = 90000;


int main(int argc, char const *argv[])
{
    /*Define Parameter*/
    double curr_t = 0;
    double t_after = 0;
    int kase = 0;

    double *curr_x;
    double *spectrum;
    double *eye;

    /*Initialization Values*/
    curr_x = malloc(dim * sizeof(double));
    spectrum = malloc(dim * sizeof(double));
    eye = malloc(dim * dim * sizeof(double));

    for (int i = 0; i < dim; i ++){
        curr_x[i] = initial_val[i];
        spectrum[i] = 0;
    }

    for (int i = 0; i < dim; i ++){
        for (int j = 0; j < dim; j ++){
            if (i == j)             eye[i*dim + j] = 1;
            else                    eye[i*dim + j] = 0;
        }
    }
    
    call_info();
    printf("delta = %lf, T_max = %lf, T_mark = %lf\n", delta_t, T_max, T_mark);
    /*Main Loop*/
    while (1){
        if (curr_t > T_max)         break;
    
        /*Runge-Kutta Calculator*/
        ode4(dim, curr_t, delta_t, curr_x, f);
    
        /*Lya_Spec Calculator*/
        if (curr_t > T_mark){
            t_after = lya_spec(dim, curr_x, delta_t, Jf, eye, spectrum, t_after);
        }

        curr_t += delta_t;
        kase ++;
        //if (kase % 100000 == 0)                         {printf("%lf / %lf:\t", curr_t, T_max); for (int i = 0; i < dim; i ++)  printf("%lf ", curr_x[i]);printf("\r");}
        //if (kase % 100000 == 0)                         printf("%lf / %lf:\t", curr_t, T_max);
        //if (curr_t > T_mark && kase % 100000 == 0)      {for (int i = 0; i < dim; i ++)  printf("%lf ", spectrum[i]);printf("\r");}
        //else                                            printf("\r");
    }
    printf("\n");
    call_info();
    printf("delta = %lf, T_max = %lf, T_mark = %lf\n", delta_t, T_max, T_mark);
    for (int i = 0; i < dim; i ++)  printf("%lf ", spectrum[i]);printf("\n");
    

    return 0;
}