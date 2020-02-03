'''
Created on 2 lut 2020

@author: Warus
'''

import copy

from smartPython import member


class Genetics(object):
    '''
    Class that will handle staff with genetic algorithms, population, mutation etc.
    '''

    def __init__(self, NN, populationSize=50):
        '''
        Constructor
        '''
        self.NN = NN
        
        self.populationSize = populationSize
        
        self.generationCounter = 0
        self.IDCounter = 0 
        
        self.population = []
        self.populationToCheck = []
        
        self.firstGeneration()

    def firstGeneration(self):
        for _ in range(self.populationSize):
            self.population.append(self.createMember(self.IDCounter))
            self.IDCounter += 1
            
        self.populationToCheck = copy.deepcopy(self.population)
        
    def newGeneration(self):
        pass
    
    def isNextMember(self):
        return True if (len(self.populationToCheck) > 0) else False
    
    def getNextMember(self):
        return self.populationToCheck.pop()

    def createMember(self, ID):
        return member.Member(ID, self.NN.getRandomWeights())

    def crossover(self, memA, memB):
        memC = memA + memB
        return memC

    def mutate(self, member):
        return member

    def fitness(self, member):  
        return member.highscore
