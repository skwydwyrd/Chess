import pygame

class Player():
    def __init__(self,color):
        self.color = color
        self.turn = self.color == 'white'
        self.in_check = False
        self.checkmated = False

        
    def set_turn(self,turn_state):
        self.turn= turn_state

        
