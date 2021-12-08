import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

rect(screen, (100, 100, 100), (0, 0, 1000, 600))
rect(screen, (80, 80, 80), (0, 0, 80, 600))
rect(screen, (50, 50, 50), (0, 100, 80, 600))
rect(screen, (70, 70, 70), (80, 100, 50, 400))
rect(screen, (50, 50, 50), (300, 30, 400, 400))
rect(screen, (30, 30, 30), (600, 0, 200, 600))
rect(screen, (255, 255, 255), (780, 0, 5, 600))
rect(screen, (0, 0, 0), (675, 0, 50, 600))
rect(screen, (30, 30, 30), (320, 100, 200, 600))
rect(screen, (80, 100, 100), (0, 620, 1000, 600))
rect(screen, (170, 170, 170), (500, 185, 550, 520))
rect(screen, (255, 255, 255), (500, 185, 550, 520), width=2)
rect(screen, (70, 90, 90), (550, 340, 120, 450))
rect(screen, (170, 170, 170), (0, 200, 550, 520))
rect(screen, (255, 255, 255), (0, 200, 550, 520), width=2)
rect(screen, (130, 140, 130), (50, 220, 150, 500))
rect(screen, (200, 200, 200), (0, 280, 150, 500))
rect(screen, (220, 220, 220), (430, 220, 150, 500))
rect(screen, (70, 90, 90), (380, 370, 150, 450))
rect(screen, (130, 140, 130), (810, 220, 150, 500))
rect(screen, (200, 200, 200), (850, 280, 150, 500))
def car1(x,y):
    rect(screen, (0, 200, 255), (x, y, 100, 20))
    rect(screen, (0, 200, 255), ((x+30), (y-10), 50, 20))
    circle(screen, (0, 0, 0), ((x+80), (y+20)), 10)
    circle(screen, (0, 0, 0), ((x+10), (y+20)), 10)
    rect(screen, (220, 230, 255), ((x+35), (y-5), 15, 15))
    rect(screen, (220, 230, 255), ((x+60), (y-5), 15, 15))
car1(50,780)
car1(460,820)
car1(610,790)
car1(850,850)
def car2(x,y):
    rect(screen, (0, 200, 255), (x, y, 400, 80))
    rect(screen, (0, 200, 255), ((x+120), (y-40), 200, 80))
    circle(screen, (0, 0, 0), ((x+320), (y+80)), 40)
    circle(screen, (0, 0, 0), ((x+40), (y+80)), 40)
    rect(screen, (220, 230, 255), ((x+140), (y-20), 60, 60))
    rect(screen, (220, 230, 255), ((x+240), (y-20), 60, 60))
car2(450,880)    
def car3(x,y):
    rect(screen, (0, 200, 255), (x, y, 400, 80))
    rect(screen, (0, 200, 255), ((x+80), (y-40), 200, 80))
    circle(screen, (0, 0, 0), ((x+320), (y+80)), 40)
    circle(screen, (0, 0, 0), ((x+40), (y+80)), 40)
    rect(screen, (220, 230, 255), ((x+100), (y-20), 60, 60))
    rect(screen, (220, 230, 255), ((x+200), (y-20), 60, 60))
car3(20,850)    
sc = pygame.Surface((1000,1000))
sc.fill((220,220,220))
sc.set_alpha(30)
ellipse(sc, (10, 30, 30), (10, 10, 500, 150))
ellipse(sc, (0, 10, 10), (530, 30, 300, 100))
ellipse(sc, (50, 70, 70), (50, 200, 400, 100))
ellipse(sc, (50, 70, 70), (670, 80, 300, 100))
ellipse(sc, (70, 90, 90), (750, 300, 300, 100))
ellipse(sc, (70, 90, 90), (250, 400, 500, 150))
screen.blit(sc, (0,0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

