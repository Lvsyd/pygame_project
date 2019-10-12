import pygame
import math

class Entity:
    def __init__(self, x, y, char, name):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        
        if self.char:
            self.char.owner = self
            
        if self.name:
            self.name.owner = self
            
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        
    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)