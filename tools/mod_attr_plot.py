import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init


FONT_SIZE = 6

def mod_attr_plot(file_list, default_x_use, default_x_range, default_t_mod):
    
    os.system("rm -rf imgs")
    os.system("mkdir imgs")
    
    size_a = (default_t_mod+1)*10-2

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
        fig = plt.figure(constrained_layout=True, figsize=(20, 3 * (default_t_mod + 1)))
        plt.rcParams.update({'font.size': FONT_SIZE})
        ax   = plt.subplot2grid(shape=(size_a, 1), loc=(loc, 0), rowspan = 10, colspan = 1)
        ax.scatter(arr_t, arr_x, s = 0.1)
        ax.set_ylim(default_x_range[0], default_x_range[1])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        for i in range(0, default_t_mod):
            plot_arr_t = []
            plot_arr_x = []
            loc += 10
            for j in range(0, len(arr_x)):
                if arr_t[j] % default_t_mod == i:
                    plot_arr_t.append(arr_t[j])
                    plot_arr_x.append(arr_x[j])
            exec("ax"+str(i)+" = plt.subplot2grid(shape=(size_a, 1), loc=(loc, 0), rowspan = 10, colspan = 1)")
            exec("ax"+str(i)+".scatter(plot_arr_t, plot_arr_x, s = 0.1)")
            exec("ax"+str(i)+".set_ylim(default_x_range[0], default_x_range[1])")
            exec("ax"+str(i)+".set_xticklabels([])")
            exec("ax"+str(i)+".set_yticklabels([])")
        plt.savefig("imgs/" + str(kase+1) + ".png")








