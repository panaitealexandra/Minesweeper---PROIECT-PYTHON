import pygame
from config import *

##class Tile 

#types of tiles
# 0 - empty
# 1 - mine
# # - clue
# * - unknown
class Tile:
    def __init__(self, x, y, img, type, revealed=False, flagged=False):
        self.x = x * tile_size
        self.y = y * tile_size
        self.img = img
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
    
    def __repr__(self):
        return f"{self.type}"
    
    def draw(self, surface):
        if self.revealed:
            surface.blit(self.img, (self.x, self.y))
        else:
            surface.blit(tiles["unknown"], (self.x, self.y))
            if self.flagged:
                surface.blit(tiles["flag"], (self.x, self.y))