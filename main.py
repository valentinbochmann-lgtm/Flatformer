import pygame
import sys
from settings import *
from player import Player
from levels import LevelManager
from button import Button

pygame.init()
pygame.display.set_caption("Flatformer")
clock = pygame.time.Clock()

level_manager = LevelManager()
world = level_manager.load_current()
player = Player(250, 650)
restart_button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, restart_img)

def main():
    global world, player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # temporary: press N to go to next level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and level_manager.has_next():
                    world = level_manager.next_level()
                    player = Player(250, 650)

        screen.blit(bg1_img, (0, 0))
        world.draw(screen)

        player.move()
        player.draw(screen)
        restart_button.draw(screen)

        player.isOnGround = False

        for tile in world.tile_list:
            tile_rect = tile[1]
            if player.rect.colliderect(tile_rect):
                if player.prev_rect.bottom <= tile_rect.top:
                    player.rect.bottom = tile_rect.top
                    player.y = player.rect.y
                    player.velocity_y = 0
                    player.isOnGround = True
                elif player.prev_rect.top >= tile_rect.bottom:
                    player.rect.top = tile_rect.bottom
                    player.y = player.rect.y
                    player.velocity_y = 0
                elif player.prev_rect.right <= tile_rect.left:
                    player.rect.right = tile_rect.left
                    player.x = player.rect.x
                    player.velocity_x = 0
                elif player.prev_rect.left >= tile_rect.right:
                    player.rect.left = tile_rect.right
                    player.x = player.rect.x
                    player.velocity_x = 0

        pygame.display.flip()
        clock.tick(60)

main()