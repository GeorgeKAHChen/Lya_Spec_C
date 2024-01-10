import matplotlib.pyplot as plt
import numpy as np
import os

dim = 10

def get_vals(file_line):
    file_line = file_line.split(" ")
    for i in range(0, dim):
        file_line[i] = float(file_line[i])
    return file_line



def final_loc_plot(file_list):
    #print(file_list)
    """
    PARAMETER DEFINITION
    """
    vals_init = [[] for n in range(dim)]
    vals_last = [[] for n in range(dim)]
    output_file_name = "final.dat"
    final_file = open(output_file_name, "w")
    """
    INITIALIZATION
    """
    for i in range(0, len(file_list)):
        file = open(file_list[i] + ".info", "r")
        print(file_list[i] + ".info")
        line_code = 0
        while 1:
            file_line = file.readline()
            if not file_line:
                break
            """
            if line_code == 8:
                file_line = get_vals(file_line, dim)
                for i in range(file_line, dim):
                    vals_init[i].append(file_line[i])
            if line_code == 15:
                file_line = get_vals(file_line, dim)
                for i in range(file_line, dim):
                    vals_last[i].append(file_line[i])
            """
            if line_code == 15:
                #print(file_line)
                final_file.write(file_line)
            line_code += 1
        file.close()
    final_file.close()
