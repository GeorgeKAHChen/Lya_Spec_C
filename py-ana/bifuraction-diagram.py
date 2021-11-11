import numpy as np
import matplotlib.pyplot as plt
import random
import Init
#total_iteration_time = 110
#record_time = 100
#initial_value = random.random()
#interval_para = [1, 4.01]
#distance_para = 0.01

total_iteration_time = 1500000
record_time = 1000000
interval_para = [0.1, 6]
distance_para = 1e-1
distance_y = 1e-2
memory_dimension = 2
delta_t = 1e-3
Block_min_max = False
min_max_boundary = [-5, 40]
x_init = [0, 0, 0]

para_a = 0.2
para_c = 0.2

def f(x, parameter):
    #print(x[2])
    return [x[0] - delta_t * (x[1] + x[2]), 
            x[1] + delta_t * (x[0] + para_a * x[1]), 
            x[2] + delta_t * (para_c + x[2] * (x[0] - parameter))]


def main():
    parameter = interval_para[0]
    y_min =  999999999
    y_max = -999999999
    para_list = [parameter]
    list_rem = 0
    fx_list = [[]]
    while 1:
        print(parameter, interval_para[1], end = "\r")
        x = x_init
        fx = f(x, parameter)
        for i in range(0, total_iteration_time):
            x = fx
            fx = f(x, parameter)
            if i > record_time:
                if not Block_min_max:
                    if y_min > fx[memory_dimension]:
                        y_min = fx[memory_dimension]
                    if y_max < fx[memory_dimension]:
                        y_max = fx[memory_dimension]
                fx_list[list_rem].append(fx[memory_dimension])
        
        parameter += distance_para
        if parameter > interval_para[1]:
            break
        para_list.append(parameter)
        fx_list.append([])
        list_rem += 1
    print(fx_list[0])
    if Block_min_max:
        y_min = min_max_boundary[0]
        y_max = min_max_boundary[1]
    img = [[255 for n in range(len(para_list))] for n in range(int((y_max - y_min) / distance_y) + 1)]
 
    for i in range(0, len(para_list) - 2):
        for j in range(0, len(fx_list[i]) - 1):
            if fx_list[i][j] > y_max or fx_list[i][j] < y_min:
                continue
            if str(fx_list[i][j]) == "nan" or str(fx_list[i][j]) == "-nan":
                continue
            loc_y = int((y_max - fx_list[i][j])/distance_y)
            loc_x = i
            img[loc_y][loc_x] = 0
    #print(img)
    img = np.float32(img)
    Init.ImageIO(file_dir = "./img.png", img = np.float32(img), io = "o", mode = "grey", backend = "")


if __name__ == '__main__':
    main()
