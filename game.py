import pygame
from config import tiles
from config import tile_size
from board import Board
from menu import Menu

class Game:
    def __init__(self, width, height, mines):
        pygame.init()
        self.width = width
        self.height = height
        self.mines = mines
        self.screen = pygame.display.set_mode((width * tile_size, height * tile_size + 50))  
        pygame.display.set_caption("Minesweeper Game")
        self.clock = pygame.time.Clock()
        self.start_time = None  
        self.font_size = max(12, min(24, (self.width * tile_size) // 10))
        self.font = pygame.font.SysFont("Comic Sans MS", self.font_size)  
    
    def new(self):
        self.board = Board(self.width, self.height, self.mines)
        self.start_time = pygame.time.get_ticks()  
        self.board.display()


    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            self.clock.tick(30) 

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
        overlay = pygame.Surface((self.width * tile_size, self.height * tile_size))
        overlay.set_alpha(128)  
        overlay.fill((0, 0, 255))  


        font_size = max(24, min(48, (self.width * tile_size) // 10))
        font = pygame.font.SysFont("Comic Sans MS", font_size)
        rendered_lines = []
        for idx, line in enumerate(message.split("\n")):
            text = font.render(line, True, (255, 255, 255)) 
            text_rect = text.get_rect(center=(
                (self.width * tile_size) // 2,  
                (self.height * tile_size) // 3 + idx * (font_size + 10)  
            ))
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
                        menu = Menu()
                        menu.run()
                        rows, cols = menu.width, menu.height
                        mines = menu.mines
                        width, height = rows * tile_size, cols * tile_size
                        game = Game(menu.width, menu.height, menu.mines)
                        game.new()
                        game.run()
                    elif event.key == pygame.K_q:  
                        pygame.quit()
                        quit()  


    def draw(self):
        self.screen.fill((211, 211, 211))
        self.board.draw(self.screen)

        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000  
        timer_text = self.font.render(f"Time: {elapsed_time} sec", True, (0,0,0))
        self.screen.blit(timer_text, (10, self.height * tile_size + 10))  

        pygame.display.flip()
  