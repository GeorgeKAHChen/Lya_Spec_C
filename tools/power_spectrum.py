import matplotlib.pyplot as plt
import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt


def power_spectrum(file_list, power_spectrum_para, default_x_use):

    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    total_file_size = power_spectrum_para[0]
    x_lim_min = power_spectrum_para[1][0]
    x_lim_max = power_spectrum_para[1][1]
    y_lim_min = power_spectrum_para[2][0]
    y_lim_max = power_spectrum_para[2][1]

    for i in range(0, len(file_list)):
        file_name = file_list[i] + "_ob.dat"

        data_arr = []
        file = open(file_name, "r")
        cnt = 0
        
        print(file_name, end = ": ")

        while 1:
            file_line = file.readline()

            if not file_line:
                break
            if cnt > total_file_size :
                break

            file_line = file_line.split(" ")

            try:
                data_arr.append(float(file_line[default_x_use]))
                cnt += 1
            except:
                continue

        print(cnt, end = ", ")

        data_arr = np.array(data_arr)

        ps = np.abs(np.fft.rfft(data_arr))**2
        print(len(ps))
        time_step = 1

        freqs = np.fft.rfftfreq(data_arr.size, time_step)
        idx = np.argsort(freqs)

        fig = plt.figure(constrained_layout=True, figsize=(12, 6))
        ax = plt.subplot(111)
        ax.semilogy(freqs[idx], ps[idx], linewidth = 0.1)
        ax.set_xlim(x_lim_min, x_lim_max)
        ax.set_ylim(y_lim_min, y_lim_max)

        plt.savefig("imgs/" + str(i) + ".png")
