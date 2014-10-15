#!/usr/bin/python
import sys
import datetime
import pygame
import math
if not pygame.font: print 'Warning, fonts disabled'




framerate = 3
pygame.init()
size = width, height = 50, 25
screen = pygame.display.set_mode(size) 
pygame.display.set_caption('test horloge')
c = pygame.time.Clock() # create a clock object for timing
white = (255, 255, 255)

s = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    now = datetime.datetime.now()
    s = now.second
    screen.fill(white)
    pygame.draw.arc(screen, (255,0,0), (0, 0, 50, 25), (5*math.pi/2) - (s * 2 * math.pi / 60),  5*math.pi/2)
    pygame.display.flip()
    c.tick(framerate)
