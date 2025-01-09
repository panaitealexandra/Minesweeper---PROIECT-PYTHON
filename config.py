import pygame
import os

'''
In config.py sunt definite configuratiile generale ale jocului si se incarca imaginile utilizate pentru afisare.

'''


tile_size = 32 # dimensiunea standard a unei celule

# dimensiunile tablei si numarul de mine default
rows, cols = 15, 15
mines = 8
width, height = tile_size * rows, tile_size * cols

def load_img(image_folder, tile_size):

    '''
    Functia load_img incarca imaginile din folderul images si le redimensioneaza la dimensiunea tile_size.

    Argumente: 
        - image_folder: folderul in care se afla imaginile
        - tile_size: dimensiunea la care se redimensioneaza imaginile

    Returneaza un dictionar cu imaginile incarcate

    '''
    images = {}
    for i in range(1, 9):
        images[f"{i}"] = pygame.transform.scale(
            pygame.image.load(os.path.join(image_folder, f"{i}.png")), 
            (tile_size, tile_size)
        )

    images["empty"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "empty.png")), 
        (tile_size, tile_size)
    )
    images["clicked-mine"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "clicked-mine.png")), 
        (tile_size, tile_size)
    )
    images["flag"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "flag.png")), 
        (tile_size, tile_size)
    )
    images["mine"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "mine.png")), 
        (tile_size, tile_size)
    )
    images["unknown"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "unknown.png")), 
        (tile_size, tile_size)
    )
    images["not-mine"] = pygame.transform.scale(
        pygame.image.load(os.path.join(image_folder, "not-mine.png")), 
        (tile_size, tile_size)
    )

    return images

tiles = load_img("images", tile_size) # dictionarul cu imaginile incarcate

