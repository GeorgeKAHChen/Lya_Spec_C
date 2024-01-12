import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle
from libpy import Init
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import time
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

FONT_SIZE = 22
FOR_TEST = False

def full_plot(file_list, default_para_use, default_x_use, default_x_range, default_ob_use, default_ob_interval, default_le_file, default_dist_file, tikz_axis):
    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Image Initialization
    +++++++++++++++++++++++++++++++++++++++++++++
    """

    fig = plt.figure(constrained_layout=True, figsize=(30, 50))
    plt.rcParams.update({'font.size': FONT_SIZE})

    ax_le   = plt.subplot2grid(shape=(49, 30), loc=( 0, 0), rowspan = 9, colspan = 30)
    ax_D_ky = plt.subplot2grid(shape=(49, 30), loc=(10, 0), rowspan = 9, colspan = 30, sharex=ax_le)
    ax_H_ks = plt.subplot2grid(shape=(49, 30), loc=(20, 0), rowspan = 9, colspan = 30, sharex=ax_le)
    ax_bf   = plt.subplot2grid(shape=(49, 30), loc=(30, 0), rowspan = 9, colspan = 30, sharex=ax_le)
    ax_dist = plt.subplot2grid(shape=(49, 30), loc=(40, 0), rowspan = 9, colspan = 30, sharex=ax_le)
    
    if tikz_axis:
        ax_le.set_xticklabels([])
        ax_D_ky.set_xticklabels([])
        ax_H_ks.set_xticklabels([])
        ax_bf.set_xticklabels([])
        ax_dist.set_xticklabels([])

        ax_le.set_yticklabels([])
        ax_D_ky.set_yticklabels([])
        ax_H_ks.set_yticklabels([])
        ax_bf.set_yticklabels([])
        ax_dist.set_yticklabels([])

    #ax0.xaxis.set_major_locator(MultipleLocator(0.025))
    ax_le.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    ax_D_ky.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    ax_H_ks.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    ax_bf.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    ax_dist.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    
    if not tikz_axis:
        ax_le.set_title("(a) sigma - LE",y=-0.1,pad=-12)
        ax_D_ky.set_title("(b) sigma - D_KY",y=-0.1,pad=-12)
        ax_H_ks.set_title("(c) sigma - H_KS",y=-0.1,pad=-12)
        ax_bf.set_title("(d) sigma - Bifurcation diagram",y=-0.1,pad=-12)
        ax_dist.set_title("(e) sigma - x_1 distribution",y=-0.1,pad=-12)
    


    """ 
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_le - ax_D_ky - ax_H_ks
    +++++++++++++++++++++++++++++++++++++++++++++
    """ 

    # data read and dky, hks computation
    file = open(default_le_file, "r")
    
    les = [[] for n in range(9)]
    x_data = []
    D_ky = []
    H_ks = []

    while 1:
        line = file.readline()

        if not line:
            break

        line = line.split(" ")

        x_data.append(float(line[2]))
        D_new = 0
        D_sum = 0
        H_new = 0
        for i in range(3, 12):
            les[i-3].append(float(line[i]))

        for i in range(3, 13):
            val = float(line[i])
            D_sum += val
            if D_sum < 0:
                D_sum -= val
                D_new = i-3 + D_sum / abs(float(line[i]))
                D_ky.append(D_new)
                break

        for i in range(3, 13):
            val = float(line[i])
            if val > 0:
                H_new += val
            else:
                H_ks.append(H_new)
                break
    
    print(len(x_data), len(D_ky), len(H_ks))


    # image plot    
    #   ax_le - LE plot
    print("ax_le plotting")
    for i in range(0, 9):
        ax_le.plot(x_data, les[i], linewidth=5.0)
        ax_le.plot([0, 0.35], [0, 0], "r-.")

    #   ax_D_ky - Dky plot
    print("ax_D_ky plotting")
    ax_D_ky.plot(x_data, D_ky, linewidth=5.0)

    #   ax_H_ks - Hks plot
    print("ax_H_ks plotting")
    ax_H_ks.plot(x_data, H_ks, linewidth=5.0)



    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_bf
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    print("ax_bf plotting")
    

    for kase in range(0, len(file_list)):
        print(kase, file_list[kase], end = ": ")

        if FOR_TEST and kase > 50:
            break
        if kase % 3 != 0:
            print()
            continue

        # read x data(parameter)
        bf_x = 0
        file = open(file_list[kase] + ".info", "r")
        
        file_lines = []
        while 1:
            line = file.readline()
            if not line:
                break
            file_lines.append(line)

        file.close()

        if default_para_use[0] != "r":
            bf_x = float(file_lines[10].split(" ")[default_para_use[1]])
        else:
            bf_x = float(file_lines[12].split(" ")[default_para_use[1]])

        file = open(file_list[kase] + "_ob.dat", "r")
        bf_y_axis = []
        while 1:
            file_line = file.readline()
            if not file_line:
                break
            bf_y_axis.append(float(file_line.split(" ")[default_x_use]))

        bf_x_axis = [bf_x for n in range(len(bf_y_axis))]
        print(bf_x, len(bf_y_axis))
        ax_bf.scatter(bf_x_axis, bf_y_axis, s = 1, c = "black", marker = ".")

    print()

    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_dist
    +++++++++++++++++++++++++++++++++++++++++++++
    """

    """
    # Init
    print("ax_dist")
    file = open(default_dist_file, "r")
    init_data = True
    print(default_dist_file)
    ax_dist.set_ylim([-2, 2])
    """

    """

    # For distribution min-max curve
    val_points = []
    x_min_points = []
    y_min_points = []
    x_max_points = []
    y_max_points = []
    while 1:
        file_line = file.readline()

        if not file_line:
            break

        file_line = file_line.split(" ")[0: -1]
        if init_data:
            for i in range(0, len(file_line) - 1):
                val_points.append((float(file_line[i])+float(file_line[i+1]))/2)
            init_data = False
            continue
        
        for i in range(0, len(file_line)):
            file_line[i] = float(file_line[i])
        
        for i in range(2, len(file_line)-1):
            if file_line[i] == 0:
                continue
            if file_line[i] - file_line[i-1] > 0.01 and file_line[i] - file_line[i+1] > 0.01:
                print(file_line[i-1], file_line[i], file_line[i+1])
                x_max_points.append(file_line[0])
                y_max_points.append(val_points[i])
            if file_line[i] - file_line[i-1] < -0.008 and file_line[i] - file_line[i+1] < -0.008:
                print(file_line[i-1], file_line[i], file_line[i+1])
                x_min_points.append(file_line[0])
                y_min_points.append(val_points[i])
    print(len(x_min_points), len(y_min_points))
    print(len(x_max_points), len(y_max_points))

    ax_dist.scatter(x_min_points, y_min_points, s = 1, color = "red")
    ax_dist.scatter(x_max_points, y_max_points, s = 1, color = "blue")
    """


    """
    # For distribution heat map
    x_vals = []
    y_vals = []
    z_vals = []

    maxx = -1
    while 1:
        file_line = file.readline()

        if not file_line:
            break

        file_line = file_line.split(" ")[0: -1]
        if init_data:
            for i in range(0, len(file_line) - 1):
                y_vals.append([float(file_line[i]), float(file_line[i+1])])
            init_data = False
            continue
        
        for i in range(0, len(file_line)):
            file_line[i] = float(file_line[i])
            maxx = max(maxx, file_line[i])
        
        x_vals.append(file_line[0])
        z_vals.append(file_line[1: ])


    maxx = 2
    x_vals = np.array(x_vals)
    y_vals = np.array(y_vals)
    z_vals = np.array(z_vals)
    print(x_vals[0], x_vals[1], x_vals[2])
    print(len(x_vals), len(y_vals))
    print(len(z_vals), len(z_vals[0]))

    #color_map_main = plt.cm.get_cmap('hsv')
    color_map_main = plt.cm.get_cmap('jet')

    delta_x = 0.001
    delta_y = 4/1000

    for i in range(0, len(x_vals)):
        print(i)
        #if FOR_TEST and i % 10 != 0:
        #    continue
        for j in range(0, len(y_vals)):
            curr_color = (1.0, 1.0, 1.0, 1.0)
            if z_vals[i][j] != 0:
                tmp_color = (z_vals[i][j] - 0) / (maxx - 0)
                tmp_color = min(tmp_color, 1.0)
                tmp_color = max(tmp_color, 0.0)
                curr_color = color_map_main(tmp_color)
            rect1 = Rectangle((x_vals[i], y_vals[j][0]), delta_x, delta_y, color = curr_color)
            ax_dist.add_patch(rect1)


    """

    """
    +++++++++++++++++++++++++++++++++++++++++++++
    FINAL Image output
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    plt.savefig("tmp_full.png")
    os.system("open tmp_full.png")




    