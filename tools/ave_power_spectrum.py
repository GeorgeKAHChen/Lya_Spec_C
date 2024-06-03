import matplotlib.pyplot as plt
import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend, windows

periodic_loc    = [20]
plot_periodic   = False 
colors = ["red", "blue", "green"]
colors = ["black", "black", "black"]
mod_data = 0 # 0 means off

def ave_power_spectrum(file_list, power_spectrum_para, default_x_use, tikz_axis, default_file_code):

    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    total_file_size = power_spectrum_para[0]
    x_lim_min = power_spectrum_para[1][0]
    x_lim_max = power_spectrum_para[1][1]
    y_lim_min = power_spectrum_para[2][0]
    y_lim_max = power_spectrum_para[2][1]

    all_in_one = False
    if power_spectrum_para[3] == "1":
        all_in_one = True
    elif power_spectrum_para[3] == "n":
        all_in_one = False
    else:
        ValueError("Import parameter error")

    file_code_use = []
    loc = 0
    for i in range(0, len(default_file_code)):
        loc += default_file_code[i][1] - default_file_code[i][0] + 1
        file_code_use.append(loc)
    print(file_code_use)

    fig, ax = 0, 0

    if all_in_one:
        fig_all_in_one = plt.figure(constrained_layout=True, figsize=(24, 12))
        ax_all_in_one = plt.subplot(111)

    freqs = []
    ps_sum = []
    cnt = 0
    loc = 0
    time_step = 1
    for kase in range(0, len(file_list)):

        file_name = file_list[kase] + "_ob.dat"

        data_arr = []
        file = open(file_name, "r")
        
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
        cnt = 0
        
        print(len(data_arr), end = ", ")
        if mod_data != 0:
            mod_data_arr = []
            for i in range(0, len(data_arr)):
                #tmp = 2
                #if kase == 1:
                #    tmp = 1
                if i % mod_data == 0:
                    mod_data_arr.append(data_arr[i])
            data_arr = mod_data_arr
            print("mod: " + str(mod_data) + ", new_size = " + str(len(data_arr)), end = ", ")


        #print("sb=============")

        data_arr = np.array(data_arr)
        data_arr -= np.mean(data_arr)

        data_arr = detrend(data_arr)
        window = windows.hann(len(data_arr))
        #print(data_arr, data_arr.size)
        data_arr = data_arr * window
        #print(data_arr, data_arr.size)
        ps = np.fft.fft(data_arr)
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps = np.abs(ps) / data_arr.size
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps = np.power(np.abs(ps), 2)
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps = ps[0: int(data_arr.size/2 + 0.1)]
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps[0] = ps[0] / 2
        ps[ps.size - 1] = ps[ps.size - 1] / 2
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps = ps * 2
        #print(ps[0], ps[1], ps[ps.size - 1])
        ps_sum.append(ps)
        #input()
        if kase == 0 or kase == file_code_use[loc - 1]:
            freqs = np.fft.fftfreq(data_arr.size, time_step)[0: int(data_arr.size/2 + 0.1)]
            print("freqs = " + str(len(freqs)) )
        else:
            print()

        if kase == file_code_use[loc] - 1:
            print("Average and output")
            ps_final = []
            for j in range(0, len(ps_sum[0])):
                val = 0
                for i in range(0, len(ps_sum)):
                    val += ps_sum[i][j]
                val /= len(ps_sum)
                
                if all_in_one:
                    val = val * pow(1e-2, loc)
                
                ps_final.append(val)

            print(len(freqs), len(ps_final))

            if all_in_one:
                ax_all_in_one.scatter(freqs, ps_final, linewidth = 0.1, color = colors[loc % 3], s = 0.1)
                ax_all_in_one.set_yscale('log')
                ax_all_in_one.set_xlim(x_lim_min, x_lim_max)
                ax_all_in_one.set_ylim(y_lim_min, y_lim_max)

            else:
                fig = plt.figure(constrained_layout=True, figsize=(24, 12))
                ax = plt.subplot(111)

                ax.scatter(freqs, ps_final, linewidth = 0.1, color = colors[loc % 3], s = 0.1)
                ax.set_yscale('log')
                ax.set_xlim(x_lim_min, x_lim_max)
                ax.set_ylim(y_lim_min, y_lim_max)

                if plot_periodic:
                    for i in range(0, len(periodic_loc)):
                        ax.plot([1/periodic_loc[i], 1/periodic_loc[i]], [y_lim_min, y_lim_min * 100], linewidth = 1, color = "black", linestyle = "dashed")
                        ax.text(x = 1/periodic_loc[i], y = y_lim_min, s = str(periodic_loc[i]))
                if tikz_axis:
                    ax.set_xticklabels([])
                    ax.set_yticklabels([])
                else:
                    plt.title(str(kase+1))

                plt.savefig("imgs/" + str(loc + 1) + ".png")

            freqs = []
            ps_sum = []
            loc += 1

    if all_in_one:
        if plot_periodic:
            for i in range(0, len(periodic_loc)):
                ax_all_in_one.plot([1/periodic_loc[i], 1/periodic_loc[i]], [y_lim_min, y_lim_min * 100], linewidth = 1, color = "black", linestyle = "dashed")
                ax_all_in_one.text(x = 1/periodic_loc[i], y = y_lim_min, s = str(periodic_loc[i]))
        if tikz_axis:
            ax_all_in_one.set_xticklabels([])
            ax_all_in_one.set_yticklabels([])
        else:
            plt.title(str(kase+1))

        plt.savefig("imgs/output.png")
        os.system("open imgs")
