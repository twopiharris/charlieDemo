import pygame, simpleGE, random

"""CharlieDemo
"""

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8        
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = 100
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("campus.jpg")
        self.charlie = Charlie(self)
        self.coin = Coin(self)
 
        
        
        self.sprites = [self.charlie,
                        self.coin]
    
    
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    
