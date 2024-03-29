# This program will help users calculate the total price as well as individual price of their meal
# The program will also show the best method/algorithm of payment depending on how many people there are
# and the price of the meal
# The program will contain two parts - one for building the UI with tkinter
# And the other for calculating/computing the total, individual price and the best algorithm for payment
# To build the UI with tkinter you will need to run the following command on the terminal of your IDE
# pip install pillow

# Import Statements 
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


# ============= Page 5 =================

# Declaring the widgets of Page 5
page5.config(background='#925D33')
img = Label(page5, image=render)
img.place(x=0, y=0)

page5_label_1 = Label(page5, text='Results', bg='#925D33',fg='white', font=('Calibri', 30, 'bold'))

# To display the total price
page5_label_2 = Label(page5, text='The total price is: ', bg='#925D33',fg='white', font=('Calibri', 13, 'normal'))
page5_entry_1 = Entry(page5, highlightthickness=2)
page5_entry_1. config(width=25, highlightcolor='#DF7861')

# To display how much each individual has to pay:
page5_label_3 = Label(page5, text='You each have to pay:', bg='#925D33',fg='white', font=('Calibri', 13, 'normal'))
page5_entry_2 = Entry(page5, highlightthickness=2)
page5_entry_2. config(width=22, highlightcolor='#DF7861')

# To display the change
page5_label_4 = Label(page5, text='Change:', bg='#925D33',fg='white', font=('Calibri', 13, 'normal'))
display_change_textbox = Text(page5, height=3, width=25, wrap=WORD, highlightthickness=2)
display_change_textbox.config(highlightcolor='#DF7861')

# To display the best possible method of payment
page5_label_5 = Label(page5, text='Best method:', bg='#925D33',fg='white', font=('Calibri', 13, 'normal'))
final_text_box = Text(page5, height=10, width=35, wrap=WORD, highlightthickness=2)
final_text_box.config(highlightcolor='#DF7861')

# Placing the widgets on to the page5 frame
page5_label_1.place(x=500, y=100)
page5_label_2.place(x=450, y=170)
page5_entry_1.place(x=585, y=170)
page5_label_3.place(x=450, y=210)
page5_entry_2.place(x=610, y=210)
page5_label_4.place(x=450, y=250)
display_change_textbox.place(x=530, y=250)
page5_label_5.place(x=450, y=305)
final_text_box.place(x=450, y=340)
# ========== End of Page 5 =============


# PART II - COMPUTATION
priceOfFood = {'shiro': 40, 'firfir': 40, 'beyeaynet': 45, 'mesir': 40, 'tastys': 40, 'pasta': 40, 'macornoni': 40,
               'tea': 7, 'buna': 10}


# Function that will be called when user wants to add an item to menu
def add_item_to_menu():
            newFood = add_item_name_entry.get()
            priceOfNewFood = int(add_item_price_entry.get())
            priceOfFood[newFood] = priceOfNewFood
            messagebox.showinfo("Successful", "You have successfully added a new item to the menu. Press continue to calculate")


# Function that will be called when user changes an items price on menu
def change_price_on_menu():
    changeWhichFood = change_name_entry.get()
    priceChange = int(change_price_entry.get())
    if changeWhichFood in priceOfFood:
        for i in priceOfFood.keys():
            if changeWhichFood == i:
                priceOfFood[i] = priceChange
        messagebox.showinfo("Successful", "You have successfully changed the price of an item on the menu. Press continue to calculate")
    else:
        messagebox.showwarning("Warning Message","Can not find the item on the menu. If item does not exist you can re-run and edit the menu.")


# Function to calculate the total price and best method/algorithm of payment
def calculate():
    # will get what meal has been eaten from entry box declared in page4.
    # after getting what meal has been eaten from entry box named page4_entry_1
    # will split each meal and add it to list called food_eaten
    whichFood = page4_entry_1.get()
    food_eaten = whichFood.split()

    peopleWhoAte = page4_entry_2.get()
    people_that_ate = peopleWhoAte.split()

    payed = page4_entry_3.get()
    payed_list = payed.split()
    map_object = map(int, payed_list)
    list_payments = list(map_object)

    number_of_people = len(people_that_ate)

    # Add inner function named popup for error handling
    def popup():
        # Incase user inputs an item that is not in menu this loop will iterate through food_eaten list
        # and check if the elements are in priceOfFood(which is the dictionary which contains the name of the meals as well as their price)
        # if the user input is not in priceOfFood warning message will be shown to tell the user to edit and add the new meal to menu before calculation
        for i in range(len(food_eaten)):
            if food_eaten[i] in priceOfFood:
                continue
            else:
                messagebox.showwarning("Warning Message", "You have entered an item that is not in the menu. Please re run and edit the menu before continuing.")
                break

        if number_of_people < len(list_payments):
            error_message_one = f"You have inputed that {number_of_people} people ate but you gave {len(list_payments)} money input. Please fix this. If a person didn't pay don't enter their name."
            messagebox.showerror("Error Message", error_message_one)

        elif number_of_people > len(list_payments):
            error_message_two = f"You said that {number_of_people} people ate but you gave {len(list_payments)} money input. Please fix this. If a person didn't pay don't enter their name."
            messagebox.showerror("Error Message", error_message_two)

        elif number_of_people == 0:
            error_message_three = "You have inputed that no body has ate. Please fix this."
            messagebox.showerror("Error Message", error_message_three)

    popup()

    totalPrice = 0
    # To find the total price of what they ate that day:
    for i in food_eaten:
        for keys in priceOfFood:
            if i == keys:
                totalPrice += priceOfFood[keys]

    page5_entry_1.insert(0, f"{totalPrice}$")
    page5_entry_1.config(state='readonly')  # Make state readonly to make sure user cant edit total price after it has been displayed

    individualPay = totalPrice / number_of_people
    page5_entry_2.insert(0, f"{individualPay}$")
    page5_entry_2.config(state='readonly')  # Make state readonly to make sure user cant edit the individual payment after it has been displayed

    # To find the change each person has:
    for j in range(len(list_payments)):
        if list_payments[j] > individualPay:
            change = list_payments[j] - individualPay
            display_change_textbox.insert('end', f"{people_that_ate[j]} has a change of {change}$.\n")
            display_change_textbox.configure(state='disabled')

        elif list_payments[j] < individualPay:
            remaining = individualPay - list_payments[j]
            display_change_textbox.insert('end', f"{people_that_ate[j]} still has to pay {remaining}$.\n")
            display_change_textbox.configure(state='disabled')

    # To find the best algorithm for payment
    for i in range(len(list_payments)):
        # Scenario 1: if an individual has money to pay for the whole thing #
        if list_payments[i] > totalPrice:
            bestMethod1 = f"{people_that_ate[i]} should pay and the rest of the members can pay {people_that_ate[i]} later."
            final_text_box.insert('end', bestMethod1)
            final_text_box.configure(state='disabled')  # disable state so user can edit the best method after it has been displayed

        # Scenario 2: if an individual can pay for more people other than themselves but not everybody #
        elif list_payments[i] > individualPay and list_payments[i] < totalPrice and list_payments[i] % individualPay == 0:
            # Person will show how many other people that individual can pay for.
            # For eg. If person = 2 they can pay for 2 more people etc..
            # We subtract 1 from person because that individual also has to pay for themselves
            person = list_payments[i] / individualPay - 1
            # To make it grammatically correct depending on the value of person
            if person == 1:
                bestMethod2 = f"{people_that_ate[i]} can pay for one more person. Let {people_that_ate[i]} pay for one more person and let that person pay {people_that_ate[i]} back another time"
                final_text_box.insert('end', bestMethod2)
                final_text_box.configure(state='disabled')
            else:
                bestMethod3 = f"{people_that_ate[i]} can pay for {person}  more people.Let {people_that_ate[i]} pay for {person} more people and let them pay {people_that_ate[i]} back another time"
                final_text_box.insert('end', bestMethod3)
                final_text_box.configure(state='disabled')


        # Scenario 3: if an individual can pay for more people other than themselves but there is remainder
        elif list_payments[i] > individualPay and list_payments[i] < totalPrice and list_payments[i] % individualPay != 0:
            remainder = list_payments[i] / individualPay
            # math.floor(remainder) will return the greatest integer that is smaller than the value of remainder
            # for eg: if remainder value is 2.5 math.floor(remainder) will return 2

            # Only will execute if math.floor(remainder) >=2 this is so that only the one who can pay for another person is considered
            if math.floor(remainder) >= 2:
                # To make it grammatically correct depending on the value of math.floor(remainder)
                if math.floor(remainder) == 2:
                    bestMethod4 = f"{people_that_ate[i]} can pay for {math.floor(remainder) - 1} more extra person. Let {people_that_ate[i]} pay for one more person and let that person pay {people_that_ate[i]} back another time"
                    final_text_box.insert('end', bestMethod4)
                    final_text_box.configure(state='disabled')

                else:
                    bestMethod5 = f" {people_that_ate[i]} can pay for {math.floor(remainder) - 1 } more extra people.Let {people_that_ate[i]} pay for {math.floor(remainder) - 1} more people and let them pay {people_that_ate[i]} back another time"
                    final_text_box.insert('end', bestMethod5)
                    final_text_box.configure(state='disabled')

    # After executing the calculate function the program will call show_frame function with argument of page5
    # This is so that page5 can be shown
    # and the results from the calculate function can be displayed on the 5th page(page5) of the UI
    show_frame(page5)


# Adding the tkinter buttons
# The tkinter buttons have been implemented here because once they have been clicked
# they will call functions like add_item_to_menu(), change_price_on_menu() and calculate()
# Therefore they can only be implemented once these functions have been implemented
add_menu_button = Button(page3, text='Add Item', fg='#925D33',font=('Calibri', 13, 'bold'), command=add_item_to_menu)
change_button = Button(page3, text='Change Price', fg='#925D33',font=('Calibri', 13, 'bold'), command=change_price_on_menu)
add_menu_button.place(x=450, y=390)
change_button.place(x=535, y=390)

calculate_button = Button(page4, text='Calculate', fg='#925D33',font=('Calibri', 13, 'bold'), command=calculate)
calculate_button.place(x=620, y=475)
mainWindow.mainloop()

