import random
import pygame
from config import tiles
from config import tile_size
from tile import Tile

'''
Clasa Board este responsabila pentru gestionarea tablei de joc, plasarea minelor si a indiciilor.

'''


class Board:
    def __init__(self, rows, cols, mines):    
        '''
        Constructorul clasei Board initializeaza tabla de joc cu dimensiunile date si plaseaza minele pe tabla.   
        
        Argumente: rows, cols - dimensiunile tablei de joc, mines - numarul de mine.

        '''
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.tiles = [[Tile(x, y, tiles["empty"], "0") for x in range(self.cols)] for y in range(self.rows)]
        self.surface = pygame.Surface((rows * tile_size, cols * tile_size))
        self.place_mines()
        self.place_clues()
        self.dug = []

    
    def dig(self, x, y):
                
        '''
        Metoda dig este responsabila pentru dezvaluirea celulelor de pe tabla 
        si implementeaza logica flood fill pentru celulele goale.

        Argumente: x, y - coordonatele celulei de pe tabla.

        Returneaza: False daca celula este mina, True altfel.
        
        '''
        self.dug.append((x, y)) 
        if self.tiles[y][x].type == "1":
            self.tiles[y][x].img = tiles["clicked-mine"]
            self.tiles[y][x].revealed = True
            for row in self.tiles:
                for tile in row:
                    tile.revealed = True
            return False
        elif self.tiles[y][x].type == "#":
            self.tiles[y][x].revealed = True
            return True
        
        self.tiles[y][x].revealed = True

        for row in range(max(0, y - 1), min(self.rows, y + 2)):
            for col in range(max(0, x - 1), min(self.cols, x + 2)):
                if (col, row) not in self.dug:
                    self.dig(col, row)
        return True


    
    def check_win(self):

        '''
        Metoda check_win verifica daca jocul a fost castigat.

        Returneaza: True daca toate celulele tip mina sunt dezvaluite, False altfel.
        
        '''
        for row in self.tiles:
            for tile in row:
                if tile.type == "1" and not tile.flagged and not tile.revealed: 
                    return False
                if tile.type != "1" and not tile.revealed: 
                    return False
        return True


    def place_clues(self):
        '''
        Metoda place_clues plaseaza indiciile pe tabla de joc.

        '''   
        for y in range(self.rows):
            for x in range(self.cols):
                if self.tiles[y][x].type == "0":
                    nr_mines = self.calculate_clues(x, y)
                    if nr_mines > 0:
                        self.tiles[y][x].type = "#"
                        self.tiles[y][x].img = tiles[str(nr_mines)]

 
    
    def calculate_clues(self, x, y):
        '''
        Metoda calculate_clues calculeaza numarul de mine din jurul fiecarei celule.

        Argumente: x, y - coordonatele celulei de pe tabla.

        '''       
        nr_mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.cols and 0 <= y + j < self.rows:
                    if self.tiles[y + j][x + i].type == "1":
                        nr_mines = nr_mines + 1
        return nr_mines
    
    
    def place_mines(self):

        '''
        Metoda place_mines plaseaza minele pe tabla de joc.
        
        '''

        for _ in range(self.mines):
            x, y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)
            while self.tiles[y][x].type == "1":
                x, y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)
            self.tiles[y][x].type = "1"
            self.tiles[y][x].img = tiles["mine"]

    def display(self):

        '''
        Metoda display afiseaza tabla de joc.
        
        '''
        for row in self.tiles:
            print(row)

    def draw(self, screen):

        '''
        Metoda draw deseneaza tabla de joc pe ecran.
        
        Argumente: screen - ecranul pe care se deseneaza tabla de joc.
        '''
        self.surface.fill((211, 211, 211))  
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                tile.draw(self.surface, x * tile_size, y * tile_size)
        screen.blit(self.surface, (0, 0))