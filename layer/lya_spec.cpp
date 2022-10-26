#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

int lya_spec_init = 0;
long double *mat_Jaco;
long double *mat_result;
long double *new_spec;
long double *old_eye;

long double inner_beta;
long double inner_ab;


void lya_spec_init_check(int dim){
    if (lya_spec_init == 0){
        old_eye = (long double*)malloc(dim * dim * sizeof(long double));
        mat_Jaco = (long double*)malloc(dim * dim * sizeof(long double));
        mat_result = (long double*)malloc(dim * dim * sizeof(long double));
        new_spec = (long double*)malloc(dim * sizeof(long double));
        
        lya_spec_init = 1;
        return ;
    }
    else
        return ;
}


void mat_multi(int dim, long double *mat_x, long double *mat_y, long double *mat_result){
    for (int i = 0; i < dim; i ++){
        for (int j = 0; j < dim; j ++){
            mat_result[i*dim + j] = 0;
            for (int k = 0; k < dim; k ++)
                mat_result[i*dim + j] += mat_x[i * dim + k] * mat_y[j + k*dim];
        }
    }
    return ;
}


void gram_schmidt(int dim, long double *mat_result, long double *eye, long double *new_spec){
    memcpy(eye, mat_result, dim * dim * sizeof(long double));

    /*gram_schmidt*/
    for (int kase = 0; kase < dim; kase ++){
        for(int i = 0; i < kase; i ++){
            inner_beta = 0;
            inner_ab = 0;
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
        new_spec[i] = (long double)0;
        for (int j = 0; j < dim; j ++)
            new_spec[i] += eye[i + dim*j] * eye[i + dim*j];
        new_spec[i] = sqrt(new_spec[i]);
        for (int j = 0; j < dim; j ++)
            eye[i + dim*j] /= new_spec[i];
    }
    
    return ;
}


void lya_spec(int dim, long double *curr_x,
              long double delta_t, void (*Jf)(long double*, long double*, long double, long double*),
              long double *eye, long double *spectrum, long double t_after, long double * para)
{
    /*Initialization*/
    lya_spec_init_check(dim);

    /*Calculate the Jacobian Matrix*/
    Jf(mat_Jaco, curr_x, delta_t, para);

    /*Matrix multiply*/
    mat_multi(dim, mat_Jaco, eye, mat_result);

    /*Gram_Schmidt and normalization*/
    gram_schmidt(dim, mat_result, eye, new_spec);

    /*Change the Spectrum*/
    for (int i = 0; i < dim; i ++)         
        spectrum[i] = (spectrum[i] * t_after + log(new_spec[i])) / (t_after + delta_t);

    return ;
}

