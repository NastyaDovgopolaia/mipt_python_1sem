import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((500, 500))

pygame.draw.circle(screen, (255, 255, 0), (200, 200), 100)
pygame.draw.line(screen, (0,0,0), (170,250), (230,250), width=5)
pygame.draw.circle(screen, (0, 0, 0), (180, 170), 10)
pygame.draw.circle(screen, (0, 0, 0), (220, 170), 10)
pygame.draw.line(screen, (0,0,0), (175,140), (185,150), width=5)
pygame.draw.line(screen, (0,0,0), (215,150), (225,140), width=5)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
