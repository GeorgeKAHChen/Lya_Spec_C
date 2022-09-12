import matplotlib.pyplot as plt
import sys

#file_names = ["output22_23", "output23_24", "output24_25", "output25_26"]
#file_names = ["output225_228"]
#file_names = ["ps_225_228"]
file_names = ["ps_0220_0225", "ps_0225_0230", "ps_0230_0235", "ps_0235_0240", "ps_0240_0245", "ps_0245_0250", "ps_0250_0255", "ps_0255_0260"] 
para_max = 1
para_min = -1

para = []
bf_points = []
le_para = []
le_1 = []
le_2 = []
le_3 = []

for i in range(0, len(file_names)):
    file = open(file_names[i], "r")
    curr_para = 0
    while 1:
        line = file.readline()
        if not line:
            break
        line = line.split(" ")
        if line[0] == "StartValue":
            curr_para = float(line[9])
            if curr_para > para_max or curr_para < para_min:
                curr_para = 114514
            else:
                continue
        if curr_para == 114514:
            continue
        if len(line) >= 9 and len(line) <= 11:
            le_para.append(curr_para)
            le_1.append(float(line[6]))
            le_2.append(float(line[7]))
            le_3.append(float(line[8]))
        else:
            para.append(curr_para)
            bf_points.append(float(line[3]))

fig, (ax0, ax1) = plt.subplots(2, figsize=(16,8), sharex=True)
ax0.plot(le_para, le_1)
ax0.plot(le_para, le_2)
ax0.plot(le_para, le_3)
ax0.title.set_text("Lyapunov Exponents(lambda 1-3)")
ax0.set_ylabel("LE")

ax1.scatter(para, bf_points, s = 0.1)
ax1.title.set_text("Bifurcation diagram")
ax1.set_ylabel("y")
ax1.set_xlabel("mu")
plt.show()
