'''
Created on 7 lut 2020

@author: k
'''


class Best(object):
    '''
    Save best weights that can be replayed with load game button
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.weights = {}
        self.iterator = 0
        self.getter = 0
        
    def saveNextGeneration(self, bestMember):
        self.iterator += 1 
        self.weights[self.iterator] = bestMember
        
    def getNextGeneration(self):
        self.getter += 1
        return self.weights[self.getter]
