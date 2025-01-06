import pygame
from config import *
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
    
    def new(self):
        self.board = Board()
        self.board.display()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x = x // tile_size
                    y = y // tile_size
                    if not self.board.tiles[y][x].flagged:
                        if not self.board.dig(x, y):
                            for row in self.board.tiles:
                                for tile in row:
                                    if tile.flagged:
                                        if not tile.type == "1":
                                            tile.img = tiles["not-mine"]
                                            tile.flagged = False
                                            tile.revealed = True
                                        else:
                                            tile.revealed = True
                                self.playing = False
                elif event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    x = x // tile_size
                    y = y // tile_size
                    if not self.board.tiles[y][x].revealed:
                        self.board.tiles[y][x].flagged = not self.board.tiles[y][x].flagged   

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        pygame.display.flip()
