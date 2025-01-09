import pygame
from config import tiles
from config import tile_size
from board import Board
from menu import Menu

'''
Clasa game.py contine logica principala a jocului, incluzând gestionarea evenimentelor, 
afisarea grafica si verificarea castigului.

Atribute:
    - width, height: dimensiunile tablei de joc
    - mines: numarul de mine de pe tabla
    - screen: suprafata de afisare
    - clock: obiectul pentru gestionarea timpului
    - start_time: timpul de inceput al jocului
    - font_size: dimensiunea fontului pentru afisarea timpului
    - font: fontul pentru afisarea timpului

'''

class Game:
    def __init__(self, width, height, mines):

        '''
        Constructorul clasei Game initializeaza tabla de joc si seteaza dimensiunile si numarul de mine.

        Argumente: width, height - dimensiunile tablei de joc, mines - numarul de mine.
        
        '''

        pygame.init()
        self.width = width
        self.height = height
        self.mines = mines
        self.screen = pygame.display.set_mode((self.width * tile_size, self.height * tile_size + 50))
        pygame.display.set_caption("Minesweeper Game")
        self.clock = pygame.time.Clock()
        self.start_time = None  
        self.font_size = max(12, min(24, (self.width * tile_size) // 10))
        self.font = pygame.font.SysFont("Comic Sans MS", self.font_size)  
    

    def new(self):
        '''
        Metoda new creeaza o tabla noua si initializeaza starea jocului.
        
        '''
        self.board = Board(self.width, self.height, self.mines)
        self.start_time = pygame.time.get_ticks()  
        self.board.display()

    
    def run(self):
        '''
        Metoda run reprezinta bucla principala a jocului. Afiseaza tabla si gestioneaza evenimentele.

        '''
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            self.clock.tick(30) 
    
    def events(self):
        '''
        Metoda events gestioneaza inputul utilizatorului cu ajutorul tastaturii.
        
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

            '''
            Se verifica daca s-a apasat click stanga sau dreapta si se gestioneaza actiunea.
            Daca s-a apasat click stanga si celula este mina, se dezvaluie toate celulele si se afiseaza mesajul de final.

            '''
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = x // tile_size
                y = y // tile_size
                if event.button == 1:
                    
                    if not self.board.tiles[y][x].flagged:
                        if not self.board.dig(x, y):
                            for row in self.board.tiles:
                                for tile in row:
                                    if tile.flagged:
                                        if not tile.type == "1":
                                            tile.img = tiles["not-mine"]
                                            tile.flagged = False
                                            tile.revealed = True
                            self.game_over("You lost!\nR - Restart\nQ - Quit")  
                            self.playing = False

                elif event.button == 3:
                    if not self.board.tiles[y][x].revealed:
                        self.board.tiles[y][x].flagged = not self.board.tiles[y][x].flagged   
                        if self.board.check_win():
                            self.playing = False
                            self.game_over("You won!\nR - Restart\nQ - Quit")  


    def game_over(self, message):
        '''
        Metoda game_over afiseaza mesajul de final si gestioneaza inputul utilizatorului folosind tastatura.

        Argumente: message - mesajul afisat la finalul jocului.

        ''' 
        for row in self.board.tiles:
            for tile in row:
                tile.revealed = True

        self.draw() 
        pygame.display.flip()  

        overlay = pygame.Surface((self.width * tile_size, self.height * tile_size))
        overlay.set_alpha(128)  
        overlay.fill((0, 0, 255))  

        '''
        se afiseaza mesajul de final si se asteapta inputul utilizatorului.

        '''

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
        '''
        Metoda draw deseneaza starea curenta a jocului.
        
        '''
        self.screen.fill((211, 211, 211))
        self.board.draw(self.screen)

        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000  
        timer_text = self.font.render(f"Time: {elapsed_time} sec", True, (0,0,0))
        self.screen.blit(timer_text, (10, self.height * tile_size + 10))  

        pygame.display.flip()
  