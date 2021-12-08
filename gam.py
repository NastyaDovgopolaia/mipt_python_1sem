import pygame
import pygame.freetype
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, CYAN]
my_font = pygame.freetype.SysFont('Times New Roman', 15)
v = [randint(-10, 10), randint(-10, 10)]

class Ball():
    def __init__(self, x=500, y=500, r=10):
        self.x = randint(100, 800)
        self.y = randint(100, 800)
        self.r = randint(40, 100)
        self.color = COLORS[randint(0, 4)]
        self.v = self.Vx, self.Vy = [randint(-10, 10), randint(-10, 10)]
    def moving(self):
        if self.x < 0 or self.x > 900:
            self.Vx = -self.Vx
        if self.y < 0 or self.y > 900:
            self.Vy = -self.Vy
        self.x += self.Vx
        self.y += self.Vy
        circle(screen, self.color, (self.x, self.y), self.r)

L=input()
L=int(L)
balls=[]
for i in range(L):
    ball=Ball()
    balls.append(ball)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

You_have = 0
You_have = int(You_have)
while not finished:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if (ball.x - event.pos[0])**2 + (ball.y - event.pos[1])**2 <= ball.r**2:
                    balls.remove(ball)
                    You_have += 1    
                    
    rect(screen, BLACK, (0, 0, 200, 100))
    my_font.render_to(screen, (5, 10), "You_have: " + str(You_have), (255, 0, 0))

    pygame.display.update()
    screen.fill(BLACK)
    for ball in balls:
        ball.moving()
    if (You_have == L) is True:
        color = COLORS[randint(0, 4)]
        line(screen, color, (200, 600), (200, 200), 5)
        line(screen, color, (200, 200), (300, 600), 5)
        line(screen, color, (300, 600), (300, 200), 5)
        line(screen, color, (350, 600), (350, 220), 5)
        line(screen, color, (350, 200), (350, 210), 5)
        line(screen, color, (400, 600), (400, 200), 5)
        line(screen, color, (500, 200), (400, 200), 5)
        line(screen, color, (500, 600), (400, 600), 5)
        line(screen, color, (550, 600), (550, 200), 5)
        line(screen, color, (550, 200), (650, 200), 5)
        line(screen, color, (550, 600), (650, 600), 5) 
        line(screen, color, (550, 400), (650, 400), 5) 
pygame.quit()
