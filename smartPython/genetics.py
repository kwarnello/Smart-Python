'''
Created on 2 lut 2020

@author: Warus
'''
import copy
import numpy as np

from smartPython import member, neuralNetwork


class Genetics(object):
    '''
    Class that will handle staff with genetic algorithms, population, mutation etc.
    '''

    def __init__(self, populationSize=1000, percentageWeak=0.9, percentageChilds=0.88):
        '''
        Constructor
        '''
        self.populationSize = populationSize
        
        self.generationCounter = 0
        self.IDCounter = 0 
        
        self.population = {}
        self.populationToCheck = []
        
        self.workerID = None
        
        self.scorerStats = []
        
        self.percentageWeak = percentageWeak
        self.percentageChilds = percentageChilds
        
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
        self.createChild()
        self.createGeneration()
        pass
    
    def countStatistics(self):
        '''
        Get basic stats that decision about killing can be made
        '''
        for v in self.population.values():
            self.scorerStats.append(v.score)
            
        self.ave = np.average(self.scorerStats)
        self.med = np.median(self.scorerStats)
        
        print("Generation {}".format(self.generationCounter))
        print("Average {:.3f} +/- {:.3f}".format(self.ave, np.std(self.scorerStats)))
        print("Median {:.3f}".format(self.med))
        print()

    def killWeak(self):
        '''
        Kill all that are weaker than median
        '''
        iShouldKill = int(self.populationSize * self.percentageWeak)
        iKilled = 0
        for k in list(self.population.keys()):
            if self.population[k].score <= self.med:
                del(self.population[k])
                iKilled += 1
            if iKilled >= iShouldKill:
                break
            
    def createChild(self):
        '''
        Create child based on random parents. Take on from beginning of shuffle list and one from the end
        '''
        keys = list(self.population.keys())
        
        for _ in range(int(self.populationSize * self.percentageChilds)):
            i, j = np.random.choice(keys), np.random.choice(keys)
            newMemberWeight = self.crossover(self.population[i], self.population[j])
            self.population[self.IDCounter] = self.createMember(self.IDCounter, newMemberWeight)
            self.IDCounter += 1

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
            self.population[self.workerID].setScore(score)

    def createMember(self, ID, weights=None):
        if weights == None:
            return member.Member(ID, neuralNetwork.getRandomWeights())
        else:
            return member.Member(ID, weights)

    def crossover(self, memA, memB):
        '''
        Old cross over ass average
        '''
        weightA = memA.getWeights()
        weightB = memB.getWeights()
        newWeights = []
        for  i in range(len(weightA) // 2):
            temp = [0] * len(weightA[i])
            for j in range(len(weightA[i])):
                temp_second = [0] * len(weightA[i][j])
                for k in range(len(weightA[i][j])):
                    if np.random.rand() > 0.5:
                        temp_second[k] = weightA[i][j][k]
                    else:
                        temp_second[k] = weightB[i][j][k]
                temp[j] = list(temp_second)
            newWeights.append(np.array(temp))
            
        for  i in range(len(weightA) // 2):
            newWeights.append(np.array([2 * np.random.rand() - 1 for _ in range(len(weightA[i][0]))]))
        
        return newWeights
    
        '''
        Old cross over ass average
        '''
        # newWeights = []
        # for i in range(len(weightA)):
        #    temp = [0] * len(weightA[i])
        #    for j in range(len(weightA[i])):      
        #        ave = np.average([weightA[i][j], weightB[i][j]], axis=0, weights=[memA.score + 0.001, memB.score + 0.001])
        #        temp[j] = list(ave)
                
        #    newWeights.append(np.array(temp))

    def mutate(self, member):
        return member

    def fitness(self, member):  
        return member.score
    
    def getMemberCount(self):
        return len(self.population) - len(self.populationToCheck)
