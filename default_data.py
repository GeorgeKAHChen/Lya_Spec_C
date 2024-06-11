tikz_axis               = True


"""
[MAIN] parameter
"""
delay_system = True

#default_folder          = ["std_ob"]
#default_file_code       = [[5, 5]]
#default_folder          = ["w_wo_noise"]
#default_file_code       = [[1, 4]]
default_folder          = ["/Users/amakawa/LocalCode/___data/GHM_N_6_151_008_ob" for n in range(3)]
#default_folder          = ["output", "output", "output", "output", "output", "output"]
default_file_code       = [[1, 1], [2, 2], [5, 5]]
#default_file_code       = [[1, 20], [21, 40], [41, 60], [61, 80], [81, 100], [101, 120]]
#default_para_use        = ["r", 0]
default_para_use        = ["r", 0]
default_x_use           = 0 # From 0

default_x_range         = [-2, 2, 400]
#default_x_range         = [1.1, 1.45, 400]
default_t_mod           = 2
default_ob_use          = [6, 1, 5]    # from 1
default_ob_interval     = [["x6", -2, 2], ["x1", -2, 2], ["x5", -2, 2]]
#default_ob_interval     = [["x6", -0.75, 1.75], ["x1", -0.75, 1.75], ["x5", -0.75, 1.75]]
#default_ob_interval     = [["x", 1, 1.6], ["y", -0.6, 0.6]]
default_ps_use          = [2, 3, 4]
default_ps_interval     = [["x", -2, 2], ["y", -2, 2], ["z", -2, 2]]
name_code_length        = 5 #include a.cde -> 5 

"""
[OB] plot ob parameters
"""
plot_ob_parameters      = [False, # Double layers
                           [
                                ["/Users/amakawa/LocalCode/___data/GHM_N_6_151_008_UPO_4_ob.dat", "orange"], 
                                ["/Users/amakawa/LocalCode/___data/GHM_N_6_151_008_UPO_2_ob.dat", "r"]
                           ], # double layers name and color
                           [0, 1], # mod plot, mod start
                           [30, 0] # 3d_plot_angle: elev, azim
                        ]



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
default_le_file         = "/Users/amakawa/LocalCode/___data/RGHM_N_6_a_151_b_008_new_LE.dat"
#default_le_file         = "/Users/amakawa/LocalCode/Lya_Spec_C/tools_other/tmp.dat"
default_dist_file       = "/Users/amakawa/LocalCode/___data/RGHM_a_151_b_008_new_dist.dat"
bf_merge                = True
full_plot_parameters    = [[0, 0.1], # x-range
                           [-0.03, 0.06], #le_1 range
                           [-2.75, -2.5], #le_2 range
                           [4.4, 5.1], #d_ky y range
                           [0.00, 0.2], #h_ks y range
                        ]




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
le_file_folder          = ["/Users/amakawa/LocalCode/___data/RGHM_N_6_sigma_020"]
le_file_code            = [[1, 1]]
le_para_use             = [[0, 1.2, 1.8, 0.002], [1, 0.05, 0.11, 0.0002]] #from 0



## [others]
le_start                = 3         # from 0
le_color_table          = [["jet", 0.00], ["jet", 0.2], ["jet", 0.4], ["jet", 0.6], 
                           ["jet", 0.8], ["jet", 1.0], ["rgba", (1.0, 1.0, 1.0, 1.0)]]
heat_map_table          = "jet"

"""
[False, _] or [True, i], and i-th parameter will be used x-axis, i should include in le_para_use
"""




"""
Power spectrum parameter group
"""
power_spectrum_para     = [100000000,               # Total time sequence use
                           [-0.001, 0.501],            # x-axis lim
                           [1e-14, 1e-2],                # y-axis lim
                           "n"                      # "1" means plot all ps in one figure, "n" means plot ps in different figure 
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




