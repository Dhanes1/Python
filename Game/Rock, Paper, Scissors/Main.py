import sys
import pygame
from pygame.display import get_surface
from pygame.locals import QUIT
import random
import time
player_score1=0
computer_score1=0
info=""
rock_clk=False
paper_clk=False
scissor_clk=False
game_start=False
player_choice=0
computer_choice=0
player_clk_time=0
update_score=False

pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Rock, Paper, Scissors")
game_image=pygame.image.load("Les\Game\Rock, Paper, Scissors\Welcome Screen.png")
game_image=pygame.transform.scale(game_image,(400,400))
left_hand=pygame.image.load("Les/Game/Rock, Paper, Scissors/Left Hand (Norm).png")
right_hand=pygame.image.load("Les/Game/Rock, Paper, Scissors/Right Hand (Norm).png")
Rock=pygame.image.load("Les/Game/Rock, Paper, Scissors/Rock.jpg")
Rock=pygame.transform.scale(Rock,(50,50))
Paper=pygame.image.load("Les/Game/Rock, Paper, Scissors/Paper.jpg")
Paper=pygame.transform.scale(Paper,(50,50))
Scissors=pygame.image.load("Les/Game/Rock, Paper, Scissors/Scissors.png")
Scissors=pygame.transform.scale(Scissors,(50,50))
start_button=pygame.Surface((100,50))
start_button_font=pygame.font.SysFont("ComicSansMS",25)
start_button_text=start_button_font.render("START",True,(0,0,0))
player_lbl=pygame.Surface((100,30))
player_lbl_font=pygame.font.SysFont("ComicSansMS", 20)
player_lbl_text=player_lbl_font.render("Player",True,(240,243,245))
computer_lbl=pygame.Surface((100,30))
computer_lbl_font=pygame.font.SysFont("ComicSansMS", 20)
computer_lbl_text=computer_lbl_font.render("Computer",True,(240,243,245))
player_score=pygame.Surface((40,40))
player_score_font=pygame.font.SysFont("ComicSansMS", 20)
player_score_text=computer_lbl_font.render("0",True,(0,0,0))
computer_score=pygame.Surface((40,40))
computer_score_font=pygame.font.SysFont("ComicSansMS", 20)
computer_score_text=computer_lbl_font.render("0",True,(0,0,0))
inf_lbl=pygame.Surface((200,30))
inf_lbl_font=pygame.font.SysFont("ComicSansMS", 12)
inf_lbl_text=inf_lbl_font.render("Choose Rock, Paper, or Scissors!",True,(0,0,0))
left_box=pygame.Surface((135,220))
right_box=pygame.Surface((135,220))
rock_font=pygame.font.SysFont("ComicSansMS", 12)
rock_lbl_text=rock_font.render("Rock",True,(0,0,0))
paper_font=pygame.font.SysFont("ComicSansMS", 12)
paper_text=paper_font.render("Paper",True,(0,0,0))
scissors_lbl_font=pygame.font.SysFont("ComicSansMS", 12)
scissors_text=scissors_lbl_font.render("Scissors",True,(0,0,0))
rps_surface=pygame.Surface((50,20))
Rock1=pygame.image.load("Les/Game/Rock, Paper, Scissors/Rock1.png")
Rock1=pygame.transform.scale(Rock1,(100,130))
Paper1=pygame.image.load("Les/Game/Rock, Paper, Scissors/Paper1.png")
Paper1=pygame.transform.scale(Paper1,(100,130))
Scissors1=pygame.image.load("Les/Game/Rock, Paper, Scissors/Scissors1.png")
Scissors1=pygame.transform.scale(Scissors1,(100,130))
Rock2=pygame.image.load("Les/Game/Rock, Paper, Scissors/Rock2.png")
Rock2=pygame.transform.scale(Rock2,(100,130))
Paper2=pygame.image.load("Les/Game/Rock, Paper, Scissors/Paper2.png")
Paper2=pygame.transform.scale(Paper2,(100,130))
Scissors2=pygame.image.load("Les/Game/Rock, Paper, Scissors/Scissors2.png")
Scissors2=pygame.transform.scale(Scissors2,(100,130))
while True:
    player_score_text=computer_lbl_font.render(str(player_score1),True,(0,0,0))
    computer_score_text=computer_lbl_font.render(str(computer_score1),True,(0,0,0))
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if game_start==False:
                if mouse_pos[0]>=350 and mouse_pos[0]<=450 and mouse_pos[1]>=400 and mouse_pos[1]<=450:
                    game_start=True
            else:
                if mouse_pos[0]>=85 and mouse_pos[0]<=165 and mouse_pos[1]>=360 and mouse_pos[1]<=440 and player_clk_time==0:
                    rock_clk=True
                    paper_clk=False
                    scissor_clk=False
                    player_choice=1
                    computer_choice=random.randint(1,3)
                    player_clk_time=pygame.time.get_ticks()
                elif mouse_pos[0]>=185 and mouse_pos[0]<=265 and mouse_pos[1]>=360 and mouse_pos[1]<=440 and player_clk_time==0:
                    rock_clk=False
                    paper_clk=True
                    scissor_clk=False
                    computer_choice=random.randint(1,3)
                    player_choice=2
                    player_clk_time=pygame.time.get_ticks()
                elif mouse_pos[0]>=285 and mouse_pos[0]<=365 and mouse_pos[1]>=360 and mouse_pos[1]<=440 and player_clk_time==0:
                    rock_clk=False
                    paper_clk=False
                    scissor_clk=True
                    computer_choice=random.randint(1,3)
                    player_choice=3
                    player_clk_time=pygame.time.get_ticks() 
    if game_start==False:
        win.blit(game_image,(50,50))
        win.blit(start_button,(350,400))
        if mouse_pos[0]>=350 and mouse_pos[0]<=450 and mouse_pos[1]>=400 and mouse_pos[1]<=450:
            start_button.fill((211,211,211))
        else:         
            start_button.fill((255,255,255))
        start_button.blit(start_button_text,(7,8))
    else:
        win.fill((173,216,230))
        win.blit(player_lbl,(25,25))
        win.blit(player_lbl_text,(43,23))
        player_lbl.fill((0,0,0))
        win.blit(computer_lbl,(300,25))
        win.blit(computer_lbl_text,(307,23))
        computer_lbl.fill((0,0,0))
        win.blit(player_score,(45,60))
        win.blit(player_score_text,(59,62))
        player_score.fill((255,255,255))
        win.blit(computer_score,(320,60))
        win.blit(computer_score_text,(334,62))
        computer_score.fill((255,255,255))
        win.blit(inf_lbl,(100,60))
        win.blit(inf_lbl_text,(110,66))
        inf_lbl.fill((255,255,255))
        win.blit(left_box,(25,125))
        win.blit(right_box,(300,125))
        left_box.fill((0,0,0))
        right_box.fill((0,0,0))
        if player_clk_time==0:
            left_box.blit(left_hand,(30,50))
            right_box.blit(right_hand,(18,50))
            if mouse_pos[0]>=85 and mouse_pos[0]<=165 and mouse_pos[1]>=360 and mouse_pos[1]<=440:
                if rock_clk==False and paper_clk==False and scissor_clk==False:
                    pygame.draw.circle(win,(211,211,211),(125,400),40,0)
                    win.blit(Rock,(100,375))
            else:
                if rock_clk==False and paper_clk==False and scissor_clk==False:       
                    pygame.draw.circle(win,(255,255,255),(125,400),40,0)
                    win.blit(Rock,(100,375))
            if mouse_pos[0]>=185 and mouse_pos[0]<=265 and mouse_pos[1]>=360 and mouse_pos[1]<=440:
                pygame.draw.circle(win,(211,211,211),(225,400),40,0)
            else:        
                pygame.draw.circle(win,(255,255,255),(225,400),40,0)
            if mouse_pos[0]>=285 and mouse_pos[0]<=365 and mouse_pos[1]>=360 and mouse_pos[1]<=440:
                pygame.draw.circle(win,(211,211,211),(325,400),40,0)
            else:        
                pygame.draw.circle(win,(255,255,255),(325,400),40,0)
            # Blits
            win.blit(Paper,(200,375))
            win.blit(Scissors,(300,375))
            rps_surface.fill((242,242,242))
            win.blit(rps_surface,(100,450))
            win.blit(rps_surface,(200,450))
            win.blit(rps_surface,(300,450))
            win.blit(rock_lbl_text,(110,450))
            win.blit(paper_text,(210,450))
            win.blit(scissors_text,(300,450))
        elif pygame.time.get_ticks()-player_clk_time>0:
            if rock_clk==True:
                win.blit(Rock1,(60,160))
            elif paper_clk==True:
                win.blit(Paper1,(60,160))
            elif scissor_clk==True:
                win.blit(Scissors1,(60,160))
        # else:    
        #     computer_choice=random.randint(1,3)
        # if rock_clk==True or paper_clk==True or scissor_clk==True:
            if computer_choice==1:
                win.blit(Rock2,(300,160))
            elif computer_choice==2:
                win.blit(Paper2,(300,160))
            elif computer_choice==3:
                win.blit(Scissors2,(300,160))
            if pygame.time.get_ticks()-player_clk_time>=2000:
                if player_choice==computer_choice:
                    inf_lbl_text=inf_lbl_font.render("Its a tie!",True,(0,0,0))
                elif player_choice==1 and computer_choice==2:
                    inf_lbl_text=inf_lbl_font.render("Computer get a point",True,(0,0,0))
                    if update_score==False:
                        computer_score1+=1
                        update_score=True
                elif player_choice==1 and computer_choice==3:
                    inf_lbl_text=inf_lbl_font.render("Player get a point",True,(0,0,0))
                    if update_score==False:
                        player_score1+=1
                        update_score=True
                elif player_choice==2 and computer_choice==1:
                    inf_lbl_text=inf_lbl_font.render("Player get a point",True,(0,0,0))
                    if update_score==False:
                        player_score1+=1
                        update_score=True
                elif player_choice==2 and computer_choice==3:
                    inf_lbl_text=inf_lbl_font.render("Computer get a point",True,(0,0,0))
                    if update_score==False:
                        computer_score1+=1
                        update_score=True
                elif player_choice==3 and computer_choice==1:
                    inf_lbl_text=inf_lbl_font.render("Computer get a point",True,(0,0,0))
                    if update_score==False:
                        computer_score1+=1
                        update_score=True
                elif player_choice==3 and computer_choice==2:
                    inf_lbl_text=inf_lbl_font.render("Player get a point",True,(0,0,0))
                    if update_score==False:
                        player_score1+=1
                        update_score=True
            if pygame.time.get_ticks()-player_clk_time>=4000:
                player_choice=0
                computer_choice=0
                update_score=False
                rock_clk=False
                paper_clk=False
                scissor_clk=False
                inf_lbl_text=inf_lbl_font.render("",True,(0,0,0))
                player_clk_time=0
    pygame.display.update()