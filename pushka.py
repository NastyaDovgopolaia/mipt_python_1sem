
import math
import random
from random import choice

import pygame
import pygame.surface
pygame.init()

FPS = 30
dv = 1.5
resist = 0.02
k = 0.8
targets_number = input()
targets_number = int(targets_number)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, CYAN]


WIDTH = 800
HEIGHT = 600
gun_x, gun_y = WIDTH//40, round(0.75 * HEIGHT)


class Ball:
    def __init__(self, surface: pygame.Surface, x=30, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.lifespan = 60
        self.lived_for = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXED!
        self.lived_for += 1
        self.x += self.vx
        self.y += self.vy
        self.vy += dv
        self.vy += -self.vy * resist
        self.vx += -self.vx * resist
        if (0 < self.x < WIDTH) is False:
            self.vx = -self.vx
        if (self.y < HEIGHT) is False:
            self.vy = -self.vy * k

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.r + obj.r)**2 >= (self.x - obj.x)**2 + (self.y - obj.y)**2


class Gun:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = CYAN
        self.max_length = 100
        self.min_length = 10
        self.width = 10

    def fire_start(self, event):
        self.f2_on = 1
        return choice(GAME_COLORS)

    def fire_end(self, event, color):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.surface)
        new_ball.color = color
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return new_ball.color

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-gun_y), (event.pos[0]-gun_x))
        if self.f2_on is False:
            self.color = GREY

    def draw(self):
        length = self.min_length + self.max_length * (self.f2_power - 10) / 90
        width = self.width
        x1, y1 = length * math.cos(self.an), length * math.sin(self.an)
        x2, y2 = width * math.sin(self.an), width * math.cos(self.an)
        pygame.draw.polygon(screen, self.color, ((gun_x, gun_y), (gun_x + x1, gun_y + y1),
                                                 (gun_x + x1 + x2, gun_y + y1 - y2), (gun_x + x2, gun_y - y2)))
        # FIXED!

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
        else:
            self.color = CYAN


class Target:
    def __init__(self, surface: pygame.Surface):
        self.live = 1
        self.cost = 1
        self.surface = surface
        self.x = random.randint(round(0.6 * WIDTH), round(0.9 * WIDTH))
        self.y = random.randint(round(0.1 * HEIGHT), round(0.9 * HEIGHT))
        self.r = random.randint(20, 60)
        self.color = choice(GAME_COLORS)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
total = 0
balls = []
targets = []
for i in range(targets_number):
    targets.append(Target(screen))

You_have = 0
You_have = int(You_have)

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for ball in balls:
        ball.draw()
    for target in targets:
        target.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color_to_shoot = gun.fire_start(event)
            gun.color = color_to_shoot
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire_end(event, color_to_shoot)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for ball in balls:
        ball.move()
        if ball.lived_for >= ball.lifespan:
            balls.remove(ball)
            continue
        for target in targets:
            if ball.hittest(target):
                total += target.cost
                balls.remove(ball)
                targets.remove(target)
    gun.power_up()            
    pygame.display.update()
    
pygame.quit() 
