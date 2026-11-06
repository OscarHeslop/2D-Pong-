
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
red = (255, 0,0)
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

        self.dx = 5
        self.dy = 3

    def draw(self,colour):
        pygame.draw.circle(screen, colour, (int(self.x), int(self.y)), self.rad)


#-----------------------
# ! instanciating classes
#-----------------------
speed = 5
rad = 20
x_dim = 20
y_dim = x_dim * 6

player = Bar(x_dim, y_dim, int(x_dim * 0.5), int(SCREEN_HEIGHT * 1/2))
enemy = Bar(x_dim, y_dim, int(SCREEN_WIDTH - int(x_dim * 0.5) - int(x_dim)), int(SCREEN_HEIGHT * 1/2))

#Ball
ball = Ball(SCREEN_WIDTH //2, SCREEN_HEIGHT//2, rad)


#-----------------------
# ! MAIN LOOP
#-----------------------
while running:

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"Mouse clicked at X: {x}, Y: {y}")


    screen.fill(white)


    #-----------------------
    # ! PLAYER CONTROLS
    #-----------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if player.y > 0:
            player.y -= speed

    if keys[pygame.K_s]:
        if player.y < (SCREEN_HEIGHT - y_dim):
            player.y += speed


    #-----------------------
    # ! BALL MOVEMENT
    #-----------------------

    ball.x += ball.dx
    ball.y += ball.dy

    # Top reflection
    if ball.y - ball.rad <= 0:
        ball.dy *= -1

    # Bottom reflection
    if ball.y + ball.rad >= SCREEN_HEIGHT:
        ball.dy *= -1

    # Left paddle collision
    if (ball.dx < 0 and
        ball.x - ball.rad <= player.x + player.x_pix and
        ball.y + ball.rad >= player.y and
        ball.y - ball.rad <= player.y + player.y_pix):

        ball.dx *= -1

    # Right paddle collision
    if (ball.dx > 0 and
        ball.x + ball.rad >= enemy.x and
        ball.y + ball.rad >= enemy.y and
        ball.y - ball.rad <= enemy.y + enemy.y_pix):

        ball.dx *= -1

    # Reset ball if it leaves the screen
    if ball.x < 0 or ball.x > SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH // 2
        ball.y = SCREEN_HEIGHT // 2
        ball.dx *= -1
        ball.dy = 3


    #-----------------------
    # ! DRAWING ON SCREEN
    #-----------------------
    player.draw(red)
    enemy.draw(blue)
    ball.draw(green)


    #-----------------------------------------
    pygame.display.flip()

    clock.tick(60)


# 4. Clean exit
pygame.quit()
sys.exit()
