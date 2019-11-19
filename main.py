import pygame
import random

pygame.init()

#Display Size and Caption for the Game
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Ping Bong")

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

#Initializing Bullet Settings
BallX=400
BallY=300


#Defining the Functions
def Player(x,y):
    screen.blit(player,(x,y))   
def Brick(x,y):
    screen.blit(brick,(x,y))
def Ball(x,y):
    screen.blit(ball,(x,y))

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
    Ball(BallX,BallY)
    #Bricks
    Brick(BrickX,BrickY)

    #Player
    if PlayerX<=0:
        PlayerX=0
    elif PlayerX>=740:
        PlayerX=740
    Player(PlayerX,PlayerY)

    pygame.display.update()