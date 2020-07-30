import pygame
import random
import tkinter as tk
from tkinter import messagebox
import math
from pygame import mixer
import time

# initialize the pygame

pygame.init()

# background image
background=pygame.image.load(r"F:\python course\spaces.jpg")

# backgrounf sound
mixer.music.load(r"F:\python course\05_Earth.mp3")
mixer.music.play(-1)

# create the screen(width,height)
screen = pygame.display.set_mode((900,600))
# bullet image
bullet=pygame.image.load(r"C:\Users\This pc\Downloads\bullet.png")


# title and icon
pygame.display.set_caption("space invaders")
icon=pygame.image.load(r"F:\python course\exit.png")
pygame.display.set_icon(icon)


# player
playerimg=pygame.image.load(r"C:\Users\This pc\Downloads\spaceship.png")

# width ka half=400 therefore 370 means along x axis player almost 
# screen ke beech me hoga nd along y axis border s thod upr hoga
playerX= 400
playerY= 480
playerX_change=0

enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemies= 6

for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load(r"C:\Users\This pc\Downloads\cartoon.png"))
    enemyX.append(random.randint(0,835))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=8
bullet_state='ready'
# ready means u cant see bullent on screen
# fire means bullet is in motion

# score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
font1=pygame.font.Font('freesansbold.ttf',50)
font2=pygame.font.Font('freesansbold.ttf',25)
textX=10
textY=10

def game_over():
    over=font1.render("GAME OVER !",True,(255,255,255))
    screen.blit(over,(300,300))
def show_score(x,y):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))


def player(x,y):
    # blit() draws image of player
    screen.blit(playerimg,(x,y))


def firebullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
    # x+16 and y+10 shows bullet shooting from center of the spaceship and from little above it

def collision(eX,eY,bX,bY):
    dis=math.sqrt((math.pow(eX-bX,2)) +(math.pow(eY-bY,2)))
    if dis<27:
        return True
    else:
        return False
# game loop
running=True
while running:
    screen.fill((150,100,70))
    # rgb=(r,g,b),[o-255]
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # checks if close button is pressed
            running=False
                         
        if event.type==pygame.KEYDOWN:
            # i.e some key is pressed
            if event.key==pygame.K_LEFT:
                playerX_change=-3
            if event.key==pygame.K_RIGHT:
                playerX_change=3
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound(r"F:\python course\shoot.wav") 
                    bullet_sound.play()
                    bulletX=playerX
                    firebullet(bulletX,bulletY) 

        if event.type==pygame.KEYUP:
            # checks if key is released
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT :
                playerX_change=0
                    

    playerX+=playerX_change

    # checking for boundaries
    if playerX<=0:
        playerX=0
    elif playerX>=836:
        # image of spaceship is 64 pixels therefore 800-64
        playerX=836
            

    for i in range(no_of_enemies):
        if enemyY[i]>=400:
            for j in range(no_of_enemies):
                enemyY[j]=2000
            game_over()
            break
        enemyX[i]+=enemyX_change[i]
            
        if enemyX[i]<=0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
                
        elif enemyX[i]>=836:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]
                    


        # collision
        col=collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if col:
            col_sound=mixer.Sound(r"F:\python course\invaderkilled.wav")
            col_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
                
            enemyX[i]=random.randint(0,835)
            enemyY[i]=random.randint(50,200)

        enemy(enemyX[i],enemyY[i],i)
                
    # bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        firebullet(bulletX,bulletY)
        bulletY-=bulletY_change
                

    player(playerX,playerY)
        
    show_score(textX,textY)
                
    pygame.display.update()

                

