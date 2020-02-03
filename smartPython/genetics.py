'''
Created on 2 lut 2020

@author: Warus
'''
import copy
import numpy as np

from smartPython import member


class Genetics(object):
    '''
    Class that will handle staff with genetic algorithms, population, mutation etc.
    '''

    def __init__(self, NN, populationSize=10, percentageWeak=0.5):
        '''
        Constructor
        '''
        self.NN = NN
        
        self.populationSize = populationSize
        
        self.generationCounter = 0
        self.IDCounter = 0 
        
        self.population = {}
        self.populationToCheck = []
        
        self.workerID = None
        
        self.scorerStats = []
        
        self.percentageWeak = percentageWeak
        
        self.createGeneration()

    def createGeneration(self):
        self.generationCounter += 1
        for _ in range(self.populationSize - len(self.population)):
            self.population[self.IDCounter] = self.createMember(self.IDCounter)
            self.IDCounter += 1
            
        self.populationToCheck = copy.deepcopy(list(self.population.values()))
        self.scorerStats = []
        
    def newGeneration(self):
        self.countStatistics()
        self.killWeak()
        
        self.createGeneration()
        pass
    
    def countStatistics(self):
        for v in self.population.values():
            self.scorerStats.append(v.highscore)
        self.ave = np.average(self.scorerStats)
        self.med = np.median(self.scorerStats)
        print("Average {:.2f} +/- {:.2f}".format(self.ave, np.std(self.scorerStats)))
        print("Median {:.2f}".format(self.med))

    def killWeak(self):
        iShouldKill = int(self.populationSize * self.percentageWeak)
        iKilled = 0
        for k in list(self.population.keys()):
            if self.population[k].highscore <= self.med:
                del(self.population[k])
                iKilled += 1
            if iKilled >= iShouldKill:
                break
    
    def isNextMember(self):
        return True if (len(self.populationToCheck) > 0) else False
    
    def getNextMember(self):
        '''
        Get next member and save its ID
        '''
        workingMember = self.populationToCheck.pop()
        self.workerID = workingMember.ID
        return workingMember
    
    def putScore(self, score):
        if self.workerID != None:
            self.population[self.workerID].setHighscore(score)

    def createMember(self, ID):
        return member.Member(ID, self.NN.getRandomWeights())

    def crossover(self, memA, memB):
        memC = memA + memB
        return memC

    def mutate(self, member):
        return member

    def fitness(self, member):  
        return member.highscore
    
    def getMemberCount(self):
        return len(self.population) - len(self.populationToCheck)
