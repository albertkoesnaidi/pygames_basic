import pygame
from sys import exit

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# Square 
square_1 = pygame.Rect(500,200, 50,50)
square_2 = pygame.Rect(400,500,250,50)

speed_x = 5
speed_y = 5
speed = 2

def animation():
    square_1.x += speed_x
    square_1.y += speed_y
    square_2.y += speed

def constrain():
    global speed_x, speed_y, speed
    if square_1.right >= screen_width or square_1.left <= 0:
        speed_x *= -1
    if square_1.top <= 0 or square_1.bottom >= screen_height:
        speed_y *= -1
    if square_2.top <= 0 or square_2.bottom >= screen_height:
        speed *= -1

def collision():
    global speed_y, speed_x
    if square_2.colliderect(square_1):
        if abs(square_1.bottom - square_2.top) <= 5 and speed_y > 0: #and square_1.top > square_2.bottom:
            speed_y *= -1
        if abs(square_1.top - square_2.bottom) <= 5 and speed_y < 0: #and square_1.top > square_2.bottom:
            speed_y *= -1
        if abs(square_1.left - square_2.right) <= 5 and speed_x < 0: #and square_1.top > square_2.bottom:
            speed_x *= -1
        if abs(square_1.right - square_2.left) <= 5 and speed_x > 0: #and square_1.top > square_2.bottom:
            speed_x *= -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    screen.fill('black')
    animation()
    constrain()
    collision()
    pygame.draw.rect(screen, (255,255,255), square_1)
    pygame.draw.rect(screen, (255,0,0), square_2)
    clock.tick(60)
