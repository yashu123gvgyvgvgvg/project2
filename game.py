from kivymd.app import MDApp
from kivymd.uix.screenmanager import Screen
from kivy.lang import Builder

import pygame as pg
from pygame.locals import *
import random

pg.init()

game_over=False


clock = pg.time.Clock()
bx=50
by=175
px=170

exit_game=False
gamedisplay=pg.display.set_mode((350,500),pg.SRCALPHA)
gametitle= pg.display.set_caption('Flappy Bird by Yash Mendiratta')

bg = pg.image.load('C:/Users/toshiba/OneDrive/Desktop/python pr/bg2.jpg')
bg=bg.convert_alpha()
bird=pg.image.load('C:/Users/toshiba/OneDrive/Desktop/python pr/bird.png').convert_alpha()

bird=pg.transform.scale(bird,(30,30))
bird_rect=bird.get_rect()
bird_rect.center=bx,by
vy=0
pipe = pg.image.load('C:/Users/toshiba/OneDrive/Desktop/python pr/pipe.png').convert_alpha()


pipe=pg.transform.scale(pipe,(70,300))
pipe2=pg.transform.rotate(pg.transform.scale(pipe,(70,170)),180)



pipes=[]
pipes2=[]
next_pipe_time = pg.time.get_ticks() + 1500
game_active=False
def createpipeup():
    
    py_up=random.randint(-7,0 )
    
    return {'x':400,'y':py_up}

def createpipedown():
    py_down=random.randint(250,350)
    
    return {'x':400,'y':py_down}

def textscreen(stext,color,x,y,font):
    font=pg.font.SysFont(None,font)
    text=font.render(stext,True,color)
    gamedisplay.blit(text,[x,y])


while not exit_game:
    if game_over:
        gamedisplay.fill([0,255,24])
        gamedisplay.blit(bg,(0,0))
        textscreen('Game Over',[0,0,0],90,100,45)
    else:
    
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit_game=True

            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    vy= -8 
                    game_active=True
                    current_time = pg.time.get_ticks()
                    if current_time > next_pipe_time:
                        pipes.append(createpipedown())
                        pipes2.append(createpipeup())
                        next_pipe_time = current_time + 1500
                        game_active=True
  
        if game_active:   
            px=px-5
            vy=vy+0.8
            by=by+vy        
            bird_rect.center=bx,by

       
        gamedisplay.fill([0,255,24])
        gamedisplay.blit(bg,(0,0))
        gamedisplay.blit(bird,bird_rect)
        

        keys=pg.key.get_pressed()
        if not game_active:
            gamedisplay.blit(bg,(0,0))
            gamedisplay.blit(bird,bird_rect)
            textscreen('Flappy Bird',[0,0,0],90,100,45)
            textscreen('Press Space bar to start',[0,0,0],80,150,25)
        else:
            pass

        
        
        for pp in pipes:
            pipe_rect = pg.Rect(int(pp['x']), int(pp['y']), pipe.get_width(), pipe.get_height())
            if bird_rect.colliderect(pipe_rect):
                game_over = True
                game_active = False
                pipes=pipes.clear()
                
                gamedisplay.fill([0,255,24])
                gamedisplay.blit(bg,(0,0))
                textscreen('Game Over',[0,0,0],90,100,45)
            else:
                pp['x']-=4
                gamedisplay.blit(pipe,(pp['x'],pp['y']))
        for pp2 in pipes2:
            pipe2_rect = pg.Rect(int(pp2['x']), int(pp2['y']), pipe2.get_width(), pipe2.get_height())
            if bird_rect.colliderect(pipe2_rect):
                game_over = True
                game_active = False
                pipes2=pipes2.clear()
                
                gamedisplay.fill([0,255,24])
                gamedisplay.blit(bg,(0,0))
                textscreen('Game Over',[0,0,0],90,100,45)
            else:    
                pp2['x']-=4
                gamedisplay.blit(pipe2,(pp2['x'],pp2['y']))

        if by>500 or by<0:
            game_over=True



    
    


    clock.tick(32)
    pg.display.update()


pg.quit()
quit()