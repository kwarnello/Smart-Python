'''
Created on 2 lut 2020

@author: Warus
'''


class Member(object):
    '''
    Member of population
    '''

    def __init__(self, ID, weights):
        '''
        Constructor
        If weights are not given generate new random one (for example for 
        first generation or new random population)
        '''
        
        self.ID = ID
        self.weights = weights
        
        self.highscore = 0
        
    def setHighscore(self, highscore):
        if highscore > self.highscore:
            self.highscore = highscore

    def getWeights(self):
        return self.weights
