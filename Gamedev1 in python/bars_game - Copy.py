
import math
import pygame, sys, random


pygame.init()
clock = pygame.time.Clock()

width = 70

# variables for screen 
Screen = pygame.display.set_mode((800, 400)) # resizing window / width = 800, height = 400
name1 = pygame.display.set_caption("create by Jaehwan")
icon = pygame.image.load('image_game/sedan.png')
pygame.display.set_icon(icon)
# title
title = pygame.image.load('image_game/title1.png').convert_alpha()
title_width = title.get_width()
title_img = pygame.transform.scale(title, (500, 400)) # resizing img
title_rect = title.get_width()

# moving image
ground = pygame.image.load('image_game/road1_1.png').convert()
ground_width = ground.get_width()
ground_img = pygame.transform.scale(ground, (600, 70)) # resizing img
ground_rect = ground.get_width()

# car
car_x = 50
car_y = 250
car_changex = 0
def carfunc(x,y):
    Screen.blit(car_img, (x, y)) # postion for img
    
# dimensios for car
car = pygame.image.load('image_game/car2_2.png').convert_alpha()
car_width = car.get_width()
car_img = pygame.transform.scale(car, (210, 180)) # resizing img
car_rect = car.get_width()

#
scroll1 = 0
scroll2 = 0
scroll3 = 0
panels = math.ceil(width / ground_width) + 2

# obs
obs_x = random.randint(0, 800)
obs_y = random.randint(200, 280)
obs_changex = 0
obs = pygame.image.load('image_game/obs1.png').convert_alpha()
obs_width = obs.get_width()
obs_img = pygame.transform.scale(obs, (210, 180)).convert_alpha()
obs_ret = obs.get_width()


# background img
bg = pygame.image.load('image_game/bg1_1.png').convert_alpha()
bg_width = bg.get_width()
bg_img = pygame.transform.scale(bg, (250, 330)) # resizing img
bg_rect = bg.get_width()


run = True
while run:
    clock.tick(120)
    
    for x in range(120):
        # Screen.blit(ground_img, (0, 330)) # position for ground img
        Screen.blit(ground_img, (x * ground_width + scroll1 - ground_width, 330))
    for bg_x in range(120):
        Screen.blit(bg_img, (bg_x * bg_width + scroll2 - bg_width, 0)) # position for img
    for j in range(120):
        Screen.blit(obs_img, (j * obs_x + scroll3 - obs_x, obs_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        # controller
        if event.type == pygame.KEYDOWN:
            print("pressed")
            if event.key == pygame.K_LEFT:
                car_changex = -1
            if event.key == pygame.K_RIGHT:
                car_changex = 1
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_changex = 0

    car_x += car_changex
    if car_x <= 0:
        car_x = 0
    elif car_x >= 600:
        car_x = 600
   
   # Screen.fill((255, 255, 255,255)) color background
   # car function
   # car_x += 0.1
    
   # functions
    carfunc(car_x,car_y)
    
    scroll1 -= 1
    if abs(scroll1) > ground_width:
        scroll1 = 0

    scroll2 -= 1
    if abs(scroll2) > bg_width:
        scroll2 = 0

    scroll3 -= 1
    if abs(scroll3) > obs_x:
        for In in range(scroll3):
            obs_x = random.randint(0, 800)

    # Screen.blit(obs_img, (obs_x, obs_y)) # postion for img
    Screen.blit(title, (280, -140))
    pygame.display.flip()
pygame.quit  
