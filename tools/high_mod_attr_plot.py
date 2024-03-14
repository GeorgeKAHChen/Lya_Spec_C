import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init


FONT_SIZE = 6
FOR_TEST = True
def high_mod_attr_plot(file_list, default_x_use, default_x_range, default_t_mod):
    
    os.system("rm -rf imgs")
    os.system("mkdir imgs")
    
    size_a = (default_t_mod+1)*10-2
    
    for kase in range(0, len(file_list)):
        read_file_name = file_list[kase] + "_ob.dat"
        file = open(read_file_name, "r")
        os.system("mkdir imgs/" + str(kase+1))
        print(read_file_name)

        arr_t = [[] for n in range(default_t_mod)]
        arr_x = [[] for n in range(default_t_mod)]
        cnt = 0

        while 1:
            if cnt % 100000 == 0:
                print(cnt, end = "\r")
            if FOR_TEST and cnt == 1000000:
                break
            line = file.readline()
            if not line:
                break
            line = line.split(" ")

            try:
                arr_x[cnt % default_t_mod].append(float(line[default_x_use]))
            except:
                break

            arr_t[cnt % default_t_mod].append(cnt)
            cnt += 1
        print(cnt)
        for i in range(0, default_t_mod):
            print(i, end = "\r")
            fig = plt.figure(constrained_layout=True, figsize=(20, 5))
            ax = plt.subplot(111)
            ax.scatter(arr_t[i], arr_x[i], s = 0.1)
            ax.set_ylim(default_x_range[0], default_x_range[1])
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            plt.savefig("imgs/" + str(kase+1) + "/" + str(i) +".png")
        print()







