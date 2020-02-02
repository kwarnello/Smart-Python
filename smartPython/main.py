'''
Created on 2 lut 2020

@author: Warus
'''

import time

from smartPython import GUI, snake, food, moveController, score, neuralNetwork, info, \
    genetics


class Main():
    '''
    Main class handles everything
    '''
    SLEEPING_TIME = 5  # in millis
    
    running = True
    
    def __init__(self):
        '''
        Constructor
        '''
        self.mainFrame = GUI.MainFrame(self)
        self.score = score.Score()
        self.info = info.Info()
        self.NN = neuralNetwork.NN()
        self.geneticsController = genetics.Genetics(self.NN)

        # It has to be at the end on constructor
        self.mainFrame.startLoop()
        
    def initializeNewGame(self):
        '''
        After losing generate new stuff
        If there is new member get it. If not generate new population.
        Reset score, create new snake and so on.
        '''
        
        if not self.geneticsController.isNextMember():
            self.geneticsController.newGeneration()
            
        member = self.geneticsController.getNextMember()
        
        self.NN.setNewWeights(member.weights)
        
        self.snake = snake.Snake(self)
        self.food = food.Food(self.snake)
        
        self.score.newGame()
        self.controller = moveController.Controller(self)

    def startMainLoop(self):
        '''
        Main loop. Firstly get inputs info, then predict decison and make decision by snake.
        '''
        inputs = self.info.getAllInfo(self.snake, self.food.position)
        decision = self.NN.predict(inputs)
        
        self.snake.update(decision)
        self.mainFrame.update()
        time.sleep(self.SLEEPING_TIME / 1000)
        self.startMainLoop()
