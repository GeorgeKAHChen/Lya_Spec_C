#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void mat_multi(int dim, double *mat_x, double *mat_y, double *mat_result){
    for (int i = 0; i < dim; i ++){
        for (int j = 0; j < dim; j ++){
            mat_result[i*dim + j] = 0;
            for (int k = 0; k < dim; k ++)
                mat_result[i*dim + j] += mat_x[i * dim + k] * mat_y[j + k*dim];
        }
    }
    return ;
}


void gram_schmidt(int dim, double *mat_result, double *eye, double *new_spec){
    double *old_eye;
    old_eye = malloc(dim * dim * sizeof(double));
    memcpy(eye, mat_result, dim * dim * sizeof(double));

    /*gram_schmidt*/
    for (int kase = 0; kase < dim; kase ++){
        for(int i = 0; i < kase; i ++){
            double inner_beta = 0;
            double inner_ab = 0;
            for (int j = 0; j < dim; j ++){
                inner_beta += eye[i+j*dim] * eye[i+j*dim];
                inner_ab += eye[i+j*dim] * mat_result[kase+j*dim];
            }
            for (int j = 0; j < dim; j ++)
                eye[kase + j*dim] -= (inner_ab/inner_beta) * eye[i+j*dim];
        }
    }

    /*Normalization*/
    for (int i = 0; i < dim; i ++){
        new_spec[i] = (double)0;
        for (int j = 0; j < dim; j ++)
            new_spec[i] += eye[i + dim*j] * eye[i + dim*j];
        new_spec[i] = sqrt(new_spec[i]);
        for (int j = 0; j < dim; j ++)
            eye[i + dim*j] /= new_spec[i];
    }
    
    return ;
}


double lya_spec(int dim, double *curr_x,
              double delta_t, void (*Jf)(double*, double*, double),
              double *eye, double *spectrum, double t_after)
{
    /*Calculate the Jacobian Matrix*/
    double *mat_Jaco;
    mat_Jaco = malloc(dim * dim * sizeof(double));
    Jf(mat_Jaco, curr_x, delta_t);

    /*Matrix multiply*/
    double *mat_result;
    mat_Jaco = malloc(dim * dim * sizeof(double));
    mat_multi(dim, mat_Jaco, eye, mat_result);

    /*Gram_Schmidt and normalization*/
    double *new_spec;
    new_spec = malloc(dim * sizeof(double));
    gram_schmidt(dim, mat_result, eye, new_spec);

    /*Change the Spectrum*/
    for (int i = 0; i < dim; i ++)         
        spectrum[i] = (spectrum[i] * t_after + log(new_spec[i])) / (t_after + delta_t);

    t_after += delta_t;
    return t_after;
}

/*
int main(int argc, char const *argv[])
{
    int dim = 3;
    double *mat_result;
    double *eye;
    double *new_spec;
    mat_result = malloc(dim * dim * sizeof(double));
    eye = malloc(dim * dim * sizeof(double));
    new_spec = malloc(dim * sizeof(double));
    for(int i = 0; i < dim*dim; i ++){
        mat_result[i] = i + 1;
        eye[i] = i + 1;
    }
    for(int i = 0; i < dim*dim; i ++)        printf("%lf\t", eye[i]);printf("\n");
    gram_schmidt(dim, mat_result, eye, new_spec);

    for(int i = 0; i < dim*dim; i ++)        printf("%lf\t", eye[i]);printf("\n");
    return 0;
}

*/