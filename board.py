import pygame
from settings import *
class Board():
    def __init__(self):
        self.size=board_size
        self.dark_brown=(170, 98, 23)
        self.light_brown=(235, 140, 80)
    def draw(self,WIN):
        for row in range(self.size):
            for col in range(self.size):
                if (row+col)%2==0:
                    pygame.draw.rect(WIN, self.light_brown, (col * square_size, row * square_size, square_size, square_size))
                else:
                    pygame.draw.rect(WIN, self.dark_brown, (col * square_size, row * square_size, square_size, square_size))

