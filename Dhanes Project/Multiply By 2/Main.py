import tkinter
from tkinter import *
win = Tk()
win.title("Multiply By 2")
win.geometry("600x500")
num = 1
list=[]
while num < 200000:
    num = num *2
    list.append(num)
num_str = str(num)
print(list)
lbl = Label(win, text=list, font="ComicSansMS 30")
lbl.place(x=20, y=20)
win.mainloop()
