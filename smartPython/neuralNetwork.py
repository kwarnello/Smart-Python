'''
Created on 2 lut 2020

@author: Warus
'''

import tensorflow as tf
import numpy as np


class NN(object):
    '''
    Class for Neural Network.
    '''

    def __init__(self, inputs=8, first=6):
        '''
        Constructor
        '''
        self.inputs = inputs
        self.first = first
        self.outputs = 4
        self.size = [self.inputs, self.first, self.outputs]
        
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self.first, activation='relu', input_shape=(self.inputs,)),
            tf.keras.layers.Dense(self.outputs, activation='softmax')
            ])
        
    def predict(self, inputs):
        return self.model.predict(inputs)
    
    def setNewWeights(self, weights):
        for i, layer in enumerate(self.model.layers):
            layer.set_weights([weights[i], weights[i + 2]])
            
        tf.keras.backend.clear_session()
        
    def getRandomWeights(self): 
        return getRandomWeights(self.inputs, self.first, self.outputs)

    
def getRandomWeights(inputs=8, first=6, outputs=4):
    weightA = np.empty([inputs, first])
    for i in range(inputs):
        for j in range(first):
            weightA[i][j] = 2 * np.random.rand() - 1
        
    weightB = np.empty([first, outputs])
    biasA = np.zeros([first])
    for i in range(first):
        biasA[i] = 2 * np.random.rand() - 1
        for j in range(outputs):
            weightB[i][j] = 2 * np.random.rand() - 1
    
    biasB = np.zeros([outputs])
    #for i in range(outputs):
    #    biasB[i] = 2 * np.random.rand() - 1

    return np.array([weightA, weightB, biasA, biasB])
