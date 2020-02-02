'''
Created on 2 lut 2020

@author: Warus
'''

class Snake(object):
    '''
    Class for snake
    '''

    def __init__(self, length=3, startingPosition = (5,5)):
        '''
        Create snake
        '''
        ### Temporary the length and starting position are fixed
        self.length = 3
        self.position = (5,5)
        
        self.snakeElements = [startingPosition, (4,5), (3,5)]
        

            