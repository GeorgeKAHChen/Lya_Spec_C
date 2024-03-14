import matplotlib.pyplot as plt
import numpy as np
from libpy import Init
import os


def bf_2_img(file_list):
    """
    PARAMETER DEFINITION
    """
    bf_2_img_init = False
    bf_data_arr = []
    bf_x_arr = []
    len_bf_arr = 0
    for kase in range(0, len(file_list)):
        file_name = file_list[kase] + "_bf.dat"
        print(file_name)
        file = open(file_name, "r")
        line = file.readline()
        """
        if not bf_2_img_init:
            bf_2_img_init = True
            line = line.split(" ")
            bf_x_arr = np.linspace(float(line[0]), float(line[1]), int(line[2]))
            len_bf_arr = int(line[2])
        """
        bf_x_arr_sub = []
        bf_x_ttl = 0
        
        while 1:
            line = file.readline()
            if not line:
                break
            bf_x_arr_sub.append(int(line))
            bf_x_ttl = max(bf_x_ttl, int(line))

        for i in range(0, len(bf_x_arr_sub)):
            #val = 255
            #if bf_x_arr_sub[i] != 0:
            #    val = 127
            #    val -= (bf_x_arr_sub[i] / bf_x_ttl) * 127
            bf_x_arr_sub[i] = (1 - bf_x_arr_sub[i] / bf_x_ttl) * 255
        bf_x_arr.append(bf_x_arr_sub)
    bf_x_arr = np.array(bf_x_arr)
    bf_x_arr = np.fliplr(bf_x_arr).T
    print(bf_x_arr)
    Init.ImageIO(file_dir = "tmp_bf.png", img = np.float32(bf_x_arr), io = "o", mode = "grey", backend = "opencv")
    os.system("open tmp_bf.png")

