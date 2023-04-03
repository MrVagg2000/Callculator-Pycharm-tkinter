from tkinter import *
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from tkinter.ttk import*
import random

window = ThemedTk(theme="equilux")
window.title("Vagg's Calculator")
window.configure(themebg = "equilux")
window.geometry("400x300")
result= ""
var=StringVar()

def clear():
    global result
    result = ""
    var.set("")




def vrasidas():
    try:
        global result
        total = str(eval(result))
        var.set(total)
        result=""
    except:
        messagebox.showerror("Error", "You can't do that .")
        result = ""



def pres(num):
    global result
    result = result + str(num)
    var.set(result)
textbox=ttk.Entry(window,width=18,font=("equilux",28),text=var)
textbox.grid(column=0,row=0,columnspan=4)
#BUTTONS
btn1 = Button(window,text="1" ,command=lambda: pres(1))
btn1.grid(column=0,row=1)

btn2 = Button(window,text="2" ,command=lambda: pres(2))
btn2.grid(column=1,row=1)

btn3 = Button(window,text="3" ,command=lambda: pres(3))
btn3.grid(column=2,row=1)

btn4 = Button(window,text="+" ,command=lambda: pres("+"))
btn4.grid(column=3,row=1)

btn5 = Button(window,text="4" ,command=lambda: pres(4))
btn5.grid(column=0,row=2)

btn6 = Button(window,text="5" ,command=lambda: pres(5))
btn6.grid(column=1,row=2)

btn7 = Button(window,text="6" ,command=lambda: pres(6))
btn7.grid(column=2,row=2)

btn8 = Button(window,text="-" ,command=lambda: pres("-"))
btn8.grid(column=3,row=2)

btn9 = Button(window,text="7" ,command=lambda: pres(7))
btn9.grid(column=0,row=3)

btn10 = Button(window,text="8" ,command=lambda: pres(8))
btn10.grid(column=1,row=3)

btn11 = Button(window,text="9" ,command=lambda: pres(9))
btn11.grid(column=2,row=3)

btn12 = Button(window,text="*" ,command=lambda:pres("*"))
btn12.grid(column=3,row=3)

btn13 = Button(window,text="0" ,command=lambda: pres(0))
btn13.grid(column=0,row=4)

btn14 = Button(window,text="clear" ,command=clear)
btn14.grid(column=3,row=4)

btn15 = Button(window,text="=" ,command=vrasidas )
btn15.grid(column=2,row=4)

btn16 = Button(window,text="/" ,command=lambda: pres("/"))
btn16.grid(column=1,row=4)

btn17 = Button(window,text="(" ,command=lambda: pres("("))
btn17.grid(column=0,row=5)

btn17 = Button(window,text=")" ,command=lambda: pres(")"))
btn17.grid(column=1,row=5)

btn19 = Button(window,text="%" ,command=lambda: pres("%"))
btn19.grid(column=2,row=5)

#btn20 = Button(window,text="√" ,command=lambda: pres("math.sqrt("))
#btn20.grid(column=3,row=5)

btn21 = Button(window,text="." ,command=lambda: pres("."))
btn21.grid(column=3,row=5)

#btn22 = Button(window,text="Dell" ,command=del1)
#btn22.grid(column=3,row=5)

window.mainloop()