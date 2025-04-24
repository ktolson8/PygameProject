import pygame
import random
from apple import Apple
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
fps = 60

class Snake:
    def __init__(self):
        self.size = 50
        self.snake_pos = [300,400]
        self.body = [[300,400],[350,400],[400,400],[450,400]]
        self.snake_color = (0,255,0)