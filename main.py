import pygame
from random import randint,choice
import math
pygame.init()

#Display Size and Caption for the Game
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Ping Bong Game")

#Loading Images
icon=pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
background=pygame.image.load('img/background.png')
player=pygame.image.load('img/Panel.png')
brick=pygame.image.load('img/brick.png')
ball=pygame.image.load('img/ball.png').convert()
ball.set_colorkey((255,255,255))
ball.set_alpha(200)

#Initializing the Brick
BrickX=400
BrickY=100

#Initializing the Player
PlayerX=360
PlayerY=450
PlayerX_Change=0

#Collision Walls
top_collision_point=[0,0]
left_collision_point=[0,0]
right_collision_point=[0,0]

#Initializing Ball Settings
BallX=randint(0,400)
BallY=randint(0,300)
BallX_Change=choice([1,-1])
BallY_Change=choice([1,-1])
global Ball_State
Ball_State="moving"

#Defining the Functions
def Player(x,y):
    screen.blit(player,(x,y))   
def Brick(x,y):
    screen.blit(brick,(x,y))
def Ball(x,y):
    screen.blit(ball,(x,y))
def Sign_Reverse(x):
    y=-x
    return y
def deflection():
    #wall referance point. It can be used to find the length of the hypotenuse when the ball deflects
    left_referance_point=[0,0]
    right_referance_point=[730,0]
    top_referance_point=[0,0]

    #I choose 5 units as the constant for adjusent length
    adj=5
    if top_collision_point[0]>0 and top_collision_point[1]==0: #top wall
        opposite=top_collision_point[0]-abs(BallX_Change)
        third_point=[opposite,adj]
        hypotenuse=math.sqrt((top_collision_point[0]-third_point[0])**2+(top_collision_point[1]-third_point[1])**2)

    if left_collision_point[0]==0 and left_collision_point[1]>0:#Left Wall
        opposite=left_collision_point[1]+abs(BallY_Change)
        third_point=[opposite,adj]
        hypotenuse=math.sqrt((left_collision_point[0]-third_point[0])**2+(left_collision_point[1]-third_point[1])**2)

    if right_collision_point[0]>0 and right_collision_point[1]>0:#Right Wall
        opposite=right_collision_point+abs(BallY_Change)
        third_point=[opposite,adj]
        hypotenuse=math.sqrt((right_collision_point[0]-third_point[0])**2+(right_collision_point[1]-third_point[1])**2)
    #Determining the angle
    theta=(1/math.sin(opposite/hypotenuse))*(180/math.pi)
    print(theta)
    
#Game Loop
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(-90,0))
    for event in pygame.event.get():
        #Exit
        if event.type==pygame.QUIT:
            running=False

        #Player Controls
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                PlayerX_Change=-5
            if event.key==pygame.K_RIGHT:
                PlayerX_Change=+5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                PlayerX_Change=0
    PlayerX+=PlayerX_Change

    #Ball
    if BallY<=0:#top wall
        # I can get the boundary collision point here
        top_collision_point=[BallX,BallY] #Reset after use
        print(top_collision_point)
        
        BallX_Change=Sign_Reverse(BallX_Change)
        BallY_Change=Sign_Reverse(BallY_Change)
        deflection()
    if BallX<=0:#left wall
        # I can get the boundary collision point here
        left_collision_point=[BallX,BallY]
        print(left_collision_point)
        
        BallX_Change=Sign_Reverse(BallX_Change)
        BallY_Change=Sign_Reverse(BallY_Change)
        deflection()
    if BallX>=730:#right wall
        # I can get the boundary collision point here
        right_collision_point=[BallX,BallY]
        print(left_collision_point)
        
        BallX_Change=Sign_Reverse(BallX_Change)
        BallY_Change=Sign_Reverse(BallY_Change)
        deflection()

    if BallY>=450:
        #Change  in the end of code
        print(BallX)
        print(BallY)
        BallX_Change=Sign_Reverse(BallX_Change)
        BallY_Change=Sign_Reverse(BallY_Change)
        #Ball_State="stop"
        #print("Game Over")

    if Ball_State=="moving":
        BallX-=BallX_Change
        BallY+=BallY_Change
        Ball(BallX,BallY)
    #Bricks
    Brick(BrickX,BrickY)

    #Player
    if PlayerX<=0:
        PlayerX=0
    elif PlayerX>=730:
        PlayerX=730
    Player(PlayerX,PlayerY)

    pygame.display.update()