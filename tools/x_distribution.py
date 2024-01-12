import matplotlib.pyplot as plt
import numpy as np
from libpy import Init
import os
import time

def x_distribution(file_list, default_para_use, default_x_use, default_x_range, to_data = False):
    if not to_data:
        os.system("rm -rf imgs")
        os.system("mkdir imgs")
    else:
        os.system("rm -rf ./distribution.dat")

    """
    PARAMETER DEFINITION
    """
    sys_dim = -1
    x_minn_val = 0
    x_maxx_val = 0
    x_ttl = 0


    """
    INITIALIZATION
    """
    if default_para_use[0] == "r":
        sys_rand = True
    file = open(file_list[0] + ".info", "r")
    file_lines = []
    while 1:
        file_line = file.readline()
        if not file_line:
            break
        file_lines.append(file_line)
    sys_dim = len(file_lines[8].split(" ")) - 1




    """
    MAIN ITERATION
    """
    for i in range(0, len(file_list)):
        print(file_list[i], end = ": ")
        # File Name Initialization
        file_name_info = file_list[i] + ".info"
        file_name_data = file_list[i]
        file_name_data += "_ob"
        file_name_data += ".dat"

        # Read Parameter
        file = open(file_name_info, "r")
        file_lines = []
        while 1:
            line = file.readline()
            if not line:
                break
            file_lines.append(line)
        file.close()

        if default_para_use[0] != "r":
            para = file_lines[10].split(" ")
            para = float(para[default_para_use[1]])
        else:
            para = file_lines[12].split(" ")
            para = float(para[default_para_use[1]])

        

        # Read Data
        file = open(file_name_data, "r")
        ob_vals = []
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.split(" ")
            ob_vals.append(float(line[default_x_use]))
        print(para, len(ob_vals))

            
        if not to_data:
            """
            IMAGE GENERATOR
            """
            fig = plt.figure(constrained_layout=True, figsize=(8, 8))
            ax = plt.subplot(111)
            ax.hist(ob_vals, bins = default_x_range[2], range = [default_x_range[0], default_x_range[1]], density=True)
            ax.set_ylim([0, 10])
            ax.set_xlabel("x_1")
            ax.set_ylabel("")
            para = str(para)
            while 1:
                if len(para) < 7:
                    para += "0"
                else:
                    break
            plt.savefig("imgs/" + str(para) + ".png")

        else:
            hist, bin_edges = np.histogram(ob_vals, bins=default_x_range[2], range = [default_x_range[0], default_x_range[1]], density=True)
            if not os.path.exists("./distribution.dat"):
                save_file_name = "./distribution.dat"
                save_file = open(save_file_name, "w")
                save_strings = ""
                for ttl in range(0, len(bin_edges)):
                    save_strings += str(bin_edges[ttl])
                    save_strings += " "
                save_strings += "\n"
                save_file.write(save_strings)
                save_file.close()


            save_file_name = "./distribution.dat"
            save_file = open(save_file_name, "a")
            save_strings = str(para) + " "
            for ttl in range(0, len(hist)):
                save_strings += str(hist[ttl])
                save_strings += " "
            save_strings += "\n"
            save_file.write(save_strings)
            save_file.close()
