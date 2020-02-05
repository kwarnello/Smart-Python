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

    def __init__(self, inputs=8, first=8, second=4):
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
        if len(weights) != 6:
            print("ERRORRORORORO, wrong weights shape")
        
        for i, layer in enumerate(self.model.layers):
            layer.set_weights([weights[i], weights[i + 3]])
            
        tf.keras.backend.clear_session()
        
    def getRandomWeights(self): 
        return getRandomWeights(self.inputs, self.first, self.second, self.outputs)

    
def getRandomWeights(inputs=8, first=8, second=4, outputs=4):
    weightA = np.empty([inputs, first])
    biasA = np.empty([first])
    for i in range(inputs):
        for j in range(first):
            weightA[i][j] = 2 * np.random.rand() - 1
            
    weightB = np.empty([first, second])
    biasB = np.empty([second])
    for i in range(first):
        for j in range(second):
            weightB[i][j] = 2 * np.random.rand() - 1
        
    weightC = np.empty([second, outputs])
    biasC = np.empty([outputs])
    for i in range(second):
        for j in range(outputs):
            weightC[i][j] = 2 * np.random.rand() - 1
        
    return np.array([weightA, weightB, weightC, biasA, biasB, biasC])
