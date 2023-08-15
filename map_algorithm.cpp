#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>

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
            if (calc_ob == 1)               t_ob_mark = (long long int)(step_max * t_ob);

        // LE parameter
            if (calc_le == 1)               t_le_mark = (long long int)(step_max * t_le);

        // PS parameter
            if (calc_ps == 1)               t_ps_mark = (long long int)(step_max * t_ps);


    /*Output Initalization*/
        map_ttl_group += 1;

        // File name init
            std::stringstream file_str_info;
            std::stringstream file_str_ob;
            std::stringstream file_str_ps;
        
        // File name write
            file_str_info << "output/" << map_ttl_group << ".info";
            file_str_ob << "output/" << map_ttl_group << "_ob.dat";
            file_str_ps << "output/" << map_ttl_group << "_ps.dat";

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
        std::cout.precision(10);
        file_info << "=============================================\n";
        file_info << "Computation Parameters: \n";
        file_info << "Iteration: delta_t, t_max: " << 1 << " " << step_max << "\n";
        file_info << "LE: compute: " << calc_le << ", t_le: " << t_le << ", mark:" <<t_ob_mark << "\n";
        file_info << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", mark:" <<t_le_mark << ", delta_t_ob: " << 1 << "\n";
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

        std::cout << "=============================================\n";
        std::cout << "Computation Parameters: \n";
        std::cout << "Iteration: delta_t, t_max: " << 1 << " " << step_max << "\n";
        std::cout << "LE: compute: " << calc_le << ", t_le: " << t_le << ", mark:" <<t_ob_mark << "\n";
        std::cout << "OB: compute: " << calc_ob << ", t_ob: " << t_le << ", mark:" <<t_le_mark << ", delta_t_ob: " << 1 << "\n";
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
                if (use_maruyama == 0)      map_calc(parameters->dim, curr_t, 1, curr_x, para, parameters->f);
                else                        rand_map_calc(parameters->dim, parameters->rand_dim, curr_t, 1, curr_x, para, rand_para, parameters->f, parameters->rand_f);        

            /*OB check and output*/
                if (calc_ob == 1 && curr_t >= t_ob_mark){
                    for (int i = 0; i < parameters->dim; i ++)
                                            file_ob << std::fixed << std::setprecision(10) << curr_x[i] << " ";
                    file_ob << "\n";
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
                }

            /*LE computation*/
                if (calc_le == 1 && curr_t >= t_le_mark){
                                            lya_spec(parameters->dim, curr_x, 1, parameters->Jf, eye, spectrum, curr_le_t, para);
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
                }

            /*PS check and output*/
                if (calc_ps == 1 && curr_t > t_ps_mark){
                    ps_print = ps_f(curr_x, ps_print, ps_return);
                    if (ps_print == 1){
                        for (int i = 0; i < parameters->dim; i ++)
                                            file_ps << std::fixed << std::setprecision(10) << ps_return[i] << " ";
                        file_ps << "\n";
                    }
                    
                    ps_print = 0;
                    if (parameters->rand_para_size == 0 || parameters->rand_dim == 0)
                                            use_maruyama = 0;
                    else                    use_maruyama = 1;
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
        // File close
            file_info.close();
            file_ob.close();
            file_ps.close();
    return ;
}