import pygame
import random
from res.Player import Player
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (30,144,255)
GREEN = (34,139,34)

 
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
 
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

    def reset_pos(self):
        
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, 530)
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_height: 
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, 530)
    
# Initialize Pygame
pygame.init() 

#bad block sound
bad_sound =  pygame.mixer.Sound("bad_block.wav")

#good block sound
good_sound =  pygame.mixer.Sound("good_block.wav")

#screen edge sound
hit_edge = pygame.mixer.Sound("bump.wav")

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
#good block list
good_block_list = pygame.sprite.Group()
#bad block list
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
all_sprites_list = pygame.sprite.Group()

#good blocks 
for i in range(50):
    
    block = Block(GREEN, 20, 15)
 
    block.rect.x = random.randrange(530)
    block.rect.y = random.randrange(screen_height)
 
    good_block_list.add(block)
    all_sprites_list.add(block)
    
#bad blocks
for i in range(50):
    # This represents a block
    block = Block(RED, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(530)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

#player
player = Player(BLUE, 20,15)
player.rect.x = 0
player.rect.y = 0

all_sprites_list.add(player)

#setting movement speed
x_speed = 0
y_speed = 0

#setting up game text 
font = pygame.font.SysFont('Calibri', 25, True, False)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        
        
        if event.type == pygame.KEYDOWN:
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
         
    player.rect.x += x_speed
    player.rect.y += y_speed
    #play bump sound when player hits edge
    if player.rect.x < 0:
       hit_edge.play()
    if player.rect.x > 530: 
       hit_edge.play() 
    if player.rect.y < 0:
       hit_edge.play() 
    if player.rect.y > 385:
       hit_edge.play()
    

    # Clear the screen
    screen.fill(WHITE)
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)

    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    #add a point if the player hits a good block
    for block in good_blocks_hit_list:
        score += 1
        block.reset_pos()
        good_sound.play()
        
    #take away score if player hits a bad block   
    for block in bad_blocks_hit_list:
        score -= 1
        block.reset_pos()
        bad_sound.play()

    #print score   
    text = font.render("Score:" + str(score),True,WHITE)
    pygame.draw.rect(screen,BLACK,[550,0,200,400])
    screen.blit(text, [580, 50])
    # Draw all the spites
    all_sprites_list.update()
    player.update()
    all_sprites_list.draw(screen)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
