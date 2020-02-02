'''
Created on 2 lut 2020

@author: Warus
'''


class Score(object):
    '''
    Score class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.score = 0
        self.highscore = 0
        
    def newGame(self):
        '''
        For new game put score to highscore if higher and reset score
        '''
        
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        
    def addScore(self):
        self.score += 1

    def getScore(self):
        return self.score

    def getHighscore(self):
        return self.highscore
