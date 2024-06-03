import matplotlib.pyplot as plt
import numpy as np
import os
"""


plot "tmp.dat" using 2:3 with lines, \
     "tmp.dat" using 2:4 with lines, \
     "tmp.dat" using 2:5 with lines, \
     "tmp.dat" using 2:6 with lines, \
     "tmp.dat" using 2:7 with lines, \
     "tmp.dat" using 2:8 with lines, \
     "tmp.dat" using 2:9 with lines, \
     [0: 0.05] 0 with lines;

     "tmp.dat" using 2:10 with lines, \
     "tmp.dat" using 2:11 with lines, \
     [0: 0.05] 0 with lines;
"""
sys_dim = 6
sys_rand = True

folder_name          = [
"/home/hchen/LocalCode/RGHM_6_a_b_008_1/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_2/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_3/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_4/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_5/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_6/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_7/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_8/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_9/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_a/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_b/output", 
"/home/hchen/LocalCode/RGHM_6_a_b_008_c/output", 
]
file_code            = [[1,  11400] for n in range(12)]
ps_name = "x"
bf_use_dim = 0      # 0 start
para_use_loc = 0

print_it = True

para_final_1 = []
para_final_2 = []
para_final_3 = []
le_final = [[] for n in range(sys_dim)]
le_p_final = []

os.system("clear")
os.system("rm -rf tmp.dat")

for kase_i in range(0, len(folder_name)):
    for kase_j in range(file_code[kase_i][0], file_code[kase_i][1] + 1):

        file_name = folder_name[kase_i] + "/" + str(kase_j)

        le_file_name = file_name + ".info"
        print(le_file_name, end = ": ")
        file = open(le_file_name, "r")
        file_lines = []
        while 1:
            line = file.readline()
            if not line:
                break
            file_lines.append(line)

        file.close()
        if len(file_lines) == 0:
            continue 
        

        """
        if not sys_rand:
            para1 = file_lines[10].split(" ")
            para1[para_use_loc] = para1[para_use_loc][:-1]
            print(para1[para_use_loc])
            para_final_1.append(float(para1[para_use_loc]))
        else:
            para1 = file_lines[12].split(" ")
            para_final_1.append(float(para1[0]))
        """
        para1 = file_lines[10].split(" ")
        para1[para_use_loc] = para1[para_use_loc][:-1]
        print(para1[0], end = ", ")
        print(para1[1], end = ", ")
        para_final_1.append(float(para1[0]))
        para_final_3.append(float(para1[1]))

        para1 = file_lines[12].split(" ")
        para_final_2.append(float(para1[0]))
        print(para1[0], end = ": ")



        le = file_lines[17]
        le = le[:-1]

        le = le.split(" ")

        for i in range(0, sys_dim):
            le_final[i].append(float(le[i]))
        print()
        """
        for i in range(0, sys_dim):
            if float(le[i]) < 0:
                le_p_final.append(i)
                print(i)
                break
        if len(le_p_final) != len(para_final_1):
            le_p_final.append(-1) 
            print(-1)
        """

FileName = "tmp.dat"
File = open(FileName, "w")    
for i in range(0, len(para_final_1)):
    tmp_str = str(para_final_1[i])
    tmp_str += " "
    tmp_str += str(para_final_3[i])
    tmp_str += " "
    tmp_str += str(para_final_2[i])
    tmp_str += " "
    #tmp_str += str(le_p_final[i])
    #tmp_str += "\n"
    for j in range(0, sys_dim-1):
        tmp_str += str(le_final[j][i])
        tmp_str += " "
    tmp_str += str(le_final[sys_dim-1][i])
    tmp_str += "\n"
    File.write(tmp_str)
File.close()







