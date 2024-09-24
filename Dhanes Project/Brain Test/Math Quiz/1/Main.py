import tkinter
from tkinter import *
import random

compans = 0
score=0
win = Tk()
win.title("Math Quiz")
win.geometry("600x500")

def two_code():
    global score, score_lbl
    generate_question()
    if ans==compans:
        score+=1
    score_lbl.config(text="Score: "+str(score))
def two_codeex():
    global score, score_lbl
    generate_question()
    print("Correct answer:", ans)
    print("Compans:", compans)
    if ans != compans:  # Only update score if the answer is incorrect
        score += 1
    print("Updated score:", score)
    score_lbl.config(text="Score: " + str(score))
def generate_question():
    global compans, ans, fake_ans, question
    num_1 = random.randint(0, 9)
    operator = random.randint(1, 4)
    num_2 = random.randint(0, 9)
    if operator == 1:
        oper_str = "+"
        ans = num_1 + num_2
    elif operator == 2:
        oper_str = "-"
        ans = num_1 - num_2
    elif operator == 3:
        oper_str = "*"
        ans = num_1 * num_2
    elif operator == 4:
        oper_str = "/"
        if num_2 == 0:  # Ensure num_2 is not zero for division operation
            num_2 = 1  # Avoid division by zero, set num_2 to 1
        ans = num_1 / num_2
        # Round the answer to avoid floating point issues
        ans = round(ans, 2)
    question = "{} {} {}".format(num_1, oper_str, num_2)
    
    # Assign correct answer to compans
    compans = ans
    
    # Randomly assign fake answer
    trueorfalse = random.randint(0, 1)
    if trueorfalse == 1:
        fake_ans = ans + random.randint(1, 10)
    else:
        fake_ans = ans - random.randint(1, 10)
    
    # Ensure fake answer is different from the correct answer
    while fake_ans == ans:
        if trueorfalse == 1:
            fake_ans = ans + random.randint(1, 10)
        else:
            fake_ans = ans - random.randint(1, 10)
    
    ques_lbl.config(text=question)
    ans_lbl.config(text=compans)


def start():
    global ques_lbl, ans_lbl, correct_btn, false_btn, score_lbl
    start_btn.destroy()
    ques_lbl = Label(win, text="", justify="center", font="ComicSansMS 50")
    ques_lbl.place(x=220, y=200)
    ans_lbl = Label(win, text="", justify="center", font="ComicSansMS 50")
    ans_lbl.place(x=220, y=280)
    generate_question()
    correct_btn = Button(win, text="✔", justify="center", font="ComicSansMS 15", width=4, command=two_code)
    correct_btn.place(x=530, y=450)
    false_btn = Button(win, text="❌", justify="center", font="ComicSansMS 15", width=4, command=two_codeex)
    false_btn.place(x=10, y=450)
    score_lbl=Label(win,text="Score: "+str(score),font="ComicSansMS 15")
    score_lbl.place(x=260,y=20)
    
    
start_btn = Button(win, text="Start", command=start, width=30, height=14, font="ComicSansMS 30", bd=0, bg="#57F948")
start_btn.place(x=-46, y=-50)
win.mainloop()
