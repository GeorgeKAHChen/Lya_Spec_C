import numpy as np
from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import cm
import os
from copy import deepcopy


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


def heat_map_dist(file_list, default_ob_use, default_ob_interval, pk_data_files, heat_map_dist_para, default_para_use, name_code_length, tikz_axis):
    
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    if len(default_ob_use) == 3:
        print("ERROR: heat map distribution can only work for 2D")
        return
    
    histograms = []

    use_x = default_ob_use[0]
    use_y = default_ob_use[1]
    use_x_min = default_ob_interval[0][1]
    use_x_max = default_ob_interval[0][2]
    use_y_min = default_ob_interval[1][1]
    use_y_max = default_ob_interval[1][2]

    final_x = []
    final_y = []
    delta_x = (use_x_max - use_x_min) / (heat_map_dist_para[0] - 1)
    delta_y = (use_y_max - use_y_min) / (heat_map_dist_para[1] - 1)

    print("read file and build distribution heat map")

    file_name = file_list[0]
    sys_dim, name_middle_str = info_read(file_name, default_para_use, name_code_length)

    color_map_main = plt.cm.get_cmap(heat_map_dist_para[2])

    for kase in range(0, len(file_list)):
        file_name = file_list[kase] + "_ob.dat"
        print(file_name, end = "\r")
        arr = []
        file = open(file_name, "r")
        cnt = 0
        while 1:
            file_line = file.readline()
            if not file_line:
                break
            arr.append(float(file_line))

        arr_x = arr[sys_dim - use_x: len(arr) - use_x + 1]
        arr_y = arr[sys_dim - use_y: len(arr) - use_y + 1]
        sub_histogram, xedges, yedges = np.histogram2d(arr_x, arr_y, bins=(np.linspace(use_x_min, use_x_max, heat_map_dist_para[0]), np.linspace(use_y_min, use_y_max, heat_map_dist_para[1])), density=True)

        if kase == 0:
            final_x = deepcopy(xedges)
            final_y = deepcopy(yedges)

        sub_final_histogram = []
        color_max = np.max(sub_histogram) + 0.01
        for i in range(0, len(sub_histogram)):
            for j in range(0, len(sub_histogram[i])):
                if sub_histogram[i][j] < 1e-5:
                    continue
                curr_color = color_map_main(min(sub_histogram[i][j] / color_max, 1))
                sub_final_histogram.append([xedges[i], yedges[j], sub_histogram[i][j], curr_color])
                """
                green_change = curr_color[1]
                if green_change >= 20/255:
                    green_change = 1
                else:
                    green_change = green_change / (20/255)
                
                curr_color = (curr_color[0], green_change, curr_color[2], curr_color[3])
                """
        histograms.append(sub_final_histogram)
    print()
    

    print("plot default heat map")
    for kase in range(0, len(histograms)):
        print("plot image code = " + str(kase) , end = "\r")

        fig = plt.figure(constrained_layout=True, figsize=(16, 16))
        ax = plt.subplot(111)
        
        for j in range(0, len(histograms[kase])):
            rect1 = Rectangle((histograms[kase][j][0], histograms[kase][j][1]), delta_x, delta_y, color = histograms[kase][j][3])
            ax.add_patch(rect1)
        
        ax.set_xlim(use_x_min, use_x_max)
        ax.set_ylim(use_y_min, use_y_max)

        if tikz_axis:
            ax.set_xticklabels([])
            ax.set_yticklabels([])
        plt.savefig("imgs/" + str(kase) + ".png")
    print()

    print("read UPO files and plot UPO - dist figure")

    for ttl in range(0, len(pk_data_files)):
        file_name = pk_data_files[ttl]
        file = open(file_name, "r")

        val_k = -1
        UPO_arr = []
        while 1:
            file_line = file.readline()
            if not file_line:
                break
            
            file_line = file_line.split(" ")

            if val_k == -1:
                val_k = int(file_line[-1])
                continue
            tmp_arr = []
            for i in range(0, len(file_line)):
                try:
                    tmp_arr.append(float(file_line[i]))
                except:
                    continue
            UPO_arr.append(tmp_arr)

        os.system("mkdir imgs/UPO_" + str(ttl))

        UPO_prob_dist_x = [n for n in range(len(histograms))]
        for i in range(0, len(UPO_arr)):
            print("current UPO group = " + str(i) + ", total = " + str(len(UPO_arr)), end = "\r")
            
            UPO_prob_dist_y = [0 for n in range(len(histograms))]
            for j in range(0, len(UPO_arr[i])):    
                loc_x = j
                loc_y = j + use_y - use_x
                while 1:
                    if loc_x >= val_k:
                        loc_x -= val_k
                    else:
                        break
                while 1:
                    if loc_y >= val_k:
                        loc_y -= val_k
                    else:
                        break
                while 1:
                    if loc_x < 0:
                        loc_x = val_k + loc_x
                    else:
                        break
                while 1:
                    if loc_y < 0:
                        loc_y = val_k + loc_y
                    else:
                        break            

                for kase in range(0, len(histograms)):
                    for q in range(0, len(histograms[kase])):
                        have_x = False
                        have_y = False
                        if UPO_arr[i][loc_x] >= histograms[kase][q][0] and UPO_arr[i][loc_x] < histograms[kase][q][0] + delta_x:
                            have_x = True
                        if UPO_arr[i][loc_y] >= histograms[kase][q][1] and UPO_arr[i][loc_y] < histograms[kase][q][1] + delta_y:
                            have_y = True
                        if have_x and have_y:
                            UPO_prob_dist_y[kase] += histograms[kase][q][2] * delta_x * delta_y

            fig = plt.figure(constrained_layout=True, figsize=(8, 8))
            ax = plt.subplot(111)
            ax.scatter(UPO_prob_dist_x, UPO_prob_dist_y, color = "red", s = 10)
            ax.set_xlim(0, len(histograms))
            ax.set_ylim(0, max(UPO_prob_dist_y))

            if tikz_axis:
                ax.set_xticklabels([])
                ax.set_yticklabels([])
            plt.savefig("imgs/UPO_" + str(ttl) + "/" + str(i) + ".png")

        print()

    return 



