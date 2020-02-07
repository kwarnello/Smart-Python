'''
Created on 2 lut 2020

@author: Warus
'''

import pickle
import time

from smartPython import GUI, snake, food, moveController, score, neuralNetwork, info, \
    genetics, bestWeights


class Main():
    '''
    Main class handles everything
    '''
    SLEEPING_TIME = 0  # in millis
    
    running = True
    
    # ## Temporary var for measure of time for debugging
    time_nn = 0
    time_snake = 0
    time_newGame = 0
    time_graphics = 0
    newGameCounter = 0
    generation = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        self.mainFrame = GUI.MainFrame(self)
        self.score = score.Score()
        self.info = info.Info()
        self.NN = neuralNetwork.NN()
        self.loadGame = False
        
        try:
            with open('model.pickle', 'rb') as f:
                self.geneticsController = pickle.load(f)
                print("Załadowałem")
        except FileNotFoundError:
            self.geneticsController = genetics.Genetics()
            
        try:
            with open('best.pickle', 'rb') as f:
                self.best = pickle.load(f)
        except FileNotFoundError:
            self.best = bestWeights.Best()

        # It has to be at the end on constructor
        self.mainFrame.startLoop()
        
    def initializeNewGame(self):
        '''
        After losing generate new stuff
        If there is new member get it. If not generate new population.
        Reset score, create new snake and so on.
        If load game just load best snakes one after one.
        '''
        if self.loadGame:
            self.loadBestSnakes()
        else:
            self.generation = self.geneticsController.generationCounter
            self.newGameCounter += 1
            start = time.time()
            
            if self.newGameCounter != 1:
                self.geneticsController.putScore(self.score.getScore())
    
            if not self.geneticsController.isNextMember():
                self.best.saveNextGeneration(self.geneticsController.getBestMember())
                self.geneticsController.newGeneration()
                self.printRaport()
                self.save()
    
            member = self.geneticsController.getNextMember()
            
            self.NN.setNewWeights(member.weights)
            
            self.snake = snake.Snake(self)
            self.food = food.Food(self.snake)
            
            self.score.newGame()
            # self.controller = moveController.Controller(self)
            self.time_newGame += (time.time() - start) 

    def startMainLoop(self):
        '''
        Main loop. Firstly get inputs info, then predict decison and make decision by snake.
        '''
        while self.running:
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
        # self.startMainLoop()
    
    def loadBestSnakes(self):
        '''
        Load best snakes for each generations from best.pickle file
        '''
        self.SLEEPING_TIME = 70
        self.loadGame = True
        try:
            bestMember = self.best.getNextGeneration()
            self.generation = self.best.getter
            self.NN.setNewWeights(bestMember.weights)
            self.snake = snake.Snake(self)
            self.food = food.Food(self.snake)
        except Exception:
            self.running = False
            self.mainFrame.flushAfterLoad()
            self.mainFrame.firstScreen()
            self.SLEEPING_TIME = 0
            
    def save(self):
        with open('model.pickle', 'wb') as f:
            pickle.dump(self.geneticsController, f)
            
        with open('best.pickle', 'wb') as f:
            pickle.dump(self.best, f)

    def printRaport(self):
        print("NN times ", self.time_nn / self.newGameCounter)
        print("Graphics times ", self.time_graphics / self.newGameCounter)
        print("Snake times ", self.time_snake / self.newGameCounter)
        print("New game times ", self.time_newGame / self.newGameCounter)
        print("###########################")
        print()

