#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>

#include "layer/ode4.cpp"
#include "layer/lya_spec.cpp"
#include "layer/maruyama.cpp"
#include "setting_parameters.cpp"


int ttl_group = 0;                      // Value for output file name

void main_algorithm(struct PARAMETERS *parameters)
{
    /*Define Parameter*/

        // Computation parameter
            long double curr_t;             // Time parameter(during the iteration)

        // System/OB parameter
            long double t_ob_mark;
            long double *curr_x;            // current x vector
            long double *para;              // Parameter vector
            long double *rand_para;         // Random parameter vector
            long double curr_ob_t = 0;

        // LE parameter
            long double t_le_mark;
            long double *spectrum;          // current spectrum vector
            long double *eye;               // Lyapunov Spectrum iteration matrix
            long double curr_le_t = 0;

        // PS parameter
            long double t_ps_mark;
            long double *ps_return;         // Poincare section value return 
            int ps_print = -1;               // Poincare section print check

        // Computation method
            int use_maruyama = 0;

    /*Memory Initialization*/

        // System/OB parameter
            curr_x = (long double*) malloc(parameters->dim * sizeof(long double));
            para = (long double*) malloc(parameters->para_size * sizeof(long double));
            rand_para = (long double*) malloc(parameters->rand_para_size * sizeof(long double));
        
        // LE parameter
            spectrum = (long double*) malloc(parameters->dim * sizeof(long double));
            eye = (long double*) malloc(parameters->dim * parameters->dim * sizeof(long double));
        
        // PS parameter
            ps_return = (long double*) malloc(parameters->dim * sizeof(long double));


        
    /*Value Initialization*/
        // System/OB parameter
            curr_t = 0;
            
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
        // OB parameter
            if (calc_ob == 1)               t_ob_mark = t_max * t_ob;

        // LE parameter
            if (calc_le == 1)               t_le_mark = t_max * t_le;

        // PS parameter
            if (calc_ps == 1)               t_ps_mark = t_max * t_ps;


    /*Output Initalization*/
        ttl_group += 1;

        // File name init
            std::stringstream file_str_info;
            std::stringstream file_str_ob;
            std::stringstream file_str_ps;
        
        // File name write
            file_str_info << "output/" << ttl_group << ".info";
            file_str_ob << "output/" << ttl_group << "_ob.dat";
            file_str_ps << "output/" << ttl_group << "_ps.dat";

        // File name string init
            std::string file_name_info;
            std::string file_name_ob;
            std::string file_name_ps;

        // File name string build
            file_str_info >> file_name_info;
            file_str_ob >> file_name_ob;
            file_str_ps >> file_name_ps;

        // File init
            std::ofstream file_info;
            std::ofstream file_ob;
            std::ofstream file_ps;

        // File open
            file_info.open(file_name_info, std::ios_base::app);
            file_ob.open(file_name_ob, std::ios_base::app);
            file_ps.open(file_name_ps, std::ios_base::app);



    /*Standard data output*/

        file_info << "=============================================\n";
        file_info << "Computation Parameters: \n";
        file_info << "Iteration: delta_t, t_max" << delta_t << " " << t_max << "\n";
        file_info << "LE: compute: " << calc_le << ", t_le: " << t_le << "\n";
        file_info << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", delta_t_ob: " << delta_t_ob << "\n";
        file_info << "PS: compute: " << calc_ps << ", t_ob: " << t_ps << "\n";
        file_info << "=============================================\n";
        file_info << "Initial Condition: \n";
        for (int i = 0; i < parameters->dim; i ++)
                                            file_info << curr_x[i] << " ";
        file_info << "\n";
        file_info << "Parameters: \n";
        for (int i = 0; i < parameters->para_size; i ++)      
                                            file_info << para[i] << " ";
        file_info << "\n";
        file_info << "Random Parameters: \n";
        for (int i = 0; i < parameters->rand_para_size; i ++)
                                            file_info << rand_para[i] << " ";
        file_info << "\n";
        file_info << "=============================================\n";

        std::cout << "=============================================\n";
        std::cout << "Computation Parameters: \n";
        std::cout << "Iteration: delta_t, t_max" << delta_t << " " << t_max << "\n";
        std::cout << "LE: compute: " << calc_le << ", t_le: " << t_le << "\n";
        std::cout << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", delta_t_ob: " << delta_t_ob << "\n";
        std::cout << "PS: compute: " << calc_ps << ", t_ob: " << t_ps << "\n";
        std::cout << "=============================================\n";
        std::cout << "Initial Condition: \n";
        for (int i = 0; i < parameters->dim; i ++)
                                            std::cout << curr_x[i] << " ";
        std::cout << "\n";
        std::cout << "Parameters: \n";
        for (int i = 0; i < parameters->para_size; i ++)      
                                            std::cout << para[i] << " ";
        std::cout << "\n";
        std::cout << "Random Parameters: \n";
        for (int i = 0; i < parameters->rand_para_size; i ++)
                                            std::cout << rand_para[i] << " ";
        std::cout << "\n";
        std::cout << "=============================================\n";


    /*Main algorithm*/
        int print_kase = 0;
        while (1){
            /*Condition check*/
                if (curr_t > t_max)         break;
                if (curr_x[0] > 1e15 || curr_x[0] < -1e15)
                                            break;
                     
            /*System Calculator*/
                if (use_maruyama == 0)      ode4(parameters->dim, curr_t, delta_t, curr_x, para, parameters->f);
                else                        maruyama(parameters->dim, parameters->rand_dim, curr_t, delta_t, curr_x, para, rand_para, parameters->f, parameters->rand_f);        
        
            /*OB check and output*/
                if (calc_ob == 1 && curr_t >= t_ob_mark && curr_ob_t >= delta_t_ob){
                    curr_ob_t = 0;
                    for (int i = 0; i < parameters->dim; i ++)
                                            file_ob << curr_x[i] << " ";
                    file_ob << "\n";
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
                }

            /*LE computation*/
                if (calc_le == 1 && curr_t >= t_le_mark){
                                            lya_spec(parameters->dim, curr_x, delta_t, parameters->Jf, eye, spectrum, curr_le_t, para);
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
                }
            /*PS check and output*/
                if (calc_ps == 1 and curr_t > t_ps_mark){
                    ps_print = ps_f(curr_x, ps_print, ps_return);
                    if (ps_print == 1){
                        for (int i = 0; i < parameters->dim; i ++)
                                            file_ps << ps_return[i] << " ";
                        file_ps << "\n";
                    }
                    
                    ps_print = 0;
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
                }

            /*Time iteartion*/
                if (calc_le == 1 && curr_t >= t_le_mark)
                                            curr_le_t += delta_t;
                if (calc_ob == 1 && curr_t >= t_ob_mark)
                                            curr_ob_t += delta_t;
                curr_t += delta_t;
                print_kase += 1;
                if (print_kase % 10000000 == 0){
                    std::cout << curr_t << " " << t_max << " " << ttl_group << " " << curr_x[0] << "\n";
                }
        }

    /*After treatment and le output*/
        // LE OUTPUT
            if (calc_le == 1){
                file_info << "Lyapunov Spectrum: \n";
                for (int i = 0; i < parameters->dim; i ++)
                                            file_info << spectrum[i] << " ";
                file_info << "\n";
            }
        // Saved end Value if system don't save orbit
            file_info << "Final Value: \n";
            for (int i = 0; i < parameters->dim; i ++)
                                        file_info << curr_x[i] << " ";
            file_info << "\n";
        // File close
            file_info.close();
            file_ob.close();
            file_ps.close();
    return ;

}