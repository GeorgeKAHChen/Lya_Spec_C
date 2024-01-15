import matplotlib.pyplot as plt
import numpy as np
from libpy import Init
import os


def order_bf(file_list, default_para_use, default_x_use, default_x_range):
    """
    PARAMETER DEFINITION
    """
    sys_dim = -1
    sys_rand = False
    is_map = False
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

    if default_para_use[0] == "r":
        sys_rand = True

    if int(file_lines[2].split(" ")[3]) == 1:
        is_map = 1
    else:
        is_map = 0

    x_minn_val, x_maxx_val, x_ttl = default_x_range



    """
    MAIN ITERATION
    """
    # Init
    img = [[] for n in range(x_ttl + 5)]
    delta_val = (x_maxx_val - x_minn_val + 1e-4)/x_ttl


    for i in range(0, len(file_list)):
        #if i % 5 != 0:
        #    continue
        # File Name Initialization
        file_name_data = file_list[i]
        if is_map:
            file_name_data += "_ob"
        else:
            file_name_data += "_ps"
        file_name_data += ".dat"



        # Read Data
        file = open(file_name_data, "r")
        bf_vals = []
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.split(" ")
            bf_vals.append(float(line[default_x_use]))
        print(file_name_data, len(bf_vals))

        

        # Image plot
        tmp_img = [255 for n in range(x_ttl + 5)]
        for j in range(0, len(bf_vals)):
            real_j = int((bf_vals[j] - x_minn_val)/delta_val)
            if real_j >= 0 and real_j <= x_ttl:
                tmp_img[x_ttl - real_j] = 0
        for j in range(0, len(tmp_img)):
            img[j].append(tmp_img[j])

    Init.ImageIO(file_dir = "tmp_bf.png", img = np.float32(img), io = "o", mode = "grey", backend = "opencv")
    os.system("open tmp_bf.png")

