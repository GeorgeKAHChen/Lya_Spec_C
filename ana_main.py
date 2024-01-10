import default_data
import sys
from tools import attr_plot
from tools import bf
from tools import le
from tools import video_plot
from tools import ob_time
from tools import multi_ps
from tools import x_distribution



def main():
    print_ob = False
    print_ps = False
    print_bf = False
    print_le = False
    print_le_ob = False
    print_ob_time = False
    print_multi_ps = False
    print_distribution = False
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
        if sys.argv[i] == "-obt":
            print_ob_time = True
        if sys.argv[i] == "-mps":
            print_multi_ps = True
        if sys.argv[i] == "-distribution" or sys.argv[i] == "-dist":
            print_distribution = True
            dist_to_data = False
        if sys.argv[i] == "-distribution-data" or sys.argv[i] == "-dist-data":
            print_distribution = True
            dist_to_data = True

    default_folder = default_data.default_folder
    default_file_code = default_data.default_file_code
    default_para_use = default_data.default_para_use
    default_x_use = default_data.default_x_use
    default_x_range = default_data.default_x_range
    default_ob_use = default_data.default_ob_use
    default_ob_interval = default_data.default_ob_interval
    default_ps_use = default_data.default_ps_use
    default_ps_interval = default_data.default_ps_interval
    name_code_length = default_data.name_code_length

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
    if print_ob_time:
        ob_time.ob_time(file_list, default_x_use, default_x_range)
    if print_multi_ps:
        multi_ps.multi_ps(file_list, default_para_use, default_ob_interval, name_code_length)
    if print_distribution:
        x_distribution.x_distribution(file_list, default_para_use, default_x_use, default_x_range, to_data = dist_to_data)
    
if __name__ == '__main__':
    main()