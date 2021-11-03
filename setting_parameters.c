#ifndef INITIALIZATION
#define INITIALIZATION
//===========================================================
/*Time parameter*/
    double delta_t = 1e-4;
    double T_max =  100000;
    double T_mark = 90000;
        /*
        `delta_t` is the step size of the code.
        `T_max` is the final time t.
        After `T_mark`, the code will try to compute the Lyapunov 
        Spectrum if `print_every_LyaSpec` or `print_final_LyaSpec`
        != 0.
        */

    double print_delta_t = 1;
        /* 
        If     
            ```      
            print_every_LyaSpec
            print_every_values
            ```
        != 0, then after every `print_delta_t`, the system will print
        the result. If `print_delta_t` <= `delta_t`, then the system
        will print every results after `delta_t`.
        */
//===========================================================





//===========================================================
/*Lyapunov Spectrum parameter*/
    int print_every_LyaSpec = 0;
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
    int print_every_values = 2;
        /*
        value: 0, 1;
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



//===========================================================
/*File Output Parameter*/
    int save_as_file = 0;
        /*
        value:0, 1;
        0 means the code will print everything on screen;
        1 means the code will print everything process into one file.
        */
//===========================================================


struct PARAMETERS{
    double *group_data;                 // [Initial value, parameter, random parameter]
    int dim;                            // Dimension of system
    int para_size;                      // Dimension of parameter
    int rand_para_size;                 // Dimension of random parameter
    void (*f)(double*, double*, double, double*);
                                        // Function of system
    void (*Jf)(double*, double*, double , double*);
                                        // Jacobian matrix of the system
};
#endif