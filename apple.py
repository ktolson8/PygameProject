import pygame
import random
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
fps = 60
size = 50

class Apple:
    def __init__(self):
        self.x = random.randint(0,750)
        self.y = random.randint(0,750)
        self.a1 = pygame.Rect(self.x,self.y,size,size)
        self.a1_surf = pygame.Surface((size,size))
        self.a1_surf.fill(color = (255,0,0))

        self.a = random.randint(0, 750)
        self.b = random.randint(0, 750)
        self.a2 = pygame.Rect(self.a, self.b, size, size)
        self.a2_surf = pygame.Surface((size, size))
        self.a2_surf.fill(color=(255, 0, 0))

        self.c = random.randint(0, 750)
        self.d = random.randint(0, 750)
        self.a3 = pygame.Rect(self.c, self.d, size, size)
        self.a3_surf = pygame.Surface((size, size))
        self.a3_surf.fill(color=(255, 0, 0))

        self.e = random.randint(0, 750)
        self.f = random.randint(0, 750)
        self.a4 = pygame.Rect(self.e, self.f, size, size)
        self.a4_surf = pygame.Surface((size, size))
        self.a4_surf.fill(color=(255, 0, 0))

        self.g = random.randint(0, 750)
        self.h = random.randint(0, 750)
        self.a5 = pygame.Rect(self.g, self.h, size, size)
        self.a5_surf = pygame.Surface((size, size))
        self.a5_surf.fill(color=(255, 0, 0))

        self.apples = [self.a1,self.a2,self.a3,self.a4,self.a5]
        self.surf = [self.a1_surf,self.a2_surf,self.a3_surf,self.a4_surf,self.a5_surf]
        self.cleared = ["a1","a2","a3","a4","a5"]
    def draw(self):
        screen.blit(self.a1_surf, (self.a1.x,self.a1.y))
        screen.blit(self.a2_surf, (self.a2.x, self.a2.y))
        screen.blit(self.a3_surf, (self.a3.x, self.a3.y))
        screen.blit(self.a4_surf, (self.a4.x, self.a4.y))
        screen.blit(self.a5_surf, (self.a5.x, self.a5.y))
