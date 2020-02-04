'''
Created on 2 lut 2020

@author: Warus
'''

import numpy as np
from smartPython import GUI


class Snake(object):
    '''
    Class for snake
    '''

    def __init__(self, main, length=3, maxStep=100):
        '''
        Create snake
        '''
        self.main = main
        
        # ## Temporary the length and starting position are fixed     
        self.length = length
        self.snakeElements = self.generateStartingSnake()
        
        self.velocity = (0, 0)  #### X, Y in range -1 to 1
        
        self.maxStep = maxStep
        self.steps = 0
        
        self.hasAte = False
        
    def generateStartingSnake(self):
        '''
        Generate new snake as long as it will be inside board
        '''
        x, y = (np.random.randint(0, GUI.getSizeOfBoard()), np.random.randint(0, GUI.getSizeOfBoard()))
        output = [(x, y)]
        
        for i in range(self.length - 1):
            while True:
                rand = np.random.rand()
                if rand > 0.5:
                    if rand > 0.75:
                        dx = 1
                    else:
                        dx = -1
                    if x + dx >= 0 and x + dx < GUI.getSizeOfBoard() and (x + dx, y) not in output:
                        x, y = x + dx, y
                        break
                else:
                    if rand > 0.25:
                        dy = 1
                    else:
                        dy = -1
                    if y + dy >= 0 and y + dy < GUI.getSizeOfBoard() and (x, y + dy) not in output:
                        (x, y) = (x, y + dy)
                        break
            output.append((x, y))
        
        return output
        
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
