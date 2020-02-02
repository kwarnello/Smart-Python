'''
Created on 2 lut 2020

@author: Warus
'''


class Snake(object):
    '''
    Class for snake
    '''

    def __init__(self, length=3, startingPosition=(5, 5)):
        '''
        Create snake
        '''
        # ## Temporary the length and starting position are fixed
        self.length = 3
        self.position = (5, 5)
        
        self.velocity = (0, 0)  #### X, Y in range -1 to 1
        
        self.snakeElements = [self.position, (4, 5), (3, 5)]
            
    def changeVelocity(self, x, y):
        self.velocity = (x, y)
        print(self.velocity)

    def update(self):
        if self.velocity != (0, 0):
            self.snakeElements.pop()
            newElement = tuple([sum(x) for x in zip(self.snakeElements[0], self.velocity)])
            print(newElement)
            self.snakeElements.insert(0, newElement)
            print(self.snakeElements)
