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

    def __init__(self, inputs=14, first=16, second=8):
        '''
        Constructor
        '''
        self.inputs = inputs
        self.first = first
        self.second = second
        self.outputs = 4
        self.zerosSize = [self.first, self.second, self.outputs]
        
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self.first, activation='relu', input_shape=(self.inputs,)),
            tf.keras.layers.Dense(self.second, activation='relu'),
            tf.keras.layers.Dense(self.outputs, activation='softmax')
            ])

        self.model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
        
    def predict(self, inputs):
        return self.model.predict(inputs)
    
    def setNewWeights(self, weights):
        if len(weights) != 3:
            print("ERRORRORORORO, wrong weights shape")
        
        for i, layer in enumerate(self.model.layers):
            layer.set_weights([weights[i], np.zeros(self.zerosSize[i])])
        
    def getRandomWeights(self):
        weightA = np.empty([self.inputs, self.first])
        for i in range(self.inputs):
            for j in range(self.first):
                weightA[i][j] = 2 * np.random.rand() - 1
        
        weightB = np.empty([self.first, self.second])
        for i in range(self.first):
            for j in range(self.second):
                weightB[i][j] = 2 * np.random.rand() - 1
        
        weightC = np.empty([self.second, self.outputs])
        for i in range(self.second):
            for j in range(self.outputs):
                weightC[i][j] = 2 * np.random.rand() - 1
        
        return np.array([weightA, weightB, weightC])
