'''
Created on 2 lut 2020

@author: Warus
'''

from smartPython import GUI, snake, food

class Main():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.snake = snake.Snake()
        self.food = food.Food(self.snake)
        self.GUI = GUI.MainFrame(self)
        