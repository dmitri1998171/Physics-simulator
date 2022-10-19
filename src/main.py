from turtle import color
import pygame, sys
from pygame.locals import *

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()

width = 1280
height = 800
speed = [2, 2]
black = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Physics Simulator")
clock = pygame.time.Clock()

ball = pygame.image.load("src\intro_ball.gif")
ballRect = ball.get_rect()

ground = pygame.Surface(size=(width, height / 6))
ground.fill((0, 200, 0))
groundRect = ground.get_rect()

while True:
    handleEvents()
            
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color=(0, 191, 235))
    screen.blit(ball, ballRect)
    screen.blit(ground, (0, (height - (height / 6))))

    pygame.display.update()
    clock.tick(60)