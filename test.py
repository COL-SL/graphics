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
    img = PhotoImage(file='.\images\warning.png')

    plt.figure(num=1, figsize=(16, 12))
    thismanager.window.tk.call('wm', 'iconphoto', thismanager.window._w, img)
    #plt.plot(date, energyplot, 'bo')
    plt.show()

