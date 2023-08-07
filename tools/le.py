import matplotlib.pyplot as plt
import numpy as np
import os

def le(file_list, default_para_use):
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



    """
    FIGURE PLOT
    """
    fig = plt.figure(constrained_layout=True, figsize=(24, 8))
    ax1 = plt.subplot(111)
    for i in range(0, len(le_list)-1):
        ax1.plot(para_list, le_list[i])
    ax1.plot([para_list[0], para_list[-1]], [0, 0], "r-.")
    plt.savefig("tmp_le.png")

