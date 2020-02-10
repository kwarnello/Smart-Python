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
        
        Dummy inputs creation
        '''
        
        inputs = np.zeros([1, 8])
        
        snakePosition = snake.snakeElements
        x, y = snakePosition[0]
        
        # North
        n = []
        for i in np.arange(y - 1, -1, -1):
            if (x, i) in snakePosition:
                dist = 1 - (i - y) / self.sizeOfBoard
                n = [abs(dist), 1, 0]
                break
        if len(n) == 0:
            n = [y / self.sizeOfBoard, 0, 1]
        inputs[0][0] = n[0]

        # South
        s = []
        for i in range(y + 1, self.sizeOfBoard + 1):
            if (x, i) in snakePosition:
                dist = 1 - (i - y) / self.sizeOfBoard
                s = [abs(dist), 1, 0]
                break
        if len(s) == 0:
            s = [(self.sizeOfBoard - y) / self.sizeOfBoard, 0, 1]
        inputs[0][1] = s[0]

        # West
        w = []
        for i in range(x, 0, -1):
            if (i, y) in snakePosition:
                dist = 1 - (x - i) / self.sizeOfBoard
                w = [abs(dist), 1, 0]
                break
        if len(w) == 0:
            w = [x / self.sizeOfBoard, 0, 1]
        inputs[0][2] = w[0]

        # East
        e = []
        for i in range(x + 1, self.sizeOfBoard + 1):
            if (i, y) in snakePosition:
                dist = 1 - (x - i) / self.sizeOfBoard
                e = [abs(dist), 1, 0]
                break
        if len(e) == 0:
            e = [(self.sizeOfBoard - x) / self.sizeOfBoard, 0, 1]
        inputs[0][3] = e[0]

        # Food
        xF, yF = foodCoords
        if xF < x:
            inputs[0][4] = 1 - ((x - xF) / self.sizeOfBoard)
        elif xF > x:
            inputs[0][5] = 1 - ((xF - x) / self.sizeOfBoard)
        if yF < y:
            inputs[0][6] = 1 - ((y - yF) / self.sizeOfBoard)
        elif yF > y:
            inputs[0][7] = 1 - ((yF - y) / self.sizeOfBoard)
            
        return inputs
