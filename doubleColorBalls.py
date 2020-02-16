'''

from tkinter import * 
from tkinter.ttk import *
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)


window = Tk()
window.title("Title with TK")
window.geometry('350x200')

combo = Combobox(window)
combo['values'] = (1,2,3,4,5)
combo.current(1)
combo.grid(column =0, row =1)


lbl = Label(window, text = "Hello!!!!!!!!!!",font = ("Arial Bold",10))
lbl.grid(column = 0,row =0)

txt = Entry(window,width=10)
txt.grid(column = 1, row =0)
txt.focus()

btn = Button(window,text = "Click Me",bg= "white", fg = "black" ,command = clicked)
btn.grid(column =2,row =0)

window.mainloop()
'''


from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=0)

window.mainloop()