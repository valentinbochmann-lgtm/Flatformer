import pygame
import sys
import os
from settings import *
from player import Player
from levels import *
from world import *

pygame.init()
pygame.display.set_caption("Flatformer")
clock = pygame.time.Clock()

bg1_img = pygame.image.load("images/BG_1.png")
bg1_img = pygame.transform.scale(bg1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_tuple = (bg1_img)


def set_level(): 
    level += 1

player = Player()
world = World()


def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg1_img, (0, 0))
        world.draw()

        player.move()
        player.draw(screen)
        
        for tile in world.tile_list:
            tile_rect = tile[1]
        
            if player.rect.colliderect(tile_rect):
                # Falling on top
                if player.prev_rect.bottom <= tile_rect.top:
                    player.rect.bottom = tile_rect.top
                    player.y = player.rect.y
                    player.velocity_y = 0
                    player.isOnGround = True

                # Hitting from below
                elif player.prev_rect.top >= tile_rect.bottom:
                    player.rect.top = tile_rect.bottom
                    player.y = player.rect.y
                    player.velocity_y = 0

                # Hitting from left
                elif player.prev_rect.right <= tile_rect.left:
                    player.rect.right = tile_rect.left
                    player.x = player.rect.x
                    player.velocity_x = 0

                # Hitting from right
                elif player.prev_rect.left >= tile_rect.right:
                    player.rect.left = tile_rect.right
                    player.x = player.rect.x
                    player.velocity_x = 0


        pygame.display.flip()
            
        clock.tick(60)

main()


