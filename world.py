import pygame
import json
from settings import *

class World():
    def __init__(self, json_data):

        self.tile_list = []

        
        dirt1_img = pygame.image.load("images/dirt1.png").convert_alpha()
        dirt2_img = pygame.image.load("images/dirt2.png").convert_alpha()

        tile_size = worldGridSize
        
        for layer in json_data["layers"]:

            
            for tile in layer["tiles"]:

                tile_id = int(tile["id"])
                x = tile["x"] * tile_size
                y = tile["y"] * tile_size

                if tile_id == 0:
                    img = pygame.transform.scale(dirt1_img, (tile_size, tile_size))
                elif tile_id == 1:
                    img = pygame.transform.scale(dirt2_img, (tile_size, tile_size))
        

                img_rect = img.get_rect()
                img_rect.topleft = (x, y)

                self.tile_list.append((img, img_rect))

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

with open("levels/level1.json", "r") as f:
    map_data = json.load(f)

world = World(map_data)   # only if your JSON is wrapped in []