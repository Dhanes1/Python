from tkinter import *
import tkinter
from unicodedata import digit
import random

from gevent import config
win = Tk()
win.title("Number Guessing Game")
win.attributes("-fullscreen", True)
digitnum=0
rannum=0
ex=77
userans=""
ansdigit=0
def easy():
    Easymode.destroy()
    Hardmode.destroy()
    onedigit.place(x=37,y=40)
    twodigit.place(x=37,y=400)
def hard():
    Easymode.destroy()
    Hardmode.destroy()
    onedigit.place(x=37,y=40)
    twodigit.place(x=37,y=400)
def onedigitt():
    global digitnum
    digitnum = 1
    onedigit.destroy()
    twodigit.destroy()
    runpro.place(x=37,y=40)
def twodigitt():
    global digitnum
    digitnum=2
    onedigit.destroy()
    twodigit.destroy()
    runpro.place(x=37,y=40)
def run():
    global rannum,ex,userans,ansdigit,digitnum
    if digit==1:
        rannum=random.randint(1,9)
    if digit==2:
        rannum=random.randint(1,99)
    ans.place(x=470,y=300)
    anslbl.place(x=430,y=100)
    runpro.destroy()
    num1.place(x=ex,y=400)
    num2.place(x=ex+120,y=400)
    num3.place(x=ex+240,y=400)
    num4.place(x=ex+360,y=400)
    num5.place(x=ex+480,y=400)
    num6.place(x=ex+600,y=400)
    num7.place(x=ex+720,y=400)
    num8.place(x=ex+840,y=400)
    num9.place(x=ex+960,y=400)
    num0.place(x=ex+1080,y=400)
    delnum.place(x=ex,y=600)
def one():
    global userans,ansdigit,digitnum
    if ansdigit!=digitnum:
        userans=userans+"1"
        ans.config(text=userans)
        ansdigit+=1
    
def two():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"2"
        ans.config(text=userans)
        ansdigit+=1
def three():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"3"
        ans.config(text=userans)
        ansdigit+=1
def four():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"4"
        ans.config(text=userans)
        ansdigit+=1
def five():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"5"
        ans.config(text=userans)
        ansdigit+=1
def six():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"6"
        ans.config(text=userans)
        ansdigit+=1
def seven():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"7"
        ans.config(text=userans)
        ansdigit+=1
def eight():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"8"
        ans.config(text=userans)
        ansdigit+=1
def nine():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"9"
        ans.config(text=userans)
        ansdigit+=1
def zero():
    global userans,ansdigit
    if ansdigit!=digitnum:
        userans=userans+"0"
        ans.config(text=userans)
        ansdigit+=1
def delete():
    global userans,ansdigit,digitnum
    ans.config(text=userans)
    if ansdigit<=digitnum:
        userans=userans[:-1]
        ansdigit-=1
Easymode=Button(win,font="ComicSansMS 20",text="Easy",bg="lightgreen",height=8,width=80,command=easy)
Easymode.place(x=37,y=40)
onedigit=Button(win,font="ComicSansMS 20",text="Rp.5000",bg="lightgreen",height=8,width=80,command=onedigitt)
Hardmode=Button(win,font="ComicSansMS 20",text="Hard",bg="red",height=8,width=80,command=hard)
Hardmode.place(x=37,y=400)
twodigit=Button(win,font="ComicSansMS 20",text="Rp.20000",bg="lightgreen",height=8,width=80,command=twodigitt)
runpro=Button(win,font="ComicSansMS 50",text="Start",bg="lightgreen",height=8,width=33,command=run)
ans=Label(win,font="ComicSansMS 50",text="",width=10)
anslbl=Label(win,font="ComicSansMS 100",text="Answer:")
num1=Button(win,font="ComicSansMS 50",text="1",command=one)
num2=Button(win,font="ComicSansMS 50",text="2",command=two)
num3=Button(win,font="ComicSansMS 50",text="3",command=three)
num4=Button(win,font="ComicSansMS 50",text="4",command=four)
num5=Button(win,font="ComicSansMS 50",text="5",command=five)
num6=Button(win,font="ComicSansMS 50",text="6",command=six)
num7=Button(win,font="ComicSansMS 50",text="7",command=seven)
num8=Button(win,font="ComicSansMS 50",text="8",command=eight)
num9=Button(win,font="ComicSansMS 50",text="9",command=nine)
num0=Button(win,font="ComicSansMS 50",text="0",command=zero)
delnum=Button(win,font="ComicSansMS 50",text="Delete",width=30,command=delete)
win.mainloop()