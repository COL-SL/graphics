
from tkinter import PhotoImage
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

PATH_WARNING = '.\images\warning.png'
PATH_TICK = '.\images\ok.png'

def test_2():

    plt.figure(num=1, figsize=(16, 12))
    thismanager = plt.get_current_fig_manager()
    img = PhotoImage(name="icon.ppm")
    thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)

    plt.figure(num=2, figsize=(10, 8))
    thismanager2 = plt.get_current_fig_manager()
    img2 = PhotoImage(name="icon.ppm")
    thismanager2.window.tk.call('wm', 'iconphoto', thismanager2.window._w, img2)

    plt.show()


def test_3():
    thismanager = plt.get_current_fig_manager()

    thismanager.window.geometry("620x622")
    thismanager.window.minsize(width=320, height =322)
    thismanager.window.state('normal')
    img = PhotoImage(file='.\images\warning.png')

    plt.figure(num=1, figsize=(9200, 3220))
    thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
    #plt.plot(date, energyplot, 'bo')
    plt.show()
'''

from matplotlib import pyplot as plt#from Qt import QtWidgets
from tkinter import PhotoImage

def test_4():
    ### for 'TkAgg' backend
    img = PhotoImage(file='.\images\warning.png')
    plt.figure(1)
    plt.switch_backend('TkAgg') #TkAgg (instead Qt4Agg)
    print ('#1 Backend:',plt.get_backend())
    plt.plot([1,2,6,4])
    mng = plt.get_current_fig_manager()
    ### works on Ubuntu??? >> did NOT working on windows
    # mng.resize(*mng.window.maxsize())
    mng.window.state('zoomed') #works fine on Windows!
    mg.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
    plt.show() #close the figure to run the next section

    ### for 'wxAgg' backend
    plt.figure(2)
    plt.switch_backend('wxAgg')
    print ('#2 Backend:',plt.get_backend())
    plt.plot([1,2,6,4])
    mng = plt.get_current_fig_manager()
    mng.frame.Maximize(True)
    plt.show() #close the figure to run the next sectio

    
    ### for 'Qt4Agg' backend
    plt.figure(3)
    plt.switch_backend('QT4Agg') #default on my system
    print ('#3 Backend:',plt.get_backend())
    plt.plot([1,2,6,4])
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
    '''

def test_5():
    import matplotlib.pyplot as plt
    #fig = plt.figure()
    fig, ax1 = plt.subplots(num=2, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')

    fig2, ax2 = plt.subplots(num=1, figsize=(5, 10), dpi=80, facecolor='w', edgecolor='k')

    plt.show()