import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from libpy import Init
import os

def le_file_heat_map(file_list, para_use, le_start, color_table, color_map):
    
    os.system("rm -rf imgs")
    os.system("mkdir imgs")

    """
    Data initialization
    """
    plt.rcParams.update({'font.size': 22})

    # parameter x-y axis init
    x_para_loc  = para_use[0][0]
    x_para_min  = para_use[0][1]
    x_para_max  = para_use[0][2]
    x_para_dis  = para_use[0][3]
    x_para_len  = int((x_para_max - x_para_min)/(x_para_dis) + 0.5) + 1

    y_para_loc  = para_use[1][0]
    y_para_min  = para_use[1][1]
    y_para_max  = para_use[1][2]
    y_para_dis  = para_use[1][3]
    y_para_len  = int((y_para_max - y_para_min)/(y_para_dis) + 0.5) + 1

    # image table init
    Le_img      = [[0 for n in range(x_para_len)] for n in range(y_para_len)]
    D_ky_img    = [[0 for n in range(x_para_len)] for n in range(y_para_len)]
    H_ks_img    = [[0 for n in range(x_para_len)] for n in range(y_para_len)]

    D_ky_minn =  99999999
    D_ky_maxx = -99999999

    H_ks_minn =  99999999
    H_ks_maxx = -99999999

    # color map init
    color_map = plt.cm.get_cmap(color_map)

    # output
    print(x_para_loc, x_para_min, x_para_max, x_para_len, x_para_dis)
    print(y_para_loc, y_para_min, y_para_max, y_para_len, y_para_dis)



    """
    File read and main calc
    """
    print("file read")
    for kase in range(0, len(file_list)):
        # file read init
        file_name = file_list[kase] + ".dat"
        file = open(file_name, "r")
        cnt = 0
        print("read: " + file_name)



        # file read main
        while 1:
            cnt += 1
            
            line = file.readline()
            if not line:
                break
            line = line.split(" ")
            
            table_loc_x =              int((float(line[x_para_loc]) - x_para_min)/x_para_dis + 0.5) - 1
            table_loc_y = y_para_len - int((float(line[y_para_loc]) - y_para_min)/y_para_dis + 0.5) - 1
            print(table_loc_x, table_loc_y)
            if table_loc_x < 0 or table_loc_x > x_para_len or table_loc_y < 0 or table_loc_y > y_para_len:
                print("Ignore data out of range, from file: " + file_name + ",line: " + str(cnt))
                continue



            # le read and calc
            le_data = []
            le_add_to_image = False
            for i in range(le_start, len(line)):
                try:
                    le_data.append(float(line[i]))
                    if float(line[i]) < 0 and le_add_to_image == False:
                        Le_img[table_loc_y][table_loc_x] = i - le_start
                        le_add_to_image = True
                except:
                    continue
            


            # D_ky calc
            D_sum = 0
            for i in range(0, len(le_data)):
                D_sum += le_data[i]
                if D_sum < 0:
                    D_sum -= le_data[i]
                    D_new = i + D_sum / abs(le_data[i])
                    D_ky_img[table_loc_y][table_loc_x] = D_new
                    D_ky_minn = min(D_ky_minn, D_new)
                    D_ky_maxx = max(D_ky_maxx, D_new)
                    break



            # H_ks calc
            H_sum = 0
            for i in range(0, len(le_data)):
                if le_data[i] > 0:
                    H_sum += le_data[i]
                else:
                    H_ks_img[table_loc_y][table_loc_x] = H_sum
                    H_ks_minn = min(H_ks_minn, H_sum)
                    H_ks_maxx = max(H_ks_maxx, H_sum)
                    break

    print(D_ky_minn, D_ky_maxx, H_ks_minn, H_ks_maxx)



    """
    Image plot
    """
    print("image output")
    D_ky_size = D_ky_maxx - D_ky_minn
    H_ks_size = H_ks_maxx - H_ks_minn
    for i in range(0, y_para_len):
        print(i, y_para_len)
        for j in range(0, x_para_len):
            Le_img[i][j]        = color_table[Le_img[i][j] % len(color_table)]

            # normalization
            D_ky_img[i][j]      = (D_ky_img[i][j] - D_ky_minn) / D_ky_size
            H_ks_img[i][j]      = (H_ks_img[i][j] - H_ks_minn) / H_ks_size
            
            # boundary check
            D_ky_img[i][j]      = min(D_ky_img[i][j], 1.0)
            H_ks_img[i][j]      = min(H_ks_img[i][j], 1.0)
            
            D_ky_img[i][j]      = max(D_ky_img[i][j], 0.0)
            H_ks_img[i][j]      = max(H_ks_img[i][j], 0.0)
            
            # val 2 color
            D_ky_img[i][j]      = color_map(D_ky_img[i][j])
            H_ks_img[i][j]      = color_map(H_ks_img[i][j])
            
            # 0,1 to 0,255
            D_ky_img[i][j]      = [int(D_ky_img[i][j][0] * 255), int(D_ky_img[i][j][1] * 255), int(D_ky_img[i][j][2] * 255), D_ky_img[i][j][3]]
            H_ks_img[i][j]      = [int(H_ks_img[i][j][0] * 255), int(H_ks_img[i][j][1] * 255), int(H_ks_img[i][j][2] * 255), H_ks_img[i][j][3]]
            
            """
            for k in range(0, 3):
                D_ky_color_2[k] = max(D_ky_color_2[k], 0)
                D_ky_color_2[k] = min(D_ky_color_2[k], 255)
                H_ks_color_2[k] = max(H_ks_color_2[k], 0)
                H_ks_color_2[k] = min(H_ks_color_2[k], 255)
            """

            # array to tuple
            Le_img[i][j]        = tuple(Le_img[i][j])
            D_ky_img[i][j]      = tuple(D_ky_img[i][j])
            H_ks_img[i][j]      = tuple(H_ks_img[i][j])

    # np.array
    Le_img                      = np.array(Le_img, dtype=np.uint8)
    D_ky_img                    = np.array(D_ky_img, dtype=np.uint8)
    H_ks_img                    = np.array(H_ks_img, dtype=np.uint8)

    # image output
    Init.ImageIO(file_dir = "imgs/tmp_le_img.png",   img = np.array(Le_img), io = "o", mode = "rgba", backend = "opencv")
    Init.ImageIO(file_dir = "imgs/tmp_d_ky_img.png", img = np.array(D_ky_img), io = "o", mode = "rgba", backend = "opencv")
    Init.ImageIO(file_dir = "imgs/tmp_H_ks_img.png", img = np.array(H_ks_img), io = "o", mode = "rgba", backend = "opencv")




    """
    Card output
    """
    # `color_table` output
    fig, (ax0) = plt.subplots(figsize=(10, 4))
    for i in range(0, len(color_table)):
        color_table[i] = (color_table[i][0] / 255, 
                          color_table[i][1] / 255,
                          color_table[i][2] / 255, 
                          color_table[i][3])
    for i in range(0, len(color_table)):
        ax0.add_patch(Rectangle((i/len(color_table), 0), 1/len(color_table), 0.1, facecolor = color_table[i]))    
    ax0.set_xlim(0, 1)
    ax0.get_xaxis().set_visible(True)
    ax0.set_ylim(0, 0.1)
    ax0.get_yaxis().set_visible(False)
    plt.savefig("imgs/tmp_color_table_card.png")

    # `color_map` output
    fig, (ax0) = plt.subplots(figsize=(10, 4))
    for i in range(0, 256):
        ax0.add_patch(Rectangle((i/256, 0), 1/256, 0.1, facecolor = color_map(i/256)))
    ax0.set_xlim(0, 1)
    ax0.get_xaxis().set_visible(False)
    ax0.set_ylim(0, 0.1)
    ax0.get_yaxis().set_visible(False)
    plt.savefig("imgs/tmp_color_map_card.png")


    return 









