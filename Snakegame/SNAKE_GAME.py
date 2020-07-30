import pygame
import math
import random
import time
import os

pygame.init()


black=(0,0,0)
red=(255,0,0)
green=(0,51,0)
peach=(255,218,185)

text_X=2
text_Y=2

screen=pygame.display.set_mode((700,500))

pygame.display.set_caption("Snake Xenzia")

appleimg=pygame.image.load(r"C:\Users\This pc\Downloads\guava.png")

icon=pygame.image.load(r"C:\Users\This pc\Downloads\snake.png")
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

font=pygame.font.Font('freesansbold.ttf',15)
font1=pygame.font.Font('freesansbold.ttf',20)
font2=pygame.font.Font('freesansbold.ttf',28)

if(not os.path.exists("high.txt")):
    with open ("high.txt","w") as f:
        f.write("0")

with open("high.txt",'r') as f:
    hiscore=f.read()

def apple(x,y):
    screen.blit(appleimg,(x,y))

def show_score(x,y,score_value):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def show_highscore(hiscore):
    hs=font.render(f"High Score: {int(hiscore)}",True,(255,255,255))
    screen.blit(hs,(580,10))

def collision(eX,eY,bX,bY):
    dis=math.sqrt((math.pow(eX-bX,2)) +(math.pow(eY-bY,2)))
    if dis<20:
        return True
    else:
        return False


def plot_snake(screen,color,snake_list,snake_dimensions):
    for i,j in snake_list:
        pygame.draw.rect(screen,color,[i,j,snake_dimensions,snake_dimensions])


def gameover(score_value):
    global hiscore
    global over_high

    if score_value>=int(hiscore):
        over_high=font1.render(f"Wohoo!! Highest Score",True,red)
        screen.blit(over_high,(200,200))
    over_1=font1.render(f" Your Score : {score_value}",True,red)
    over_2=font1.render(f"High Score : {int(hiscore)}",True,red)
    over=font1.render(f"OOPS!! GAME OVER..Let's play again! (Press ENTER)",True,red)
    screen.blit(over,(65,250))
    screen.blit(over_1,(0,0))
    screen.blit(over_2,(550,0))
    
def welcome():
    running=True
    while running:
        screen.fill(peach)
        background=pygame.image.load(r"F:\python course\nsnake.jpg")
        screen.blit(background,(0,0))
        a=font2.render("Welcome to SNAKE XENZIA :)",True,(0,0,0))
        b=font1.render("Press Space Bar to start the game",True,(0,0,0))
        screen.blit(a,(140,200))
        screen.blit(b,(170,270))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    mixer.music.load(r"F:\Lost-Jungle_Looping.mp3")
                    mixer.music.play(-1)
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

        
       

def gameloop():
    change_x=0
    change_y=0
    snake_x=100

    snake_y=120
    snake_dimensions=20
    apple_x=random.randint(50,650)
    apple_y=random.randint(50,450)
    score_value=0

    fps=60


    init_velocity=5
    snake_list=[]
    snake_length=1

    running=True
    game_over=False

    while running:
        global hiscore
        if game_over:
            with open("high.txt",'w') as f:
                f.write(str(hiscore))
            screen.fill(peach)
            gameover(score_value)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
        
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        
        else:

            screen.fill(black)
            # pygame.draw.rect(screen,green,(snake_x,snake_y,snake_dimensions,snake_dimensions))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False

                if event.type==pygame.KEYDOWN:
                    # i.e some key is pressed
                    if event.key==pygame.K_LEFT:
                        change_x=-init_velocity
                        change_y=0

                    if event.key==pygame.K_RIGHT:
                        change_x=init_velocity
                        change_y=0

                    if event.key==pygame.K_UP:
                        change_y=-init_velocity
                        change_x=0

                    if event.key==pygame.K_DOWN:
                        change_y=init_velocity
                        change_x=0

                
            if snake_x<=0:
                snake_x=695
            elif snake_x>=695:
                snake_x=0
            
            if snake_y<=0:
                snake_y=495
            elif snake_y>=495:
                snake_y=0
        
            
            snake_x=snake_x + change_x
            snake_y=snake_y + change_y
    

            col=collision(apple_x,apple_y,snake_x,snake_y)

            if col:
                col_sound=mixer.Sound(r"C:\Users\This pc\Downloads\275015__wadaltmon__bite-apple.wav")
                col_sound.play()
                score_value+=1
                snake_length+=5
                # we increased by 5 bcoz these are coordinates
                apple_x=random.randint(50,650)
                apple_y=random.randint(50,450)
                apple(apple_x,apple_y)
                
                if score_value>=int(hiscore):
                    hiscore=score_value
                
            
            show_score(text_X,text_Y,score_value)
            show_highscore(hiscore)

            snake_Head=[]
            snake_Head.append(snake_x)
            snake_Head.append(snake_y)
            snake_list.append(snake_Head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            
            if snake_Head in snake_list[:-1]:
                game_over=True
                
            

            plot_snake(screen,red,snake_list,snake_dimensions)


            apple(apple_x,apple_y)
            

        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()
welcome()

