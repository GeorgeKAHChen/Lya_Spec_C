import matplotlib.pyplot as plt
import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

periodic_loc    = [2,3,4,5,6,7,8,9,10,12,18,25,35]
plot_periodic   = True 

def power_spectrum(file_list, power_spectrum_para, default_x_use, tikz_axis):

    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    total_file_size = power_spectrum_para[0]
    x_lim_min = power_spectrum_para[1][0]
    x_lim_max = power_spectrum_para[1][1]
    y_lim_min = power_spectrum_para[2][0]
    y_lim_max = power_spectrum_para[2][1]

    #for kase in range(0, len(file_list)):
    fig = plt.figure(constrained_layout=True, figsize=(24, 12))
    ax = plt.subplot(111)
    colors = ["red", "blue", "green"]
    for kase in range(0, len(file_list)):
        file_name = file_list[kase] + "_ob.dat"

        data_arr = []
        file = open(file_name, "r")
        cnt = 0
        
        print(file_name, end = ": ")

        while 1:
            file_line = file.readline()

            if not file_line:
                break
            if cnt >= total_file_size :
                break

            file_line = file_line.split(" ")

            try:
                data_arr.append(float(file_line[default_x_use]))
                cnt += 1
            except:
                continue

        print(cnt, end = ", ")
        print(len(data_arr), end = "! ")
        data_arr = np.array(data_arr)

        ps = np.abs(np.fft.rfft(data_arr))**2
        print(len(ps))
        time_step = 1

        freqs = np.fft.rfftfreq(data_arr.size, time_step)
        ps = ps * pow(1e-3, kase)
        idx = np.argsort(freqs)
        #ax.semilogy(freqs[idx], ps[idx], linewidth = 0.1, color = colors[kase % 3])
        ax.plot(freqs[idx], ps[idx], linewidth = 0.1, color = colors[kase % 3])
        #ax.scatter(freqs, ps, linewidth = 0.1, color = colors[kase % 3], s = 0.01)
        #ax.loglog(freqs[idx], ps[idx], linewidth = 0.1, color[kase])
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

    plt.savefig("imgs/" + str(kase+1) + ".png")
