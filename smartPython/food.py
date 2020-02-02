'''
Created on 2 lut 2020

@author: Warus
'''

import random
from smartPython import main, snake

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
        size = main.GUI.getSizeOfBoard()
        
        while True:
            newPosition = (random.randint(0, size), random.randint(0, size))
            if newPosition not in self.snake.snakeElements:
                print("Nowa pozycja", newPosition)
                return newPosition