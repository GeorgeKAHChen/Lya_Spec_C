from libpy import Init
import os
import numpy as np

GROUP_SIZE = 1000



def ob_time(file_list, default_x_use, default_x_range):
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    
    for i in range(0, len(file_list)):
        height = default_x_range[2]
        delta_x = (default_x_range[1] - default_x_range[0]) / (default_x_range[2] - 1)
        data_for_plot = [[] for n in range(height)]
        read_file_name = file_list[i] + "_ob.dat"
        file = open(read_file_name, "r")
        print(read_file_name, end = ": ")
        count = 0
        sub_plot = [255 for n in range(height)]
        
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.split(" ")
            loc = int((float(line[default_x_use]) - default_x_range[0]) / delta_x)
            if loc < 0 or loc >= height:
                continue
            sub_plot[loc] = 0
            count += 1
            if count == GROUP_SIZE:
                #print(sub_plot)
                for p in range(0, len(sub_plot)):
                    data_for_plot[p].append(sub_plot[p])
                
                count = 0
                sub_plot = [255 for n in range(height)]

        file.close()
    
        Init.ImageIO(file_dir = "imgs/" + str(i) + ".png", img = np.float32(data_for_plot), io = "o", mode = "grey", backend = "opencv")


    return 
