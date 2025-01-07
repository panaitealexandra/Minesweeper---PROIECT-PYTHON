import pygame
from config import *
from game import Game
from menu import Menu

if __name__ == "__main__":

    menu = Menu()
    menu.run()

    rows, cols = menu.width, menu.height
    mines = menu.mines
    width, height = rows * tile_size, cols * tile_size
    game = Game(menu.width, menu.height, menu.mines)
    game.new()
    game.run()