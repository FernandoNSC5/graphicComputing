# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
size = [1000, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Enarin")

done = False
clock = pygame.time.Clock()
 
while not done:
 
    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 
     
    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    #Update function based on clock
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()