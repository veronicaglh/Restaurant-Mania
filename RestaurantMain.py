# This program will help users calculate the total price as well as individual price of their meal
# The program will also show the best method/algorithm of payment depending on how many people there are
# and the price of the meal
# The program will contain two parts - one for building the UI with tkinter
# And the other for calculating/computing the total, individual price and the best algorithm for payment
# To build the UI with tkinter you will need to run the following command on the terminal of your IDE
# pip install pillow

import math
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# PART I - TKINTER GUI

mainWindow = Tk()
mainWindow.geometry('773x550')
mainWindow.rowconfigure(0, weight=1)
mainWindow.columnconfigure(0, weight=1)
mainWindow['background'] = '#925D33'
mainWindow.title("Restaurant Mania")


page1 = Frame(mainWindow)
page2 = Frame(mainWindow)
page3 = Frame(mainWindow)
page4 = Frame(mainWindow)
page5 = Frame(mainWindow)

for frame in (page1, page2, page3, page4, page5):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(page1)