import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init


FONT_SIZE = 6
sub_mod = 0 # 0 off

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
            if cnt > 10000:
                break

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
            if sub_mod == 0:
                curr_color = color_map_main(i / (default_t_mod-1))
                ax.scatter(plot_arr_t, plot_arr_x, color = "black", s = 5)
                #ax.plot(plot_arr_t, plot_arr_x, color = curr_color)#, s = 5)
            else:
                sub_plot_arr_t = [[] for n in range(sub_mod)]
                sub_plot_arr_x = [[] for n in range(sub_mod)]
                for j in range(0, len(plot_arr_t)):
                    sub_plot_arr_t[j % sub_mod].append(plot_arr_t[j])
                    sub_plot_arr_x[j % sub_mod].append(plot_arr_x[j])
                #print(sub_plot_arr_t[0])
                for j in range(0, sub_mod):
                    curr_color = color_map_main(j / (sub_mod-1))
                    ax.plot(sub_plot_arr_t[j], sub_plot_arr_x[j], color = curr_color)#, s = 1)

        #break
        ax.set_xlim([0, cnt])
        ax.set_ylim([default_x_range[0], default_x_range[1]])
        plt.savefig("imgs/" + str(kase+1) + ".png")








