import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init
from sklearn.cluster import DBSCAN

FONT_SIZE = 6
sys_dim = 6
distance = [0.01, 0.2, 10]
minimal_size = 100

def dbscan(file_list, default_x_use):
    color_map_main = plt.cm.get_cmap('jet')
    dbscan_x = np.linspace(distance[0], distance[1], distance[2])
    dbscan_y = []

    for kase in range(0, len(file_list)):
        # Data io
        read_file_name = file_list[kase] + "_ob.dat"
        file = open(read_file_name, "r")
        print(read_file_name)

        arr_x = []
        cnt = 0

        while 1:
            line = file.readline()
            if not line:
                break
            line = line.split(" ")

            try:
                arr_x.append(float(line[default_x_use]))
            except:
                break

            cnt += 1
            if cnt > 1e5:
                break
        

        # Data expansion

        data_arr = []
        for i in range(0, sys_dim):
            data_arr.append(arr_x[i: len(arr_x) - sys_dim + i])

        final_data_arr = []
        for i in range(0, len(data_arr[0])):
            tmp_arr = []
            for j in range(0, sys_dim):
                tmp_arr.append(data_arr[j][i])
            final_data_arr.append(tmp_arr)
        final_data_arr = np.array(final_data_arr)


        dbscan_y_sub = []
        # K-means
        for used_distance in dbscan_x:
            print(used_distance, end = ": ")
            dbscan = DBSCAN(eps=used_distance, min_samples=minimal_size)
            labels = dbscan.fit_predict(final_data_arr)
            
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)
            print("cluster = " + str(n_clusters_) + ", noise = " + str(n_noise_))
            dbscan_y_sub.append(n_clusters_)
        dbscan_y_sub.append(dbscan_y_sub)
    
    fig = plt.figure(constrained_layout=True, figsize=(30, 10 * sum(ax_will_plot)))
    
    fig = plt.figure(constrained_layout=True, figsize=(20, 5))
    ax = plt.subplot(111)
    for i in range(0, len(k_means_y)):
        plot_x = k_means_x
        plot_y = k_means_y[i]
        curr_color = color_map_main(i / (clusters[1] - clusters[0] + 1))
        ax.plot(plot_x, plot_y, color = curr_color)#, s = 0.1)
    ax.set_xlim([clusters[0], clusters[1]])
    plt.savefig("imgs/dbscan.png")