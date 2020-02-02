'''
Created on 1 lut 2020

@author: Warus
'''

import tkinter


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
    SNAKE_PLACE_SIZE = 702
    SIZE_OF_ONE_CELL = 25  #### So the size of boardgame is 28x28

    def __init__(self, main):
        '''
        Constructor
        '''
        self.main = main
        
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

        self.firstScreen()
        
    def firstScreen(self):
        '''
        First screen where user can start new game, load, options or exit
        '''
        newGameButton = tkinter.Button(self.root,
                                    text='New game',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH,
                                    command=self.newGame).place(relx=0.5, rely=0.38)
        
        loadButton = tkinter.Button(self.root,
                                    text='Load',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH).place(relx=0.5, rely=0.46)
        
        optionsButton = tkinter.Button(self.root,
                                    text='Options',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH).place(relx=0.5, rely=0.54)
        
        exitButton = tkinter.Button(self.root,
                                    text='Exit',
                                    width=self.BUTTON_WIDTH,
                                    borderwidth=self.BORDER_WIDTH,
                                    command=self.exitCommand).place(relx=0.5, rely=0.62)
        
        # newGameButton.pack()
        # loadButton.pack()
        # optionsButton.pack()
        # exitButton.pack()
        
    def newGame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.main.initializeNewGame()
        self.initializeGameScreen()
        self.root.after(10, self.main.startMainLoop)
    
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
        self.placeForSnake = (20, 10, self.SNAKE_PLACE_SIZE + 20, self.SNAKE_PLACE_SIZE + 10)
        self.placeForNeurons = (self.SNAKE_PLACE_SIZE + 30, 10, 1080, self.SNAKE_PLACE_SIZE + 10)
        
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.create_rectangle(self.placeForSnake, outline='white')
        
        # self.canvas.create_rectangle(self.placeForNeurons, outline='white')
        self.canvas.configure(bg='black')
        
        self.highscoreLabel = tkinter.Label(self.canvas, text="Highscore: 0", bg="Black", foreground="White")
        self.highscoreLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[3] - 75)
        self.scoreLabel = tkinter.Label(self.canvas, text="Score: 0", bg="Black", foreground="White")
        self.scoreLabel.place(x=self.placeForNeurons[0], y=self.placeForNeurons[3] - 55)
        
        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        
        self.drawSnake()
        self.drawFood()
        
    def drawSnake(self):
        '''
        Draw snake based on list of its elements
        '''
        for part in self.main.snake.snakeElements:
            self.canvas.create_rectangle(self.findRectangleCoordinates(part), fill='white', outline='black')
            
    def drawFood(self):
        '''
        Draw snake based on list of its elements
        '''
        self.canvas.create_rectangle(self.findRectangleCoordinates(self.main.food.position), fill='red', outline='black')
        
    def findRectangleCoordinates(self, coordinates):
        a = self.placeForSnake[0] + coordinates[0] * self.SIZE_OF_ONE_CELL
        b = self.placeForSnake[1] + coordinates[1] * self.SIZE_OF_ONE_CELL
        c = a + self.SIZE_OF_ONE_CELL
        d = b + self.SIZE_OF_ONE_CELL
        return (a, b, c, d)
    
    def update(self):
        '''
        Update snake frame and after that redraw everything
        '''
        self.canvas.create_rectangle(self.placeForSnake, outline='white', fill="black")
        
        self.drawSnake()
        self.drawFood()
        
        self.highscoreLabel.config(text="Highscore: " + str(self.main.score.getHighscore()))
        self.scoreLabel.config(text="Score: " + str(self.main.score.getScore()))

        self.root.update()
        
    def getSizeOfBoard(self):
        return getSizeOfBoard()

        
def getSizeOfBoard():
    return (MainFrame.SNAKE_PLACE_SIZE - 2) // MainFrame.SIZE_OF_ONE_CELL
        
