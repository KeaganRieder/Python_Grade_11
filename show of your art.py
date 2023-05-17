from random import randint 
import pygame
i= 0
x = 0
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SEA = (0, 105, 148)#ocean
YELLOW = (255,255,0)#biulding lights
NIGHT = (7, 26, 76)#night sky
GREY = (128, 128, 128)#sea wall shadow
DARKGREY = (105,105,105)#sea wall
ORANGE = (255, 197, 143)#lights
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Initalizing the Stars Positions
stars_position = [0] * 600

for star_y in range (599):
    stars_position[star_y] = randint(0,150)

#Initialize the building Heights
building_height = [0] * 14

for building in range (14):
    building_height[building] = randint(20, 140)
        
  
# -------- Main Program Loop -----------
#stars

while not done:
    # --- Main event loop
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    screen.fill(NIGHT)

    # --- Drawing code should go here
##    pygame.draw.rect(screen, GREY, [x axis, yaxis, legth, hight], )
    #stars

    y = 0
    for x in range (0,1000,6):
        pygame.draw.ellipse(screen, WHITE, [x,stars_position[y],5,5])
        y = y + 1

    #cites silhouette
    building = 0
    for x in range (0,700, 50):
        pygame.draw.rect(screen, BLACK, [x,building_height[building],70,300])
        building = building + 1
        
    building = 0
    for x in range (0, 700, 50):
        building_num_pos = 50*(1+building)
        for light_x_pos in range (x+5,building_num_pos, 13):
            for light_y_pos in range (building_height[building], 250, 15):
                    if ((light_y_pos % 4 == 1) and (light_x_pos % 4 == 3)):
                        pygame.draw.rect (screen, YELLOW, [light_x_pos,light_y_pos,6,6])
                    elif ((light_y_pos % 8 == 6) and (light_x_pos % 8 == 6 )):
                        pygame.draw.rect (screen, YELLOW, [light_x_pos,light_y_pos,6,6])
                    

        building = building + 1
        
   #street lights
    for x in range (0,1000, 50):
        if x == 900:
                break
        pygame.draw.ellipse(screen, ORANGE, [x,280,5,5])
    
   #sea wall 
    pygame.draw.rect(screen, GREY, [0, 300, 700, 100] )
    pygame.draw.rect(screen, DARKGREY, [0, 320, 700, 100] )
    pygame.draw.rect(screen, SEA, [0, 340, 700, 500] )

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

 
    # --- Limit to 60 frames per second
    clock.tick(6000)


# Close the window and quit.
pygame.quit()
