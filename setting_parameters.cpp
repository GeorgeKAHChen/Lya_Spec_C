#ifndef INITIALIZATION
#define INITIALIZATION

/* Global setting flags*/

    int         ONLY_LE_MODE    = 0; // not finish0130
    int         ATTR_CHECK_MODE = 0; // not finish
    int         OB_ONLY_XI      = 1; // time delay system plot
    int         OB_XI_USE       = 0; // START FROM 0

/* Noise add delay*/
    int         NOISE_ADD_RM    = 0;
    long double noise_change[]  = {1 - 3e-3, 1 - 7e-3};

/* Deterministic system and map*/

    long double delta_t         =     1e-4; //-5
    long double t_max           =     1e5;  //5
    
    long long int step_max      =     1e8; //1e9 typically
    
    int         calc_le         = 0;
    long double t_le            = 0.5; // 0.5 typically

    int         calc_ob         = 1;
    long double delta_t_ob      = 1e-3;
    long double t_ob            = 1 - 1e-2; //0.995 typically //(2e5/1e-5) * 5e-3 = 1e8
    //long double t_ob            = 0.9;
    //long double t_ob            = 1e-4; //0.995 typically //(2e5/1e-5) * 5e-3 = 1e8

    int         calc_ps         = 0;
    long double t_ps            = 5e-2; // 0.5 typically


    int         calc_bf         = 0;
    long double t_bf            = 1 - 1e-2;

    int         bf_x_use        = 0; // START FROM 0
    long double bf_x_limit[]    = {-1, 1.6};
    int         bf_total_x      = 10001;



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
