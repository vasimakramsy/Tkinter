from tkinter import *
from tkinter import messagebox

def calculate():
    Wigt = e1_val.get()
    Hight = e2_val.get()
    # time = float(time)

    # if time<=0:
        # return messagebox.showwarning('invalid','please enter posive number')
    Hight=(Hight/100)**2
    bmi = (Wigt/Hight)
    e3.delete(0,END)
    e3.insert(END,format(bmi, '.4f'))
    if bmi<=18.5:
        return messagebox.showinfo('Underweight','You can try to get weight')
    elif bmi>18.5 and bmi<=25:
        return messagebox.showinfo('Normal','You are perfectly fit')
    elif bmi>25 and bmi<=30:
        return messagebox.showinfo('Overweight','You try to reduce weight')
    else:
        return messagebox.showinfo('Obese','You need to consider your weight Thing seriously about it')
tk = Tk()
tk.geometry('460x320')
tk.title(' BMI-CALCULATOR')
tk.configure(background='#F00DD2')

l1 = Label(tk,text='Your weight(in kg)',font=('Helvetica',12,'bold'),bg='#F00DD2')
l1.place(x=60,y=50,width=200,height=40)

e1_val =IntVar()
e1 = Entry(tk,textvariable=e1_val,font =('Italic',20))
e1.place(x=240,y=50,width=200,height=40)

l2 = Label(tk,text='Your height(in cm)',font=('Helvetica',12,'bold'),bg='#F00DD2')
l2.place(x=20,y=100,width=200,height=40)

e2_val =IntVar()
e2 = Entry(tk,textvariable=e2_val,font =('Italic',20))
e2.place(x=240,y=100,width=200,height=40)

b1 = Button(tk,command = calculate,text='Calculate',font=('Helvetica',26,'bold'),bg='green')
b1.place(x=130,y=180,width=200,height=40)

l3 = Label(tk,text='BMI',font=('Helvetica',18,'bold'),bg='#F00DD2')
l3.place(x=20,y=260,width=200,height=40)

e3 = Entry(tk,font=('Italic',20))
e3.place(x=240,y=260,width=200,height=40)

tk.mainloop()