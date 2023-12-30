import pygame
from sys import exit
from random import randint

HEIGHT = 500
WIDTH = 1920
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
radius = 20
rate = -1.1


class Circle:
    def __init__(self, color, direction, center_x, center_y):
        self.color = color
        self.direction = direction
        self.center_x = center_x
        self.center_y = center_y
        self.line_list = []

    def bounce_check(self):
        if self.center_x + radius > screen.get_width():
            self.direction[0] *= rate
            self.line_list.append(
                (self.center_x + radius, self.center_y, (randint(0, 255), randint(0, 255), randint(0, 255))))

        if self.center_y + radius > screen.get_height():
            self.direction[1] *= rate
            self.line_list.append(
                (self.center_x, self.center_y + radius, (randint(0, 255), randint(0, 255), randint(0, 255))))

        if self.center_x - radius < 0:
            self.direction[0] *= rate
            self.line_list.append(
                (self.center_x - radius, self.center_y, (randint(0, 255), randint(0, 255), randint(0, 255))))

        if self.center_y - radius < 0:
            self.direction[1] *= rate
            self.line_list.append(
                (self.center_x, self.center_y - radius, (randint(0, 255), randint(0, 255), randint(0, 255))))

    def moving_parts(self):
        self.center_x += self.direction[0]
        self.center_y += self.direction[1]

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), radius)
        for i in self.line_list:
            pygame.draw.line(screen, i[2], (self.center_x, self.center_y), (i[0], i[1]))


circles = [
    Circle('blue', [1, 1], screen.get_width() / 2, screen.get_height() / 2),
    Circle("yellow", [1, -1], screen.get_width() / 2, screen.get_height() / 2),
    Circle("red", [-1, -1], screen.get_width() / 2, screen.get_height() / 2),
    Circle("green", [-1, 1], screen.get_width() / 2, screen.get_height() / 2),
]

for i in circles:
    i.moving_parts()
    i.bounce_check()
    i.draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    screen.fill("black")

    for i in circles:
        i.moving_parts()
        i.bounce_check()
        i.draw()

    pygame.display.flip()
    clock.tick(60)
