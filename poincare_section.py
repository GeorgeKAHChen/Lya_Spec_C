import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys
import os

os.system("rm -rf output_fig")
os.system("mkdir output_fig")
#filename = "output225_228"
#filename = "output_ps_225_228"
#filename = "output_rand_001_01_10"
#filename = "long_ob_022761_022764"
filename = "long_ps_022761_022764"
#filename = "tmp"
para_int = [1, 2, 4]
print_group = []


file = open(filename, "r")
array_x = []
array_y = []
array_w = []
paraname = ["x", "y", "z", "w"]
curr_para = -1
will_print = 0
while 1:
    line = file.readline()
    if not line:
        break
    line = line.split(" ")

    if line[0] == "StartValue":
        curr_para = float(line[9])
        if len(print_group) != 0:
            for i in range(0, len(print_group)):
                if curr_para == print_group:
                    will_print = 1
                    break
            if not will_print:
                curr_para = 114514
        continue    

    if curr_para == 114514:
        continue

    if len(line) > 7:
        print("Poincare section, mu = " + str(curr_para), len(array_x), len(array_y), len(array_w))
        fig = plt.figure(figsize = (9, 9))
        ax = plt.axes(projection ="3d")
        ax.scatter3D(array_x, array_y, array_w, s = 1)
        ax.set_xlabel(paraname[para_int[0]-1])
        ax.set_ylabel(paraname[para_int[1]-1])
        ax.set_zlabel(paraname[para_int[2]-1])
        plt.title("Poincare section, mu = " + str(curr_para) + ": " + str(line[6]) + ", " + str(line[7]) + ", " + str(line[8]))
        #plt.show()
        plt.savefig("output_fig/" + str(curr_para) + ".png")

        array_x = []
        array_y = []
        array_w = []
        continue

    array_x.append(float(line[para_int[0]+1]))
    array_y.append(float(line[para_int[1]+1]))
    array_w.append(float(line[para_int[2]+1]))   
