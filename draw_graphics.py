import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import mysql.connector as mariadb
import numpy as np
from matplotlib.lines import Line2D


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
                   "%s AND %s",('2018-08-30 10:00:00', '2018-08-30 20:00:00'))

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
    check_total_countrys_code_593 = True
    check_total_countrys_code_51 = True
    check_axis_code_34 = True
    check_axis_code_44 = True
    check_axis_code_58 = True
    check_axis_code_593 = True
    check_axis_code_51 = True
    check_count = 0
    check_country_code_34 = 0
    check_country_code_44 = 0
    check_country_code_58 = 0
    check_country_code_593 = 0
    check_country_code_51 = 0
    #ig0, ax0 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    #ig0.canvas.set_window_title('HIGH FAILURE RATE')
    number_country_code_34 = 0
    number_country_code_44 = 0
    number_country_code_58 = 0
    number_country_code_593 = 0
    number_country_code_51 = 0

    for row in list_result_failure_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 44:
                number_country_code_44 = number_country_code_44 + 1
            elif country_code == row[1] and country_code == 34:
                number_country_code_34 = number_country_code_34 + 1
            elif country_code == row[1] and country_code == 58:
                number_country_code_58 = number_country_code_58 + 1
            elif country_code == row[1] and country_code == 593:
                number_country_code_593 = number_country_code_593 + 1
            elif country_code == row[1] and country_code == 51:
                number_country_code_51 = number_country_code_51 + 1



    print('HIGH FAILURE RATE :', number_country_code_34)

    for row in list_result_failure_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 34:
                check_country_code_34 = check_country_code_34 + 1
                if check_total_countrys_code_34 == True:
                    country = row[2]
                    print(country)
                    country =  country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH FAILURE RATE: ' + country)
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
                    check_total_countrys_code_34 = False
                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]

                x_axis = 0.5
                x_axis_2 = 1
                x_axis_3 = 1.5

                ax1.plot(x_axis, percent, 'ro')
                ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')

                if check_country_code_34 == number_country_code_34:
                    print("\npasamos number_country_code_34: ",check_country_code_34, number_country_code_34)
                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1, 1),
                                       fc=(1., 1, 1),
                                       )
                             )
                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1.0, 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )

                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, 2, 0, 100+1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)

                    max_total_messages = max_total_messages
                    ax2.axis((0, 2, 0, max_total_messages + 100))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    plt.margins(10.9)
                    #plt.show()

            elif country_code == row[1] and country_code == 58:
                check_country_code_58 = check_country_code_58 + 1

                if check_total_countrys_code_58 == True:
                    country = row[2]
                    print(country)
                    country =  country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH FAILURE RATE: ' + country)
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
                    check_total_countrys_code_58 = False

                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.5
                x_axis_2 = 1
                x_axis_3 = 1.5
                ax1.plot(x_axis, percent, 'ro')
                ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')

                print ("\ncheck_count: ", check_country_code_58 )
                print ("number_country_code_58: ", number_country_code_58)

                if check_country_code_58 == number_country_code_58:

                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1, 1),
                                       fc=(1., 1, 1),
                                       )
                             )

                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1.0, 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )

                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, total_countrys, 0, 100+1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)

                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 100))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    plt.margins(10.9)
                    #plt.show()

            elif country_code == row[1] and country_code == 593:
                check_country_code_593 = check_country_code_593 + 1

                if check_total_countrys_code_593 == True:
                    country = row[2]
                    print(country)
                    country = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH FAILURE RATE: ' + country)
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
                    check_total_countrys_code_593 = False

                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.5
                x_axis_2 = 1
                x_axis_3 = 1.5
                #list_axis_y_ax1 = list_axis_y_ax1.append(percent)
                ax1.plot(x_axis, percent, 'ro')
                ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')

                print ("\ncheck_count: ", check_country_code_593)
                print ("number_country_code_58: ", number_country_code_593)

                if check_country_code_593 == number_country_code_593:
                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1, 1),
                                       fc=(1., 1, 1),
                                       )
                             )

                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1., 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                             ha="center", va="bottom",
                             bbox=dict(boxstyle="round",
                                       ec=(1., 1.0, 1.0),
                                       fc=(1., 1.0, 1.0),
                                       )
                             )

                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, total_countrys, 0, 100 + 1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)

                    max_total_messages = max_total_messages
                    ax2.axis((0, total_countrys, 0, max_total_messages + 100))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    plt.margins(10.9)
                    # plt.show()

            elif country_code == row[1] and country_code == 51:
                print ("PASAMOS A PERUUUUUUUUU!!!!!!!!!!!!!!")
                check_country_code_51 = check_country_code_51 + 1
                #list_axis_y_ax1 = []


                if check_total_countrys_code_51 == True:
                    country = row[2]
                    print(country)
                    country = country + ", Gateway: " + str(row[0])
                    fig, ax1 = plt.subplots(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
                    fig.canvas.set_window_title('HIGH FAILURE RATE: ' + country)
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
                    check_total_countrys_code_51 = False

                print(country_code)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                if max_total_messages < row[6]:
                    max_total_messages = row[6]
                x_axis = 0.5
                x_axis_2 = 1
                x_axis_3 = 1.5

                x1, y1 = [x_axis_2, x_axis_3], [affected_messages, total_messages]
                ax2.plot(x1, y1,linewidth=0.3, color='C5')
                ax1.plot(x1, y1, linewidth=0.3, color='C5')

                point_one = ax1.plot(x_axis, percent, 'ro')
                point_two = ax2.plot(x_axis_2, affected_messages, 'bs', color='blue')
                ax2.plot(x_axis_3, total_messages, 'g^', color='green')




                '''
                A = np.array([[0.5, 100], [1, 175], [1.5, 5], [0.5, 5], [1, 175], [1, 7], [1, 2], [1, 5], [0.5, 5], [0.5, 200]])
                ax2.scatter(A[:, 0], A[:, 1])

                print ("A[0][0] ",A[0][0])
                print ("A[0][1] ", A[0][1])
                print("A[9][0] - A[2][0] ", A[9][0] - A[2][0])

                ax1.arrow(A[0][0], A[0][1], A[1][0] - A[0][0], A[1][1] - A[0][1], width=0.02, color='red',
                          head_length=0.0, head_width=0.0)
                '''
                '''
                ax2.arrow(A[2][0], A[2][1], 100, A[9][1], width=0.002, color='red',
                          head_length=0.0, head_width=0.0)
                

                ax2.arrow(A[4][0], A[4][1], A[6][0], A[6][1], width=0.002, color='red',
                          head_length=0.0, head_width=0.0)

                '''
                #plt.show()

                #plt.show()
                #plt.show()


                print ("\ncheck_count: ", check_country_code_51)
                print ("number_country_code_51: ", number_country_code_51)

                if check_country_code_51 == number_country_code_51:
                    plt.text(x_axis, -5, "Percent Failure", size=14, rotation=0.,
                                ha="center", va="bottom",
                                bbox=dict(boxstyle="round",
                                           ec=(1., 1, 1),
                                           fc=(1., 1, 1),
                                           )
                                 )

                    plt.text(x_axis_2, -5, "Affected Messages", size=14, rotation=0.,
                                 ha="center", va="bottom",
                                 bbox=dict(boxstyle="round",
                                           ec=(1., 1., 1.0),
                                           fc=(1., 1.0, 1.0),
                                           )
                                 )
                    plt.text(x_axis_3, -5, "Total Messages", size=14, rotation=0.,
                                 ha="center", va="bottom",
                                 bbox=dict(boxstyle="round",
                                           ec=(1., 1.0, 1.0),
                                           fc=(1., 1.0, 1.0),
                                           )
                                 )

                    print("ultimoooooooooooooooooooooooooo")
                    ax1.axis((0, total_countrys, 0, 100 + 1))
                    color = 'tab:red'
                    ax1.tick_params(axis='y', labelcolor=color)
                    #x1.add_line(l)

                    max_total_messages = max_total_messages
                    print("max_total_messages: ",max_total_messages + 100)
                    ax2.axis((0, total_countrys, 0, max_total_messages + 100))
                    color = 'tab:green'
                    ax2.tick_params(axis='y', labelcolor=color)

                    fig.tight_layout()  # otherwise the right y-label is slightly clipped
                    plt.margins(10.9)





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
                    plt.show()

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