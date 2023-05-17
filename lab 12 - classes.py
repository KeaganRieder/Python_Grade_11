import pygame
from random import randint 
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Rectangle():
    def _init_(self):
        self.color = ''
        self.x = 0 
        self.y = 0
        self.length = 0
        self.width = 0 
        self.x_change = 0
        self.y_change = 0
       
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x,self.y,self.length,self.width])
        
    def move(self):
        if self.x > 1920 or self.x < 0:
            self.x_change = self.x_change * -1
        if self.y > 1080 or self.y < 0:
            self.y_change = self.y_change * -1
        self.x += self.x_change
        self.y += self.y_change
        return self.x
        return self.y

class Ellipse(Rectangle):
    def _init_(self):
        Rectangle._init_(self)
        
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x,self.y,self.length,self.width])
    
    

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size)
   
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
my_list = []
#rectangle
for i in range(500):
    #making random colors
    R = randint(0,250)
    G = randint(0,250)
    B = randint(0,250)
    COLOR = (R,G,B)
    #defining vales for rectangle class
    rectangle = Rectangle()
    rectangle.color =  COLOR
    rectangle.x = randint(0,700)
    rectangle.y = randint(0,500)
    rectangle.width = randint(20,70)
    rectangle.length = randint(20,70)
    rectangle.x_change = randint(-3,3)
    rectangle.y_change = randint(-3,3)  
    #adding values to my_list
    my_list.append(rectangle)
#ellipse
for i in range(500):
    #making random colors
    R = randint(0,250)
    G = randint(0,250)
    B = randint(0,250)
    COLOR = (R,G,B)
    #defining vales for ellipse class
    ellipse = Ellipse() 
    ellipse.color =  COLOR
    ellipse.x = randint(0,650)
    ellipse.y = randint(0,450)
    ellipse.width = randint(20,70)
    ellipse.length = randint(20,70)
    ellipse.x_change = randint(-3,3)
    ellipse.y_change = randint(-3,3)  
    my_list.append(ellipse)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
    # --- Game logic should go here
   
    
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for item in my_list:
        item.draw(screen)
        item.move()

        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
