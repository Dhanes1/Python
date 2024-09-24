import datetime
import time
from tkinter import *
from tkinter import ttk
question=1
score=0
month_list=["January","February","March","April","May","June","July","August","September","October","November","December"]
year_list=[]
for i in range(1950,2021):
    year_list.append(i)
ques_list=["Yang tidak termasuk Surat Izin Mengemudi untuk kendaraan roda 4 atau lebih adalah...",
           "Pengereman mendadak di jalan yang licin terutama pada kecepatan tinggi akan mengakibatkan, kecuali...",
           "Manakah yang tidak termasuk dalam peralatan pendukung kendaraan beroda dua?",
           "Mengapa anda diharuskan menyalakan lampu kendaraan walaupun di siang hari?",
           "Pada saat berkendara di jalan yang tidak ada larangan mendahului, pengemudi dapat melewati kendaraan lain, kecuali..."]
ans_choice_list1=[["A. SIM C","B. SIM A","C. SIM B1","D. SIM B2"],
                  ["A. Tidak berakibat apa-apa kalau pengemudi mahir","B. Kendaraan akan slip (tergelincir)","C. Membahayakan kendaraan lain di belakang","D. Kendaraan sulit dikendalikan"],
                  ["A. Helm yang berstandar SNI","B. Rompi pemantul cahaya","C. Sepatu yang menutup tumit","D. Kacamata hitam"],
                  ["A. Karena diatur oleh Undang-undang","B. Supaya tetap bisa melihat jalan kalau tiba-tiba cuaca menjadi gelap","C. Agar pengisian aki kendaraan lebih baik","D. Agar kendaraan lebih terlihat oleh pengguna jalan yang lain"],
                  ["A. Rombongan anak sekolah yang menggunakan sepeda","B. Kendaraan lain yang sedang memberi kesempatan menyeberang kepada pejalan kaki atau pengendara sepeda","C. Rombongan pawai/karnaval","D. Rombongan jenazah"]]
ans_key_list=['A','A','D','D','D']
win=Tk()
def submit_btn_clk():
    name=input_name.get()
    brt_mth=month_list.index(month_cb.get())+1
    brt_yr=int(year_cb.get())
    today_date=datetime.date.today()
    mth_age=today_date.month-brt_mth
    yr_age=today_date.year-brt_yr
    if mth_age<0:
        yr_age-=1
        mth_age+=12
    sentence="Hello "+name+", you're born on "+month_list[brt_mth-1]+" "+str(brt_yr)+"."
    sentence+="\nYou are "+str(yr_age)+" years and "+str(mth_age)+" months old."
    if yr_age>=17 and yr_age<80:
        sentence+="""

You are eligible for a driving license, but you have to pass the driving license test."""
        test_btn.place(x=20,y=140)
    else:
        sentence+="""

Sorry, you're not eligible for a driving license."""
    inf_txt.insert(END,sentence)
    submit_btn.destroy()
def Test_btn_clk():
    test_btn.destroy()
    ques_lbl.place(x=20,y=160)
    scr_lbl.place(x=200,y=160)
    btn_a.place(x=20,y=320)
    btn_b.place(x=70,y=320)
    btn_c.place(x=120,y=320)
    btn_d.place(x=170,y=320)
    show_ques(question)
def a_btn_clk():
    global question
    global score
    inf_txt.delete('1.0','end')
    if ans_key_list[question-1]=='A':
        score+=1
        scr_lbl=Label(win,text="Score: "+str(score))
        scr_lbl.place(x=200,y=160)
    time.sleep(1)
    if question<5:
        question+=1
        ques_lbl=Label(win,text="Question: "+str(question))
        ques_lbl.place(x=20,y=160)
        show_ques(question)
    else:
        ques_done()
def b_btn_clk():
    global question
    global score
    inf_txt.delete('1.0','end')
    if ans_key_list[question-1]=='B':
        score+=1
        scr_lbl=Label(win,text="Score: "+str(score))
        scr_lbl.place(x=200,y=160)
    time.sleep(1)
    if question<5:
        question+=1
        ques_lbl=Label(win,text="Question: "+str(question))
        ques_lbl.place(x=20,y=160)
        show_ques(question)
    else:
        ques_done()
def c_btn_clk():
    global question
    global score
    inf_txt.delete('1.0','end')
    if ans_key_list[question-1]=='C':
        score+=1
        scr_lbl=Label(win,text="Score: "+str(score))
        scr_lbl.place(x=200,y=160)
    time.sleep(1)
    if question<5:
        question+=1
        ques_lbl=Label(win,text="Question: "+str(question))
        ques_lbl.place(x=20,y=160)
        show_ques(question)
    else:
        ques_done()
def d_btn_clk():
    global question
    global score
    global question
    global score
    inf_txt.delete('1.0','end')
    if ans_key_list[question-1]=='D':
        score+=1
        scr_lbl=Label(win,text="Score: "+str(score))
        scr_lbl.place(x=200,y=160)
    time.sleep(1)
    if question<5:
        question+=1
        ques_lbl=Label(win,text="Question: "+str(question))
        ques_lbl.place(x=20,y=160)
        show_ques(question)
    else:
        ques_done()
def show_ques(question):
    inf_txt.delete('1.0','end')
    inf_txt.insert(END,ques_list[question-1]+'\n'+'\n')
    for i in range(4):
        inf_txt.insert(END,ans_choice_list1[question-1][i]+'\n')       
    # inf_txt.insert(END,ans_choice_list1[0])
def ques_done():
    inf_txt.delete('1.0','end')
    btn_a.destroy()
    btn_b.destroy()
    btn_c.destroy()
    btn_d.destroy()
    if score==5:
        name=input_name.get()
        sentence="Selamat {}, anda lulus ujian tes ujian mengemudi!".format(name)
        inf_txt.insert(END,sentence)
    else:
        name=input_name.get()
        sentence="Maaf {}, anda tidak lulus ujian tes ujian mengemudi.".format(name)
        inf_txt.insert(END,sentence)
win.title("Driving License")
win.geometry('600x400')
lbl_name=Label(win,text="Name:",width=20,height=1)
lbl_name.place(x=10,y=10)
lbl_month=Label(win,text="Birth Month: ",width=20,height=1)
lbl_month.place(x=10,y=50)
lbl_year=Label(win,text="Birth Year",width=20,height=1)
lbl_year.place(x=10,y=90)
input_name=Entry(win,width=20)
input_name.place(x=150,y=10)
month_clk=StringVar()
month_cb=ttk.Combobox(win,textvariable=month_clk,values=month_list)
month_cb.place(x=150,y=50)
year_clk=IntVar()
year_clk.set("")
year_cb=ttk.Combobox(win,textvariable=year_clk,values=year_list)
year_cb.place(x=150,y=90)
submit_btn=Button(win,text="Submit",command=submit_btn_clk)
submit_btn.place(x=20,y=140)
test_btn=Button(win,text="Test",command=Test_btn_clk)
inf_txt=Text(win,height=7,width=50,bg="light blue")
inf_txt.place(x=10,y=200)
ques_lbl=Label(win,text="Question: "+str(question))
scr_lbl=Label(win,text="Score: "+str(score))
btn_a=Button(win,text="A",command=a_btn_clk,width=5)
btn_b=Button(win,text="B",command=b_btn_clk,width=5)
btn_c=Button(win,text="C",command=c_btn_clk,width=5)
btn_d=Button(win,text="D",command=d_btn_clk,width=5)
win.mainloop()