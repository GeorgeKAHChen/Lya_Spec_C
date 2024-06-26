#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

//#include <chrono>

#include "layer/map_calc.cpp"
#include "layer/rand_map_calc.cpp"
#include "setting_parameters.cpp"
#include "layer/lya_spec.cpp"


int map_ttl_group = 0;    


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


        // LE parameter
            long long int t_le_mark;
            long double *spectrum;          // current spectrum vector
            long double *eye;               // Lyapunov Spectrum iteration matrix
            long long int curr_le_t = 0;

        // PS parameter
            long long int t_ps_mark;
            long double *ps_return;
            int ps_print = -1;

        // BF parameter
            long long int t_bf_mark;
            double bf_distance;
            long long int *bf_output_arr;
            int curr_x_bf_loc;
        // Computation method
            int use_maruyama = 0;

        // Other parameter
            long double *noise_change_mark;
            long long int *noise_change_memo;




    /*Memory Initialization*/
        // System/OB parameter
            curr_x              = (long double*) malloc(parameters->dim * sizeof(long double));
            para                = (long double*) malloc(parameters->para_size * sizeof(long double));
            rand_para           = (long double*) malloc(parameters->rand_para_size * sizeof(long double));
        
        // LE parameter
            spectrum            = (long double*) malloc(parameters->dim * sizeof(long double));
            eye                 = (long double*) malloc(parameters->dim * parameters->dim * sizeof(long double));

        // PS parameter
            ps_return           = (long double*) malloc(parameters->dim * sizeof(long double));

        // BF parameter
            bf_output_arr       = (long long int*) malloc(bf_total_x  * sizeof(long long int));

        // Other parameter 
            noise_change_mark   = (long double*) malloc(NOISE_ADD_RM * sizeof(long double));
            noise_change_memo   = (long long int*) malloc(NOISE_ADD_RM * sizeof(long long int));




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
            if (calc_ob == 1)               t_ob_mark = (long long int)(step_max * t_ob);

        // LE parameter
            if (calc_le == 1)               t_le_mark = (long long int)(step_max * t_le);

        // PS parameter
            if (calc_ps == 1)               t_ps_mark = (long long int)(step_max * t_ps);

        // BF parameter
            if (calc_bf == 1){
                                            t_bf_mark = (long long int)(step_max * t_bf);
                for (int i = 0; i < bf_total_x; i ++){
                                            bf_output_arr[i] = 0;
                }
                                            bf_distance = (bf_x_limit[1] - bf_x_limit[0]) / (bf_total_x - 1);
            }

        // Other parameter
            for (int i = 0; i < NOISE_ADD_RM; i ++){
                noise_change_mark[i] = (long long int)(step_max * noise_change[i]);
                noise_change_memo[i] = 0;
            }


    /*Output Initalization*/
        map_ttl_group += 1;

        // File name init
            std::stringstream file_str_info;
            std::stringstream file_str_ob;
            std::stringstream file_str_ps;
            std::stringstream file_str_bf;
        
        // File name write
            file_str_info << "output/" << map_ttl_group << ".info";
            file_str_ob << "output/" << map_ttl_group << "_ob.dat";
            file_str_ps << "output/" << map_ttl_group << "_ps.dat";
            file_str_bf << "output/" << map_ttl_group << "_bf.dat";

        // File name string init
            std::string file_name_info;
            std::string file_name_ob;
            std::string file_name_ps;
            std::string file_name_bf;

        // File name string build
            file_str_info >> file_name_info;
            file_str_ob >> file_name_ob;
            file_str_ps >> file_name_ps;
            file_str_bf >> file_name_bf;

        // File init
            std::ofstream file_info;
            std::ofstream file_ob;
            std::ofstream file_ps;
            std::ofstream file_bf;

        // File open
            file_info.open(file_name_info, std::ios_base::app);
            file_ob.open(file_name_ob, std::ios_base::app);
            file_ps.open(file_name_ps, std::ios_base::app);
            file_bf.open(file_name_bf, std::ios_base::app);



    /*Standard data output*/
        std::cout.precision(10);
        file_info << "=============================================\n";
        file_info << "Computation Parameters: \n";
        file_info << "Iteration: delta_t, t_max: " << 1 << " " << step_max << "\n";
        file_info << "LE: compute: " << calc_le << ", t_le: " << t_le << ", mark:" <<t_le_mark << "\n";
        file_info << "OB: compute: " << calc_ob << ", t_ob: " << t_ob << ", mark:" <<t_ob_mark << ", delta_t_ob: " << 1 << "\n";
        file_info << "PS: compute: " << calc_ps << ", t_ps: " << t_ps << ", mark:" <<t_ps_mark << "\n";
        file_info << "=============================================\n";
        file_info << "Initial Condition: \n";
        for (int i = 0; i < parameters->dim; i ++)
                                            file_info << std::fixed << std::setprecision(10) << curr_x[i] << " ";
        file_info << "\n";
        file_info << "Parameters: \n";
        for (int i = 0; i < parameters->para_size; i ++)      
                                            file_info << std::fixed << std::setprecision(10) << para[i] << " ";
        file_info << "\n";
        file_info << "Random Parameters: \n";
        for (int i = 0; i < parameters->rand_para_size; i ++)
                                            file_info << std::fixed << std::setprecision(10) << rand_para[i] << " ";
        file_info << "\n";
        file_info << "=============================================\n";
        file_info << "BF: compute: " << calc_bf << ", t_ps: " << t_bf << ", mark:" <<t_bf_mark << "\n";
        file_info << "=============================================\n";

        std::cout << "=============================================\n";
        std::cout << "Computation Parameters: \n";
        std::cout << "Iteration: delta_t, t_max: " << 1 << " " << step_max << "\n";
        std::cout << "LE: compute: " << calc_le << ", t_le: " << t_le << ", mark:" <<t_le_mark << "\n";
        std::cout << "OB: compute: " << calc_ob << ", t_ob: " << t_ob << ", mark:" <<t_ob_mark << ", delta_t_ob: " << 1 << "\n";
        std::cout << "PS: compute: " << calc_ps << ", t_ps: " << t_ps << ", mark:" <<t_ps_mark << "\n";
        std::cout << "=============================================\n";
        std::cout << "Initial Condition: \n";
        for (int i = 0; i < parameters->dim; i ++)
                                            std::cout << std::setprecision(10) << curr_x[i] << " ";
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
        std::cout << "BF: compute: " << calc_bf << ", t_ps: " << t_bf << ", mark:" <<t_bf_mark << "\n";
        std::cout << "=============================================\n";











    /*Main algorithm*/
        int print_kase = 0;
        //auto run_time_mark = std::chrono::high_resolution_clock::now();
        //std::chrono::duration<double> diff;

        while (1){
            /*Condition check*/
                if (curr_t > step_max)      break;
                if (curr_x[0] > 1e15 || curr_x[0] < -1e15)
                                            break;
            /*System Calculator*/
                //if (curr_t > t_ob_mark && curr_t % 10000 == 0)
                //    std::cout << use_maruyama << "\n";
                if (use_maruyama == 0)      map_calc(parameters->dim, curr_t, 1, curr_x, para, parameters->f);
                else                        rand_map_calc(parameters->dim, parameters->rand_dim, curr_t, 1, curr_x, para, rand_para, parameters->f, parameters->rand_f);        
            
            /*Noise Add Check*/
                if (parameters->rand_para_size != 0 and parameters->rand_dim != 0){
                    if (NOISE_ADD_RM > 0){
                        for(int i = 0; i < NOISE_ADD_RM; i ++){
                            if (curr_t >= noise_change_mark[i] && noise_change_memo[i] == 0){
                                use_maruyama = 1 - use_maruyama;
                                noise_change_memo[i] = 1;
                                std::cout << "test: " << use_maruyama << ", " << curr_t << std::endl;
                            }
                        }
                    }
                    else if (curr_t == t_ob_mark || curr_t ==t_le_mark || curr_t == t_ps_mark || curr_t == t_bf_mark){
                        use_maruyama = 1;
                    }
                }

            /*OB check and output*/
                if (calc_ob == 1 && curr_t >= t_ob_mark){
                    if (OB_ONLY_XI){
                                            file_ob << std::fixed << std::setprecision(10) << curr_x[OB_XI_USE] << " ";
                    }
                    else{
                        for (int i = 0; i < parameters->dim; i ++)
                                            file_ob << std::fixed << std::setprecision(10) << curr_x[i] << " ";
                    }
                    file_ob << "\n";
                }

            /*LE computation*/
                if (calc_le == 1 && curr_t >= t_le_mark){
                                            lya_spec(parameters->dim, curr_x, 1, parameters->Jf, eye, spectrum, curr_le_t, para);
                }

            /*PS check and output*/
                if (calc_ps == 1 && curr_t >= t_ps_mark){
                    ps_print = ps_f(curr_x, ps_print, ps_return);
                    if (ps_print >= 1){
                        file_ps << ps_print << " ";
                        for (int i = 0; i < parameters->dim; i ++)
                                            file_ps << std::fixed << std::setprecision(10) << ps_return[i] << " ";
                        file_ps << "\n";
                    }
                    
                    ps_print = 0;
                }
            /*BF check and output*/
                if (calc_bf == 1 && curr_t >= t_bf_mark){
                    curr_x_bf_loc = (int)((curr_x[bf_x_use] - bf_x_limit[0]) / bf_distance);
                    if (curr_x_bf_loc >= 0 && curr_x_bf_loc < bf_total_x)
                                            bf_output_arr[curr_x_bf_loc] += 1;
                }

            /*Time iteartion*/
                if (calc_le == 1 && curr_t >= t_le_mark)
                                            curr_le_t += 1;


                curr_t += 1;
                print_kase += 1;
                if (print_kase % 10000000 == 0){
                    //diff =  std::chrono::high_resolution_clock::now() - run_time_mark;
                    std::cout << curr_t << " " << step_max << " " << map_ttl_group << " " << curr_x[0] << "\n";// << " " << diff.count() << "\n";
                    //run_time_mark = std::chrono::high_resolution_clock::now();
                }
        }

    /*After treatment and le output*/
        // LE OUTPUT
            if (calc_le == 1){
                file_info << "Lyapunov Spectrum: \n";
                for (int i = 0; i < parameters->dim; i ++)
                                            file_info <<  std::setprecision(10) << spectrum[i] << " ";
                file_info << "\n";
            }
        // Saved end Value if system don't save orbit
            file_info << "Final Value: \n";
            for (int i = 0; i < parameters->dim; i ++)
                                            file_info << std::setprecision(10) << curr_x[i] << " ";
            file_info << "\n";
        // BF OUTPUT
            if (calc_bf == 1){
                file_bf << std::setprecision(10) << bf_x_limit[0] << " " << bf_x_limit[1] << " " << bf_total_x << "\n";
                for (int i = 0; i < bf_total_x; i ++)
                                            file_bf << std::setprecision(10) << bf_output_arr[i] << "\n";
            }
        // File close
            file_info.close();
            file_ob.close();
            file_ps.close();
    return ;
}