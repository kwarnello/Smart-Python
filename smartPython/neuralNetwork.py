'''
Created on 2 lut 2020

@author: Warus
'''

import tensorflow as tf


class NN(object):
    '''
    Class for Neural Network.
    '''

    def __init__(self, first=16, second=8):
        '''
        Constructor
        '''
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(first, activation='relu', input_shape=(14,)),
            tf.keras.layers.Dense(second, activation='relu'),
            tf.keras.layers.Dense(4, activation='softmax')
            ])

        self.model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
        
        print(self.model.summary())
