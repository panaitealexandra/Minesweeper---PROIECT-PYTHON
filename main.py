import pygame
from config import *
from game import Game


if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()