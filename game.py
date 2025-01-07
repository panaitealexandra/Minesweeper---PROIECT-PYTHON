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
                                self.game_over("You lost!\nR - Restart\nQ - Quit")  

                elif event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    x = x // tile_size
                    y = y // tile_size
                    if not self.board.tiles[y][x].revealed:
                        self.board.tiles[y][x].flagged = not self.board.tiles[y][x].flagged   
                        if self.board.check_win():
                            self.playing = False
                            self.game_over("You won!\nR - Restart\nQ - Quit")  


    def game_over(self, message):
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(128)  
        overlay.fill((0, 0, 0))  


        font = pygame.font.SysFont("Verdana", 48)  
        rendered_lines = []
        for idx, line in enumerate(message.split("\n")):
            text = font.render(line, True, (255, 255, 255)) 
            text_rect = text.get_rect(center=(width // 2, height // 3 + idx * 50))
            rendered_lines.append((text, text_rect))

        self.screen.blit(overlay, (0, 0))
        for text, rect in rendered_lines:
            self.screen.blit(text, rect)

        pygame.display.flip()  

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  
                        self.new()
                        self.run()
                    elif event.key == pygame.K_q:  
                        pygame.quit()
                        quit()  


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        pygame.display.flip()
  