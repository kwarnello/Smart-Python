'''
Created on 2 lut 2020

@author: Warus
'''


class Snake(object):
    '''
    Class for snake
    '''

    def __init__(self, main, length=3, startingPosition=(5, 5)):
        '''
        Create snake
        '''
        self.main = main
        
        # ## Temporary the length and starting position are fixed     
        self.length = 3
        self.position = (5, 5)
        
        self.velocity = (0, 0)  #### X, Y in range -1 to 1
        
        self.hasAte = False
        self.gameOver = False
        
        self.snakeElements = [self.position, (4, 5), (3, 5)]
            
    def changeVelocity(self, x, y):
        '''
        If the button that can be interpreted as 'backward' do nothing
        else change velocity
        '''
        if self.velocity[0] + x == 0 and self.velocity[1] + y == 0:
            return
        self.velocity = (x, y)

    def update(self):
        '''
        Update snake every frame.
        Firstly check if hit the food.
        Next move it
        '''
        if self.velocity != (0, 0):
            if not self.hasAte:
                self.snakeElements.pop()
            newElement = tuple([sum(x) for x in zip(self.snakeElements[0], self.velocity)])
            self.snakeElements.insert(0, newElement)
            
            self.checkLogic(newElement)
            
    def checkLogic(self, newElement):
        '''
        Check if snake got some snacks or bites itself
        '''
        self.hasAte = False
        self.gameOver = False
        
        if self.main.food.ate(newElement):
            self.hasAte = True
        elif self.checkIfGameOver(newElement):
            self.gameOver = True
            self.main.initializeNewGame()
            
    def checkIfGameOver(self, newElement):
        size = self.main.mainFrame.getSizeOfBoard() - 1
        
        result = False
        x, y = newElement
        if (x > size or x < 0):
            result = True
        elif (y > size or y < 0):
            result = True
        elif newElement in self.snakeElements[1:]:
            result = True

        return result
