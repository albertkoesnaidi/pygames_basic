import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/link.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400,400))
        self.health = 5
        self.max_health = 10
    
    def get_damage(self):
        if self.health > 0:
            self.health -= 1

    def get_health(self):
        if self.health < self.max_health:
            self.health += 1

    def full_hearts(self):
        for i in range(self.health):
            screen.blit(full_heart, (i *50,45))
    
    def empty_hearts(self):
        for i in range(self.max_health):
            if i < self.health:
                screen.blit(full_heart, (i * 50, 80))
            else:
                screen.blit(empty_heart, (i* 50, 80))
    
    def half_hearts(self):
        half_hearts_total = self.health/2
        half_heart_exists = half_hearts_total - int(half_hearts_total) != 0

        for i in range(int(self.max_health/2)):
            if int(half_hearts_total) > i:
                screen.blit(full_heart, (i * 50, 160))
            elif half_heart_exists & (int(half_hearts_total) == i):
                screen.blit(half_heart, (i * 50, 160))
            else:
                screen.blit(empty_heart, (i * 50, 160))

    def update(self):
        self.full_hearts()
        self.empty_hearts()
        self.half_hearts()

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

player = Player()
link = pygame.sprite.GroupSingle()
link.add(player)

full_heart = pygame.image.load('graphics/full_heart.png').convert_alpha()
half_heart = pygame.image.load('graphics/half_heart.png').convert_alpha()
empty_heart = pygame.image.load('graphics/empty_heart.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                link.sprite.get_health()
            if event.key == pygame.K_DOWN:
                link.sprite.get_damage()
    
    screen.fill((30,30,30))
    link.draw(screen)
    link.update()
    pygame.display.update()
    
    
    clock.tick(60)