//===========================================================
/*Time parameter*/
    double delta_t = 1e-4;
    double T_max = 100000;
    double T_mark = 90000;
        /*
        delta_t is the step size of the code
        T_max is the final time t
        after T_mark, the code will try to compute the Lyapunov Spectrum
        */
//===========================================================





//===========================================================
/*Lyapunov Spectrum parameter*/
    int print_every_LyaSpec = 0;
        /*
        value: 0, 1;
        0 means not print every Lyapunov spectrum
        1 means print every Lyapunov spectrum after T_mark
        */

    int print_final_LyaSpec = 1;
        /*
        value: 0, 1;
        0 means not print the final Lyapunov spectrum;
        1 means print final Lyapunov spectrum
        */
    /*
    If both `print_every_LyaSpec` and `print_final_LyaSpec` are 0, 
    then the code will not compute the Lyapunov Spectrum
    */
//===========================================================




//===========================================================
/*Main Computation parameter*/
    int print_every_values = 0;
        /*
        value: 0, 1;
        0 means not print every value
        1 means print every value after T_mark
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
        0 means the code will print every on screen
        1 means the code will print every process into one file
        */
//===========================================================
