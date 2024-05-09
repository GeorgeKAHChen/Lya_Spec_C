tikz_axis               = False


"""
[MAIN] parameter
"""

#default_folder          = ["std_ob"]
#default_file_code       = [[5, 5]]
#default_folder          = ["w_wo_noise"]
#default_file_code       = [[1, 4]]
default_folder          = ["output"]
default_file_code       = [[1, 5]]
#default_para_use        = ["r", 0]
default_para_use        = ["r", 0]
default_x_use           = 0 # From 0

default_x_range         = [0, 1, 400]
#default_x_range         = [1.1, 1.45, 5001]
default_t_mod           = 4
default_ob_use          = [1, 2]    # from 1
default_ob_interval     = [["x", -1.5, 1.5], ["y", -1.5, 1.5]]
#default_ob_interval     = [["x", 1, 1.6], ["y", -0.6, 0.6]]
default_ps_use          = [2, 3, 4]
default_ps_interval     = [["x", -2, 2], ["y", -2, 2], ["z", -2, 2]]
name_code_length        = 5 #include a.cde -> 5 


"""
[FULL] curve plot parameter (le_dky_hks_bf_dist plot)
"""
ax_will_plot            = [1,   #ax_le
                           1,   #ax_D_ky
                           1,   #ax_H_ks
                           0,   #ax_dist
                           0,   #ax_bf
                        ]
#default_le_file         = "/Users/amakawa/LocalCode/___data/a_145_155_b_008_simga_000_1.dat"
default_le_file         = "/Users/amakawa/LocalCode/___data/RGHM_a_151_b_008_new_LE.dat"
#default_le_file         = "/Users/amakawa/LocalCode/Lya_Spec_C/tools_other/tmp.dat"
default_dist_file       = "/Users/amakawa/LocalCode/___data/RGHM_a_151_b_008_new_dist.dat"
bf_merge                = True






"""
[HEAT MAP] plot parameter (le_dky_hks heat map - 2d)
"""

"""
## [b-simga]: fix a 
le_file_folder          = ["/Users/amakawa/LocalCode/___data/results_240117_nf/a_151_1",
                           "/Users/amakawa/LocalCode/___data/results_240117_nf/a_151_2"]
le_file_code            = [[1, 8], [1, 10]]
le_para_use             = [[1, 0.05, 0.11, 0.0002], [2, 0.00, 0.35, 0.001]] #from 0
"""

"""
## [a-sigma]: fix b
le_file_folder          = ["/Users/amakawa/LocalCode/___data/results_240117_nf/b_080_2"]
le_file_code            = [[1, 12]]
le_para_use             = [[0, 1.2, 1.6, 0.002], [2, 0.00, 0.35, 0.001]] #from 0
"""

## [a-b]: fix sigma
le_file_folder          = ["/Users/amakawa/LocalCode/___data/RGHM_sigma_002_LE"]
le_file_code            = [[1, 1]]
le_para_use             = [[0, 1.2, 1.8, 0.002], [1, 0.05, 0.11, 0.0002]] #from 0



## [others]
le_start                = 3         # from 0
le_color_table          = [["jet", 0.00], ["jet", 0.11], ["jet", 0.22], ["jet", 0.33], 
                           ["jet", 0.44], ["jet", 0.55], ["jet", 0.66], ["jet", 0.77],
                           ["jet", 0.88], ["jet", 1.00], ["rgba", (1.0, 1.0, 1.0, 1.0)]]
heat_map_table          = "jet"

"""
[False, _] or [True, i], and i-th parameter will be used x-axis, i should include in le_para_use
"""




"""
Power spectrum parameter group
"""
power_spectrum_para     = [100000000,               # Total time sequence use
                           [0, 0.5],            # x-axis lim
                           [1e1, 1e7],                # y-axis lim
                           "1"                      # "1" means plot all ps in one figure, "n" means plot ps in different figure 
                          ]



"""
2-d distribution and UPO
"""
heat_map_dist_para      = [int(5e2),                # x-axis nodes
                           int(5e2),                # y-axis nodes
                           'jet'                    # heat map color
                          ]
pk_data_files           = [
                           "/Users/amakawa/LocalCode/___data/pk_6/pk_6_1.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_2.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_3.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_4.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_5.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_6.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_7.dat", 
                           #"/Users/amakawa/LocalCode/___data/pk_6/pk_6_8.dat"
                           ]




