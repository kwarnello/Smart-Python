'''
Created on 2 lut 2020

@author: Warus
'''

import pandas as pd


class Genetics(object):
    '''
    Class that will handle staff with genetic algorithms, population, mutation etc.
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def fitness(self):  
        return 1
    
    def crossover(self, a, b):
        c = a + b
        return c

    def mutate(self, member):
        return member
    
    def createMember(self):
        member = 0
        return member

    def newGeneration(self, population):
        return population
