import random
import pygame
from config import *
from tile import Tile


class Board:
    def __init__(self):
        self.tiles = [[Tile(x, y, tiles["empty"], "0") for x in range(rows)] for y in range(cols)]
        self.surface = pygame.Surface((width, height))
        self.place_mines()
        self.place_clues()
        self.dug = []
        
    def dig(self, x, y):
        self.dug.append((x, y))
        if self.tiles[y][x].type == "1":
            self.tiles[y][x].img = tiles["clicked-mine"]
            self.tiles[y][x].revealed = True
            return False
        elif self.tiles[y][x].type == "#":
            self.tiles[y][x].revealed = True
            return True
        self.tiles[y][x].revealed = True

        for row in range(max(0, x-1), min(rows-1, x+1) + 1):
            for col in range(max(0, y-1), min(cols-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def check_win(self):
        for row in self.tiles:
            for tile in row:
                if (tile.type == "1" and not tile.flagged) or (tile.type != "1" and tile.flagged):
                    return False
        return True


    def place_clues(self):
        for y in range(rows):
            for x in range(cols):
                if self.tiles[y][x].type == "0":
                    nr_mines = self.calculate_clues(x, y)
                    if nr_mines > 0:
                        self.tiles[y][x].type = "#"
                        self.tiles[y][x].img = tiles[str(nr_mines)]

    
    def calculate_clues(self, x, y):
        nr_mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < rows and 0 <= y + j < cols:
                    if self.tiles[y + j][x + i].type == "1":
                        nr_mines = nr_mines + 1
        return nr_mines
    
    
    def place_mines(self):
        for _ in range(mines):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            while self.tiles[y][x].type == "1":
                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            self.tiles[y][x].type = "1"
            self.tiles[y][x].img = tiles["mine"]

    def display(self):
        for row in self.tiles:
            print(row)

    def draw(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.surface)
        screen.blit(self.surface, (0, 0))