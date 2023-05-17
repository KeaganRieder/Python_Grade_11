import pygame


class Player(pygame.sprite.Sprite):
    
     def __init__(self, color, width, height):
 
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        
     def update(self):
          if self.rect.x < 0:
               self.rect.x = 0
               
          if self.rect.x > 530:
               self.rect.x = 530
               
          if self.rect.y < 0:
               self.rect.y = 0
               
          if self.rect.y > 385:
               self.rect.y = 385
