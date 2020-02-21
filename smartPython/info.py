'''
Created on 2 lut 2020

@author: Warus
'''
from smartPython.GUI import getSizeOfBoard
import numpy as np


class Info(object):
    '''
    Get information about surrounding of snake. There is 4 rays that will give information about distance to wall or snake (depending what if closer).
    As 5th parameter the vector to the food is shown.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.sizeOfBoard = getSizeOfBoard()

    def getAllInfo(self, snake, foodCoords):
        '''
        Inputs as follows: first distance (normalized between 0 and size of board), second snake, third wall.
        0 - North, 1 - South, 2 - West, 3 - East, 4-7 - vector to the food
        Distance is squared to get bigger impact for closer walls
        '''
        
        inputs = np.zeros([1, 8])
        
        snakePosition = snake.snakeElements
        x, y = snakePosition[0]
        
        # North
        n = -1
        for i in np.arange(y - 1, -1, -1):
            if (x, i) in snakePosition:
                n = (1 - (y - i - 1) / self.sizeOfBoard) ** 3
                break
        if n == -1:
            n = (1 - (y / self.sizeOfBoard)) ** 3
        inputs[0][0] = n

        # South
        s = -1
        for i in range(y + 1, self.sizeOfBoard + 1):
            if (x, i) in snakePosition:
                s = (1 - (i - y - 1) / self.sizeOfBoard) ** 3
                break
        if s == -1:
            s = (1 - (self.sizeOfBoard - y - 1) / self.sizeOfBoard) ** 3
        inputs[0][1] = s

        # West
        w = -1
        for i in range(x - 1, -1, -1):
            if (i, y) in snakePosition:
                w = (1 - (x - i - 1) / self.sizeOfBoard) ** 3
                break
        if w == -1:
            w = (1 - (x / self.sizeOfBoard)) ** 3
        inputs[0][2] = w

        # East
        e = -1
        for i in range(x + 1, self.sizeOfBoard + 1):
            if (i, y) in snakePosition:
                e = (1 - (i - x - 1) / self.sizeOfBoard) ** 3
                break
        if e == -1:
            e = (1 - (self.sizeOfBoard - x - 1) / self.sizeOfBoard) ** 3
        inputs[0][3] = e

        # Food
        xF, yF = foodCoords
        if xF < x:
            inputs[0][4] = 1 - (x - xF) / self.sizeOfBoard
        elif xF > x:
            inputs[0][5] = 1 - (xF - x) / self.sizeOfBoard
            
        if yF < y:
            inputs[0][6] = 1 - (y - yF) / self.sizeOfBoard
        elif yF > y:
            inputs[0][7] = 1 - (yF - y) / self.sizeOfBoard
            
        return inputs
