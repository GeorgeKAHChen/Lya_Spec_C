import default_data

import sys
import matplotlib.pyplot as plt

from tools import attr_plot
from tools import bf
from tools import le
from tools import video_plot
from tools import ob_time
from tools import multi_ps
from tools import x_distribution
from tools import full_plot
from tools import order_bf
from tools import le_file_heat_map
from tools import mod_attr_plot
from tools import power_spectrum
from tools import ave_power_spectrum
from tools import high_mod_attr_plot
from tools import bf_2_img

def main():
    """
    FLAG INIT
    """ 
    print_ob = False
    print_ps = False
    print_bf = False
    print_le = False
    print_le_ob = False
    print_ob_time = False
    print_multi_ps = False
    print_distribution = False
    print_all = False
    print_order_bf = False
    plot_heat_map = False
    plot_mod_ob = False
    plot_high_mod_ob = False
    plot_power_spectrum = False
    ave_plot_power_spectrum = False
    plot_bf_2_img = False

    """
    FLAG CHECKING
    """
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
        if sys.argv[i] == "-f" or sys.argv[i] == "-full":
            print_all = True
        if sys.argv[i] == "-obf":
            print_order_bf = True
        if sys.argv[i] == "-map":
            plot_heat_map = True
        if sys.argv[i] == "-mod-ob" or sys.argv[i] == "-ob-mod":
            plot_mod_ob = True
        if sys.argv[i] == "-hmod":
            plot_high_mod_ob = True
        if sys.argv[i] == "-fft":
            plot_power_spectrum = True
        if sys.argv[i] == "-afft":
            ave_plot_power_spectrum = True
        if sys.argv[i] == "-bfd":
            plot_bf_2_img = True


    """
    DEFAULT SETTING READING
    """
    default_folder      = default_data.default_folder
    default_file_code   = default_data.default_file_code
    default_para_use    = default_data.default_para_use
    default_x_use       = default_data.default_x_use
    default_x_range     = default_data.default_x_range
    default_t_mod       = default_data.default_t_mod
    default_ob_use      = default_data.default_ob_use
    default_ob_interval = default_data.default_ob_interval
    default_ps_use      = default_data.default_ps_use
    default_ps_interval = default_data.default_ps_interval
    name_code_length    = default_data.name_code_length
    default_le_file     = default_data.default_le_file
    default_dist_file   = default_data.default_dist_file
    tikz_axis           = default_data.tikz_axis
    bf_merge            = default_data.bf_merge
    le_file_folder      = default_data.le_file_folder
    le_file_code        = default_data.le_file_code
    le_para_use         = default_data.le_para_use
    le_start            = default_data.le_start
    le_color_table      = default_data.le_color_table
    heat_map_table      = default_data.heat_map_table
    ax_will_plot        = default_data.ax_will_plot
    power_spectrum_para = default_data.power_spectrum_para

    """
    FILE LIST / LE FILE LIST INITIALIZATION
    """
    # File list init
    file_list = []
    for i in range(0, len(default_folder)):
        for j in range(default_file_code[i][0], default_file_code[i][1]+1):
            if default_folder[i][-1] != "/":
                file_list.append(default_folder[i] + "/" + str(j))
            else:
                file_list.append(default_folder[i] + str(j))

    # LE file list init
    le_file_list = []
    for i in range(0, len(le_file_folder)):
        for j in range(le_file_code[i][0], le_file_code[i][1]+1):
            if le_file_folder[i][-1] != "/":
                le_file_list.append(le_file_folder[i] + "/" + str(j))
            else:
                le_file_list.append(le_file_folder[i] + str(j))

    # LE Color map init
    for i in range(0, len(le_color_table)):
        if le_color_table[i][0] == "rgb" or le_color_table[i][0] == "rgba":
            le_color_table[i] = le_color_table[i][1]
        else:
            color_map = plt.cm.get_cmap(le_color_table[i][0])
            le_color_table[i] = color_map(le_color_table[i][1])
    for i in range(0, len(le_color_table)):
        le_color_table[i] = (255 * le_color_table[i][0], 
                             255 * le_color_table[i][1],
                             255 * le_color_table[i][2], 
                             le_color_table[i][3])



    """
    MAIN FUNCTION USING
    """
    if print_ob:
        attr_plot.attr_plot(file_list, 
            default_ob_use, 
            default_para_use, 
            default_ob_interval, 
            "ob", 
            name_code_length)

    if print_ps:
        attr_plot.attr_plot(file_list, 
            default_ps_use, 
            default_para_use, 
            default_ps_interval, 
            "ps", 
            name_code_length)

    if print_bf:
        bf.bf(file_list, 
            default_para_use, 
            default_x_use, 
            default_x_range)

    if print_le:
        le.le(file_list, 
            default_para_use)

    if print_le_ob:
        video_plot.video_plot(file_list, 
            default_ob_use, 
            default_para_use, 
            default_ob_interval, 
            "ob", 
            name_code_length)

    if print_ob_time:
        ob_time.ob_time(file_list, 
            default_x_use, 
            default_x_range)

    if print_multi_ps:
        multi_ps.multi_ps(file_list, 
            default_para_use, 
            default_ob_interval, 
            name_code_length)

    if print_distribution:
        x_distribution.x_distribution(file_list, 
            default_para_use, 
            default_x_use, 
            default_x_range, 
            dist_to_data,
            )

    if print_all:
        full_plot.full_plot(file_list, 
            default_para_use, 
            default_x_use, 
            default_x_range, 
            default_ob_use, 
            default_ob_interval, 
            default_le_file, 
            default_dist_file, 
            tikz_axis,
            bf_merge,
            ax_will_plot)

    if print_order_bf:
        order_bf.order_bf(file_list, 
            default_para_use, 
            default_x_use, 
            default_x_range)

    if plot_heat_map:
        le_file_heat_map.le_file_heat_map(le_file_list,
            le_para_use,
            le_start,
            le_color_table,
            heat_map_table)

    if plot_mod_ob:
        mod_attr_plot.mod_attr_plot(file_list,
            default_x_use, 
            default_x_range,
            default_t_mod
            )

    if plot_power_spectrum:
        power_spectrum.power_spectrum(file_list,
            power_spectrum_para,
            default_x_use,
            tikz_axis
            )

    if ave_plot_power_spectrum:
        ave_power_spectrum.ave_power_spectrum(file_list,
            power_spectrum_para,
            default_x_use,
            tikz_axis,
            default_file_code
            )

    if plot_high_mod_ob:
        high_mod_attr_plot.high_mod_attr_plot(file_list,
            default_x_use, 
            default_x_range,
            default_t_mod
            )

    if plot_bf_2_img:
        bf_2_img.bf_2_img(file_list)
    return 



if __name__ == '__main__':
    main()









