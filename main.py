from components import _image_library, get_image
from random import randrange
import pygame
import pygame.locals
from tile_map import load_tile_table

def main():
    # Initialize the screen
    pygame.init()
    screen_size = screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    
    # Fill the background
    background = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    background = background.convert()
    table = load_tile_table('testing_tileset.png', 64, 48)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*17, y*17))
    pygame.display.flip()
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
