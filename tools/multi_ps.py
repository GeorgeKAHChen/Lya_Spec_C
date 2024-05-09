import matplotlib.pyplot as plt
import os
import numpy as np


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

    name_middle_str = str(float(para[default_para_use[1]]))
    while 1:
        if len(name_middle_str) < name_code_length:
            name_middle_str += "0"
        else:
            break

    return sys_dim, name_middle_str



def multi_ps(file_list, default_para_use, default_interval, name_code_length):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    for i in range(0, len(file_list)):
        title_name = file_list[i]
        _, name_middle_str = info_read(title_name, default_para_use, name_code_length)

        file_name = title_name + "_ps.dat"
        file = open(file_name, "r")

        plot_data = []
        ps_code = []
        while 1:
            file_line = file.readline()
            if not file_line:
                break

            file_line = file_line.split(" ")
            save_ps_code = -1
            for i in range(0, len(ps_code)):
                if ps_code[i] == file_line[0]:
                    save_ps_code = i

            if save_ps_code == -1:
                save_ps_code = len(ps_code)
                ps_code.append(file_line[0])
                plot_data.append([[], []])

            #plot_data[save_ps_code][0].append(float(file_line[(int(file_line[0])+1) % 10]))
            #plot_data[save_ps_code][1].append(float(file_line[(int(file_line[0])+2) % 10]))
            plot_data[save_ps_code][0].append(float(file_line[1]))
            plot_data[save_ps_code][1].append(float(file_line[3]))

        file.close()

        print(file_name, end = ": ")

        for j in range(0, len(plot_data)):
            print(ps_code[j] + ": " + str(len(plot_data[j][0])), end = ", ")

            output_name = "imgs/ps_" +  ps_code[j] + "_" + name_middle_str + ".png"
            
            fig = plt.figure(constrained_layout=True, figsize=(8, 8))
            ax = plt.subplot(111)
            ax.scatter(plot_data[j][0], plot_data[j][1], color = "b", s = 0.1)
            #ax.set_xlim(default_interval[0][1], default_interval[0][2])
            ax.set_xlabel("x_1")
            #ax.set_ylim(default_interval[1][1], default_interval[1][2])
            ax.set_ylabel("x_" + ps_code[j])
            plt.savefig(output_name)

        print()

    return 









