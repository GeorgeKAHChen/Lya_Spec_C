#ifndef INITIALIZATION
#define INITIALIZATION

/* Deterministic system and map*/

    long double delta_t         = 1e-5; //-5
    long double t_max           = 1e5;  //5
    
    long long int step_max      = 1e8;
    
    int         calc_le         = 1;
    long double t_le            = 0.5;

    int         calc_ob         = 0;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 0.999; //0.995 typically //(2e5/1e-5) * 5e-3 = 1e8

    int         calc_ps         = 0;
    long double t_ps            = 0.95;


/* Local Test Parameter */
/*
    long double delta_t         = 1e-5;
    long double t_max           = 1e5;
    
    long long int step_max      = 1e10;
    
    int         calc_le         = 1;
    long double t_le            = 0.5;

    int         calc_ob         = 1;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 0.999; //(1e5/1e-5) * 0.001 = 1e7

    int         calc_ps         = 1;
    long double t_ps            = 0.25;
*/
/* Rand system and map (start from attractor)*/
/*
    long double delta_t         = 1e-5;
    long double t_max           = 2e5;
    
    long long int step_max      = 2e10;
    
    int         calc_le         = 1;
    long double t_le            = 0.01;

    int         calc_ob         = 1;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 0.99; //（2e5/1e-3) * 0.01 = 1e6

    int         calc_ps         = 1;
    long double t_ps            = 0.01;
*/
/* Rand - short test*/
/*
    long double delta_t         = 1e-4;
    long double t_max           = 2e5;
    
    long long int step_max      = 1e8;
    
    int         calc_le         = 1;
    long double t_le            = 0.01;

    int         calc_ob         = 0;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 0.5;

    int         calc_ps         = 1;
    long double t_ps            = 0.01;
*/
/* STD + RAND*/
/*
    long double delta_t         = 1e-5;
    long double t_max           = 4e5;
    
    long long int step_max      = 4e10;
    
    int         calc_le         = 1;
    long double t_le            = 0.5;

    int         calc_ob         = 0;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 0.5;

    int         calc_ps         = 1;
    long double t_ps            = 0.5;
*/
//===========================================================
/*Time parameter*/

    //long double delta_t         = 1e-5;
    //long double t_max           = 200000;
        /*
            Main iteration parameter time(continuous system)

            delta_t             time step size for simulation
            T_max               the max time for simulation
        */

    //long long int step_max      = 1000000;

        /*
            Main iteration parameter time(discrete system/map)

            calc_ps = 0:        not output poincare section
            calc_ps = 1:        output poincare section

            step_max:           the max time for simulation
        */
    //int         calc_le         = 1;
    //long double t_le            = 0.8;

        /*
            Time for lyapunov spectrum computation

            calc_le = 0:        not compute LE
            calc_le = 1:        compute LE
            
            T_le:               T_max * T_le = time start compute LE
        */

    //int         calc_ob         = 1;
    //long double delta_t_ob      = 1e-3;
    //long double t_ob            = 0.999;

        /*
            Time for orbit/attractor output

            calc_le = 0:        not output orbit
            calc_le = 1:        output orbit
            
            delta_t_ob:         orbit output delta_t

            T_ob:               T_max * T_ob = time start output orbit
        */

    //int         calc_ps         = 1;
    //long double t_ps            = 0.25;

        /*
            Time for orbit/attractor output

            calc_ps = 0:        not output poincare section
            calc_ps = 1:        output poincare section

            T_ps:               T_max * T_ps = time start output poincare section
        */
//===========================================================



struct PARAMETERS{
    long double *group_data;            // [Initial value, parameter, random parameter]
    int dim;                            // Dimension of system
    int rand_dim;                       // Dimension of random value
    int para_size;                      // Dimension of parameter
    int rand_para_size;                 // Dimension of random parameter
    int this_is_map;                    // System is map or not
    void (*f)(long double*, long double*, long double, long double*);
                                        // Function of system
    void (*Jf)(long double*, long double*, long double , long double*);
                                        // Jacobian matrix of the system
    void (*rand_f)(long double*, long double*, long double, long double*, long double*, long double);
                                        // Random part of the system
    int (*ps_f)(long double*, int, long double*);
                                        // Function to find the poincare section
};
#endif
