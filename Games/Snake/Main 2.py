import pygame
import time
import random
pygame.init()
width=600
height=600
display=pygame.display.set_mode((height,width))
pygame.display.update()
pygame.display.set_caption('Snake Game')
snake_size=20
food_x=round(random.randrange(snake_size,width-snake_size)/snake_size)*snake_size
food_y=round(random.randrange(snake_size,height-snake_size)/snake_size)*snake_size
x=width/2
y=height/2
snake_speed=5
clock=pygame.time.Clock()
message_font=pygame.font.SysFont("comicsansms",50)
eat_food=False
score=0
def show_message(text,color):
    text_show=message_font.render(text,True,color)
    display.blit(text_show,[width/3,height/3])
def show_score(score):
    text_show = pygame.font.SysFont("comicsansms",25).render("Score: "+str(score), True, red)
    display.blit(text_show,(0,0))
# color code
blue=(0,0,255)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
x_change=0
y_change=0
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-snake_size
                y_change=0
            if event.key==pygame.K_RIGHT:
                y_change=0
                x_change=snake_size
            if event.key==pygame.K_DOWN:
                y_change=snake_size
                x_change=0
            if event.key==pygame.K_UP:
                y_change=-snake_size
                x_change=0
    x+=x_change
    y+=y_change
    display.fill(black)
    if x>=width or x<0 or y>=height or y<0:
        game_over=True
    else:
        pygame.draw.rect(display,green,[x,y,snake_size,snake_size])
        pygame.draw.rect(display,red,[food_x,food_y,snake_size,snake_size])
        if x==food_x and y==food_y:
            score+=1
            eat_food=True
        if eat_food and score<10:
            show_message("Yummy",green)
            eat_food=False
            food_x = round(random.randrange(snake_size, width - snake_size) / snake_size) * snake_size
            food_y = round(random.randrange(snake_size, height - snake_size) / snake_size) * snake_size
    show_score(score)
    pygame.display.update()
    clock.tick(snake_speed)
    if score==10:
        game_over=True
if score==10:
    show_message("You Win!", red)
else:
    show_message('You lost',red)
pygame.display.update()
time.sleep(3)
pygame.quit()
quit()