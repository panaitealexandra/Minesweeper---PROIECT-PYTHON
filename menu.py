import random
import pygame
from config import *

##class Menu


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.width = rows
        self.height = cols
        self.mines = mines
        self.active_field = 0  
        self.error_message = None  

    def run(self):
        while self.running:
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                elif event.key == pygame.K_s:
                    if self.mines > self.width * self.height:
                        self.error_message = "Too many mines! Reduce the count."
                    else:
                        self.running = False  
                        return

                elif event.key == pygame.K_UP:
                    self.active_field = (self.active_field - 1) % 3  
                elif event.key == pygame.K_DOWN:
                    self.active_field = (self.active_field + 1) % 3  
                
                elif event.key == pygame.K_BACKSPACE:
                    if self.active_field == 0 and self.width > 0:
                        self.width = self.width // 10
                    elif self.active_field == 1 and self.height > 0:
                        self.height = self.height // 10
                    elif self.active_field == 2 and self.mines > 0:
                        self.mines = self.mines // 10
                
                elif event.unicode.isdigit():
                    digit = int(event.unicode)
                    if self.active_field == 0:
                        self.width = self.width * 10 + digit
                    elif self.active_field == 1:
                        self.height = self.height * 10 + digit
                    elif self.active_field == 2:
                        self.mines = self.mines * 10 + digit

    def draw(self):
        self.screen.fill((147, 112, 219))
        font = pygame.font.SysFont("Comic Sans MS", 32)
        small_font = pygame.font.SysFont("Comic Sans MS", 24)

        fields = [f"width - {self.width}",
                  f"height - {self.height}",
                  f"mines - {self.mines}"]

        for i, field in enumerate(fields):
            color = (255, 255, 255) if i == self.active_field else (200, 200, 200)
            text = font.render(field, True, color)
            self.screen.blit(text, (width // 2 - text.get_width() // 2, height // 3 + i * 50))

        quit_text = small_font.render("Q - Quit", True, (255, 255, 255))
        start_text = small_font.render("S - Start", True, (255, 255, 255))
        self.screen.blit(quit_text, (50, height - 50))
        self.screen.blit(start_text, (width - start_text.get_width() - 50, height - 50))

        if self.error_message:
            error_text = small_font.render(self.error_message, True, (255, 0, 0))
            self.screen.blit(error_text, (width // 2 - error_text.get_width() // 2, height - 100))

        pygame.display.flip()
        self.clock.tick(30)
