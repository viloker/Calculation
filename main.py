from tkinter import *

tk = Tk(className='калькулятор')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=700, bg='#3d3d3d', highlightthickness=0)
rectangle = canvas.create_rectangle(1, 20, 499, 120, width=2)  # рамка для числ

cord_list = []  # кординати числ
expression = []  # приклад
history = []   # зберігання розвязків
def create0():
    global cor0
    cor0 = 20
    while cor0 in cord_list:
        cor0 += 20
    cord_list.append(cor0)
    canvas.create_text(cor0, 70, text=0, font=('', 30))
    expression.extend('0')
def create1():
    global cor1
    cor1 = 20
    while cor1 in cord_list:
        cor1 += 20
    cord_list.append(cor1)
    canvas.create_text(cor1, 70, text=1, font=('', 30))
    expression.extend('1')
def create2():
    global cor2
    cor2 = 20
    while cor2 in cord_list:
        cor2 += 20
    cord_list.append(cor2)
    canvas.create_text(cor2, 70, text=2, font=('', 30))
    expression.extend('2')
def create3():
    global cor3
    cor3 = 20
    while cor3 in cord_list:
        cor3 += 20
    cord_list.append(cor3)
    canvas.create_text(cor3, 70, text=3, font=('', 30))
    expression.extend('3')
def create4():
    global cor4
    cor4 = 20
    while cor4 in cord_list:
        cor4 += 20
    cord_list.append(cor4)
    canvas.create_text(cor4, 70, text=4, font=('', 30))
    expression.extend('4')
def create5():
    global cor5
    cor5 = 20
    while cor5 in cord_list:
        cor5 += 20
    cord_list.append(cor5)
    canvas.create_text(cor5, 70, text=5, font=('', 30))
    expression.extend('5')
def create6():
    global cor6
    cor6 = 20
    while cor6 in cord_list:
        cor6 += 20
    cord_list.append(cor6)
    canvas.create_text(cor6, 70, text=6, font=('', 30))
    expression.extend('6')
def create7():
    global cor7
    cor7 = 20
    while cor7 in cord_list:
        cor7 += 20
    cord_list.append(cor7)
    canvas.create_text(cor7, 70, text=7, font=('', 30))
    expression.extend('7')
def create8():
    global cor8
    cor8 = 20
    while cor8 in cord_list:
        cor8 += 20
    cord_list.append(cor8)
    canvas.create_text(cor8, 70, text=8, font=('', 30))
    expression.extend('8')
def create9():
    global cor9
    cor9 = 20
    while cor9 in cord_list:
        cor9 += 20
    cord_list.append(cor9)
    canvas.create_text(cor9, 70, text=9, font=('', 30))
    expression.extend('9')

""" ДІЇ"""
def add():
    global cor_x1
    cor_x1 = 20
    while cor_x1 in cord_list:
        cor_x1 += 20
    cord_list.append(cor_x1)
    canvas.create_text(cor_x1, 70, text='+', font=('', 30))
    expression.extend('+')
def subtraction():
    global cor_x2
    cor_x2 = 20
    while cor_x2 in cord_list:
        cor_x2 += 20
    cord_list.append(cor_x2)
    canvas.create_text(cor_x2, 67, text='-', font=('', 30))
    expression.extend('-')
def multiplication():
    global cor_x3
    cor_x3 = 20
    while cor_x3 in cord_list:
        cor_x3 += 20
    cord_list.append(cor_x3)
    canvas.create_text(cor_x3, 67, text='x', font=('', 25))
    expression.extend('x')
def divide():
    global cor_x4
    cor_x4 = 20
    while cor_x4 in cord_list:
        cor_x4 += 20
    cord_list.append(cor_x4)
    canvas.create_text(cor_x4, 70, text='/', font=('', 30))
    expression.extend('/')
'''ДОРІВНЮЄ'''
def equal():
    a = ''
    for item in expression:
        try:
            a = a + str(int(item))
        except:
            if item == '+':
                a = a + '+'

            elif item == '-':
                a = a + '-'

            elif item == 'x':
                a = a + '*'

            elif item == '/':
                a = a + '/'
    end0 = eval(a)
    history.append(end0)

    if len(history) > 1:
        canvas.create_rectangle(5, 125, 499, 200,width=0 ,fill="#3d3d3d")
        last_text = canvas.create_text(250, 140, text=end0,state='normal',fill='white' ,font=('',30))
    else:
        last_text = canvas.create_text(250, 140, text=end0, state='normal', fill='white', font=('', 30))
''' Стерти '''
def clean():
    canvas.create_rectangle(5, 25, 498, 115, width=0, fill='#3d3d3d')
    expression.clear()
    cord_list.clear()

B0 = Button(canvas, width=15, height=3, text=0, command=create0, bg='#575757')
B0.place(x=120, y=640)

B1 = Button(canvas, width=15, height=3, text=1, command=create1, bg='#575757')
B1.place(x=1, y=580)

B2 = Button(canvas, width=15, height=3, text=2, command=create2, bg='#575757')
B2.place(x=120, y=580)

B3 = Button(canvas, width=15, height=3, text=3, command=create3, bg='#575757')
B3.place(x=240, y=580)

B4 = Button(canvas, width=15, height=3, text=4, command=create4, bg='#575757')
B4.place(x=1, y=520)

B5 = Button(canvas, width=15, height=3, text=5, command=create5, bg='#575757')
B5.place(x=120, y=520)

B6 = Button(canvas, width=15, height=3, text=6, command=create6, bg='#575757')
B6.place(x=240, y=520)

B7 = Button(canvas, width=15, height=3, text=7, command=create7, bg='#575757')
B7.place(x=1, y=460)

B8 = Button(canvas, width=15, height=3, text=8, command=create8, bg='#575757')
B8.place(x=120, y=460)

B9 = Button(canvas, width=15, height=3, text=9, command=create9, bg='#575757')
B9.place(x=240, y=460)

""" дії """
# додавання
B_add = Button(canvas, width=15, height=3, text='+', command=add, bg='#575757')
B_add.place(x=1, y=400)
# віднімання
B_sub = Button(canvas, width=15, height=3, text='-', command=subtraction, bg='#575757')
B_sub.place(x=120, y=400)
# множення
B_mul = Button(canvas, width=15, height=3, text='x', command=multiplication, bg='#575757')
B_mul.place(x=240, y=400)
# ділення
B_divide = Button(canvas, width=15, height=3, text='/', command=divide, bg='#575757')
B_divide.place(x=360, y=400)
# дорівнює
B_equal = Button(canvas, width=15, height=3, text='=', command=equal, bg='#575757')
B_equal.place(x=380, y=640)
# стерти
cleaning = Button(canvas, width=15, height=3, text='cleaning', command=clean, bg='#575757')
cleaning.place(x=360, y=460)

tk.update()
canvas.pack()
tk.mainloop()
