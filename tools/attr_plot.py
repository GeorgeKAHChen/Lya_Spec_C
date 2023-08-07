import matplotlib.pyplot as plt
import os
import numpy as np

os.system("rm -rf imgs")
os.system("mkdir imgs")



def plot_main(read_file_name, save_file_loc, default_ob_use, default_interval):
    """
    INTIALIZATION
    """
    image_dim = len(default_ob_use)
    data_for_plot = [[] for n in range(image_dim)]



    """
    READ FILE
    """
    file = open(read_file_name, "r")
    print(read_file_name, end = ": ")
    count = 0
    while 1:
        if count >= 500000:
            break
        else:
            count += 1
        line = file.readline()
        if not line:
            break
        line = line.split(" ")
        for i in range(0, len(default_ob_use)):
            data_for_plot[i].append(float(line[default_ob_use[i]]))
    file.close()

    print(len(data_for_plot[0]))
    if image_dim == 2:
        fig = plt.figure(constrained_layout=True, figsize=(8, 8))
        ax = plt.subplot(111)
        ax.scatter(data_for_plot[0], data_for_plot[1], color = "b", s = 0.1)


    else:
        fig = plt.figure(constrained_layout=True, figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(data_for_plot[0], data_for_plot[1], data_for_plot[2], color = "b", s = 0.1)
        ax.view_init(elev=45, azim=135)
        ax.set_zlabel(default_interval[2][0])
        ax.set_zlim(default_interval[2][1], default_interval[2][2])

    ax.set_xlabel(default_interval[0][0])
    ax.set_xlim(default_interval[0][1], default_interval[0][2])
    ax.set_ylabel(default_interval[1][0])
    ax.set_ylim(default_interval[1][1], default_interval[1][2])
    plt.savefig(save_file_loc)

def info_read(file_name, default_para_use):
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

    return len(file_lines[8].split(" ")) - 1, str(float(para[default_para_use[1]]))



def attr_plot(file_list, default_ob_use, default_para_use, default_interval, flag):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    for i in range(0, len(file_list)):
        sys_dim, name_middle_str = info_read(file_list[i], default_para_use)
        
        for j in range(0, len(default_ob_use)):
            if default_ob_use[j] < 0:
                default_ob_use[j] += sys_dim

        read_file_name = file_list[i] + "_" + flag + ".dat" 
        save_file_loc = "imgs/ob_" + name_middle_str + ".png"
        plot_main(read_file_name, save_file_loc, default_ob_use, default_interval)

    return 