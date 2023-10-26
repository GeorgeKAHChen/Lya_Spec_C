import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.gridspec import GridSpec
from copy import deepcopy
import time
# png2mp4
# ffmpeg -r 15 -s 1920x1080 -pattern_type glob -i 'imgs/ob_0.*.png' -vcodec libx264 -crf 22 video.mp4 -y


global LAYER_NAME
LAYER_NAME = "1_ob.dat"
le_max = 0.02
le_min = -0.02
sub_img_int = [[-0.3, 0.3], [-0.3, 0.3]]

img_x = 0
img_y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
main_plot_x = 9
main_plot_y = 1
def get_le_list(file_list, default_para_use):
    """
    PARAMETER DEFINITION
    """
    para_list = []
    le_list = []
    sys_dim = -1
    sys_rand = False
    para_loc = default_para_use[1]



    """
    INITIALIZATION
    """
    file = open(file_list[0] + ".info", "r")
    file_lines = []
    while 1:
        file_line = file.readline()
        if not file_line:
            break
        file_lines.append(file_line)
    sys_dim = len(file_lines[8].split(" ")) - 1
    
    for i in range(0, sys_dim):
        le_list.append([])

    if default_para_use[0] == "r":
        sys_rand = True



    """
    GET LE FROM FILE
    """
    for i in range(0, len(file_list)):
        file = open(file_list[i] + ".info", "r")
        print("le: " + file_list[i] + ".info")
        
        file_lines = []
        while 1:
            line = file.readline()
            if not line:
                break
            file_lines.append(line)

        file.close()

        if not sys_rand:
            para = file_lines[10].split(" ")
            para[para_loc] = para[para_loc][:-1]
            para_list.append(float(para[para_loc]))
        else:
            para = file_lines[12].split(" ")
            para_list.append(float(para[para_loc]))

        le = file_lines[15]
        le = le[:-1]

        le = le.split(" ")

        for i in range(0, sys_dim):
            le_list[i].append(float(le[i]))

    return para_list, le_list


def plot_main(read_file_name, save_file_loc, default_ob_use, default_interval, para_list, le_list, curr_para, le_str, sys_dim):
    """
    INTIALIZATION
    """
    image_dim = len(default_ob_use)
    data_for_plot = [[] for n in range(sys_dim)]



    """
    READ FILE
    """
    file = open(read_file_name, "r")
    print(read_file_name, end = ": ")
    print(LAYER_NAME)
    count = 0
    while 1:
        if count >= 100001:
            break
        else:
            count += 1
        line = file.readline()
        if not line:
            break
        line = line.split(" ")
        #print(line)
        #for i in range(0, len(default_ob_use)):
        #    data_for_plot[i].append(float(line[default_ob_use[i]]))
        for i in range(0, sys_dim):
            #print(i)
            data_for_plot[i].append(float(line[i]))
    file.close()

    file_2 = open(LAYER_NAME, "r")
    old_data_for_plot = [[] for n in range(sys_dim)]
    count = 0
    while 1:
        if count >= 500000:
            break
        else:
            count += 1
        line = file_2.readline()
        if not line:
            break
        line = line.split(" ")
        for i in range(0, sys_dim):
            old_data_for_plot[i].append(float(line[i]))
    file_2.close()


    fig  = plt.figure(constrained_layout=True, figsize=(18, 9))
    fig.suptitle('sigma = ' + str(curr_para) + ", LE = " + le_str)
    ax1  = plt.subplot2grid(shape=(3, 18), loc=(0, 0), colspan = 6)
    ax2  = plt.subplot2grid(shape=(3, 18), loc=(0, 6), colspan = 2)
    ax3  = plt.subplot2grid(shape=(3, 18), loc=(1, 0), colspan = 4, rowspan = 2)
    ax4  = plt.subplot2grid(shape=(3, 18), loc=(1, 4), colspan = 4, rowspan = 2)

    ax12 = plt.subplot2grid(shape=(3, 18), loc=(0,  9), colspan = 3)
    ax13 = plt.subplot2grid(shape=(3, 18), loc=(1,  9), colspan = 3)
    ax14 = plt.subplot2grid(shape=(3, 18), loc=(2,  9), colspan = 3)
    ax15 = plt.subplot2grid(shape=(3, 18), loc=(0, 12), colspan = 3)
    ax16 = plt.subplot2grid(shape=(3, 18), loc=(1, 12), colspan = 3)
    ax17 = plt.subplot2grid(shape=(3, 18), loc=(2, 12), colspan = 3)
    ax18 = plt.subplot2grid(shape=(3, 18), loc=(0, 15), colspan = 3)
    ax19 = plt.subplot2grid(shape=(3, 18), loc=(1, 15), colspan = 3)
    ax10 = plt.subplot2grid(shape=(3, 18), loc=(2, 15), colspan = 3)

    for i in range(0, len(le_list)-1):
        ax1.plot(para_list, le_list[i])
    ax1.set_xlabel("sigma")
    ax1.set_ylabel("lambda 1-9")
    ax1.plot([curr_para, curr_para], [le_min, le_max], "r-.")
    ax1.plot([para_list[0], para_list[-1]], [0, 0], "r-.")

    ax2.scatter(data_for_plot[main_plot_x], data_for_plot[main_plot_y], color = "b", s = 0.1)
    ax2.scatter(old_data_for_plot[main_plot_x], old_data_for_plot[main_plot_y], color = "r", s = 0.1)
    ax2.set_xlabel("x^{(" + str(main_plot_x + 1) + ")}")
    ax2.set_xlim(sub_img_int[0][0], sub_img_int[0][1])
    ax2.set_ylabel("x^{(" + str(main_plot_y + 1) + ")}")
    ax2.set_ylim(sub_img_int[1][0], sub_img_int[1][1])

    ax3.scatter(data_for_plot[main_plot_x], data_for_plot[main_plot_y], color = "b", s = 0.1)
    ax2.set_xlabel("x^{(" + str(main_plot_x + 1) + ")}")
    ax3.set_xlim(default_interval[0][1], default_interval[0][2])
    ax2.set_ylabel("x^{(" + str(main_plot_y + 1) + ")}")
    ax3.set_ylim(default_interval[1][1], default_interval[1][2])

    ax4.scatter(data_for_plot[main_plot_x], data_for_plot[main_plot_y], color = "b", s = 0.1)
    ax4.scatter(old_data_for_plot[main_plot_x], old_data_for_plot[main_plot_y], color = "r", s = 0.1)
    ax4.set_xlabel("x^{(" + str(main_plot_x + 1) + ")}")
    ax4.set_xlim(default_interval[0][1], default_interval[0][2])
    ax4.set_ylabel("x^{(" + str(main_plot_y + 1) + ")}")
    ax4.set_ylim(default_interval[1][1], default_interval[1][2])
    
    ax12.scatter(data_for_plot[img_x], data_for_plot[img_y[0]], color = "b", s = 0.1)
    ax12.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax12.set_ylabel("x^{(" + str(img_y[0] + 1) + ")}")
    ax13.scatter(data_for_plot[img_x], data_for_plot[img_y[1]], color = "b", s = 0.1)
    ax13.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax13.set_ylabel("x^{(" + str(img_y[1] + 1) + ")}")
    ax14.scatter(data_for_plot[img_x], data_for_plot[img_y[2]], color = "b", s = 0.1)
    ax14.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax14.set_ylabel("x^{(" + str(img_y[2] + 1) + ")}")
    ax15.scatter(data_for_plot[img_x], data_for_plot[img_y[3]], color = "b", s = 0.1)
    ax15.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax15.set_ylabel("x^{(" + str(img_y[3] + 1) + ")}")
    ax16.scatter(data_for_plot[img_x], data_for_plot[img_y[4]], color = "b", s = 0.1)
    ax16.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax16.set_ylabel("x^{(" + str(img_y[4] + 1) + ")}")
    ax17.scatter(data_for_plot[img_x], data_for_plot[img_y[5]], color = "b", s = 0.1)
    ax17.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax17.set_ylabel("x^{(" + str(img_y[5] + 1) + ")}")
    ax18.scatter(data_for_plot[img_x], data_for_plot[img_y[6]], color = "b", s = 0.1)
    ax18.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax18.set_ylabel("x^{(" + str(img_y[6] + 1) + ")}")
    ax19.scatter(data_for_plot[img_x], data_for_plot[img_y[7]], color = "b", s = 0.1)
    ax19.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax19.set_ylabel("x^{(" + str(img_y[7] + 1) + ")}")
    ax10.scatter(data_for_plot[img_x], data_for_plot[img_y[8]], color = "b", s = 0.1)
    ax10.set_xlabel("x^{(" + str(img_x + 1) + ")}")
    ax10.set_ylabel("x^{(" + str(img_y[8] + 1) + ")}")

    
    plt.savefig(save_file_loc)



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

    curr_para = float(para[default_para_use[1]])

    return sys_dim, name_middle_str, curr_para



def video_plot(file_list, default_ob_use, default_para_use, default_interval, flag, name_code_length):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    det_img = deepcopy(file_list[0])
    det_img = det_img.split("/")
    real_name = ""

    for i in range(0, len(det_img) - 1):
        real_name += det_img[i]
        real_name += "/"
    
    global LAYER_NAME
    LAYER_NAME = real_name + LAYER_NAME
    
    print(LAYER_NAME)
    
    para_list, le_list = get_le_list(file_list, default_para_use)

    for i in range(0, len(file_list)):
        sys_dim, name_middle_str, curr_para = info_read(file_list[i], default_para_use, name_code_length)
        
        for j in range(0, len(default_ob_use)):
            if default_ob_use[j] < 0:
                default_ob_use[j] += sys_dim

        read_file_name = file_list[i] + "_" + flag + ".dat" 
        save_file_loc = "imgs/ob_" + name_middle_str + ".png"

        le_str = "("
        for j in range(0, sys_dim):
            curr_le = le_list[j][i]
            curr_le = round(curr_le, 3)
            le_str += str(curr_le)
            if j != sys_dim-1:
                le_str += ", "
        le_str += ")"
        plot_main(read_file_name, save_file_loc, default_ob_use, default_interval, para_list, le_list, curr_para, le_str, sys_dim)

    time.sleep(5)
    os.system("ffmpeg -r 5 -s 1920x1080 -pattern_type glob -i 'imgs/ob_0.*.png' -vcodec libx264 -crf 22 video.mp4 -y")
    return 


