'''
Created on 2 lut 2020

@author: Warus
'''

from smartPython import GUI, snake, food, moveController

class Main():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.GUI = GUI.MainFrame(self)
        
        
    def initializeNewGame(self):
        self.snake = snake.Snake()
        self.food = food.Food(self.snake)
        self.moveController = moveController.Controller(self)
