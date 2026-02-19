import pygame
import sys
import os
from settings import *
from player import Player
from levels import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flatformer")
clock = pygame.time.Clock()

class World():
    def __init__(self, data):
        self.tile_list = []

        platform1_img = pygame.image.load("images/Platform_1.png")
        platform2_img = pygame.image.load("images/Platform_2.png")
        bg1_img = pygame.image.load("images/BG_1.png")

        
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(platform1_img, (TILE_SIZE, TILE_SIZE))
                elif tile == 2:
                    img = pygame.transform.scale(platform2_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                column_count += 1
            row_count += 1

player = Player()
world = World(level1_data)

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

def set_level(): 
    level += 1


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(world.bg1_img, (0, 0))

        print(world)

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


