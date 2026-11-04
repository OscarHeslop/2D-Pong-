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
blue = (0,0,255)
red = (255, 0,0) #RGB
green = (0,255,0)




#-----------------------

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
        self.colour = None
    def draw(self,colour):
        self.colour = colour
        pygame.draw.rect(screen, colour, (self.x, self.y, self.x_pix, self.y_pix))

class Ball:
    def __init__(self, x, y, rad):
        self.x = x 
        self.y = y
        self.rad = rad
    def draw(self,colour):
        pygame.draw.circle(screen, colour, (int(self.x), int(int(self.y))), self.rad)
#-----------------------
# ! instanciating classes
#-----------------------
# ! init vars
speed = 5
rad = 20
x_dim = 20 #dimensions
y_dim = x_dim * 6
player = Bar(x_dim, y_dim , int(x_dim * 0.5), int(SCREEN_HEIGHT * 1/2)) # is x then y
enemy = Bar(x_dim, y_dim , int(SCREEN_WIDTH - int(x_dim * 0.5) - int(x_dim)), int(SCREEN_HEIGHT * 1/2)) # is x then y

#Ball 
ball = Ball(SCREEN_WIDTH //2, SCREEN_HEIGHT//2, rad)
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


    if event.type == pygame.MOUSEBUTTONDOWN:
        # event.pos contains (x, y)
        x, y = event.pos
        print(f"Mouse clicked at X: {x}, Y: {y}")

    #-----------------------
    # ! PLAYER CONTROLS
    #-----------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player.y >(0):
            player.y -= speed
        
    if keys[pygame.K_s]:
        if player.y < (SCREEN_HEIGHT - y_dim):
            player.y += speed



    
    #-----------------------
    # ! DRAWING ON SCREEN 
    #-----------------------
    player.draw(red)
    enemy.draw(blue)
    # DRAWING BALL 
    ball.draw(green)
    


    #-----------------------------------------
    pygame.display.flip()

    clock.tick(60)



# 4. Clean exit
pygame.quit()
sys.exit()


"""
For me - skip over

changing current push path
git remote set-url origin https://github.com/OscarHeslop/2D-Pong-.git

check current push path 
git remote -v 


add speech marks to name
git add "RL\PingPong\pingpongCNN.py" 
use relative path

removing from staging area 
git reset


"""