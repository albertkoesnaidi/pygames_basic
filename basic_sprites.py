import pygame
from sys import exit
import random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('png_shootgame/HUD/crosshair_red_small.png')
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('audio/audio_laser.wav')
    
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group,dokill=True)
    
    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self,file, x,y):
        super().__init__()
        filepath = 'png_shootgame/Objects/duck_target_'+ file + '.png'
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    
class GameState:
    def __init__(self):
        self.game_state = 'intro'

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
        
        pygame.display.flip()
        screen.blit(bg,(0,0))
        target_group.add(new_target)
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
                if crosshair.rect.colliderect(ready_text_rect):
                    self.game_state = 'main_game'
                    self.main_game()

        screen.blit(intro,(0,0))
        screen.blit(ready_text, ready_text_rect)    
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()
    
    def state_manager(self):
        if self.game_state == 'intro':
            self.intro()
        elif self.game_state == 'main_game':
            self.main_game()

pygame.init()
screen_width = 1280
screen_height = 780
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

gamestate = GameState()

# Background
bg = pygame.image.load('png_shootgame/Stall/bg_wood.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))
intro = pygame.image.load('png_shootgame/Stall/bg_blue.png')
intro = pygame.transform.scale(intro, (screen_width, screen_height))
ready_text = pygame.image.load('png_shootgame/HUD/text_ready.png')
ready_text_rect = ready_text.get_rect(center =(screen_width/2, screen_height/2))

# Crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.GroupSingle(crosshair)

# Target
target_group = pygame.sprite.Group()
for i in range(20):
    new_target = Target(random.choice(['brown', 'white', 'yellow']), random.randrange(0,screen_width), random.randrange(0,screen_height))
    target_group.add(new_target)

pygame.mouse.set_visible(False)

while True:
    gamestate.state_manager()
    clock.tick(60)