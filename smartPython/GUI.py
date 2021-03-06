'''
Created on 1 lut 2020

@author: Warus
'''

import tkinter
import numpy as np


class MainFrame(object):
    '''
    Create base frame, initialize first screen and allows to go further
    '''
    # ## Main frame variables
    WIDTH = 1100
    HEIGHT = 720
    
    # ## First frame variables
    BUTTON_WIDTH = 35
    BORDER_WIDTH = 1
    
    # ## Game frame variables
    SNAKE_PLACE_SIZE = 700
    SIZE_OF_ONE_CELL = 25  #### So the size of boardgame is 28x28

    def __init__(self, main):
        '''
        Constructor
        '''
        self.main = main
        self.canvasExists = False
        
        self.root = tkinter.Tk()
        
        self.initializeFrame();
        
    def startLoop(self):
        self.root.mainloop()     
           
    def initializeFrame(self):
        '''
        Initialize base things for smartPython frame
        '''

        self.root.resizable(False, False)
        self.root.minsize(self.WIDTH, self.HEIGHT)
        self.root.title("Smart Python")
        
        self.root.configure(bg='black')
        self.canvas = tkinter.Canvas(self.root)

        self.firstScreen()
        
    def firstScreen(self):
        '''
        First screen where user can start new game, load, options or exit
        '''
        tkinter.Button(self.root,
                        text='New game',
                        width=self.BUTTON_WIDTH,
                        borderwidth=self.BORDER_WIDTH,
                        command=self.newGame).place(relx=0.38, rely=0.38)
        
        tkinter.Button(self.root,
                        text='Load',
                        width=self.BUTTON_WIDTH,
                        borderwidth=self.BORDER_WIDTH,
                        command=self.loadGame).place(relx=0.38, rely=0.46)
        
        tkinter.Button(self.root,
                        text='Options',
                        width=self.BUTTON_WIDTH,
                        borderwidth=self.BORDER_WIDTH).place(relx=0.38, rely=0.54)
        
        tkinter.Button(self.root,
                        text='Exit',
                        width=self.BUTTON_WIDTH,
                        borderwidth=self.BORDER_WIDTH,
                        command=self.exitCommand).place(relx=0.38, rely=0.62)
        
    def newGame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.main.initializeNewGame()
        self.initializeGameScreen()
        self.root.after(10, self.main.startMainLoop)
    
    def loadGame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.main.loadBestSnakes()
        self.initializeGameScreen()
        self.root.after(10, self.main.startMainLoop)
        
    def flushAfterLoad(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def options(self):
        pass
    
    def exitCommand(self):
        exit()
        
    def initializeGameScreen(self):
        '''
        Main game screen.
        Left border with play space.
        Right part info about NN.
        '''        
        self.placeForSnake = (20, 10, self.SNAKE_PLACE_SIZE + 20, self.SNAKE_PLACE_SIZE + 10)
        self.placeForNeurons = (self.SNAKE_PLACE_SIZE + 30, 10, 1080, self.SNAKE_PLACE_SIZE + 10)
                
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.create_rectangle(self.placeForSnake, outline='white')
        
        self.canvas.configure(bg='black')
        
        self.highscoreLabel = tkinter.Label(self.root, text="Highscore: 0", bg="Black", foreground="White")
        self.highscoreLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[3] - 75)
        self.scoreLabel = tkinter.Label(self.root, text="Score: 0", bg="Black", foreground="White")
        self.scoreLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[3] - 55)
        self.generationLabel = tkinter.Label(self.root, text="Generation: 0", bg="Black", foreground="White", font=(16))
        self.generationLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[1] + 20)
        self.snakeLabel = tkinter.Label(self.root, text="Snake number: 0", bg="Black", foreground="White", font=(14))
        self.snakeLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[1] + 40)
                
        self.drawNN()

        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        
        self.drawSnake()
        self.drawFood()
        
        # ## dummy implementation for draw connection fixed
        self.canvasExists = True
        
    def drawSnake(self):
        '''
        Draw snake based on list of its elements
        '''
        for part in self.main.snake.snakeElements:
            self.canvas.create_rectangle(self.findRectangleCoordinates(part), fill='white', outline='black', tags='refreshable')
            
    def drawFood(self):
        '''
        Draw snake based on list of its elements
        '''
        self.canvas.create_rectangle(self.findRectangleCoordinates(self.main.food.position), fill='red', outline='black', tags='refreshable')
     
    def findRectangleCoordinates(self, coordinates):
        a = self.placeForSnake[0] + coordinates[0] * self.SIZE_OF_ONE_CELL
        b = self.placeForSnake[1] + coordinates[1] * self.SIZE_OF_ONE_CELL
        c = a + self.SIZE_OF_ONE_CELL
        d = b + self.SIZE_OF_ONE_CELL
        return (a, b, c, d)
       
    def drawNN(self):
        '''
        Draw base for NN (neurons, connections etc.).
        Firstly create dict with brain structure
        '''
        # ## Oval size, padding and so on
        ovalDiameter = 45
        
        paddingTop = 15
        paddingLeft = 15
        
        hPaddingBetweenNeurons = 80
        vPaddingBetweenNeurons = 25

        modelSize = self.main.NN.size
        self.connections = {}
        self.neurons = {}

        #### Create neurons. Simplest calculation of coordinates (no border parameter detections!)
        for n in range(len(modelSize)):
            # ## Find padding that layer is in the center
            paddingTopForLayer = (modelSize[n] * ((abs(self.placeForNeurons[1] - self.placeForNeurons[3]) // modelSize[n]) - ovalDiameter - vPaddingBetweenNeurons)) // 2
            for y in range(modelSize[n]): 
                xCoor = self.placeForNeurons[0] + n * (ovalDiameter + hPaddingBetweenNeurons) + paddingLeft
                yCoor = self.placeForNeurons[1] + y * (ovalDiameter + vPaddingBetweenNeurons) + paddingTop + paddingTopForLayer
                coordinates = (xCoor,
                               yCoor,
                               xCoor + ovalDiameter,
                               yCoor + ovalDiameter)
                self.neurons[(n, y)] = [self.canvas.create_oval(coordinates, fill='black', outline='white'), (xCoor, yCoor)]  # ## store each neurons as ID and coordinates
                
        #### Create connections. Simplest calculation of coordinates (no border parameter detections!)
        for k, v in self.neurons.items():
            if k[0] == 2:
                break
            
            # ## iterate through each neuron in next layer and to create connections
            for x in range(modelSize[k[0] + 1]):
                nextNeuronsCoord = self.neurons[(k[0] + 1, x)][1]
                coordinates = (v[1][0] + ovalDiameter,
                               v[1][1] + ovalDiameter // 2,
                               nextNeuronsCoord[0],
                               nextNeuronsCoord[1] + ovalDiameter // 2)
                self.connections[(k[0], k[1], k[0] + 1, x)] = self.canvas.create_line(coordinates, fill="green", width=0.5, smooth=True)
    
    def updateNeurons(self, inputs, outputs):

        def clamp(x): 
            return max(0, min(x, 255))

        for index, input in enumerate(inputs[0]):
            color = "#{0:02x}{1:02x}{2:02x}".format(0, clamp(int(255 * input)), 0)
            self.canvas.itemconfig(self.neurons[(0, index)][0], fill=color)

        for index, output in enumerate(outputs[0]):
            if np.isnan(output):
                break
            color = "#{0:02x}{1:02x}{2:02x}".format(0, clamp(int(255 * output)), 0)
            self.canvas.itemconfig(self.neurons[(2, index)][0], fill=color)
            
    def update(self):
        '''
        Update snake frame and after that redraw everything
        '''
        self.canvas.delete('refreshable')
            
        self.drawSnake()
        self.drawFood()
        
        self.scoreLabel.config(text="Score: " + str(self.main.score.getScore()))
        
        self.root.update()
        
    def updateNewSnake(self, weights):
        if self.canvasExists:
            self.generationLabel.config(text="Generation: " + str(self.main.generation))
            self.snakeLabel.config(text="Snake: {} ({})".format(self.main.geneticsController.getMemberCount(), self.main.geneticsController.populationSize))
            self.highscoreLabel.config(text="Highscore: " + str(self.main.score.getHighscore()))
            
            self.updateConections(weights)

    def updateConections(self, weights):

        def clamp(x): 
            return max(0, min(x, 255))

        for layer in range(2):
            for i1, x in enumerate(weights[layer]):
                for i2, y in enumerate(x):
                    if y < 0:
                        y = abs(y)
                        color = "#{0:02x}{1:02x}{2:02x}".format(clamp(int(255 * y)), 0, clamp(int(134 * y)))
                    else:
                        color = "#{0:02x}{1:02x}{2:02x}".format(clamp(int(12 * y)), 0, clamp(int(255 * y)))                 
                    self.canvas.itemconfig(self.connections[(layer, i1, layer + 1, i2)], fill=color, width=4 * y)

    def getSizeOfBoard(self):
        return getSizeOfBoard()

        
def getSizeOfBoard():
    return MainFrame.SNAKE_PLACE_SIZE // MainFrame.SIZE_OF_ONE_CELL
        
