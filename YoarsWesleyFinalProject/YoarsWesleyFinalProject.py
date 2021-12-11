"""Importing contents"""

from tkinter import * # Importing tkinter
from types import LambdaType # Importing lambda
import math # Imports math
from PIL import Image, ImageTk # Imports from Pillow

"""Making the first window and its grid"""

root = Tk()  # Adding first window
root.title("Simple Calcultor") # Setting roots title name
img1 = Image.open("basicmath.png") # Opens picture
resize_img1 = img1.resize((80, 80)) # Resize picture
imgroot = ImageTk.PhotoImage(resize_img1) # Places the picture
labelroot = Label(root, image = imgroot, text = "Picture of the four basic math operators.") # Puts picture into a label with alt text
labelexplainroot = Label(root, text="Type a number, an operation, type another\n number, and then hit equals") # Lablel to explain the window

e = Entry(root, width=35, borderwidth=5) # Makes the text box 
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Sets up the grid for root

"""Making the second window and its grid"""

top = Tk()  # Adding second window
top.title("Advanced Calcultor") #Setting tops title name
labelexplaintop = Label(top, text="Type a number, an operation, and then hit equals") # Lablel to explain the window

f = Entry(top, width=35, borderwidth=5) # Makes the text box
f.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Sets up the grid for top

"""Defining all the buttons that will be used"""

def button_click(number): # Defines a button
    current = e.get() # When clicked, it gets the button content and stores it
    e.delete(0, END) # Deletes contents in text box
    e.insert(0, str(current) + str(number)) # Inserts the contents stored

def button_clicktop(number): # Defines a button
    current = f.get() # When clicked, it gets the button content and stores it
    f.delete(0, END) # Deletes contents in text box
    f.insert(0, str(current) + str(number)) # Inserts the contents stored

def button_clear(): # Defines a button
    e.delete(0, END) # Deletes contents in text box

def button_cleartop(): # Defines a button
    f.delete(0, END) # Deletes contents in text box

def button_add(): # Defines a button
    first_number = e.get()  # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "addition" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    e.delete(0, END) # Deletes contents in text box

def button_equal(): # Defines a button
    second_number = int(e.get()) # When clicked, it gets the button content and stores it
    e.delete(0, END) # Deletes contents in text box

    if math == "addition":
        e.insert(0, f_num + int(second_number)) # Inserts the contents stored
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number)) # Inserts the contents stored
   
    if math == "multipulcation":
        e.insert(0, f_num * int(second_number)) # Inserts the contents stored
    
    if math == "division":
        e.insert(0, f_num / int(second_number)) # Inserts the contents stored

def button_equaltop(): # Defines a button

    if math == "percentage":
        f.insert(0, f_num / 100) # Inserts the contents stored

    if math == "sqrt(x)":
        f.insert(0, f_num ** .5) # Inserts the contents stored

    if math == "^x":
        f.insert(0, f_num ** 2) # Inserts the contents stored

def button_subtract(): # Defines a button
    first_number = e.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "subtraction" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    e.delete(0, END) # Deletes contents in text box

def button_multiply(): # Defines a button
    first_number = e.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "multipulcation" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    e.delete(0, END) # Deletes contents in text box

def button_divide(): # Defines a button
    first_number = e.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "division" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    e.delete(0, END) # Deletes contents in text box

def button_percent(): # Defines a button
    first_number = f.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "percentage" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    f.delete(0, END) # Deletes contents in text box

def button_root(): # Defines a button
    first_number = f.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "sqrt(x)" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    f.delete(0, END) # Deletes contents in text box

def button_squared(): # Defines a button
    first_number = f.get() # When clicked, it gets the button content and stores it
    global f_num # Makes the variable "f_num" a global variable
    global math # Sets the variable "math" to a global variable
    math = "^x" # Sets the global variable "math" to a string
    f_num = int(first_number) #Sets "f_num" to the first number clicked
    f.delete(0, END) # Deletes contents in text box

"""Sizing all the buttons and gives each a command to do when it has been clicked"""

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)) # Sizes button and gives a command to do when clicked
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)) # Sizes button and gives a command to do when clicked
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)) # Sizes button and gives a command to do when clicked
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)) # Sizes button and gives a command to do when clicked
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)) # Sizes button and gives a command to do when clicked
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)) # Sizes button and gives a command to do when clicked
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)) # Sizes button and gives a command to do when clicked
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)) # Sizes button and gives a command to do when clicked
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)) # Sizes button and gives a command to do when clicked
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)) # Sizes button and gives a command to do when clicked
button_Add = Button(root, text="+", padx=39, pady=20, command=button_add) # Sizes button and gives a command to do when clicked
button_Equal = Button(root, text="=", padx=87, pady=20, command=button_equal) # Sizes button and gives a command to do when clicked
button_Clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear) # Sizes button and gives a command to do when clicked
button_Subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract) # Sizes button and gives a command to do when clicked
button_Multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply) # Sizes button and gives a command to do when clicked
button_Divide = Button(root, text="/", padx=40, pady=20, command=button_divide) # Sizes button and gives a command to do when clicked

button_1top = Button(top, text="1", padx=40, pady=20, command=lambda: button_clicktop(1)) # Sizes button and gives a command to do when clicked
button_2top = Button(top, text="2", padx=40, pady=20, command=lambda: button_clicktop(2)) # Sizes button and gives a command to do when clicked
button_3top = Button(top, text="3", padx=40, pady=20, command=lambda: button_clicktop(3)) # Sizes button and gives a command to do when clicked
button_4top = Button(top, text="4", padx=40, pady=20, command=lambda: button_clicktop(4)) # Sizes button and gives a command to do when clicked
button_5top = Button(top, text="5", padx=40, pady=20, command=lambda: button_clicktop(5)) # Sizes button and gives a command to do when clicked
button_6top = Button(top, text="6", padx=40, pady=20, command=lambda: button_clicktop(6)) # Sizes button and gives a command to do when clicked
button_7top = Button(top, text="7", padx=40, pady=20, command=lambda: button_clicktop(7)) # Sizes button and gives a command to do when clicked
button_8top = Button(top, text="8", padx=40, pady=20, command=lambda: button_clicktop(8)) # Sizes button and gives a command to do when clicked
button_9top = Button(top, text="9", padx=40, pady=20, command=lambda: button_clicktop(9)) # Sizes button and gives a command to do when clicked
button_0top = Button(top, text="0", padx=40, pady=20, command=lambda: button_clicktop(0)) # Sizes button and gives a command to do when clicked
button_Equaltop = Button(top, text="=", padx=87, pady=20, command=button_equaltop) # Sizes button and gives a command to do when clicked
button_Cleartop = Button(top, text="Clear", padx=77, pady=20, command=button_cleartop) # Sizes button and gives a command to do when clicked
buttonPercent = Button(top, text="%", padx=38, pady=20, command=button_percent) # Sizes button and gives a command to do when clicked
button_squareroot = Button(top, text="sqrt(x)", padx=26, pady=20, command=button_root) # Sizes button and gives a command to do when clicked
button_square = Button(top, text="^x", padx=40, pady=20, command=button_squared) # Sizes button and gives a command to do when clicked


"""Putting all of the buttons on the screen using a grid system"""

button_1.grid(row=5, column=0) # Places button in certain area
button_2.grid(row=5, column=1) # Places button in certain area
button_3.grid(row=5, column=2) # Places button in certain area

button_4.grid(row=4, column=0) # Places button in certain area
button_5.grid(row=4, column=1) # Places button in certain area
button_6.grid(row=4, column=2) # Places button in certain area

button_7.grid(row=3, column=0) # Places button in certain area
button_8.grid(row=3, column=1) # Places button in certain area
button_9.grid(row=3, column=2) # Places button in certain area

button_0.grid(row=6, column=0) # Places button in certain area
button_Clear.grid(row=6, column=1, columnspan=2) # Places button in certain area
button_Add.grid(row=7, column=0) # Places button in certain area
button_Equal.grid(row=7, column=1, columnspan=2) # Places button in certain area

button_Subtract.grid(row=8, column=0) # Places button in certain area
button_Multiply.grid(row=8, column=1) # Places button in certain area
button_Divide.grid(row=8, column=2) # Places button in certain area

button_1top.grid(row=5, column=0) # Places button in certain area
button_2top.grid(row=5, column=1) # Places button in certain area
button_3top.grid(row=5, column=2) # Places button in certain area

button_4top.grid(row=4, column=0) # Places button in certain area
button_5top.grid(row=4, column=1) # Places button in certain area
button_6top.grid(row=4, column=2) # Places button in certain area

button_7top.grid(row=3, column=0) # Places button in certain area
button_8top.grid(row=3, column=1) # Places button in certain area
button_9top.grid(row=3, column=2) # Places button in certain area

button_0top.grid(row=6, column=0) # Places button in certain area
button_Cleartop.grid(row=6, column=1, columnspan=2) # Places button in certain area
buttonPercent.grid(row=7, column=0) # Places button in certain area
button_Equaltop.grid(row=7, column=1, columnspan=2) # Places button in certain area

button_squareroot.grid(row=8, column=0) # Places button in certain area
button_square.grid(row=8, column=1) # Places button in certain area

labelroot.grid(row=9, column=0, rowspan=3, columnspan=3) # Places button in certain area
labelexplainroot.grid(row=1, column=0, columnspan=3) # Places button in certain area
labelexplaintop.grid(row=1, column=0, columnspan=3) # Places button in certain area

"""Starts the main loop"""

root.mainloop() # Starts the main program
    