import matplotlib.pyplot as plt
import os
import numpy as np
from copy import deepcopy

DOUBLE_LAYER = True
#LAYER_NAME = "results_0810/RGHM_N_10_b_006/1_ob.dat"
LAYER_NAME = "/Users/amakawa/LocalCode/___data/GHM_N_6_151_008_UPO_20_ob.dat"
delay_system = True
local_kase = 1
mod_plot = 4 # 0 means off
def plot_main(sys_dim, read_file_name, save_file_loc, default_ob_use, default_interval, tikz_axis):
    """
    INTIALIZATION
    """
    image_dim = len(default_ob_use)
    data_for_plot = [[] for n in range(image_dim)]
    tmp_data_for_plot = []
    
    """
    READ FILE
    """
    file = open(read_file_name, "r")
    print(read_file_name, end = ": ")
    count = 0
    while 1:
        if count >= int(15000):
            break
        else:
            count += 1
        line = file.readline()
        if not line:
            break
        line = line.split(" ")
        if not delay_system:
            for i in range(0, len(default_ob_use)):
                data_for_plot[i].append(float(line[default_ob_use[i]]))
        else:
            tmp_data_for_plot.append(float(line[0]))
    file.close()

    if delay_system:
        print(sys_dim, end = ", ")
        for i in range(0, len(default_ob_use)):
            data_for_plot[i] = tmp_data_for_plot[sys_dim - default_ob_use[i]: len(tmp_data_for_plot) - default_ob_use[i] + 1]

    print(len(data_for_plot[0]))

    for frame_cnt in range(0, 2000):
        print(frame_cnt)
        plot_back_x = data_for_plot[0][0: (10000 + frame_cnt - 1)]
        plot_back_y = data_for_plot[1][0: (10000 + frame_cnt - 1)]
        fig = plt.figure(constrained_layout=True, figsize=(8, 8))
        ax = plt.subplot(111)
        
        ax.scatter(plot_back_x, plot_back_y, color = "b", s = 0.1)
        ax.scatter([data_for_plot[0][10000 + frame_cnt]], [data_for_plot[1][10000 + frame_cnt]], color = "r", s = 5)
        ax.set_xlim(default_interval[0][1], default_interval[0][2])
        ax.set_ylim(default_interval[1][1], default_interval[1][2])
    
        plt.savefig("imgs/" + str(frame_cnt) + ".png")



def info_read(file_name, default_para_use, name_code_length):
    file = open(file_name + ".info", "r")
    file_lines = []
    while 1:
        file_line = file.readline()
        if not file_line:
            break
        file_lines.append(file_line)
    
    para = ""
    if not default_para_use[0] == "r":
        para = file_lines[10].split(" ")
    else:
        para = file_lines[12].split(" ")

    sys_dim = len(file_lines[8].split(" ")) - 1
    if default_para_use[1] == -1:
        global local_kase
        name_middle_str = str(local_kase)
        local_kase += 1
    else:
        name_middle_str = str(float(para[default_para_use[1]]))
    while 1:
        if len(name_middle_str) < name_code_length:
            name_middle_str += "0"
        else:
            break

    return sys_dim, name_middle_str



def anime(file_list, default_ob_use, default_para_use, default_interval, flag, name_code_length, tikz_axis):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    for i in range(0, len(file_list)):
        sys_dim, name_middle_str = info_read(file_list[i], default_para_use, name_code_length)
        
        for j in range(0, len(default_ob_use)):
            if default_ob_use[j] < 0:
                default_ob_use[j] += sys_dim

        read_file_name = file_list[i] + "_" + flag + ".dat" 
        save_file_loc = "imgs/ob_" + name_middle_str + ".png"
        plot_main(sys_dim, read_file_name, save_file_loc, default_ob_use, default_interval, tikz_axis)

        return 

    return 
