import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            button_press_time = pygame.time.get_ticks()
            screen.fill('white')
        


    print(f'current time: {current_time}, button time: {button_press_time}')
    if current_time - button_press_time > 2000:
        screen.fill('black')
    pygame.display.flip()
    clock.tick(30)

