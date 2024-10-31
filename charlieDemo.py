import pygame, simpleGE

"""CharlieDemo
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("campus.jpg")
        
        self.sprites = []
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    
