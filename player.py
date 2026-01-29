import pygame
import os
import sys
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, GRAVITY, FPS

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH / 2 - self.width / 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.base_speed = 20
        self.velocity_x = 0
        self.velocity_y = 0
        self.isOnGround = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.prev_rect = self.rect.copy()
        # cinar etisi boah ich han so richtig bok was leckeres zu ässe  
        #
    def move(self):
        self.prev_rect = self.rect.copy()

        keys = pygame.key.get_press
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.base_speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.base_speed
        else:
            self.velocity_x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w] and self.isOnGround:
            self.velocity_y = -10
            self.isOnGround = False

        self.x += self.velocity_x
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        # Screen boundaries
        if self.x >= SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
        if self.x < 0:
            self.x = 0
        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.velocity_y = 0
            self.isOnGround = True

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, ("Red"), self.rect)   

player = Player()

