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

# ============= Page 1 ================

# Declaring the widgets of Page 1
page1.config(background='#925D33')
load = Image.open('Images\\backgroundImage.jpg')
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


# ============= Page 2 =================

# Declaring the widgets of Page 2
page2.config(background='#925D33')
img = Label(page2, image=render)
img.place(x=0, y=0)


page2_label_1 = Label(page2, text='Menu', bg='#925D33',fg='white', font=('Calibri', 30, 'bold'))

# Adding Menu Items on menu canvas
menu_canvas = Canvas(page2, bg='#d19480', width=280, height=200, bd=1)
menu_item_1 = Label(page2, text="Shiro ................................... 40$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_2 = Label(page2, text="Firfir .................................. 40$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_3 = Label(page2, text="Mesir ................................... 40$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_4 = Label(page2, text="Beyeaynet ............................... 45$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_5 = Label(page2, text="Tasty Soya............................... 40$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_6 = Label(page2, text="Tibs .................................... 60$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_7 = Label(page2, text="Pasta ................................... 40$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_8 = Label(page2, text="Tea ...................................... 7$", bg="#d19480", fg="white", font="Calibri 13 italic")
menu_item_9 = Label(page2, text="Buna ..................................... 10$", bg="#d19480", fg="white", font="Calibri 13 italic")


page2_edit_menu_button = Button(page2, text='Edit Menu', fg='#925D33', font=('Calibri', 13, 'bold'), command=lambda: show_frame(page3))
page2_calculate_button = Button(page2, text='Calculate', fg='#925D33', font=('Calibri', 13, 'bold'), command=lambda: show_frame(page4))
page2_calculate_button. config(width=10)

# Placing the widgets on to the page2 frame
page2_label_1.place(x=450, y=120)
menu_canvas.place(x=450, y=180)
menu_item_1.place(x=455, y=190)
menu_item_2.place(x=455, y=210)
menu_item_3.place(x=455, y=230)
menu_item_4.place(x=455, y=250)
menu_item_5.place(x=455, y=270)
menu_item_6.place(x=455, y=290)
menu_item_7.place(x=455, y=310)
menu_item_8.place(x=455, y=330)
menu_item_9.place(x=455, y=350)
page2_edit_menu_button.place(x=450, y=400)
page2_calculate_button.place(x=550, y=400)
# ========== End of Page 2 =============


# ============= Page 3 =================

# Declaring the widgets of Page 3
page3.config(background='#925D33')
img = Label(page3, image=render)
img.place(x=0, y=0)

page3_label_1 = Label(page3, text='Edit Menu', bg='#925D33',fg='white', font=('Calibri', 30, 'bold'))
page3_label_2 = Label(page3, text='If you would like to add an item to menu', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))

# To add an item to the menu
add_name = Label(page3, text='Name:',bg='#925D33',fg='white', font=('Calibri', 13, 'italic'))
add_item_name_entry = Entry(page3, highlightthickness=2)
add_item_name_entry. config(width=22, highlightcolor='#DF7861')

add_price = Label(page3, text='Price:',bg='#925D33',fg='white', font=('Calibri', 13, 'italic'))
add_item_price_entry = Entry(page3, highlightthickness=2)
add_item_price_entry. config(width=22, highlightcolor='#DF7861')

# To change an item  in the menu
change_label = Label(page3, text='If you would like to change an items price', bg='#925D33',fg='white',font=('Calibri', 13, 'normal'))
change_name = Label(page3, text='Name:',bg='#925D33',fg='white', font=('Calibri', 13, 'italic'))
change_name_entry = Entry(page3, highlightthickness=2)
change_name_entry. config(width=22, highlightcolor='#DF7861')

change_price = Label(page3, text='Price:',bg='#925D33',fg='white', font=('Calibri', 13, 'italic'))
change_price_entry = Entry(page3, highlightthickness=2)
change_price_entry. config(width=22, highlightcolor='#DF7861')

# Buttons
continue_button = Button(page3, text='Continue', fg='#925D33',font=('Calibri', 13, 'bold'), command=lambda: show_frame(page4))

# Placing the widgets on to the page3 frame
page3_label_1.place(x=450, y=120)
page3_label_2.place(x=450, y=190)
add_name.place(x=490, y=210)
add_item_name_entry.place(x=540, y=215)
add_price.place(x=490, y=235)
add_item_price_entry.place(x=540, y=240)
change_label.place(x=450, y=300)
change_name.place(x=490, y=320)
change_name_entry.place(x=540, y=325)
change_price.place(x=490, y=340)
change_price_entry.place(x=540, y=350)
continue_button.place(x=645, y=390)
# ========== End of Page 3 =============


# ============= Page 4 =================

# Declaring the widgets of Page 4
page4.config(background='#925D33')
img = Label(page4, image=render)
img.place(x=0, y=0)

page4_label_1 = Label(page4, text='Calculate', bg='#925D33',fg='white', font=('Calibri', 30, 'bold'))

# To get what user has eaten that day
page4_label_2 = Label(page4, text='What did you eat today?Please enter separate', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_label_3 = Label(page4, text='foods with space', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_entry_1 = Entry(page4, highlightthickness=2)
page4_entry_1. config(width=40, highlightcolor='#DF7861')


# To get who has eaten that day
page4_label_4 = Label(page4, text='Who ate today? Please enter with space', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_label_5 = Label(page4, text='Only enter those who are going to pay', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_entry_2 = Entry(page4, highlightthickness=2)
page4_entry_2. config(width=40, highlightcolor='#DF7861')


# To get how much each person is ready to pay
page4_label_6 = Label(page4, text='How much is each person ready to pay?', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_label_7 = Label(page4, text='Enter respective to previous entry', bg='#925D33',fg='white', font=('Calibri', 12, 'normal'))
page4_entry_3 = Entry(page4, highlightthickness=2)
page4_entry_3. config(width=40, highlightcolor='#C54F1F')


# Placing the widgets on to the page4 frame
page4_label_1.place(x=500, y=120)
page4_label_2.place(x=450, y=200)
page4_label_3.place(x=450, y=220)
page4_entry_1.place(x=450, y=245)
page4_label_4.place(x=450, y=300)
page4_label_5.place(x=450, y=320)
page4_entry_2.place(x=450, y=345)
page4_label_6.place(x=450, y=397)
page4_label_7.place(x=450, y=417)
page4_entry_3.place(x=450, y=442)
# ========== End of Page 4 =============




mainWindow.mainloop()