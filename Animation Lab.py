import pygame
from random import randint
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY =(105,105,105)
SILVER = (192,192,192)
GREY = (128,128,128)
LIGHTGREY = (50,50,50)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#shape size
length = 200
width = 200
length2 = 150
width2 = 150
length3 = 100
width3 = 100
length_change = 5
width_change = 5
length_change2 = 5
width_change2 = 5
length_change3 = 5
width_change3 = 5

#shape start location
rect_x = 250
rect_y = 150
rect_x_change = 2
rect_y_change = 2

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 200 , 200])
    #rect number 1
    pygame.draw.rect(screen, RED, [rect_x, rect_y, length , width])  
    #rect number 2
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, length2 , width2])
    #rect number 3
    pygame.draw.rect(screen, GREEN, [rect_x, rect_y, length3, width3])
  
    

    #rect number 1
    if length >= 200 or length <= 0:
        length_change = length_change *-1
    if width >= 200 or width <= 0:
        width_change = width_change *-1
    width += width_change
    length += length_change
    
    #rect number 2
    if length2 >= 150 or length2 <= 0:
        length_change2 = length_change2 *-1
        
    if width2 >= 150 or width2 <= 0:
        width_change2 = width_change2 *-1
    
    width2 += width_change2
    length2 += length_change2
    
    #rect number 3
    if length3 >= 100 or length3 <= 0:
        length_change3 = length_change3 *-1
        
    if width3 >= 100 or width3 <= 0:
        width_change3 = width_change3 *-1
    
    width3 += width_change3
    length3 += length_change3

    #moving rectangles around
    if rect_y > 300 or rect_y < 0:
        rect_y_change = rect_y_change * -1
        
    if rect_x > 500 or rect_x < 0:
        rect_x_change = rect_x_change * -1
        
    rect_x += rect_x_change
    rect_y += rect_y_change     
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
