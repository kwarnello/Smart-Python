'''
Created on 2 lut 2020

@author: Warus
'''

from smartPython import GUI, snake

class Main():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.snake = snake.Snake()
        self.GUI = GUI.MainFrame(self)
        