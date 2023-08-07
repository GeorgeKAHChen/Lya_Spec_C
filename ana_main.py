import ana_default_data
import sys
from tools import attr_plot
from tools import bf
from tools import le

def main():
    print_ob = False
    print_ps = False
    print_bf = False
    print_le = False
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == "-ob":
            print_ob = True
        if sys.argv[i] == "-ps":
            print_ps = True
        if sys.argv[i] == "-bf":
            print_bf = True
        if sys.argv[i] == "-le":
            print_le = True

    file_list = []
    for i in range(0, len(ana_default_data.default_folder)):
        for j in range(ana_default_data.default_file_code[i][0], ana_default_data.default_file_code[i][1]+1):
            file_list.append(ana_default_data.default_folder[i] + "/" + str(j))
    #print(file_list)
    if print_ob:
        default_ob_use = ana_default_data.default_ob_use
        default_para_use = ana_default_data.default_para_use
        default_ob_interval = ana_default_data.default_ob_interval
        attr_plot.attr_plot(file_list, default_ob_use, default_para_use, default_ob_interval, "ob")
    if print_ps:
        default_ps_use = ana_default_data.default_ps_use
        default_para_use = ana_default_data.default_para_use
        default_ps_interval = ana_default_data.default_ps_interval
        attr_plot.attr_plot(file_list, default_ps_use, default_para_use, default_ps_interval, "ps")
    if print_bf:
        default_para_use = ana_default_data.default_para_use
        default_x_use = ana_default_data.default_x_use
        default_x_range = ana_default_data.default_x_range
        bf.bf(file_list, default_para_use, default_x_use, default_x_range)
    if print_le:
        default_para_use = ana_default_data.default_para_use
        le.le(file_list, default_para_use)


    
if __name__ == '__main__':
    main()