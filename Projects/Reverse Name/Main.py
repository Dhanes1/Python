import pygame, sys
from pygame.locals import QUIT
from pygame.display import get_surface
name_input_active=False
name_input_text=""
ok_btn_clk=False
name_input_rev=""
pygame.init()
win=pygame.display.set_mode((600,500))
pygame.display.set_caption("Reverse Name")
name_lbl_font=pygame.font.SysFont("Arial",20)
name_lbl=pygame.Surface((70,30))
name_input_font=pygame.font.SysFont("Arial",20)
name_input=pygame.Surface((200,30))
ok_btn=pygame.Surface((40,30))
ok_btn_fnt=pygame.font.SysFont("Arial", 20)
ok_btn_txt=ok_btn_fnt.render("Ok", True, (0,0,0))
key_fnt=pygame.font.SysFont("Arial", 20)
rev_name_lbl=pygame.Surface((100,30))
rev_name_lbl_fnt=pygame.font.SysFont("Arial", 20)
rev_name_txt=rev_name_lbl_fnt.render("Rev. Name", True, (0,0,0))
output_name_surface=pygame.Surface((200,30))
output_name_fnt=pygame.font.SysFont("Arial",20)

while True:
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0]>=120 and mouse_pos[0]<=320 and mouse_pos[1]>=25 and mouse_pos[1]<=55:
                name_input_active=True
            elif mouse_pos[0]>=335 and mouse_pos[0]<=375 and mouse_pos[1]>=25 and mouse_pos[1]<=55:
                if name_input_text!="":
                    num=len(name_input_text)
                    for i in range(len(name_input_text)):
                        num-=1
                        name_input_rev+=name_input_text[num]
                        
                    output_name_txt=output_name_fnt.render(name_input_rev,True, (0,0,0))
                    ok_btn_clk=True
            else:
                name_input_active=False
        if event.type==pygame.KEYDOWN:
            if name_input_active==True and ok_btn_clk==False:
                
                if event.key==pygame.K_BACKSPACE:
                    name_input_text=name_input_text[:-1]
                else:
                    
                    name_input_text+=event.unicode
            
    win.fill((200,200,200))
    win.blit(name_lbl,(25,25))
    name_lbl.fill((255,255,255))
    key_text=key_fnt.render(name_input_text, True, (0,0,0))
    win.blit(name_input,(120,25))
    
    if name_input_active==False:
        name_input.fill("gray")
        name_input_text=""
    else:
        name_input.fill("white")
        if ok_btn_clk== False:
            
            win.blit(ok_btn,(335,25))
            ok_btn.fill((255,255,255))
            ok_btn.blit(ok_btn_txt,(5,3))
        name_input.blit(key_text,(5,3))
        if ok_btn_clk==True:
            win.blit(rev_name_lbl,(25,100))
            rev_name_lbl.fill("white")
            rev_name_lbl.blit(rev_name_txt,(5,3))
            win.blit(output_name_surface,(150,100))
            output_name_surface.fill("white")
            output_name_surface.blit(output_name_txt,(5,3))
    name_lbl_text=name_lbl_font.render("Name: ",True,(0,0,0))
    name_lbl.blit(name_lbl_text,(5,5))       
    pygame.display.update()