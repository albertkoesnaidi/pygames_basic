import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((75,75)) 
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        
    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.Surface((50,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (x,y))

    def update(self):
        self.rect.x +=5
        if self.rect.x >= screen_width + 50:
            self.kill()
            


pygame.init()
screen_width, screen_height = 800,800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player()
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(player)

bullet_sprite = pygame.sprite.Group()


pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_sprite.add(player.create_bullet())
    
    pygame.display.flip()
    screen.fill('black')
    bullet_sprite.draw(screen)
    player_sprite.draw(screen)
    
    player_sprite.update()
    bullet_sprite.update()
    print(bullet_sprite)
    clock.tick(60)
