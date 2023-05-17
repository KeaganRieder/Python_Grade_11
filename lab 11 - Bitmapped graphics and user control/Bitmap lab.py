import pygame
 
#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
##RED = (255, 0, 0)
##GREEN = (0, 255, 0)
##BLUE = (0, 0, 255)

 
pygame.init()



# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#importing an image call spacebackground.jpg
background_image = pygame.image.load("res\spacebackground.jpg").convert()

#making so the background image works in the 700 x 500 window
background_image = pygame.transform.scale(background_image, (700, 500))

#setting up player model
player_model = pygame.image.load("res\ship.png").convert()
player_model = pygame.transform.scale(player_model, (100, 100))
player_model.set_colorkey(WHITE)

def darw_player(screen,x,y):
    screen.blit(player_model,[x,y])
#lazer
#def

#creating thruster sound
click_sound = pygame.mixer.Sound("res\laser5.ogg")


#setting up controller values for player model
#speed of pixels per frame
x_speed = 0
y_speed = 0
#current postion
x_coord = 10
y_coord = 10
              

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -2
            elif event.key == pygame.K_RIGHT:
                x_speed = 2
            elif event.key == pygame.K_UP:
                y_speed = -2
            elif event.key == pygame.K_DOWN:
                y_speed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    if x_coord < 0:
       x_coord = 0
       
    if x_coord > 600:
       x_coord = 600

    if y_coord < 0:
       y_coord = 0
       
    if y_coord > 400:
        y_coord = 400

    x_coord += x_speed
    y_coord += y_speed

    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    screen.blit(background_image,[0,0])
    darw_player(screen, x_coord,y_coord)
    
 
    # --- Drawing code should go here
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
