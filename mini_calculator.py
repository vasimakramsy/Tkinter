from tkinter import *

def btn_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def equal():
    val = e.get()
    e.delete(0,END)
    if "+" in str(val):
        val = val.split("+")
        # e.delete(0,END)
        e.insert(0,int(val[0])+int(val[1]))
    elif "-"in str(val):
        val = val.split("-")
        e.insert(0,int(val[0])-int(val[1]))
    elif "*"in str(val):
        val = val.split("*")
        e.insert(0,int(val[0])*int(val[1]))
    elif "/"in str(val):
        val = val.split("/")
        # e.insert(0,int(val[0]/int(val[1])))
        if val[1] =='0':
            e.insert(0,'Division by zero')
        else:
            e.insert(0,int(val[0])/int(val[1]))
root = Tk()
root.title('Calculator')
root.configure(background='#F00DD2')
e =Entry(root,width=50,borderwidth=8)
e.grid(row=0,padx=10,pady=15,columnspan=5)

btn2=Button(root,text='2',width=5,bg='red',command=lambda:btn_click(2)).grid(row=3,column=1,ipadx=2,ipady=4)
btn1=Button(root,text='1',width=5,bg='red',command=lambda:btn_click(1)).grid(row=3,column=2,ipadx=2,ipady=4)
btn3=Button(root,text='3',width=5,bg='red',command=lambda:btn_click(3)).grid(row=3,column=0,ipadx=2,ipady=4)
btn4=Button(root,text='4',width=5,bg='red',command=lambda:btn_click(4)).grid(row=2,column=0,ipadx=2,ipady=4)
btn5=Button(root,text='5',width=5,bg='red',command=lambda:btn_click(5)).grid(row=2,column=1,ipadx=2,ipady=4)
btn6=Button(root,text='6',width=5,bg='red',command=lambda:btn_click(6)).grid(row=2,column=2,ipadx=2,ipady=4)
btn7=Button(root,text='7',width=5,bg='red',command=lambda:btn_click(7)).grid(row=1,column=0,ipadx=2,ipady=4)
btn8=Button(root,text='8',width=5,bg='red',command=lambda:btn_click(8)).grid(row=1,column=1,ipadx=2,ipady=4)
btn9=Button(root,text='9',width=5,bg='red',command=lambda:btn_click(9)).grid(row=1,column=2,ipadx=2,ipady=4)
btn0=Button(root,text='0',width=5,bg='red',command=lambda:btn_click(0)).grid(row=3,column=3,ipadx=10,ipady=4)

btn_eql=Button(root,text='=',width=5,bg='red',command=equal).grid(row=3,column=4,ipadx=10,ipady=4)
btn_clr=Button(root,text='Delete',width=5,bg='red',command=clear).grid(row=4,columnspan=6,ipadx=110,ipady=4)


btn_add=Button(root,text='+',width=5,bg='red',command=lambda:btn_click("+")).grid(row=2,column=4,ipadx=10,ipady=4)
btn_sub=Button(root,text='-',width=5,bg='red',command=lambda:btn_click("-")).grid(row=2,column=3,ipadx=10,ipady=4)
btn_mul=Button(root,text='*',width=5,bg='red',command=lambda:btn_click("*")).grid(row=1,column=4,ipadx=10,ipady=4)
btn_div=Button(root,text='/',width=5,bg='red',command=lambda:btn_click("/")).grid(row=1,column=3,ipadx=10,ipady=4)

root.mainloop()