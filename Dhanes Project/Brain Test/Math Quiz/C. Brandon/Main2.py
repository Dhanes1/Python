from tkinter import *
import random
win=Tk()
win.title("Brandon's Math Quiz")
win.geometry("700x600")
win.resizable(0,0)
digits=0
equation=0
num1=0
num2=0
ans=0
multiplechoice=[]
temp=0
ques=""
score=0
num_of_questions=0
def del_score():
    score_lbl.destroy()
    exit_btn.destroy()
def easy():
    global digits
    btn_1d.destroy()
    btn_2d.destroy()
    digits=1
    plus.config(bg="lightgreen")
    minusa.config(bg="lightgreen")
    muliplication.config(bg="lightgreen")
    plus.place(x=20,y=20)
    minusa.place(x=20,y=150)
    muliplication.place(x=20,y=280)
def hard():
    global digits
    btn_1d.destroy()
    btn_2d.destroy()
    digits=2
    plus.place(x=20,y=20)
    minusa.place(x=20,y=150)
    muliplication.place(x=20,y=280)
def add():
    global equation,ans,multiplechoice,ques,ques_lbl,score
    equation=1
    plus.destroy()
    minusa.destroy()
    muliplication.destroy()
    ques_lbl.place(x=20,y=100)
    score_lbl.place(x=20,y=20)
    if digits==1:
        def run_question():
            global correctchoice
            num1=random.randint(1,9)
            num2=random.randint(1,9)
            ans=num1+num2
            ques="{}+{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,18)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()
    else:
        def run_question():
            global correctchoice
            num1=random.randint(1,99)
            num2=random.randint(1,99)
            ans=num1+num2
            ques="{}+{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,198)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()   
def minus():
    global equation,ans,multiplechoice,ques,ques_lbl,score
    equation=1
    plus.destroy()
    minusa.destroy()
    muliplication.destroy()
    ques_lbl.place(x=20,y=100)
    score_lbl.place(x=20,y=20)
    if digits==1:
        def run_question():
            global correctchoice
            num1=random.randint(1,9)
            num2=random.randint(1,9)
            ans=num1-num2
            ques="{}-{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-8,8)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()
    if digits==2:
        def run_question():
            global correctchoice
            num1=random.randint(1,99)
            num2=random.randint(1,99)
            ans=num1-num2
            ques="{}-{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(-98,98)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()
def multiplication():
    global equation,ans,multiplechoice,ques,ques_lbl,score
    equation=1
    plus.destroy()
    minusa.destroy()
    muliplication.destroy()
    ques_lbl.place(x=20,y=100)
    score_lbl.place(x=20,y=20)
    if digits==1:
        def run_question():
            global correctchoice
            num1=random.randint(1,9)
            num2=random.randint(1,9)
            ans=num1*num2
            ques="{}✖{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,81)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()
    if digits==2:
        def run_question():
            global correctchoice
            num1=random.randint(1,99)
            num2=random.randint(1,99)
            ans=num1*num2
            ques="{}✖{}".format(num1,num2)
            ques_lbl.config(text=ques)
            correctchoice=random.randint(1,4)
            
            if correctchoice==1:
                ans_1.config(text=ans)
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==2:
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                ans_2.config(text=ans)
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==3:
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                ans_3.config(text=ans)
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_4.config(text=temp)
                        break
                    else:
                        pass
            elif correctchoice==4:
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_1.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_2.config(text=temp)
                        break
                    else:
                        pass
                while True:
                    temp=random.randint(1,9801)
                    if temp != ans:
                        ans_3.config(text=temp)
                        break
                    else:
                        pass
                ans_4.config(text=ans)
        def ans_1():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==1:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_2():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==2:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_3():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==3:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        def ans_4():
            global score,score_text,correctchoice,num_of_questions
            num_of_questions+=1
            if correctchoice==4:
                score+=1
                score_text="Score: {}".format(score)
                score_lbl.config(text=score_text)
            if num_of_questions<10:
                run_question()
                
            else:
                exit_btn.place(x=20,y=300)
                ques_lbl.destroy()
                ans_1.destroy()
                ans_2.destroy()
                ans_3.destroy()
                ans_4.destroy()
        ans_1=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_1)
        ans_2=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_2)
        ans_3=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_3)
        ans_4=Button(win,font="ComicSansMS 20",width=8,height=1,text="",command=ans_4)
        ans_1.place(x=20, y=400)
        ans_2.place(x=180, y=400)
        ans_3.place(x=340, y=400)
        ans_4.place(x=500, y=400)
        run_question()



btn_1d=Button(win,font="ComicSansMS 30",width=28,height=3,text="1 Digit", bg="lightgreen",command=easy)
btn_1d.place(x=20,y=20)

btn_2d=Button(win,font="ComicSansMS 30",width=28,height=3,text="2 Digit",bg="red",command=hard)
btn_2d.place(x=20,y=330)

plus=Button(win,font="ComicSansMS 40",width=21,height=1,text="+",bg="pink",command=add)
minusa=Button(win,font="ComicSansMS 40",width=21,height=1,text="-",bg="pink",command=minus)
muliplication=Button(win,font="ComicSansMS 40",width=21,height=1,text="x",bg="pink",command=multiplication)

ques_lbl = Label(win, text="", justify="center",width=17, font="ComicSansMS 50")

score_lbl=Label(win, text="Score: 0", justify="center", font="ComicSansMS 20")

exit_btn=Button(win,font="ComicSansMS 30",width=28,height=3,text="Done!", bg="lightgreen",command=del_score)





win.mainloop()