import pygame
import sys
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GRAVITY
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

player = Player(colour="Red")

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        
        pygame.draw.rect(screen, ("White"), self.rect)


platforms = [Platform(100, 500, 100, 30), Platform(200, 400, 100, 30), Platform(300, 300, 100, 30)]

def draw(colour, rect):
    pygame.draw.rect(screen, colour, rect)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill((0,0,0))

        player.move()
        draw(player.colour, player.rect)
        for platform in platforms:
            platform.draw()

        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                # Falling on top
                if player.prev_rect.bottom <= platform.rect.top:
                    player.rect.bottom = platform.rect.top
                    player.y = player.rect.y
                    player.velocity_y = 0
                    player.isOnGround = True

                # Hitting from below
                elif player.prev_rect.top >= platform.rect.bottom:
                    player.rect.top = platform.rect.bottom
                    player.y = player.rect.y
                    player.velocity_y = 0

                # Hitting from left
                elif player.prev_rect.right <= platform.rect.left:
                    player.rect.right = platform.rect.left
                    player.x = player.rect.x
                    player.velocity_x = 0

                # Hitting from right
                elif player.prev_rect.left >= platform.rect.right:
                    player.rect.left = platform.rect.right
                    player.x = player.rect.x
                    player.velocity_x = 0

        pygame.display.flip()
            
        clock.tick(60)

main()


