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
        0-2 - North, 3-5 - South, 6-8 - West, 9-11 - East, 12-13 - vector to the food
        
        Dummy inputs creation
        '''
        
        inputs = np.zeros([1, 14])
        
        snakePosition = snake.snakeElements
        x, y = snakePosition[0]
        
        # North
        n = []
        for i in np.arange(y - 1, -1, -1):
            if (x, i) in snakePosition:
                dist = (i - y) / self.sizeOfBoard
                n = [dist, 1, 0]
                break
        if len(n) == 0:
            n = [y / self.sizeOfBoard, 0, 1]
        inputs[0][0] = n[0]
        inputs[0][1] = n[1]
        inputs[0][2] = n[2]

        # South
        s = []
        for i in range(y + 1, self.sizeOfBoard + 1):
            if (x, i) in snakePosition:
                dist = (y - i) / self.sizeOfBoard
                s = [dist, 1, 0]
                break
        if len(s) == 0:
            s = [(self.sizeOfBoard - y) / self.sizeOfBoard, 0, 1]
        inputs[0][3] = s[0]
        inputs[0][4] = s[1]
        inputs[0][5] = s[2]

        # West
        w = []
        for i in range(0, x):
            if (i, y) in snakePosition:
                dist = (x - i) / self.sizeOfBoard
                w = [dist, 1, 0]
                break
        if len(w) == 0:
            w = [x / self.sizeOfBoard, 0, 1]
        inputs[0][6] = w[0]
        inputs[0][7] = w[1]
        inputs[0][8] = w[2]

        # East
        e = []
        for i in range(x + 1, self.sizeOfBoard + 1):
            if (i, y) in snakePosition:
                dist = (i - x) / self.sizeOfBoard
                e = [dist, 1, 0]
                break
        if len(e) == 0:
            e = [(self.sizeOfBoard - x) / self.sizeOfBoard, 0, 1]
        inputs[0][9] = e[0]
        inputs[0][10] = e[1]
        inputs[0][11] = e[2]

        # Food
        inputs[0][12] = (foodCoords[0] - x) / self.sizeOfBoard
        inputs[0][13] = (foodCoords[1] - y) / self.sizeOfBoard
        
        return inputs
