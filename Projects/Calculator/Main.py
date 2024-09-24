from tkinter import *
win=Tk()
win.title("Calculator")
win.geometry("350x350")
win.resizable(0,0)
display_frame=Frame(win,width=300,height=50,bd=0,highlightbackground='white',highlightcolor="black",highlightthickness=2)
display_frame.place(x=10,y=10)
display_entry=Entry(display_frame,font=("arial",18,"bold"),textvariable=StringVar(),width=14,bg="#eee",bd=0,justify=RIGHT)
display_entry.grid(row=0,column=0)
display_entry.insert(END,"0")
btn_frame=Frame(win,width=250,height=200,bg="grey")
btn_frame.place(x=10,y=70)
display_text="0"
operator=0
#+=1
#-=2
#*=3
#/=4
def enable_all_btn():
    btn_1.config(state=NORMAL)
    btn_2.config(state=NORMAL)
    btn_3.config(state=NORMAL)
    btn_4.config(state=NORMAL)
    btn_5.config(state=NORMAL)
    btn_6.config(state=NORMAL)
    btn_7.config(state=NORMAL)
    btn_8.config(state=NORMAL)
    btn_9.config(state=NORMAL)
    btn_0.config(state=NORMAL)
    btn_c.config(state=NORMAL)
    btn_eq.config(state=NORMAL)
def disable_all_btn():
    btn_1.config(state=DISABLED)
    btn_2.config(state=DISABLED)
    btn_3.config(state=DISABLED)
    btn_4.config(state=DISABLED)
    btn_5.config(state=DISABLED)
    btn_6.config(state=DISABLED)
    btn_7.config(state=DISABLED)
    btn_8.config(state=DISABLED)
    btn_9.config(state=DISABLED)
    btn_0.config(state=DISABLED)
    btn_c.config(state=DISABLED)
    btn_eq.config(state=DISABLED)
def disable_operator():
    btn_dvd.config(state=DISABLED)
    btn_times.config(state=DISABLED)
    btn_minus.config(state=DISABLED)
    btn_plus.config(state=DISABLED)
def enable_operator():
    btn_dvd.config(state=NORMAL)
    btn_times.config(state=NORMAL)
    btn_minus.config(state=NORMAL)
    btn_plus.config(state=NORMAL)
def num_1_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="1"
    else:
        display_text+="1"
    display_entry.insert(END,"1")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_2_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="2"
    else:
        display_text+="2"
    display_entry.insert(END,"2")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_3_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="3"
    else:
        display_text+="3"
    display_entry.insert(END,"3")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_4_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="4"
    else:
        display_text+="4"
    display_entry.insert(END,"4")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_5_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="5"
    else:
        display_text+="5"
    display_entry.insert(END,"5")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_6_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="6"
    else:
        display_text+="6"
    display_entry.insert(END,"6")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_7_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="7"
    else:
        display_text+="7"
    display_entry.insert(END,"7")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_8_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="8"
    else:
        display_text+="8"
    display_entry.insert(END,"8")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_9_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="9"
    else:
        display_text+="9"
    display_entry.insert(END,"9")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def num_0_clk():
    global display_text
    if display_text=="0":
        display_entry.delete('0','end')
        display_text="0"
    else:
        display_text+="0"
    display_entry.insert(END,"0")
    btn_c.config(state=NORMAL)
    if operator != 0:
        btn_eq.config(state=NORMAL)
    else:
        enable_operator()
def dvd():
    global display_text, operator
    operator=4
    display_text+=" ➗ "
    display_entry.insert(END," ➗ ")
    disable_operator()
    btn_eq.config(state=DISABLED)
def times():
    global display_text, operator
    operator=3
    display_text+=" x "
    display_entry.insert(END," x ")
    disable_operator()
    btn_eq.config(state=DISABLED)
def minus():
    global display_text, operator
    operator=2
    display_text+=" - "
    display_entry.insert(END," - ")
    disable_operator()
    btn_eq.config(state=DISABLED)
def plus():
    global display_text, operator
    operator=1
    display_text+=" + "
    display_entry.insert(END," + ")
    disable_operator()
    btn_eq.config(state=DISABLED)
def eq_btn_clk():
    global display_text
    # temp_num=0
    first_num_str=""
    second_num_str=""
    character=0
    result=0
    while display_text[character]!=" ":
        first_num_str+=display_text[character]
        character+=1
    character+=3
    while character<len(display_text):
        second_num_str+=display_text[character]
        character+=1
    first_num_int=int(first_num_str)
    second_num_int=int(second_num_str)
    # print(first_num_int,"      ", second_num_int)
    if operator==1:
        result=first_num_int+second_num_int
        display_text+=" = "
        display_entry.insert(END," = ")
    elif operator==2:
        result=first_num_int-second_num_int
        display_text+=" = "
        display_entry.insert(END," = ")
    elif operator==3:
        result=first_num_int*second_num_int
        display_text+=" = "
        display_entry.insert(END," = ")
    elif operator==4:
        result=first_num_int/second_num_int
        display_text+=" = "
        display_entry.insert(END," = ")
    display_entry.insert(END,result)
    display_text+=str(result)
    disable_all_btn()
    # for i in display_text:
    #     if i == " " or i == "+":
    #         if temp_num==3:
    #             second_num_str+=i
    #             temp_num=2
    #     temp_num+=1
    # for i in display_text:
    #     if i == " ":
    #         break
    #     first_num_str+=i
    # print(first_num_str,"     ",second_num_str )
def reset_btn_clk():
    global display_text,operator
    display_entry.delete(0,END)
    display_entry.insert(END,0)
    display_text="0"
    enable_all_btn()
    enable_operator()
    operator=0
    btn_eq.config(state=DISABLED)
def btn_c_clk():
    global display_text,operator
    if len(display_text) == 1:
        display_entry.delete(0,END)
        display_entry.insert(END,"0")
        display_text="0"
        btn_c.config(state=DISABLED)
    else:
        if display_text.endswith(" "):
            display_entry.delete(len(display_text)-3,END)
            display_text=display_text[0:len(display_text)-3]
            operator=0
            enable_operator()            
        else:
            display_entry.delete(len(display_text)-1,END)
            display_text=display_text[0:len(display_text)-1]
btn_1=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="1",command=num_1_clk)
btn_1.grid(row=2,column=0,padx=1,pady=1)
btn_2=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="2",command=num_2_clk)
btn_2.grid(row=2,column=1,padx=1,pady=1)
btn_3=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="3",command=num_3_clk)
btn_3.grid(row=2,column=2,padx=1,pady=1)
btn_4=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="4",command=num_4_clk)
btn_4.grid(row=1,column=0,padx=1,pady=1)
btn_5=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="5",command=num_5_clk)
btn_5.grid(row=1,column=1,padx=1,pady=1)
btn_6=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="6",command=num_6_clk)
btn_6.grid(row=1,column=2,padx=1,pady=1)
btn_7=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="7",command=num_7_clk)
btn_7.grid(row=0,column=0,padx=1,pady=1)
btn_8=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="8",command=num_8_clk)
btn_8.grid(row=0,column=1,padx=1,pady=1)
btn_9=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="9",command=num_9_clk)
btn_9.grid(row=0,column=2,padx=1,pady=1)
btn_0=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="0",command=num_0_clk)
btn_0.grid(row=3,column=1,padx=1,pady=1)
btn_c=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="C",state=DISABLED,command=btn_c_clk)
btn_c.grid(row=3,column=0,padx=1,pady=1)
btn_eq=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="=",state=DISABLED,command=eq_btn_clk)
btn_eq.grid(row=3,column=2,padx=1,pady=1)
btn_dvd=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="/",command=dvd)
btn_dvd.grid(row=0,column=3,padx=1,pady=1)
btn_times=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="x",command=times)
btn_times.grid(row=1,column=3,padx=1,pady=1)
btn_minus=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="-",command=minus)
btn_minus.grid(row=2,column=3,padx=1,pady=1)
btn_plus=Button(btn_frame,width=4,height=2,bd=0,bg="#fff",text="+",command=plus)
btn_plus.grid(row=3,column=3,padx=1,pady=1)
btn_reset=Button(btn_frame,width=20,height=2,bd=0,bg="#fff",text="Reset",command=reset_btn_clk)
btn_reset.grid(row=4,column=0,columnspan=4,padx=1,pady=1)
win.mainloop()