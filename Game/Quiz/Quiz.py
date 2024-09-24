import sys
import pygame
from pygame.locals import QUIT
import time
import random
pygame.init()
win=pygame.display.set_mode((800,400))
pygame.display.set_caption("Math Quiz")
question_number=1
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
num1=random.randint(1,99)
num2=random.randint(1,99)
question_font=pygame.font.SysFont("ComicSansms",80)
answer_font=pygame.font.SysFont("ComicSansms",160)
score_font=pygame.font.SysFont("ComicSansms",40)
over_font=pygame.font.SysFont("ComicSansms",80)
def display_question(num1,num2):
    question=question_font.render(str(num1)+" + "+str(num2)+" =",True,black)
    win.blit(question,(50,50))

def display_answer(answer_text):
    answer=answer_font.render(answer_text,True,black)
    win.blit(answer,(50,150))

def display_score(score):
    score5=score_font.render("Score: "+str(score),True,black)
    win.blit(score5,(600,50))

def display_check():
    pygame.draw.line(win,green,(500,300),(550,350),20)
    pygame.draw.line(win,green,(550,350),(650,200),20)

def display_cross():
    pygame.draw.line(win,red,(500,200),(300,400),20)
    pygame.draw.line(win,red,(300,200),(500,400),20)

def display_quiz_over():
    over=over_font.render("Quiz Over",True,black)
    win.blit(over,(250,250))
question_time=pygame.time.get_ticks()
answer_text=""
answer_int=0
has_answer=False
score=0
update_score=False
while question_number<10:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_0:
                answer_text+="0"
            elif event.key==pygame.K_1:
                answer_text+="1"
            elif event.key==pygame.K_2:
                answer_text+="2"
            elif event.key==pygame.K_3:
                answer_text+="3"
            elif event.key==pygame.K_4:
                answer_text+="4"
            elif event.key==pygame.K_5:
                answer_text+="5"
            elif event.key==pygame.K_6:
                answer_text+="6"
            elif event.key==pygame.K_7:
                answer_text+="7"
            elif event.key==pygame.K_8:
                answer_text+="8"
            elif event.key==pygame.K_9:
                answer_text+="9"
            elif event.key==pygame.K_BACKSPACE:
                answer_text=answer_text[:-1]
            elif event.key==pygame.K_RETURN:
                has_answer=True
                if answer_text!="":
                    answer_int=int(answer_text)
            
    win.fill(white)
    if pygame.time.get_ticks()-question_time>7000:
        num1=random.randint(1,99)
        num2=random.randint(1,99)
        question_number+=1
        answer_text=""
        has_answer=False
        update_score=False
        question_time=pygame.time.get_ticks()
    display_question(num1,num2)
    display_answer(answer_text)
    display_score(score)
    if has_answer==True:
        if answer_int==num1+num2:
            display_check()
            if update_score==False:
                score+=1
                
                update_score=True
    if has_answer==True:
        if answer_int!=num1+num2:
            display_cross()
    pygame.display.update()
win.fill(green)
display_quiz_over()
pygame.display.update()
time.sleep(5)
pygame.QUIT()
QUIT()