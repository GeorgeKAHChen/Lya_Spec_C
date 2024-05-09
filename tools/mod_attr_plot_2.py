import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init


FONT_SIZE = 6

def mod_attr_plot_2(file_list, default_x_use, default_x_range, default_t_mod):
    
    os.system("rm -rf imgs")
    os.system("mkdir imgs")
    
    color_map_main = plt.cm.get_cmap('jet')
    for kase in range(0, len(file_list)):
        read_file_name = file_list[kase] + "_ob.dat"
        file = open(read_file_name, "r")
        print(read_file_name)

        arr_t = []
        arr_x = []
        cnt = 0

        while 1:
            line = file.readline()
            if not line:
                break
            line = line.split(" ")

            try:
                arr_x.append(float(line[default_x_use]))
            except:
                break

            arr_t.append(cnt)
            cnt += 1

        loc = 0
        fig = plt.figure(constrained_layout=True, figsize=(20, 5))
        ax = plt.subplot(111)
        for i in range(0, default_t_mod):
            plot_arr_t = []
            plot_arr_x = []
            loc += 10
            for j in range(0, len(arr_x)):
                if arr_t[j] % default_t_mod == i:
                    plot_arr_t.append(arr_t[j])
                    plot_arr_x.append(arr_x[j])

            curr_color = color_map_main(i / (default_t_mod-1))
            ax.scatter(plot_arr_t, plot_arr_x, color = curr_color, s = 0.1)
        ax.set_xlim([0, cnt])
        ax.set_ylim([default_x_range[0], default_x_range[1]])
        plt.savefig("imgs/" + str(kase+1) + ".png")








