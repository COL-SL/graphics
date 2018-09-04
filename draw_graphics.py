from tkinter import PhotoImage
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import mysql.connector as mariadb
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import plotly.tools as tls
import random

PATH_WARNING = '.\images\warning.png'
PATH_OK = '.\images\ok.png'
NUMBER_PROCCES = 0
#fig, ax1 = plt.subplots(num=10, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
#fig, ax1 = plt.subplots(num=10, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
#thismanager = plt.get_current_fig_manager()
#thismanager.window.geometry("1160x820")
#thismanager.window.minsize(width=820, height=822)
#thismanager.window.state('wit''hdrawn')


def draw_last_two_hour():
    list_result_query = []
    SEVEN_ITEMS = 7
    list_result_failure_rate = []
    list_result_enroute_rate = []
    HIGH_FAILURE_RATE = "high failure rate"
    HIGH_ENROUTE_RATE = "high enroute rate"
    MARIADB_CONNECTION = mariadb.connect(user='root', password='', database='infracast_monitor')
    CURSOR = MARIADB_CONNECTION.cursor()
    CURSOR.execute("SELECT gateway, country_code, country, high_rate, percent, affected_messages, "
                   "total_messages FROM alarmas_infracast  WHERE date BETWEEN"
                   "%s AND %s",('2018-09-04 16:00:00', '2018-09-04 17:00:00'))

    for row in CURSOR:
        list_result_query.append(row)

    list_result_query = sorted(list_result_query)

    for row in list_result_query:
        for content in row:
            if content == HIGH_FAILURE_RATE:
                list_result_failure_rate.append(row)
            elif content == HIGH_ENROUTE_RATE:
                list_result_enroute_rate.append(row)

    draw_failure_rate(list_result_failure_rate)
    draw_enroute_rate(list_result_enroute_rate)



def draw_failure_rate(list_result_failure_rate):
    print('HIGH FAILURE RATE :', list_result_failure_rate)
    check_total_countrys_code_34 = True
    check_total_countrys_code_44 = True
    check_total_countrys_code_58 = True
    check_total_countrys_code_55 = True
    check_total_countrys_code_505 = True
    check_total_countrys_code_593 = True
    check_total_countrys_code_51 = True
    check_axis_code_34 = True
    check_axis_code_44 = True
    check_axis_code_58 = True
    check_axis_code_55 = True
    check_axis_code_505 = True
    check_axis_code_593 = True
    check_axis_code_51 = True
    check_axis_code_51_percent = True
    check_axis_code_58 = True
    check_axis_code_55 = True
    check_axis_code_505 = True
    check_axis_code_58_percent = True
    check_axis_code_55_percent = True
    check_axis_code_505_percent = True
    check_axis_code_593_percent = True
    check_percent_51 = True
    check_percent_58 = True
    check_percent_55 = True
    check_percent_505 = True
    check_count = 0
    check_country_code_34 = 0
    check_country_code_44 = 0
    check_country_code_58 = 0
    check_country_code_55 = 0
    check_country_code_505 = 0
    check_country_code_593 = 0
    check_country_code_51 = 0
    check_country_code_58 = 0
    check_country_code_55 = 0
    check_country_code_505 = 0
    #ig0, ax0 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    #ig0.canvas.set_window_title('HIGH FAILURE RATE')
    number_country_code_34 = 0
    number_country_code_44 = 0
    number_country_code_58 = 0
    number_country_code_55 = 0
    number_country_code_505 = 0
    number_country_code_593 = 0
    number_country_code_51 = 0
    max_total_messages_draw_51 = 0
    number_country_code_58 = 0
    number_country_code_55 = 0
    number_country_code_505 = 0
    max_total_messages_draw_58 = 0
    max_total_messages_draw_55 = 0
    max_total_messages_draw_505 = 0
    max_total_messages_draw_593 = 0

    font_warning = {'color': 'r',
            'weight':
                'bold',

            'size': 16}

    font_no_warning = {'color': 'k',
                    'weight': 'bold',
                    'size': 16}

    list_axis_y_ax1_51 = []
    list_axis_y_ax1_58 = []
    list_axis_y_ax1_55 = []
    list_axis_y_ax1_505 = []
    list_axis_y_ax1_593 = []
    list_affected_messages_y_ax2_593 = []
    list_affected_messages_y_ax2_51 = []
    list_affected_messages_y_ax2_58 = []
    list_affected_messages_y_ax2_55 = []
    list_affected_messages_y_ax2_505 = []
    list_color_ramdom_505 = []

    for row in list_result_failure_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 44:
                number_country_code_44 = number_country_code_44 + 1
            elif country_code == row[1] and country_code == 34:
                number_country_code_34 = number_country_code_34 + 1
            elif country_code == row[1] and country_code == 58:
                number_country_code_58 = number_country_code_58 + 1
            elif country_code == row[1] and country_code == 55:
                number_country_code_55 = number_country_code_55 + 1
            elif country_code == row[1] and country_code == 505:
                number_country_code_505 = number_country_code_505 + 1
            elif country_code == row[1] and country_code == 593:
                number_country_code_593 = number_country_code_593 + 1
            elif country_code == row[1] and country_code == 51:
                number_country_code_51 = number_country_code_51 + 1

    print('HIGH FAILURE RATE :', number_country_code_34)

    for row in list_result_failure_rate:
        for country_code in row:
            #print (country_code)
            #print (row[1])
            #print ('\n')
            if country_code == row[1] and country_code == 593: #Ecuador
                check_country_code_593 = check_country_code_593 + 1
                if check_total_countrys_code_593 == True:
                    country = row[2]
                    country_gateway = country
                    country_gateway = country + ", Gateway: " + str(row[0])
                    #thismanager = plt.get_current_fig_manager()
                    #thismanager.window.geometry("1160x820")
                    #thismanager.window.minsize(width=820, height=822)
                    #thismanager.window.state('wit''hdrawn')
                    fig, ax1 = plt.subplots(num=country, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values', size=15)
                    ax1.set_ylabel('Percent failure rate', color=color, size=15)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                       color=color, size=15)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys_code_593 = False
                percent = row[4]
                if percent >= 60:
                    img = PhotoImage(file='.\images\warning.png')
                    #thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr = 'EXCEEDS 60% of FAILED messages'
                    pkg_name_arr_gateway = 'WARNING!!! HIGH FAILURE RATE: '+ country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway)
                    ax1.set_title('WARNING!!! ' + country_gateway + '. ' + pkg_name_arr, **font_warning)
                    check_percent_593 = False
                if percent < 60 and check_percent_593 == True:
                    img = PhotoImage(file='.\images\ok.png')
                    #thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr_gateway = 'HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway, )
                    ax1.set_title(country_gateway + ' ' + pkg_name_arr, **font_no_warning)

                list_axis_y_ax1_593.append(percent)
                affected_messages = row[5]
                list_affected_messages_y_ax2_593.append(affected_messages)
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.25
                x_axis_2 = 1
                x_axis_3 = 1.75

                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1,linewidth=0.3, color='C5')

                if check_axis_code_593 ==  False:
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green')
                elif check_axis_code_593 == True:
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green', label='Total Messages')
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue', label='Affected Messages')
                    check_axis_code_593 = False

                if check_country_code_593 == number_country_code_593:
                    count_points = 0
                    max_total_messages_draw_593 = max_total_messages + 50
                    for point_y_ax1 in list_axis_y_ax1_593:
                        point_final_converter = (point_y_ax1 * max_total_messages_draw_593) / 101
                        point_final_converter = int(point_final_converter)
                        point_final_total_messages = list_affected_messages_y_ax2_593[count_points]
                        x1, y1 = [x_axis, x_axis_2], [point_final_converter, point_final_total_messages]
                        count_points = count_points + 1
                        if check_axis_code_593_percent == False:
                            ax2.plot(x1, y1, linewidth=0.3, color='C5')
                            ax2.plot(x_axis, point_final_converter, 'ro')
                        elif check_axis_code_593_percent == True:
                            ax2.plot(x_axis, point_final_converter, 'ro',  label='Percent Failure')
                            ax2.plot(x1, y1, linewidth=0.3, color='C5', label='At the same time')
                            check_axis_code_593_percent = False

                    ax2.legend(loc='best', fancybox=True, framealpha=0.5)
                    ax1.axis((0, total_countrys, 0, 101))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 50))
                    color = 'tab:blue'
                    ax2.tick_params(axis='y', labelcolor=color)
                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    #plt.show()

            elif country_code == row[1] and country_code == 51: #Peru
                check_country_code_51 = check_country_code_51 + 1
                if check_total_countrys_code_51 == True:
                    NUMBER_PROCCES = country_code + 1
                    country = row[2]
                    country_gateway = country
                    country_gateway = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=country, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    #thismanager = plt.get_current_fig_manager()
                    #thismanager.window.geometry("1160x820")
                    #thismanager.window.minsize(width=820, height=822)
                    #thismanager.window.state('wit''hdrawn')
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values', size=15)
                    ax1.set_ylabel('Percent failure rate', color=color, size=15)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                       color=color, size=15)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys_code_51 = False
                percent = row[4]
                if percent >= 60:
                    #thismanager = plt.get_current_fig_manager()
                    #thismanager.window.geometry("1160x820")
                    #thismanager.window.minsize(width=820, height=822)
                    #thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\warning.png')
                    #thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr = 'EXCEEDS 60% of FAILED messages'
                    pkg_name_arr_gateway = 'WARNING!!! HIGH FAILURE RATE: '+ country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway)
                    ax1.set_title('WARNING!!! ' + country_gateway + '. ' + pkg_name_arr, **font_warning)
                    check_percent_51 = False
                if percent < 60 and check_percent_51 == True:
                    #thismanager = plt.get_current_fig_manager()
                    #thismanager.window.geometry("1160x820")
                    #thismanager.window.minsize(width=820, height=822)
                    #thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\ok.png')
                    #thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr_gateway = 'HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway, )
                    ax1.set_title(country_gateway + ' ' + pkg_name_arr, **font_no_warning)

                list_axis_y_ax1_51.append(percent)
                affected_messages = row[5]
                list_affected_messages_y_ax2_51.append(affected_messages)
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.25
                x_axis_2 = 1
                x_axis_3 = 1.75

                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1,linewidth=0.3, color='C5')

                if check_axis_code_51 ==  False:
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green')
                elif check_axis_code_51 == True:
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green', label='Total Messages')
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue', label='Affected Messages')
                    check_axis_code_51 = False

                if check_country_code_51 == number_country_code_51:
                    count_points = 0
                    max_total_messages_draw_51 = max_total_messages + 50
                    for point_y_ax1 in list_axis_y_ax1_51:
                        point_final_converter = (point_y_ax1 * max_total_messages_draw_51) / 101
                        point_final_converter = int(point_final_converter)
                        point_final_total_messages = list_affected_messages_y_ax2_51[count_points]
                        x1, y1 = [x_axis, x_axis_2], [point_final_converter, point_final_total_messages]
                        count_points = count_points + 1
                        if check_axis_code_51_percent == False:
                            ax2.plot(x1, y1, linewidth=0.3, color='C5')
                            ax2.plot(x_axis, point_final_converter, 'ro')
                        elif check_axis_code_51_percent == True:
                            ax2.plot(x_axis, point_final_converter, 'ro',  label='Percent Failure')
                            ax2.plot(x1, y1, linewidth=0.3, color='C5', label='At the same time')
                            check_axis_code_51_percent = False

                    ax2.legend(loc='best', fancybox=True, framealpha=0.5)
                    ax1.axis((0, total_countrys, 0, 101))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 50))
                    color = 'tab:blue'
                    ax2.tick_params(axis='y', labelcolor=color)
                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    NUMBER_PROCCES = NUMBER_PROCCES + 1
                    #plt.show()

            elif country_code == row[1] and country_code == 58: #Venezuela
                check_country_code_58 = check_country_code_58 + 1
                if check_total_countrys_code_58 == True:
                    NUMBER_PROCCES = country_code + 1
                    country = row[2]
                    country_gateway = country
                    country_gateway = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=country, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values', size=15)
                    ax1.set_ylabel('Percent failure rate', color=color, size=15)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                       color=color, size=15)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys_code_58 = False
                percent = row[4]
                if percent >= 60:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\warning.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr = 'EXCEEDS 60% of FAILED messages'
                    pkg_name_arr_gateway = 'WARNING!!! HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway)
                    ax1.set_title('WARNING!!! ' + country_gateway + '. ' + pkg_name_arr, **font_warning)
                    check_percent_58 = False
                if percent < 60 and check_percent_58 == True:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\ok.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr_gateway = 'HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway, )
                    ax1.set_title(country_gateway + ' ' + pkg_name_arr, **font_no_warning)

                list_axis_y_ax1_58.append(percent)
                affected_messages = row[5]
                list_affected_messages_y_ax2_58.append(affected_messages)
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.25
                x_axis_2 = 1
                x_axis_3 = 1.75

                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1, linewidth=0.3, color='C5')

                if check_axis_code_58 == False:
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green')
                elif check_axis_code_58 == True:
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green', label='Total Messages')
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue', label='Affected Messages')
                    check_axis_code_58 = False

                if check_country_code_58 == number_country_code_58:
                    count_points = 0
                    max_total_messages_draw_58 = max_total_messages + 50
                    for point_y_ax1 in list_axis_y_ax1_58:
                        point_final_converter = (point_y_ax1 * max_total_messages_draw_58) / 101
                        point_final_converter = int(point_final_converter)
                        point_final_total_messages = list_affected_messages_y_ax2_58[count_points]
                        x1, y1 = [x_axis, x_axis_2], [point_final_converter, point_final_total_messages]
                        count_points = count_points + 1
                        if check_axis_code_58_percent == False:
                            ax2.plot(x1, y1, linewidth=0.3, color='C5')
                            ax2.plot(x_axis, point_final_converter, 'ro')
                        elif check_axis_code_58_percent == True:
                            ax2.plot(x_axis, point_final_converter, 'ro', label='Percent Failure')
                            ax2.plot(x1, y1, linewidth=0.3, color='C5', label='At the same time')
                            check_axis_code_58_percent = False

                    ax2.legend(loc='best', fancybox=True, framealpha=0.5)
                    ax1.axis((0, total_countrys, 0, 101))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 50))
                    color = 'tab:blue'
                    ax2.tick_params(axis='y', labelcolor=color)
                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    NUMBER_PROCCES = NUMBER_PROCCES + 1
                    # plt.show()

            elif country_code == row[1] and country_code == 55: #Brazil
                check_country_code_55 = check_country_code_55 + 1
                if check_total_countrys_code_55 == True:
                    NUMBER_PROCCES = country_code + 1
                    country = row[2]
                    country_gateway = country
                    country_gateway = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=country, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values', size=15)
                    ax1.set_ylabel('Percent failure rate', color=color, size=15)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                       color=color, size=15)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys_code_55 = False
                percent = row[4]
                if percent >= 60:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\warning.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr = 'EXCEEDS 60% of FAILED messages'
                    pkg_name_arr_gateway = 'WARNING!!! HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway)
                    ax1.set_title('WARNING!!! ' + country_gateway + '. ' + pkg_name_arr, **font_warning)
                    check_percent_55 = False
                if percent < 60 and check_percent_55 == True:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\ok.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr_gateway = 'HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway, )
                    ax1.set_title(country_gateway + ' ' + pkg_name_arr, **font_no_warning)

                list_axis_y_ax1_55.append(percent)
                affected_messages = row[5]
                list_affected_messages_y_ax2_55.append(affected_messages)
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.25
                x_axis_2 = 1
                x_axis_3 = 1.75

                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1, linewidth=0.3, color='C5')

                if check_axis_code_55 == False:
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green')
                elif check_axis_code_55 == True:
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green', label='Total Messages')
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue', label='Affected Messages')
                    check_axis_code_55 = False

                if check_country_code_55 == number_country_code_55:
                    count_points = 0
                    max_total_messages_draw_55 = max_total_messages + 10
                    for point_y_ax1 in list_axis_y_ax1_55:
                        point_final_converter = (point_y_ax1 * max_total_messages_draw_55) / 101
                        point_final_converter = int(point_final_converter)
                        point_final_total_messages = list_affected_messages_y_ax2_55[count_points]
                        x1, y1 = [x_axis, x_axis_2], [point_final_converter, point_final_total_messages]
                        count_points = count_points + 1
                        if check_axis_code_55_percent == False:
                            ax2.plot(x1, y1, linewidth=0.3, color='C5')
                            ax2.plot(x_axis, point_final_converter, 'ro')
                        elif check_axis_code_55_percent == True:
                            ax2.plot(x_axis, point_final_converter, 'ro', label='Percent Failure')
                            ax2.plot(x1, y1, linewidth=0.3, color='C5', label='At the same time')
                            check_axis_code_55_percent = False

                    ax2.legend(loc='best', fancybox=True, framealpha=0.5)
                    ax1.axis((0, total_countrys, 0, 101))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 10))
                    color = 'tab:blue'
                    ax2.tick_params(axis='y', labelcolor=color)
                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    NUMBER_PROCCES = NUMBER_PROCCES + 1
                    # plt.show()

            elif country_code == row[1] and country_code == 505: #Nicaragua
                check_country_code_505 = check_country_code_505 + 1
                if check_total_countrys_code_505 == True:
                    NUMBER_PROCCES = country_code + 1
                    country = row[2]
                    country_gateway = country
                    country_gateway = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=country, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values', size=15)
                    ax1.set_ylabel('Percent failure rate', color=color, size=15)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                       color=color, size=15)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys_code_505 = False
                percent = row[4]
                if percent >= 60:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\warning.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr = 'EXCEEDS 60% of FAILED messages'
                    pkg_name_arr_gateway = 'WARNING!!! HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway)
                    ax1.set_title('WARNING!!! ' + country_gateway + '. ' + pkg_name_arr, **font_warning)
                    check_percent_505 = False
                if percent < 60 and check_percent_505 == True:
                    # thismanager = plt.get_current_fig_manager()
                    # thismanager.window.geometry("1160x820")
                    # thismanager.window.minsize(width=820, height=822)
                    # thismanager.window.state('wit''hdrawn')
                    img = PhotoImage(file='.\images\ok.png')
                    # thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
                    pkg_name_arr = ''
                    pkg_name_arr_gateway = 'HIGH FAILURE RATE: ' + country_gateway
                    fig.canvas.set_window_title(pkg_name_arr_gateway, )
                    ax1.set_title(country_gateway + ' ' + pkg_name_arr, **font_no_warning)

                list_axis_y_ax1_505.append(percent)
                affected_messages = row[5]
                list_affected_messages_y_ax2_505.append(affected_messages)
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.25
                x_axis_2 = 1
                x_axis_3 = 1.75

                number_random = random.randrange(10)
                color_ramdom = 'C' + str(number_random)
                print ("ARRIBA: ", color_ramdom)
                list_color_ramdom_505.append(color_ramdom)


                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1, linewidth=0.4, color=color_ramdom)

                if check_axis_code_505 == False:
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green')
                elif check_axis_code_505 == True:
                    ax2.plot(x_axis_3, total_messages, 'g^', color='green', label='Total Messages')
                    ax2.plot(x_axis_2, affected_messages, 'bs', color='blue', label='Affected Messages')
                    check_axis_code_505 = False

                if check_country_code_505 == number_country_code_505:
                    count_points = 0
                    count_points_color = 0
                    max_total_messages_draw_505 = max_total_messages + 10
                    for point_y_ax1 in list_axis_y_ax1_505:
                        point_final_converter = (point_y_ax1 * max_total_messages_draw_505) / 101
                        point_final_converter = int(point_final_converter)
                        point_final_total_messages = list_affected_messages_y_ax2_505[count_points]
                        x1, y1 = [x_axis, x_axis_2], [point_final_converter, point_final_total_messages]
                        color_ramdom_down = list_color_ramdom_505[count_points]

                        print ("count_points_color: ", count_points_color)
                        count_points = count_points + 1
                        if check_axis_code_505_percent == False:
                            count_points_color = count_points_color + 1
                            print ("ABAJO: ", color_ramdom_down)
                            ax2.plot(x1, y1, linewidth=0.4, color=color_ramdom_down)
                            ax2.plot(x_axis, point_final_converter, 'ro')
                        elif check_axis_code_505_percent == True:
                            print ("ABAJO: ", color_ramdom_down)
                            ax2.plot(x_axis, point_final_converter, 'ro', label='Percent Failure')
                            ax2.plot(x1, y1, linewidth=0.4, color=color_ramdom_down, label='At the same time')
                            check_axis_code_505_percent = False

                    ax2.legend(loc='best', fancybox=True, framealpha=0.5)
                    ax1.axis((0, total_countrys, 0, 101))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 10))
                    color = 'tab:blue'
                    ax2.tick_params(axis='y', labelcolor=color)
                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    NUMBER_PROCCES = NUMBER_PROCCES + 1
                    # plt.show()









def draw_enroute_rate(list_result_enroute_rate):
    print('HIGH ENROUTE RATE :', list_result_enroute_rate)
    check_total_countrys = True
    check_axis = True
    check_count = 0
    # ig0, ax0 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    # ig0.canvas.set_window_title('HIGH FAILURE RATE')
    number_country_code_34 = 0
    number_country_code_33 = 0
    number_country_code_44 = 0

    for row in list_result_enroute_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 34:
                number_country_code_34 = number_country_code_34 + 1

    for row in list_result_enroute_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 44:
                number_country_code_44 = number_country_code_44 + 1

    for row in list_result_enroute_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 33:
                number_country_code_33 = number_country_code_33 + 1

    #print('HIGH ENROUTE RATE :', number_country_code_34)

    for row in list_result_enroute_rate:
        for country_code in row:

            if country_code == row[1] and country_code == 44:
                check_count = check_count + 1
                if check_total_countrys == True:
                    country = row[2]
                    print(country)
                    country = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH ENROUTE RATE: ' + country)
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values')
                    ax1.set_ylabel('Percent failure rate', color=color)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                   color=color)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    x_axis = 0
                    x_axis_2 = 0
                    x_axis_3 = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys = False
                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                if check_axis == True:
                    x_axis = x_axis + 0.5
                    x_axis_2 = x_axis + 0.5
                    x_axis_3 = x_axis_2 + 0.5
                    check_axis = False
                ax1.plot(x_axis, percent, 'ro')
                ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')

                if check_count == number_country_code_44:
                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    check_axis = True
                    check_total_countrys = True
                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, total_countrys, 0, 100+1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)

                    max_total_messages = max_total_messages + 200
                    ax2.axis((0, total_countrys, 0, max_total_messages))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    #plt.show()

            if country_code == row[1] and country_code == 33:
                check_count = check_count + 1
                if check_total_countrys == True:
                    country = row[2]
                    print(country)
                    country = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH ENROUTE RATE: ' + country)
                    color = 'tab:red'
                    ax1.set_xlabel('Differents values')
                    ax1.set_ylabel('Percent failure rate', color=color)
                    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
                    color = 'tab:blue'
                    ax2.set_ylabel('Affected messages and Total messages',
                                   color=color)  # we already handled the x-label with ax1
                    max_total_messages = 0
                    total_countrys = 0
                    x_axis = 0
                    x_axis_2 = 0
                    x_axis_3 = 0
                    total_countrys = total_countrys + 2
                    check_total_countrys = False
                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                if check_axis == True:
                    x_axis = x_axis + 0.5
                    x_axis_2 = x_axis + 0.5
                    x_axis_3 = x_axis_2 + 0.5
                    check_axis = False
                ax1.plot(x_axis, percent, 'ro')
                ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')

                if check_count == number_country_code_33:
                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.),
                                       fc=(1., 1., 1.),
                                       )
                             )
                    check_axis = True
                    check_total_countrys = True
                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, total_countrys, 0, 100+1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)

                    max_total_messages = max_total_messages + 200
                    ax2.axis((0, total_countrys, 0, max_total_messages))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    #plt.show()

    plt.show()
