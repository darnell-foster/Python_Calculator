from tkinter import * 
root = Tk()
root.title('Darnell\'s Simple Calculator') # .title names the tab

"""
NOTE
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""
result = 0
operation = "None"

"""
NOTE
Columnspan is used if you want one box to take up multiple columns
"""
display = Entry(root,bg="black",fg="white",width=35,borderwidth=5)
display.grid(row=0, column=0,columnspan=4,padx=10,pady=10)

"""
Takes the current contents of display and coppies it, then deletes the contents of display
and insterts new contents into the display
the new contents are created from the  button click plus the old display 
"""
def button_click(num):
    current_display = display.get() #Gets the contetns of the display(technicaly user entry widget and is just reading the entries)
    display.delete(0, END)#Deletes whats in the box from the begining to the end
    display.insert(0, str(current_display) + str(num))

def clear():
    global result,operation #makes sure it refer to the varible result that was defined outside the scope of the function
    display.delete(0, END)#Deletes whats in the box from the begining to the end
    result = 0
    operation = "None"

def addition():
    global result, operation
    
    if operation == "None":
        result = float(display.get())
    else:
        result += float(display.get())

    display.delete(0, END)
    operation = 'A'

def division():
    global operation,result
    
    if operation == 'None':
        result = float(display.get())
    else: 
        result = result/ float(display.get())

    display.delete(0, END)
    operation = 'D'

def multiplication():
    global result, operation
    
    if operation == 'None':
        result = float(display.get())
    else: 
        result *= float(display.get())

    display.delete(0, END)
    operation = 'M'

def subtraction():
    global result, operation
    
    if operation == 'None':
        result = float(display.get())
    else: 
        result -= float(display.get())

    display.delete(0, END)
    operation = 'S'


def equal():
    global result, operation
      
    if operation == 'A':
        result += float(display.get())
    elif operation == 'S':
        result -= float(display.get())
    elif operation == 'M':
        result *= float(display.get())
    elif operation == 'D':
        result /= float(display.get())

    operation = 'None'
    display.delete(0, END)#Deletes whats in the box from the begining to the end
    if result - float(result) == 0:
        display.insert(0, '{0:.3g}'.format(result)) #formats a number(result) into a string with no decimals
    else:
        display.insert(0, str(result))

def main():

    """
    NOTE
    when using "command=" adding "lambda: FUNC_NAME"
    Allows you to put in paramaters for the function 
    """
    button_0 = Button(root,text="0",padx=40, pady=20, command=lambda: button_click(0))
    button_1 = Button(root,text="1",padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root,text="2",padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root,text="3",padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root,text="4",padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root,text="5",padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root,text="6",padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root,text="7",padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root,text="8",padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root,text="9",padx=40, pady=20, command=lambda: button_click(9))
    button_decimal = Button(root,text=".",padx=40, pady=20, command = lambda: button_click("."))


    button_plus = Button(root,text="+",padx=40, pady=20, command =addition)
    button_minus = Button(root,text="-",padx=40, pady=20, command =subtraction)
    button_multiply = Button(root,text="X",padx=40, pady=20, command =multiplication)
    button_divide = Button(root,text="\U000000F7",padx=40, pady=20, command =division)
    button_equal = Button(root,text="=",padx=40, pady=20, command =equal)
    button_Clear= Button(root,text="Clear",padx=30, pady=20, command=clear)

    button_quit= Button(root,text='QUIT', command=root.quit,width=35,borderwidth=5) #a quit button


    #Row 2 of Calculator
    button_divide.grid(row=1,column=3)
    button_9.grid(row=1,column=2)
    button_8.grid(row=1,column=1)
    button_7.grid(row=1,column=0)

    #Row 2 of Calculator
    button_multiply.grid(row=2,column=3)
    button_6.grid(row=2,column=2)
    button_5.grid(row=2,column=1)
    button_4.grid(row=2,column=0)

    #Row 3 of Calculator
    button_minus.grid(row=3,column=3)
    button_3.grid(row=3,column=2)
    button_2.grid(row=3,column=1)
    button_1.grid(row=3,column=0)

    #Row 3 of Calculator
    button_plus.grid(row=4,column=3)
    button_equal.grid(row=4,column=2)
    button_Clear.grid(row=4,column=1)
    button_0.grid(row=4,column=0)

    #Row 4 of the Calculator
    button_quit.grid(row=5,column=1,columnspan=3,padx=10,pady=10)
    button_decimal.grid(row=5,column=0,columnspan=1,padx=10,pady=10)

    root.mainloop()


if __name__ == "__main__": #main guard, i.e., allows you to run code from the file and also use functions and class in other files without the main code exucte
    main()

