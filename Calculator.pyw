from tkinter import *
# ===============================
window = Tk()
window.title('ماشین حساب')
window.geometry("250x300")
window.resizable(width=False, height=False)
window.iconbitmap("calc.ico")
color = "#0F7BDB"
window.configure(bg=color)
num1 = StringVar()
num2 = StringVar()
# ===============================
Label(window, text="مقدار را وارد کنید",bg=color,fg="white",font=(None,17)).place(x=55,y=5)
# ===============================
first_num = Entry(window, textvariable=num1).place(x= 30 ,y=50)
Label(window, text=":عدد اول",bg=color,fg="white",font=(None,13)).place(x=180,y=50)
# ===============================
second_num = Entry(window, textvariable=num2).place(x=30,y=90)
Label(window, text=":عدد دوم",bg=color,fg="white",font=(None,13)).place(x=180,y=90)
# ===============================
B_mul    =Button(window, text = "X",font=(None,20),command= lambda:mul())   .place(x=20, y=130,width=45)
B_plus   =Button(window, text = "+",font=(None,20),command= lambda:plus())  .place(x=75, y=130,width=45)
B_minus  =Button(window, text = "-",font=(None,20),command= lambda:minus()) .place(x=133,y=130,width=45)
B_div    =Button(window, text = "÷",font=(None,20),command= lambda:div())   .place(x=190,y=130,width=45)
EXIT     =Button(window, text="خروج",width=10,height=2 ,command=window.destroy).place(x=85,y=250)
B_result =Label(window,bg=color,   width=20,font=(None,13))
B_result.place(x=30,y=200)

def result(x):
    if x == 'error':
        B_result.config(bg ='red')
        B_result.config(text = '!مشکلی پیش آمد')

    elif x == 'division zero error':
        B_result.config(bg = 'pink')
        B_result.config(fg = 'black')
        B_result.config(text= 'نمیتوان بر صفر تقسیم کرد')
        
    else:
        B_result.config(bg = 'black')
        B_result.config(fg = 'white')
        B_result.config(text = x)

def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        result(value)
    except:
        result('error')

def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        result(value)
    except:
        result('error')

def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        result(value)
    except:
        result('error')

def div():
    if num2.get() == '0':
        result('division zero error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            result(value)
        except:
            result('error')

window.mainloop()
