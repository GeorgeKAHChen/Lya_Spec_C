import ana_default_data
import sys
from tools import attr_plot
from tools import bf
from tools import le
from tools import video_plot

def main():
    print_ob = False
    print_ps = False
    print_bf = False
    print_le = False
    print_le_ob = False
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == "-ob":
            print_ob = True
        if sys.argv[i] == "-ps":
            print_ps = True
        if sys.argv[i] == "-bf":
            print_bf = True
        if sys.argv[i] == "-le":
            print_le = True
        if sys.argv[i] == "-le-ob" or sys.argv[i] == "-ob-le":
            print_le_ob = True

    default_folder = ana_default_data.default_folder
    default_file_code = ana_default_data.default_file_code
    default_para_use = ana_default_data.default_para_use
    default_x_use = ana_default_data.default_x_use
    default_x_range = ana_default_data.default_x_range
    default_ob_use = ana_default_data.default_ob_use
    default_ob_interval = ana_default_data.default_ob_interval
    default_ps_use = ana_default_data.default_ps_use
    default_ps_interval = ana_default_data.default_ps_interval
    name_code_length = ana_default_data.name_code_length

    file_list = []
    for i in range(0, len(default_folder)):
        for j in range(default_file_code[i][0], default_file_code[i][1]+1):
            file_list.append(default_folder[i] + "/" + str(j))

    if print_ob:
        attr_plot.attr_plot(file_list, default_ob_use, default_para_use, default_ob_interval, "ob", name_code_length)
    if print_ps:
        attr_plot.attr_plot(file_list, default_ps_use, default_para_use, default_ps_interval, "ps", name_code_length)
    if print_bf:
        bf.bf(file_list, default_para_use, default_x_use, default_x_range)
    if print_le:
        le.le(file_list, default_para_use)
    if print_le_ob:
        video_plot.video_plot(file_list, default_ob_use, default_para_use, default_ob_interval, "ob", name_code_length)


    
if __name__ == '__main__':
    main()