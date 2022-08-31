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

# The UI will have 5 different pages so that is why there are 5 different frames
page1 = Frame(mainWindow)
page2 = Frame(mainWindow)
page3 = Frame(mainWindow)
page4 = Frame(mainWindow)
page5 = Frame(mainWindow)

for frame in (page1, page2, page3, page4, page5):
    frame.grid(row=0, column=0, sticky='nsew')


# The function show_frame() will display the page when called.
# For eg if page1 is given as an argument(show_frame(page1)) it will display page1
# It will start by displaying page1
def show_frame(frame):
    frame.tkraise()


show_frame(page1)

# Let us start building the tkinter UI with each page

# ========= Page 1 =========

# Declaring the widgets of Page 1
page1.config(background='#925D33')
load = Image.open('Images\\Page1Img3.jpg')
render = ImageTk.PhotoImage(load)
img = Label(page1, image=render)
img.place(x=0, y=0)

page1_label_1 = Label(page1, text='Welcome to Restaurant Mania', bg='#925D33',fg='white',font=('Calibri', 19, 'bold'))
page1_label_2 = Label(page1, text='We will help you with addressing how you', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_3 = Label(page1, text='should pay the bill. We will calculate the', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_4 = Label(page1, text='total price of your meal. We will also calculate ', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_5 = Label(page1, text='how much each person needs to pay.', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_6 = Label(page1, text='Depending on how much money each person', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_7 = Label(page1, text='has we will show you show you the best', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_8 = Label(page1, text='method to pay the bill. We recommend checking', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_9 = Label(page1, text='the menu before calculating. Incase there is', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_10 = Label(page1, text='a new item or if the price of an item has changed ', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
page1_label_11 = Label(page1, text='you can edit our menu before calculating', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))

page1_menu_button = Button(page1, text='Menu',fg='#925D33',font=('Calibri', 13, 'bold'), command=lambda: show_frame(page2))
page1_menu_button. config(width=10)

page1_calculate_button = Button(page1, text='Calculate',fg='#925D33',font=('Calibri', 13, 'bold'), command=lambda: show_frame(page4))
page1_calculate_button. config(width=10)

# Placing the widgets on to the page1 frame
page1_label_1.place(x=425, y=160)
page1_label_2.place(x=425, y=195)
page1_label_3.place(x=425, y=220)
page1_label_4.place(x=425, y=245)
page1_label_5.place(x=425, y=270)
page1_label_6.place(x=425, y=295)
page1_label_7.place(x=425, y=320)
page1_label_8.place(x=425, y=345)
page1_label_9.place(x=425, y=370)
page1_label_10.place(x=425, y=395)
page1_label_11.place(x=425, y=420)
page1_menu_button.place(x=425, y=460)
page1_calculate_button.place(x=530, y=460)
# ========== End of Page 1 =============
mainWindow.mainloop()