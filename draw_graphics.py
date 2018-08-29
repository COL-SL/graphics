import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import mysql.connector as mariadb
import numpy as np


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
                   "total_messages FROM alarmas_infracast WHERE date BETWEEN  "
                   "%s AND %s",('2018-08-29 01:00:00', '2018-08-29 17:00:00'))

    for row in CURSOR:
        list_result_query.append(row)

    for row in list_result_query:
        for content in row:
            if content == HIGH_FAILURE_RATE:
                list_result_failure_rate.append(row)
            elif content == HIGH_ENROUTE_RATE:
                list_result_enroute_rate.append(row)

    draw_failure_rate(list_result_failure_rate)
    draw_enroute_rate(list_result_enroute_rate)


def draw_failure_rate(list_result_failure_rate):
    ig0, ax0 = plt.subplots()

    print(list_result_failure_rate)

    for row in list_result_failure_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 53:
                print(country_code)
                #print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                print(country)
                x_axis = 10
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs',color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 34:
                #print(row)
                #print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                print(country)
                x_axis = 20
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs',color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 44:
                #print(row)
                #print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                print(country)
                x_axis = 30
                ax0.plot(x_axis , percent, 'ro')
                ax0.plot(x_axis , affected_messages, 'bs',color='C1')
                ax0.plot(x_axis , total_messages, 'g^', color='C2')
                plt.text(x_axis , -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 33:
                print(country_code)
                #print(row)
                #print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 40
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                print("country ",country)
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 55:
                print(country_code)
                # print(row)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 40
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                print("country ", country)
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )
    l = mlines.Line2D([0, 100], [100, 100], color='red', markersize=10, label='limit percent')
    plt.text(-7, 80.0, "Warning!! \n maxim failure rate", size=6, rotation=0.,
             ha="center", va="bottom",
             bbox=dict(boxstyle="round",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )
    ax0.add_line(l)
    ax0.axis((0, 100, 0, 1000))
      # dotted red
    plt.show()

    #X, Y = (np.linspace(-10, 3, 100),
    #        np.linspace(-10, 3, 100))

    #U, V = np.mgrid[-3:3:100j, 0:0:100j]

    #seed_points = np.array([[70,0, 0], [0,500, 0]])

    #fig0, ax0 = plt.subplots()
    #strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2,
    #                      cmap=plt.cm.autumn, start_points=seed_points.T)
    #fig0.colorbar(strm.lines)
    '''
    ig0, ax0 = plt.subplots()
    ax0.plot(300, 1111, 'bo')

    ax0.axis((0, 600, 0, 3000))

    plt.show()
  
    '''


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


def draw_enroute_rate(list_result_enroute_rate):
    ig0, ax0 = plt.subplots()

    for row in list_result_enroute_rate:
        for country_code in row:
            if country_code == row[1] and country_code == 53:
                print(country_code)
                print(row)
                print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 10
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 34:
                print(country_code)
                print(row)
                print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 20
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 44:
                print(country_code)
                print(row)
                print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = 'UK'
                x_axis = 30
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 33:
                print(country_code)
                print(row)
                print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 40
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

            elif country_code == row[1] and country_code == 55:
                print(country_code)
                # print(row)
                # print(row[4])
                percent = row[4]
                affected_messages = row[5]
                total_messages = row[6]
                country = row[2]
                x_axis = 40
                ax0.plot(x_axis, percent, 'ro')
                ax0.plot(x_axis, affected_messages, 'bs', color='C1')
                ax0.plot(x_axis, total_messages, 'g^', color='C2')
                print("country ", country)
                plt.text(x_axis, -55.0, country, size=8, rotation=0.,
                         ha="center", va="bottom",
                         bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8),
                                   )
                         )

    ax0.axis((0, 100, 0, 1100))
    plt.show()