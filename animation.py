import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        sprites = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png', 'attack_7.png', 'attack_8.png', 'attack_9.png', 'attack_10.png']
        self.is_animate = False
        self.sprites=[]
        for i in range(len(sprites)):
            self.sprites.append(pygame.image.load('graphics/'+sprites[i]))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def animate(self):
        self.is_animate = True

            

    def update(self):
        if self.is_animate == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animate = False
            self.image = self.sprites[int(self.current_sprite)]

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

# Creating the sprites and groups
player_sprite = pygame.sprite.GroupSingle()
player = Player(10,10)
player_sprite.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.animate()


    screen.fill('black')
    player_sprite.draw(screen)
    player_sprite.update()
    pygame.display.flip()
    clock.tick(60)