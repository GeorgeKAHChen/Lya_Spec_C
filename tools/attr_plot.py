import matplotlib.pyplot as plt
import os
import numpy as np
from copy import deepcopy

def plot_main(sys_dim, read_file_name, save_file_loc, default_ob_use, default_interval, tikz_axis, plot_ob_parameters, delay_system):


    DOUBLE_LAYER = plot_ob_parameters[0]
    LAYER_NAME = plot_ob_parameters[1]
    mod_plot = plot_ob_parameters[2][0]
    local_kase = plot_ob_parameters[2][1]
    td_plot_angle = plot_ob_parameters[3]

    

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
        if count >= int(50000):
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
    if mod_plot > 0:
        mod_data_for_plot = [[] for n in range(len(data_for_plot))]
        for i in range(0, len(data_for_plot[0])):
            if i % mod_plot == 2:
                for j in range(0, len(mod_data_for_plot)):
                    mod_data_for_plot[j].append(data_for_plot[j][i])
        data_for_plot = mod_data_for_plot

    print(len(data_for_plot[0]))
    if image_dim == 2:
        fig = plt.figure(constrained_layout=True, figsize=(8, 8))
        ax = plt.subplot(111)
        ax.scatter(data_for_plot[0], data_for_plot[1], color = "black", s = 0.1)


    else:
        if tikz_axis:
            fig = plt.figure(constrained_layout=True, figsize=(20, 20))
        else:
            fig = plt.figure(constrained_layout=True, figsize=(12, 12))
        fig.subplots_adjust( left=None, bottom=None,  right=None, top=None, wspace=None, hspace=None)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(data_for_plot[0], data_for_plot[1], data_for_plot[2], color = "black", s = 0.1)
        ax.view_init(elev=td_plot_angle[0], azim=td_plot_angle[1])
        if tikz_axis:
            ax.set_zticklabels([])
        else:
            ax.set_zlabel("\n" + default_interval[2][0], fontsize = 12)
        ax.set_zlim(default_interval[2][1], default_interval[2][2])

    if tikz_axis:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    else:
        ax.set_xlabel(default_interval[0][0], fontsize = 12)
        ax.set_ylabel(default_interval[1][0], fontsize = 12)
    ax.set_xlim(default_interval[0][1], default_interval[0][2])
    ax.set_ylim(default_interval[1][1], default_interval[1][2])
    if DOUBLE_LAYER:
        for double_layer_name in LAYER_NAME:
            File2 = open(double_layer_name[0], "r")
            old_data_for_plot = [[] for n in range(len(default_ob_use))]
            count = 0
            while 1:
                if count >= int(1e3):
                    break
                else:
                    count += 1
                line = File2.readline()
                if not line:
                    break
                line = line.split(" ")
                if delay_system:
                    for i in range(0, len(default_ob_use)):
                        old_data_for_plot[i].append(float(line[0]))
                else:                
                    for i in range(0, len(default_ob_use)):
                        old_data_for_plot[i].append(float(line[default_ob_use[i]]))
            if delay_system:
                for i in range(0, len(default_ob_use)):
                    #print(sys_dim - default_ob_use[i], len(old_data_for_plot[i]) - default_ob_use[i] + 1)
                    old_data_for_plot[i] = old_data_for_plot[i][sys_dim - default_ob_use[i]: len(old_data_for_plot[i]) - default_ob_use[i] + 1]

            if image_dim == 2:
                print(len(old_data_for_plot[0]))
                ax.scatter(old_data_for_plot[0], old_data_for_plot[1], color = double_layer_name[1], s = 500, marker = "1")
            else:
                ax.scatter3D(old_data_for_plot[0], old_data_for_plot[1], old_data_for_plot[2], color = double_layer_name[1], s = 500, marker ="1")
            File2.close()
    #plt.show()
    plt.savefig(save_file_loc)



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



def attr_plot(file_list, default_ob_use, default_para_use, default_interval, flag, name_code_length, tikz_axis, plot_ob_parameters, delay_system):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    for i in range(0, len(file_list)):
        sys_dim, name_middle_str = info_read(file_list[i], default_para_use, name_code_length)
        
        for j in range(0, len(default_ob_use)):
            if default_ob_use[j] < 0:
                default_ob_use[j] += sys_dim

        read_file_name = file_list[i] + "_" + flag + ".dat" 
        save_file_loc = "imgs/ob_" + name_middle_str + ".png"
        plot_main(sys_dim, read_file_name, save_file_loc, default_ob_use, default_interval, tikz_axis, plot_ob_parameters, delay_system)

    return 
