import os
import sys
from components import _image_library, get_image
#from player import Player
from random import randrange
import pygame
import pygame.locals
from tile_map import load_tile_table


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.move_y = 0
        self.fps = 0
        self.animation_cycles = 6
        self.player_images = []

        # Player model
        for i in range(1, 6):
            img = pygame.image.load(
                'models//heroes//knight//' + 'run' + str(i) + '.png').convert()
            img.convert_alpha()
            self.player_images.append(img)
            self.image = self.player_images[0]
            self.rect = self.image.get_rect()

    def movement(self, x, y):
        self.move_x += x
        self.move_y += y

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y

        if self.move_x < 0:
            self.fps += 1

            if self.fps > 3*self.animation_cycles:
                self.fps = 0
            self.image = self.player_images[self.fps//self.animation_cycles]
        
        if self.move_x > 0:
            self.fps += 1
            
            if self.fps > 3*self.animation_cycles:
                self.fps = 0
            self.image = self.player_images[(self.fps//self.animation_cycles)]

def main():
    # Initialize the screen and fill the background
    screen_size = screen_width, screen_height = 640, 480
    fps = 40
    animation_cycles = 4
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    done = False
    
    
    screen.fill((0, 0, 0))
    background = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA).convert()

    table = pygame.image.load('models//tiles//floor//floor_1.png')
    table_rect = table.get_rect(center=(250, 300))
    
    player = Player()
    player.rect.x = 0
    player.rect.y = 0
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 2
    
    pygame.key.set_repeat(10, 10)
    
    # Event loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.move_x -= 2
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.move_x += 2
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.move_y -= 2
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.move_y += 2
            
                
        screen.blit(table, table_rect)
        player.update()
        player_list.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
        
        
        
if __name__ == "__main__":
    main()
