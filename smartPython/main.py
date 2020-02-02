'''
Created on 2 lut 2020

@author: Warus
'''

import time

from smartPython import GUI, snake, food, moveController


class Main():
    '''
    Main class handles everything
    '''
    SLEEPING_TIME = 200  # # in millis
    
    running = True
    
    def __init__(self):
        '''
        Constructor
        '''
        self.mainFrame = GUI.MainFrame(self)
        self.mainFrame.startLoop()
        
    def initializeNewGame(self):
        self.snake = snake.Snake(self)
        self.food = food.Food(self.snake)
        self.controller = moveController.Controller(self)
        
    def startMainLoop(self):
        self.snake.update()
        self.mainFrame.update()
        time.sleep(self.SLEEPING_TIME / 1000)
        self.startMainLoop()
