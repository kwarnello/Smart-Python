'''
Created on 1 lut 2020

@author: Warus
'''

import tkinter


class MainFrame():
    '''
    Create base frame, initialize first screen and allows to go further
    '''

    WIDTH = 1100
    HEIGHT = 720
    BUTTON_WIDTH = 35
    BORDER_WIDTH = 1

    def __init__(self):
        '''
        Constructor
        '''
        self.root = tkinter.Tk()
        
        self.initializeFrame();

        self.root.deb
        self.root.mainloop()
        
    def initializeFrame(self):
        '''
        Initialize base things for main frame
        '''

        self.root.resizable(False, False)
        self.root.minsize(self.WIDTH, self.HEIGHT)
        self.root.title("Smart Python")
        
        self.firstScreen()
        
        
    def firstScreen(self):
        '''
        First screen where user can start new game, load, options or exit
        '''
        newGameButton = tkinter.Button(self.root,
                                    text='New game',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH,
                                    command=self.newGame)
        
        loadButton = tkinter.Button(self.root,
                                    text='Load',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH)
        
        optionsButton = tkinter.Button(self.root,
                                    text='Options',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH)
        
        exitButton = tkinter.Button(self.root,
                                    text='Exit',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH,
                                    command=self.exitCommand)
        
        newGameButton.pack()
        loadButton.pack()
        optionsButton.pack()
        exitButton.pack()
        
    def newGame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.initializeGameScreen()
    
    def loadGame(self):
        pass
    
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
        placeForSnake = (50, 10, 700, 700)
        placeForNeurons = (750, 10, 300, 700)
        
        canvas = tkinter.Canvas(self.root)
        canvas.create_rectangle(placeForSnake)
        canvas.create_rectangle(placeForNeurons, fill="red")

        canvas.pack(fill=tkinter.BOTH, expand=1)
        
        
