#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>

#include "setting_parameters.cpp"

void map_algorithm(struct PARAMETERS *parameters)
{
    /*Define Parameter*/
        // Computation parameter
            long long int curr_t;           // Time parameter(during the iteration)

        // System/OB parameter
            long long int t_ob_mark;
            long double *curr_x;            // current x vector
            long double *para;              // Parameter vector
            long double *rand_para;         // Random parameter vector
            long long int curr_ob_t = 0;

        // LE parameter
            long long int t_le_mark;
            long double *spectrum;          // current spectrum vector
            long double *eye;               // Lyapunov Spectrum iteration matrix
            long long int curr_le_t = 0;



    /*Memory Initialization*/
        // System/OB parameter
            curr_x = (long double*) malloc(parameters->dim * sizeof(long double));
            para = (long double*) malloc(parameters->para_size * sizeof(long double));
            rand_para = (long double*) malloc(parameters->rand_para_size * sizeof(long double));
        
        // LE parameter
            spectrum = (long double*) malloc(parameters->dim * sizeof(long double));
            eye = (long double*) malloc(parameters->dim * parameters->dim * sizeof(long double));



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
            if (calc_ob == 1)               t_ob_mark = step_max * t_ob;

        // LE parameter
            if (calc_le == 1)               t_le_mark = step_max * t_le;



    /*Output Initalization*/
        ttl_group += 1;

        // File name init
            std::stringstream file_str_info;
            std::stringstream file_str_ob;
        
        // File name write
            file_str_info << "output/" << ttl_group << ".info";
            file_str_ob << "output/" << ttl_group << "_ob.dat";

        // File name string init
            std::string file_name_info;
            std::string file_name_ob;

        // File name string build
            file_str_info >> file_name_info;
            file_str_ob >> file_name_ob;

        // File init
            std::ofstream file_info;
            std::ofstream file_ob;

        // File open
            file_info.open(file_name_info, std::ios_base::app);
            file_ob.open(file_name_ob, std::ios_base::app);



    /*Standard data output*/
        file_info << "=============================================\n";
        file_info << "Computation Parameters: \n";
        file_info << "Iteration: delta_t, step_max" << delta_t << " " << step_max << "\n";
        file_info << "LE: compute: " << calc_le << ", t_le: " << t_le << "\n";
        file_info << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", delta_t_ob: " << "N/A" << "\n";
        file_info << "PS: compute: " << "N/A" << "\n";
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
        std::cout << "Iteration: delta_t, step_max" << delta_t << " " << step_max << "\n";
        std::cout << "LE: compute: " << calc_le << ", t_le: " << t_le << "\n";
        std::cout << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", delta_t_ob: " << "N/A" << "\n";
        std::cout << "PS: compute: " << "N/A" << "\n";
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
                if (curr_t > step_max)         break;
                if (curr_x[0] > 1e15 || curr_x[0] < -1e15)
                                            break;
                     
            /*System Calculator*/
                parameters->f(curr_x, curr_x, curr_t, para);
        
            /*OB check and output*/
                if (calc_ob == 1 && curr_t >= t_ob_mark){
                    for (int i = 0; i < parameters->dim; i ++)
                                            file_ob << curr_x[i] << " ";
                    file_ob << "\n";
                }

            /*LE computation*/
                if (calc_le == 1 && curr_t >= t_le_mark)
                                            lya_spec(parameters->dim, curr_x, 1, parameters->Jf, eye, spectrum, curr_le_t, para);

            /*PS check and output*/


            /*Time iteartion*/
                if (calc_le == 1 && curr_t >= t_le_mark)
                                            curr_le_t += 1;
                curr_t += 1;
                print_kase += 1;
                if (print_kase % 10000000 == 0){
                    std::cout << curr_t << " " << step_max << " " << ttl_group << " " << curr_x[0] << "\n";
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

        // File close
            file_info.close();
            file_ob.close();
    return ;
}