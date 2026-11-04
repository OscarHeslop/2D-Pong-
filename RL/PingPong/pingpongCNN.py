"""create a class to display the rectangle, needs x y coords, width, height"""
import pygame
import sys

# 1. Initialize Pygame
pygame.init()



#-----------------------
# ! init variables 
#-----------------------
#colours 
white = (255, 255, 255)
red = (255, 0,0)
#pygame 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oscar Pong 2d")
clock = pygame.time.Clock()
running = True



#-----------------------
# ! Defining classes
#-----------------------
class Bar:
    global red
    def __init__(self,x_pix,y_pix, x, y):
        self.x_pix = x_pix 
        self.y_pix = y_pix
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.x_pix, self.y_pix))

#-----------------------
# ! instanciating classes
#-----------------------
x = 100 
y = x * 2
player = Bar(x, y , int(SCREEN_WIDTH * 1/3), int(SCREEN_HEIGHT * 1/3))





#-----------------------
# ! MAIN LOOP
#-----------------------

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        # Check if the user clicks the close window button (X)
        if event.type == pygame.QUIT:
            running = False


    screen.fill(white) #takes in tuple 



    
    #-----------------------
    # ! DRAWING ON SCREEN 
    #-----------------------
    player.draw()



    pygame.display.flip()

    clock.tick(60)



# 4. Clean exit
pygame.quit()
sys.exit()



