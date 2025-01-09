import pygame
from config import *
from game import Game
from menu import Menu
''' 
Minesweeper: Implementare in Python folosind Pygame

Acest joc Minesweeper este implementat in Python utilizand biblioteca Pygame. 

Module si fisiere:
------------------
1. **main.py**: Punctul de intrare al aplicatiei.
2. **config.py**: Configuratiile generale si incărcarea resurselor.
3. **menu.py**: Clasa pentru meniul principal.
4. **game.py**: Clasa principala pentru logica jocului.
5. **board.py**: Clasa pentru gestionarea tablei de joc.
6. **tile.py**: Clasa pentru reprezentarea fiecarei celule de pe tabla.

''' 
if __name__ == "__main__":

    #initializare meniu
    menu = Menu()
    menu.run()

    #preluarea dimensiunilor si numarului de mine
    rows, cols = menu.width, menu.height
    mines = menu.mines
    width, height = rows * tile_size, cols * tile_size

    #intializarea jocului
    game = Game(menu.width, menu.height, menu.mines)
    game.new()
    game.run()