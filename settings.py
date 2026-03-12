import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
worldGridSize = 50
GRAVITY = 0.4
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#load images
dirt1_img = pygame.image.load("images/dirt1.png").convert_alpha()
dirt2_img = pygame.image.load("images/dirt2.png").convert_alpha()
dirt3_img = pygame.image.load("images/dirt3.png").convert_alpha()
darkstone_img = pygame.image.load("images/dark_stone.png").convert_alpha()
enemy_img = pygame.image.load("images/enemy.png").convert_alpha()
restart_img = pygame.image.load("images/restart_button.png").convert_alpha()

#background images
bg1_img = pygame.image.load("images/bg1.png")
bg1_img = pygame.transform.scale(bg1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_list = [bg1_img]


