from tkinter import *

#  function for evaluating the calculation and get it in entry widget
def click(event):
    global svalue
    text = event.widget.cget("text")
    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            #  if any one type wrong expression then it print the "ERROR" inside entry widget
            try:
                value = eval(svalue.get())
            except Exception as e:
                value = "ERROR"
                
                
        svalue.set(value)
        screen.update()
        #  clear the screen (sets the empty svalue[variable] in entry widget)
    elif text == "C":
        svalue.set(" ")
    else:
        svalue.set(svalue.get() + text)
        screen.update()
    
    
root = Tk()

root.geometry("600x680")


root.title("My Calculator")

#  Initially nothing on the entry
svalue = StringVar()
svalue.set("")

#  Make An Entry-Widget Screen
screen = Entry(root,textvariable = svalue,width=35,borderwidth=10, font="lucida 20 bold")
screen.grid(row=0,column=0,columnspan=4,padx=10,pady=40)
 
#  Buttons in Calculator
b1 = Button(root, text="9",font="lucida 25 bold",padx = 45,pady = 20)
b1.grid(row=1, column=0)
b1.bind("<Button-1>",click)
b2 = Button(root, text="8",font="lucida 25 bold",padx = 45,pady = 20)
b2.grid(row=1, column=1)
b2.bind("<Button-1>",click)
b3= Button(root, text="7",font="lucida 25 bold",padx = 45,pady = 20)
b3.grid(row=1, column=2)
b3.bind("<Button-1>",click)


b4= Button(root, text="6",font="lucida 25 bold",padx = 45,pady = 18)
b4.grid(row=2, column=0)
b4.bind("<Button-1>",click)
b5= Button(root, text="5",font="lucida 25 bold",padx = 45,pady = 18)
b5.grid(row=2, column=1)
b5.bind("<Button-1>",click)
b6 = Button(root, text="4",font="lucida 25 bold",padx = 45,pady = 18)
b6.grid(row=2, column=2)
b6.bind("<Button-1>",click)

 
b7 = Button(root, text="3",font="lucida 25 bold",padx = 45,pady = 18)
b7.grid(row=3, column=0)
b7.bind("<Button-1>",click)
b8= Button(root, text="2",font="lucida 25 bold",padx = 45,pady = 18)
b8.grid(row=3, column=1)
b8.bind("<Button-1>",click)
b9= Button(root, text="1",font="lucida 25 bold",padx = 45,pady = 18)
b9.grid(row=3, column=2)
b9.bind("<Button-1>",click)

b_zero= Button(root, text="0",font="lucida 25 bold",padx = 45,pady = 18)
b_zero.grid(row=4, column=0)
b_zero.bind("<Button-1>",click)

#  special Buttons["-", "+", "C", "%", "/", "*", "="]

b_min= Button(root, text="-",font="lucida 25 bold",padx = 45,pady = 18)
b_min.grid(row=1, column=3)
b_min.bind("<Button-1>",click)

b_add= Button(root, text="+",font="lucida 25 bold",padx = 42,pady = 18)
b_add.grid(row=2, column=3)
b_add.bind("<Button-1>",click)

b_mul= Button(root, text="*",font="lucida 25 bold",padx = 45,pady = 18)
b_mul.grid(row=3, column=3)
b_mul.bind("<Button-1>",click)

b_div= Button(root, text="/",font="lucida 25 bold",padx = 49,pady = 16)
b_div.grid(row=4, column=2)
b_div.bind("<Button-1>",click)

b_per= Button(root, text="%",font="lucida 24 bold",padx = 40,pady = 16)
b_per.grid(row=4, column=3)
b_per.bind("<Button-1>",click)

b_eq= Button(root, text="=",width=20, font="lucida 30 bold",bg="blue")
b_eq.grid(row=5,column=0,columnspan=4,padx=10,pady=40)
b_eq.bind("<Button-1>",click)

b_cle= Button(root, text="C",font="lucida 24 bold",padx = 44,pady = 18)
b_cle.grid(row=4, column=1)
b_cle.bind("<Button-1>",click)


root.mainloop()
