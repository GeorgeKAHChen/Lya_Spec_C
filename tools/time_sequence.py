import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init


FONT_SIZE = 6
sys_dim = 6

def time_sequence(file_list, default_x_use, default_x_range):
    
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
            if cnt > 200:
                break

        fig = plt.figure(constrained_layout=True, figsize=(20, 5))
        ax = plt.subplot(111)
        plot_arr_t = arr_t[0: len(arr_x) - sys_dim]
        for i in range(0, sys_dim):
            
            plot_arr_x = arr_x[i: len(arr_x) - sys_dim + i]
            #print(plot_arr_t[0], plot_arr_t[len(plot_arr_t) - 1])
            curr_color = color_map_main(i / (sys_dim-1))
            #ax.plot(plot_arr_t, plot_arr_x, color = curr_color)#, s = 0.1)
            ax.plot(plot_arr_t, plot_arr_x, color = curr_color)#, s = 5)
            break




        ax.set_xlim([plot_arr_t[0], plot_arr_t[len(plot_arr_t) - 1]])
        ax.set_ylim([default_x_range[0], default_x_range[1]])
        #ax.set_ylim([1.1, 1.45])
        #ax.set_ylim([1.3, 1.35])
        plt.savefig("imgs/" + str(kase+1) + ".png")








