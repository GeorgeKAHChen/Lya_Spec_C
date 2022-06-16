#ifndef INITIALIZATION
#define INITIALIZATION
//===========================================================
/*Time parameter*/
    long double delta_t = 1e-4;
    /*Full interval*/
    long double T_max =  1000;
    long double T_mark = 900;
    
    /*Value in attractor*/
    //long double T_max =  10000;
    //long double T_mark = 1;

        /*
        `delta_t` is the step size of the code.
        `T_max` is the final time t.
        After `T_mark`, the code will try to compute the Lyapunov 
        Spectrum if `print_every_LyaSpec` or `print_final_LyaSpec`
        != 0.
        */

    long double print_delta_t = -1;
    //long double print_delta_t = 1e-4;
        /* 
        If     
            ```      
            print_every_LyaSpec
            print_every_values
            ```
        != 0, then after every `print_delta_t`, the system will print
        the result. If `print_delta_t` <= `delta_t`, then the system
        will print every results after `delta_t`.


        If print_delta_t = -1, then the system will print every result.
        */
//===========================================================





//===========================================================
/*Lyapunov Spectrum parameter*/
    int print_every_LyaSpec = 1;
        /*
        value: 0, 1;
        0 means not print every Lyapunov spectrum;
        1 means print every Lyapunov spectrum after T_mark.
        */

    int print_final_LyaSpec = 1;
        /*
        value: 0, 1;
        0 means not print the final Lyapunov spectrum;
        1 means print final Lyapunov spectrum.
        */
    /*
    If both `print_every_LyaSpec` and `print_final_LyaSpec` are 0, 
    then the code will not compute the Lyapunov Spectrum.
    */
//===========================================================




//===========================================================
/*Main Computation parameter*/
    int print_every_values = 1;
        /*
        value: 0, 1, 2;
        0 means not print every value;
        1 means print every value after T_mark.
        2 means print every value from the begining
        */
    /*
    If `rand_para_size` in model files is 0, 
    then the code will use Runge-Kutta 4 method (ode4), 
    else, the code will use the Euler-Maruyama method.
    */
//===========================================================



struct PARAMETERS{
    long double *group_data;                 // [Initial value, parameter, random parameter]
    int dim;                            // Dimension of system
    int rand_dim;                       // Dimension of random value
    int para_size;                      // Dimension of parameter
    int rand_para_size;                 // Dimension of random parameter
    void (*f)(long double*, long double*, long double, long double*);
                                        // Function of system
    void (*Jf)(long double*, long double*, long double , long double*);
                                        // Jacobian matrix of the system
    void (*rand_f)(long double*, long double*, long double, long double*, long double*, long double);
                                        // Random part of the system
};
#endif