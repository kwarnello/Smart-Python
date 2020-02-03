'''
Created on 2 lut 2020

@author: Warus
'''


class Snake(object):
    '''
    Class for snake
    '''

    def __init__(self, main, length=4, startingPosition=(5, 5), maxStep=500):
        '''
        Create snake
        '''
        self.main = main
        
        # ## Temporary the length and starting position are fixed     
        self.length = 3
        self.position = (5, 5)
        
        self.velocity = (0, 0)  #### X, Y in range -1 to 1
        
        self.maxStep = maxStep
        self.steps = 0
        
        self.hasAte = False
        
        self.snakeElements = [self.position, (4, 5), (4, 4), (5, 4)]
        
    def changeVelocity(self, x, y):
        '''
        If the button that can be interpreted as 'backward' do nothing
        else change velocity
        '''
        if self.velocity[0] + x == 0 and self.velocity[1] + y == 0:
            return
        self.velocity = (x, y)

    def update(self, decision):
        '''
        Update snake every frame.
        Firstly check if hit the food.
        Next move it
        '''
        self.steps += 1
        if self.steps >= self.maxStep:
            self.gameOver()
        
        self.makeVelocityDecision(decision)
        # print(decision)
        if self.velocity != (0, 0):
            if not self.hasAte:
                self.snakeElements.pop()
            newElement = tuple([sum(x) for x in zip(self.snakeElements[0], self.velocity)])
            self.snakeElements.insert(0, newElement)
            
            self.checkLogic(newElement)
            
    def makeVelocityDecision(self, decision):
        '''
        Based on prediction from NN change velocity
        '''
        index = decision.argmax()
        if index == 0:
            self.changeVelocity(0, -1)
        if index == 1:
            self.changeVelocity(0, 1)
        if index == 2:
            self.changeVelocity(-1, 0)
        if index == 3:
            self.changeVelocity(1, 0)
            
    def checkLogic(self, newElement):
        '''
        Check if snake got some snacks or bites itself
        '''
        self.hasAte = False
        
        if self.main.food.ate(newElement):
            self.hasAte = True
            self.main.score.addScore()
        elif self.checkIfGameOver(newElement):
            self.gameOver()
            
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
    
    def gameOver(self):
        self.main.initializeNewGame()
