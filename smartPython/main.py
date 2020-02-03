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
    SLEEPING_TIME = 0  # in millis
    
    running = True
    
    ### Temporary var for measure of time for debugging
    time_nn = 0
    time_snake = 0
    time_newGame = 0
    time_graphics = 0
    newGameCounter = 0
    
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
        self.newGameCounter += 1
        start = time.time()

        if not self.geneticsController.isNextMember():
            # self.geneticsController.newGeneration()
            self.geneticsController = genetics.Genetics(self.NN)  # ## temporary just get new pop

        member = self.geneticsController.getNextMember()
        
        self.NN.setNewWeights(member.weights)
        
        self.snake = snake.Snake(self)
        self.food = food.Food(self.snake)
        
        self.score.newGame()
        # self.controller = moveController.Controller(self)
        self.time_newGame += (time.time() - start)
        
        self.printRaport()

    def startMainLoop(self):
        '''
        Main loop. Firstly get inputs info, then predict decison and make decision by snake.
        '''
        start = time.time()
        inputs = self.info.getAllInfo(self.snake, self.food.position)
        decision = self.NN.predict(inputs)
        self.time_nn += (time.time() - start)
        
        start = time.time()
        self.snake.update(decision)
        self.time_snake += (time.time() - start)
        
        start = time.time()
        self.mainFrame.update()
        self.time_graphics += (time.time() - start)

        time.sleep(self.SLEEPING_TIME / 1000)
        self.startMainLoop()
        
    def printRaport(self):
        print("NN times ", self.time_nn / self.newGameCounter)
        print("Graphics times ", self.time_graphics / self.newGameCounter)
        print("Snake times ", self.time_snake / self.newGameCounter)
        print("New game times ", self.time_newGame / self.newGameCounter)

