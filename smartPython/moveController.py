'''
Created on 2 lut 2020

@author: Warus
'''

import keyboard


class Controller(object):
    '''
    classdocs
    '''

    def __init__(self, main):
        '''
        Constructor
        '''
        self.main = main
        
        self.gameStartsInitialize()
        
    def gameStartsInitialize(self):
        '''
        Initialize keyboard inputs after "New game" button is pressed
        '''
        keyboard.add_hotkey('w', self.main.snake.changeVelocity, args=((0, 1)))
        keyboard.add_hotkey('s', self.main.snake.changeVelocity, args=((0, -1)))
        keyboard.add_hotkey('a', self.main.snake.changeVelocity, args=((-1, 0)))
        keyboard.add_hotkey('d', self.main.snake.changeVelocity, args=((1, 0)))
