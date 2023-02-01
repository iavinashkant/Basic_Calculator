from tkinter import *


def click(event):
    global SV
    text = event.widget.cget('text')
    print(text)
    if text == '=':
        if SV.get().isdigit():
            value = int(SV.get())
        else:
            value = eval(Screen.get())

        SV.set(value)
        Screen.update()

    elif text == 'C':
        SV.set('')
        Screen.update()
    else:
        SV.set(SV.get() + text)
        Screen.update()


m = Tk()

m.title('CalC By Avinash')
m.wm_iconbitmap('c.ico')
m.geometry('283x400')

SV = StringVar()
SV.set('')

# width = m.winfo_width()
# height = m.winfo_height()


Screen = Entry(m, textvariable=SV, font=('lucid', 28, "bold"))

Screen.pack(fill=X, ipadx=10, pady=10, padx=10)

b = Button(m, text='C', padx=8, pady=0, font='lucid 25 bold')
b.place(x=9, y=58)
b.bind('<Button-1>', click)

b = Button(m, text='/', padx=14, pady=0, font='lucid 25 bold')
b.place(x=78, y=58)
b.bind('<Button-1>', click)

b = Button(m, text='*', padx=12, pady=0, font='lucid 25 bold')
b.place(x=145, y=58)
b.bind('<Button-1>', click)

b = Button(m, text='-', padx=12, pady=0, font='lucid 25 bold')
b.place(x=211, y=58)
b.bind('<Button-1>', click)
##############################

b = Button(m, text='7', padx=11, font='lucid 25 bold')
b.place(x=9, y=124)
b.bind('<Button-1>', click)

b = Button(m, text='8', padx=9, font='lucid 25 bold')
b.place(x=78, y=124)
b.bind('<Button-1>', click)

b = Button(m, text='9', padx=9, font='lucid 25 bold')
b.place(x=145, y=124)
b.bind('<Button-1>', click)

b = Button(m, text='+', padx=8, pady=35, font='lucid 25 bold')
b.place(x=211, y=124)
b.bind('<Button-1>', click)
##############################

b = Button(m, text='4', padx=11, font='lucid 25 bold')
b.place(x=9, y=192)
b.bind('<Button-1>', click)

b = Button(m, text='5', padx=9, font='lucid 25 bold')
b.place(x=78, y=192)
b.bind('<Button-1>', click)

b = Button(m, text='6', padx=9, font='lucid 25 bold')
b.place(x=145, y=192)
b.bind('<Button-1>', click)

################


b = Button(m, text='1', padx=11, font='lucid 25 bold')
b.place(x=9, y=260)
b.bind('<Button-1>', click)

b = Button(m, text='2', padx=9, font='lucid 25 bold')
b.place(x=78, y=260)
b.bind('<Button-1>', click)

b = Button(m, text='3', padx=9, font='lucid 25 bold')
b.place(x=145, y=260)
b.bind('<Button-1>', click)

b = Button(m, text='=', padx=8, pady=35, font='lucid 25 bold')
b.place(x=211, y=260)
b.bind('<Button-1>', click)

##############################

b = Button(m, text='0', padx=11, font='lucid 25 bold')
b.place(x=9, y=328)
b.bind('<Button-1>', click)

b = Button(m, text='00', padx=5, font='lucid 25 bold')
b.place(x=78, y=328)
b.bind('<Button-1>', click)

b = Button(m, text='.', padx=13, font='lucid 25 bold')
b.place(x=145, y=328)
b.bind('<Button-1>', click)

###################################

m.mainloop()
