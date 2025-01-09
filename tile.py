import pygame
from config import *

''''
Clasa Tile defineste comportamentul si reprezentarea grafica a celulelor de pe tabla de joc.

Atribute:
    - x, y: coordonatele celulei pe tabla
    - img: imaginea afisata pentru celula
    - type: tipul celulei (mina, indiciu, celula goala)
    - revealed: daca celula este dezvaluita
    - flagged: daca celula este marcata cu un steag

''' 

#types of tiles
# 0 - empty
# 1 - mine
# # - clue
# * - unknown

class Tile:
    def __init__(self, x, y, img, type, revealed=False, flagged=False):

        '''
        Constructorul clasei Tile initializeaza o celula de pe tabla de joc.

        Argumente: x, y - coordonatele celulei pe tabla, img - imaginea afisata pentru celula,
        
        '''
    
        self.x = x * tile_size
        self.y = y * tile_size
        self.img = img
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
    
    def __repr__(self):
        return f"{self.type}"
    
    def draw(self, surface, x, y):

        '''
        Metoda draw deseneaza celula pe suprafata data la coordonatele x, y.
        
        Argumente: surface - suprafata de desenare, x, y - coordonatele celulei pe ecran.

        '''
        surface.blit(self.img, (x, y))
        if self.revealed:
            surface.blit(self.img, (self.x, self.y))
        else:
            surface.blit(tiles["unknown"], (self.x, self.y))
            if self.flagged:
                surface.blit(tiles["flag"], (self.x, self.y))