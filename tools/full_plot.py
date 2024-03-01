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
D_KY_TEST = False
def full_plot(file_list, 
              default_para_use, 
              default_x_use, 
              default_x_range, 
              default_ob_use, 
              default_ob_interval, 
              default_le_file, 
              default_dist_file, 
              tikz_axis, 
              bf_merge = True,
              ax_will_plot = [1, 1, 1, 1, 1]):
    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Image Initialization
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    size_a = sum(ax_will_plot)*11-2

    fig = plt.figure(constrained_layout=True, figsize=(30, 10 * sum(ax_will_plot)))
    plt.rcParams.update({'font.size': FONT_SIZE})

    loc = 0
    if ax_will_plot[0]:
        ax_le   = plt.subplot2grid(shape=(size_a, 30), loc=(loc, 0), rowspan = 9, colspan = 30)
        loc += 11
    if ax_will_plot[1]:
        ax_D_ky = plt.subplot2grid(shape=(size_a, 30), loc=(loc, 0), rowspan = 9, colspan = 30, sharex=ax_le)
        loc += 11
    if ax_will_plot[2]:
        ax_H_ks = plt.subplot2grid(shape=(size_a, 30), loc=(loc, 0), rowspan = 9, colspan = 30, sharex=ax_le)
        loc += 11
    if ax_will_plot[3]:
        ax_dist = plt.subplot2grid(shape=(size_a, 30), loc=(loc, 0), rowspan = 9, colspan = 30, sharex=ax_le)
        loc += 11
    #ax_bf   = plt.subplot2grid(shape=(49, 30), loc=(40, 0), rowspan = 9, colspan = 30, sharex=ax_le)
    
    if tikz_axis:
        if ax_will_plot[0]:
            ax_le.set_xticklabels([])
            ax_le.set_yticklabels([])
        if ax_will_plot[1]:
            ax_D_ky.set_xticklabels([])
            ax_D_ky.set_yticklabels([])
        if ax_will_plot[2]:
            ax_H_ks.set_xticklabels([])
            ax_H_ks.set_yticklabels([])
        if ax_will_plot[3]:
            ax_dist.set_xticklabels([])
            ax_dist.set_yticklabels([])
        
        #ax_bf.set_xticklabels([])
        #ax_bf.set_yticklabels([])

    #ax0.xaxis.set_major_locator(MultipleLocator(0.025))
    if ax_will_plot[0]:
        ax_le.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    if ax_will_plot[1]:
        ax_D_ky.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    if ax_will_plot[2]:
        ax_H_ks.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    if ax_will_plot[3]:
        ax_dist.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    #ax_bf.grid(which='major', color='grey', linestyle='-', linewidth=0.4)
    
    if not tikz_axis:
        if ax_will_plot[0]:
            ax_le.set_title("(a) sigma - LE",y=-0.1,pad=-12)
        if ax_will_plot[1]:
            ax_D_ky.set_title("(b) sigma - D_KY",y=-0.1,pad=-12)
        if ax_will_plot[2]:
            ax_H_ks.set_title("(c) sigma - H_KS",y=-0.1,pad=-12)
        if ax_will_plot[3]:
            ax_dist.set_title("(d) sigma - x_1 distribution",y=-0.1,pad=-12)
        #ax_bf.set_title("(d) sigma - Bifurcation diagram",y=-0.1,pad=-12)
    


    """ 
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_le - ax_D_ky - ax_H_ks
    +++++++++++++++++++++++++++++++++++++++++++++
    """ 
    if ax_will_plot[0] == 1 or ax_will_plot[1] == 1 or ax_will_plot[2] == 1:
        # data read and dky, hks computation
        file = open(default_le_file, "r")
        
        les = [[] for n in range(9)]
        x_data = []
        D_ky = []
        H_ks = []

        if D_KY_TEST:
            D_ky_9 = []
            D_ky_8 = []
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
                    print(i-3)
                    break
            if D_KY_TEST:
                D_ky_8_sum = 0
                D_ky_9_sum = 0
                for i in range(3, 3+8):
                    D_ky_8_sum += float(line[i])
                for i in range(3, 3+9):
                    D_ky_9_sum += float(line[i])
                #print(D_ky_8_sum, D_ky_9_sum)
                D_ky_9.append(9+D_ky_9_sum / abs(float(line[3+9])))
                D_ky_8.append(8+D_ky_8_sum / abs(float(line[3+8])))
            #print(D_ky[len(D_ky) - 1], D_ky_8[len(D_ky_8) - 1], D_ky_9[len(D_ky_9) - 1])
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
        if ax_will_plot[0] == 1:
            print("ax_le plotting")
            min_para_x = min(x_data)
            max_para_x = max(x_data)
            for i in range(0, 9):
                ax_le.plot(x_data, les[i], linewidth=3.0)
            ax_le.plot([min_para_x, max_para_x], [0, 0], "r-.")

        #   ax_D_ky - Dky plot
        if ax_will_plot[1] == 1:
            print("ax_D_ky plotting")
            ax_D_ky.plot(x_data, D_ky, linewidth=3.0)
            if D_KY_TEST:
                ax_D_ky.plot(x_data, D_ky_8, linewidth=3.0, linestyle="dotted")
                ax_D_ky.plot(x_data, D_ky_9, linewidth=3.0, linestyle="dotted")
                ax_D_ky.set_ylim(8.2, 9.2)
        #   ax_H_ks - Hks plot
        if ax_will_plot[2] == 1:
            print("ax_H_ks plotting")
            ax_H_ks.plot(x_data, H_ks, linewidth=3.0)



    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_dist / ax_bf_dist_merge
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    if ax_will_plot[3] == 1:
        # Init
        print("ax_dist")
        file = open(default_dist_file, "r")
        init_data = True
        print(default_dist_file)
        ax_dist.set_ylim([default_x_range[0], default_x_range[1]])


        
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

        minn = 0
        maxx = 2
        x_vals = np.array(x_vals)
        y_vals = np.array(y_vals)
        z_vals = np.array(z_vals)
        print(x_vals[0], x_vals[1], x_vals[2])
        print(len(x_vals), len(y_vals))
        print(len(z_vals), len(z_vals[0]))

        #color_map_main = plt.cm.get_cmap('hsv')
        color_map_main = plt.cm.get_cmap('jet')

        
        

        for i in range(0, len(x_vals)-1):
            print(i)
            if FOR_TEST and i % 30 != 0:
                continue
            delta_x = x_vals[i+1] - x_vals[i]
            for j in range(0, len(y_vals)):
                delta_y = y_vals[j][1]-y_vals[j][0]
                curr_color = (1.0, 1.0, 1.0, 1.0)
                if z_vals[i][j] != 0:
                    tmp_color = (z_vals[i][j] - minn) / (maxx - minn)
                    tmp_color = min(tmp_color, 1.0)
                    tmp_color = max(tmp_color, 0.0)
                    curr_color = color_map_main(tmp_color)
                rect1 = Rectangle((x_vals[i], y_vals[j][0]), delta_x, delta_y, color = curr_color)
                ax_dist.add_patch(rect1)



    """
    +++++++++++++++++++++++++++++++++++++++++++++
    Plot ax_bf
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    """
    if ax_will_plot[4] == 1:
        if not bf_merge:
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
    """
    +++++++++++++++++++++++++++++++++++++++++++++
    FINAL Image output
    +++++++++++++++++++++++++++++++++++++++++++++
    """
    plt.savefig("tmp_full.png")
    os.system("open tmp_full.png")




    
