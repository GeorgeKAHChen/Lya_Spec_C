import matplotlib.pyplot as plt
import numpy as np
from libpy import Init
import os
import time

#pk_points = [[-1.882237, "r"], [0.802237, "r"], [-0.256994, "b"], [1.336994, "b"]] # 46810 p12
#pk_points = [[-1.882237, "r"], [0.802237, "r"], [0.879851, "b"], [-1.799851, "b"]] # 579 p12
#pk_points = [[1.242996, "g"], [-0.409346, "g"], [1.397173, "g"], [-0.032444, "g"]] # 48 p4

#pk_points = [[-0.256994, "b"], [1.336994, "b"]] # p2 for 6, 10
# p5 for 6
#pk_points = [-1.88223687, "b"], [-1.88223481, "b"], [-1.88216997, "b"], [-1.88216778, "b"], [-1.87992219, "b"], [-1.87991988, "b"], [-1.87985087, "b"], [-1.87984842, "b"], [-1.80231236, "b"], [-1.8023103, "b"], [-1.8022369, "b"], [-1.80223457, "b"], [-1.79985074, "b"], [-1.79984843, "b"], [-1.79977934, "b"], [-1.79977717, "b"], [0.79977749, "b"], [0.79977963, "b"], [0.7998487, "b"], [0.79985084, "b"], [0.80223473, "b"], [0.80223701, "b"], [0.80231043, "b"], [0.80231263, "b"], [0.87984866, "b"], [0.87985089, "b"], [0.87992007, "b"], [0.87992223, "b"], [0.88216798, "b"], [0.88216998, "b"], [0.88223505, "b"], [0.88223674, "b"]
# p4N6
#pk_points = [[-0.455352170851475, "b"], [1.39824080951107, "b"], [0.128435118366160, "b"], [1.19079513573996, "b"]]
#p2N6 + p4N6
#pk_points = [[-0.256994, "r"], [1.336994, "r"], [-0.455352170851475, "orange"], [1.39824080951107, "orange"], [0.128435118366160, "orange"], [1.19079513573996, "orange"]]
# p20N6
#pk_points = [[0.059499939, "b"], [-0.680491794, "b"], [-0.679887847, "b"], [0.337633811, "b"], [-0.3338548, "b"], [1.400279517, "b"], [1.042170923, "b"], [1.10219186, "b"], [1.450394438, "b"], [1.371530268, "b"], [-0.424074342, "b"], [0.311857405, "b"], [0.211799431, "b"], [-0.681819373, "b"], [-0.48712683, "b"], [1.220438531, "b"], [1.446670906, "b"], [1.440192409, "b"], [1.028178388, "b"], [1.327253001, "b"]]
mod_plot = 0 # 0 means off

def x_distribution(file_list, default_para_use, default_x_use, default_x_range, to_data = False, tikz_axis = False):
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
    for kase in range(0, len(file_list)):
        print(file_list[kase], end = ": ")
        # File Name Initialization
        file_name_info = file_list[kase] + ".info"
        file_name_data = file_list[kase]
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
        
        if mod_plot:
            ob_vals_sub =[]
            for i in range(0, len(ob_vals)):
                tmp = 2
                if kase == 1:
                    tmp = 1
                if i % mod_plot == tmp:
                    ob_vals_sub.append(ob_vals[i])
            ob_vals = ob_vals_sub

        print(para, len(ob_vals))
        if not to_data:
            """
            IMAGE GENERATOR
            """
            fig = plt.figure(constrained_layout=True, figsize=(8, 8))
            ax = plt.subplot(111)
            ax.hist(ob_vals, bins = default_x_range[2], range = [default_x_range[0], default_x_range[1]], density=True, color = "black")
            ax.set_xlim([default_x_range[0], default_x_range[1]])
            ax.set_ylim([0, 6])
            try: 
                print(len(pk_points))
            except:
                pass
            else:
                for val in (pk_points):
                    ax.plot([val[0], val[0]], [0, 6], val[1], linewidth = 2)
            ax.set_xlabel("x_1")
            ax.set_ylabel("")
            para = str(para)
            while 1:
                if len(para) < 7:
                    para += "0"
                else:
                    break
            plt.savefig("imgs/" + str(para) + ".png")
            if tikz_axis:
                ax.set_xticklabels()
                ax.set_yticklabels()
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
