'''
Created on 2 lut 2020

@author: Warus
'''

import random

from smartPython import main


class Food(object):
    '''
    Class for gainer for snake
    '''

    def __init__(self, snake):
        '''
        Constructor
        '''
        self.snake = snake
        
        self.position = self.generatePosition()
        
    def generatePosition(self):
        '''
        Generate new food and check if that food is not inside the snake
        '''
        size = main.GUI.getSizeOfBoard() - 1
        
        while True:
            newPosition = (random.randint(0, size), random.randint(0, size))
            if newPosition not in self.snake.snakeElements:
                return newPosition
    
    def ate(self, newElement):
        if newElement == self.position:
            self.position = self.generatePosition()
            return True
        else:
            return False
