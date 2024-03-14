tikz_axis               = True


"""
[MAIN] parameter
"""

default_folder          = ["./output"]
default_file_code       = [[1, 101]]
#default_para_use        = ["r", 0]
default_para_use        = ["", 0]
default_x_use           = 0 # From 0

default_x_range         = [-1, 1.6, 400]
#default_x_range         = [1.1, 1.45, 5001]
default_t_mod           = 4
default_ob_use          = [0, 1]
default_ob_interval     = [["x_1", -1, 1.6], ["x_2", -1, 1.6], ["x_10", -2, 2]]
#default_ob_interval     = [["x", 1, 1.6], ["y", -0.6, 0.6]]
default_ps_use          = [0, -1, -2]
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
default_le_file         = "/Users/amakawa/LocalCode/___data/a_145_155_b_008_simga_000_1.dat"
#default_le_file         = "/Users/amakawa/LocalCode/Lya_Spec_CPP/tools_other/tmp.dat"
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
power_spectrum_para     = [524288,             # Total time sequence use
                           [0.0, 0.51],     # x-axis lim
                           [1e-40, 1e20]     # y-axis lim
                          ]

