
import math
import pygame, sys, random


pygame.init()
clock = pygame.time.Clock()

width = 70

# variables for screen 
Screen = pygame.display.set_mode((300, 400))
# moving image
ground = pygame.image.load('image_game/ground_move1.1.png').convert()
ground_width = ground.get_width()
ground_img = pygame.transform.scale(ground, (600, 70))
ground_rect = ground.get_width()

car = pygame.image.load('image_game/car1_1.png').convert_alpha()
car_width = car.get_width()
car_img = pygame.transform.scale(car, (210, 130))
car_rect = car.get_width()
scroll = 0
panels = math.ceil(width / ground_width) + 2

run = True
while run:
    clock.tick(120)

    for x in range(120):
        # Screen.blit(ground_img, (0, 330)) # position for ground img
        Screen.blit(ground_img, (x * ground_width + scroll - ground_width, 330))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
   # Screen.fill((255, 255, 255,255))
    scroll -= 5
    if abs(scroll) > ground_width:
        scroll = 0
    
    Screen.blit(car_img, (30, 285))
    pygame.display.flip()
pygame.quit  
