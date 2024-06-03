import matplotlib.pyplot as plt
import os
import numpy as np
from libpy import Init
from sklearn.cluster import KMeans

FONT_SIZE = 6
sys_dim = 6
clusters = [1, 16]
def k_means(file_list, default_x_use):
    color_map_main = plt.cm.get_cmap('jet')
    k_means_x = [n for n in range(clusters[0], clusters[1] + 1)]
    k_means_y = []

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
            if cnt > 1e6:
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


        k_means_y_sub = []
        # K-means
        for val_cluster in range(clusters[0], clusters[1] + 1):
            print(val_cluster, end = ": wcss = ")
            kmeans = KMeans(n_clusters=val_cluster, random_state=0)
            kmeans.fit(final_data_arr)
            wcss = kmeans.inertia_
            print(wcss)
            k_means_y_sub.append(wcss)
        k_means_y.append(k_means_y_sub)
        
    fig = plt.figure(constrained_layout=True, figsize=(20, 5))
    ax = plt.subplot(111)
    for i in range(0, len(k_means_y)):
        plot_x = k_means_x
        plot_y = k_means_y[i]
        curr_color = color_map_main(i / (clusters[1] - clusters[0] + 1))
        ax.plot(plot_x, plot_y, color = curr_color)#, s = 0.1)
    ax.set_xlim([clusters[0], clusters[1]])
    plt.savefig("imgs/k_means.png")