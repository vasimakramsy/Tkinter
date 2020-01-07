from tkinter import *
from tkinter import messagebox

def calculate():
    dist = e1_val.get()
    time = e2_val.get()
    time = float(time)
    if time<=0:

        return messagebox.showwarning('invalid','please enter posive number')
    speed = (dist/time)
    e3.delete(0,END)
    e3.insert(END,format(speed, '.4f'))

tk = Tk()
tk.geometry('460x320')
tk.title('Speed Calculator')
tk.configure(background='#F00DD2')

l1 = Label(tk,text='Distance',font=('Helvetica',26,'bold'),bg='#F00DD2')
l1.place(x=60,y=50,width=200,height=40)

e1_val =IntVar()
e1 = Entry(tk,textvariable=e1_val,font =('Italic',20))
e1.place(x=240,y=50,width=200,height=40)

l2 = Label(tk,text='time in hr',font=('Helvetica',26,'bold'),bg='#F00DD2')
l2.place(x=20,y=100,width=200,height=40)

e2_val =IntVar()
e2 = Entry(tk,textvariable=e2_val,font =('Italic',20))
e2.place(x=240,y=100,width=200,height=40)

b1 = Button(tk,command = calculate,text='Calculate',font=('Helvetica',26,'bold'),bg='green')
b1.place(x=130,y=180,width=200,height=40)

l3 = Label(tk,text='Speed (km/hr)',font=('Helvetica',18,'bold'),bg='#F00DD2')
l3.place(x=20,y=260,width=200,height=40)

e3 = Entry(tk,font=('Italic',20))
e3.place(x=240,y=260,width=200,height=40)

tk.mainloop()