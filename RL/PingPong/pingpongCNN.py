import pygame
import sys
import random
import math

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
    def rect(self):
        return(pygame.Rect(self.x - int(self.x_pix//2), self.y - int(self.y_pix //2), self.x_pix, self.y_pix)) #x, y, width, height

class Ball:
    def __init__(self, x, y, rad, paddle_pad):
        self.x = x 
        self.y = y
        self.rad = rad
        self.paddle_pad = paddle_pad
        angle = random.uniform(0, 2 * math.pi) 
        self.dx = math.cos(angle) * self.paddle_pad#uses radians
        self.dy = math.sin(angle) * self.paddle_pad
    def draw(self,colour):
        pygame.draw.circle(screen, colour, (int(self.x), int(int(self.y))), self.rad)
    def rect(self):
        return(pygame.Rect(ball.x - ball.rad, ball.y - ball.rad, ball.rad * 2, ball.rad * 2))
#-----------------------
# ! instanciating classes
#-----------------------
# ! init vars
paddle_paddle_pad = 5 #player_paddle_pad
paddle_speed = 10
rad = 20
x_dim = 20 #dimensions
y_dim = x_dim * 6
player = Bar(x_dim, y_dim , int(x_dim * 0.5), int(SCREEN_HEIGHT * 1/2)) # is x then y
enemy = Bar(x_dim, y_dim , int(SCREEN_WIDTH - int(x_dim * 0.5) - int(x_dim)), int(SCREEN_HEIGHT * 1/2)) # is x then y

#Ball 
ball = Ball(SCREEN_WIDTH //2, SCREEN_HEIGHT//2, rad,10)


def reset():
    ball.x, ball.y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
    
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
            player.y -= paddle_speed
        
    if keys[pygame.K_s]:
        if player.y < (SCREEN_HEIGHT - y_dim):
            player.y += paddle_speed
        



    
    #-----------------------
    # ! DRAWING ON SCREEN 
    #-----------------------
    player.draw(red)
    enemy.draw(blue)

    #-----------------------
    # ! COLLISION DETECTION
    #-----------------------
    ball_rect = ball.rect()
    player_rect = player.rect()
    enemy_rect = enemy.rect()

    #BALL:
    #HITS PADDLE
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(enemy_rect): #player left hand side
        ball.dx *= -1 #horz flip 



    #HITS WALL
    if (ball.y < 0) or (ball.y >SCREEN_HEIGHT):  
        ball.dy *= -1 #vert flip
    
    
    # DRAWING BALL 
    if (0< ball.x <SCREEN_WIDTH) or (0< ball.y <SCREEN_HEIGHT): #hit player 
        ball.draw(green)
        ball.x += ball.dx
        ball.y += ball.dy

    #LOST POINT
    if ball.x <0:
        print("enemy +1")
        reset()
        
    
    if ball.x >SCREEN_WIDTH:
        print("enemy +1")
        reset()

    


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