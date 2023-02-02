import math
import pygame, sys, random

pygame.init()
class CarClass(object):
    def __init__(self, car_x, car_y, car_changex, car_changey):
        self.car_x = car_x
        self.car_y = car_y
        self.car_changex = car_changex
        self.car_changey = car_changey
    def limit_w_h(self,Screen):
        car_val.car_x += car_val.car_changex
        if car_val.car_x <= 0:
            car_val.car_x = 0
        elif car_val.car_x >= 600:  # width from left to right
            car_val.car_x = 600
        car_val.car_y += car_val.car_changey
        if car_val.car_y <= 220:  # height from to top to bottom / like limitations
            car_val.car_y = 220
        elif car_val.car_y >= 288:
            car_val.car_y = 288
            print("car is heigth: ", car_val.car_y)

class moving_img(object):
    def __init__(self, scroll1, scroll2, scroll3):
        self.scroll1 = scroll1
        self.scroll2 = scroll2
        self.scroll3 = scroll3
    def conditon_to_scrollIMg(self, Screen):
        moving_img_val.scroll1 -= 1
        if abs(moving_img_val.scroll1) > ground_width:
            moving_img_val.scroll1 = 0
        moving_img_val.scroll2 -= 1
        if abs(moving_img_val.scroll2) > bg_width:
            moving_img_val.scroll2 = 0

clock = pygame.time.Clock()
width = 70
# variables for screen
Screen = pygame.display.set_mode((800, 400))  # resizing window / width = 800, height = 400
name1 = pygame.display.set_caption("create by Jaehwan")
icon = pygame.image.load('image_game/sedan.png')
pygame.display.set_icon(icon)

# title
title = pygame.image.load('image_game/title1.png').convert_alpha()
title_width = title.get_width()
title_img = pygame.transform.scale(title, (500, 400))  # resizing img
title_rect = title.get_width()

# moving image
ground = pygame.image.load('image_game/road1_1.png').convert()
ground_width = ground.get_width()
ground_img = pygame.transform.scale(ground, (600, 70))  # resizing img
ground_rect = ground.get_width()

# car
def carfunc(x, y):
    Screen.blit(car_img, (x, y))  # postion for img

car = pygame.image.load('image_game/car2_2.png').convert_alpha()
car_width = car.get_width()
car_img = pygame.transform.scale(car, (160, 150))  # resizing img
car_rect = car.get_width()

# obs
def create_obs():
    random_obs_pos = random.choice(obs_height)
    buttom_obs = obs_img.get_rect(midright=(900, random_obs_pos))
    top_obs = obs_img.get_rect(midbottom=(900, obs_y - 310))
    return buttom_obs, top_obs


def move_obs(obstacles):
    for obstacle in obstacles:
        obstacle.centerx -= 1
    return obstacles


def draw_obs(obstacles):
    for obstacle in obstacles:
        Screen.blit(obs_img, obstacle)


obs_x = random.randint(0, 1000)
obs_y = random.randint(500, 1080)
obs_changex = 0

obs = pygame.image.load('image_game/obs1.png').convert_alpha()
obs_width = obs.get_width()
obs_img = pygame.transform.scale(obs, (210, 130)).convert_alpha()
obs_list = []
obs_height = [340, 320]  # [260, 255, 230, 320]
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 2000)

# background img
bg = pygame.image.load('image_game/bg1_1.png').convert_alpha()
bg_width = bg.get_width()
bg_img = pygame.transform.scale(bg, (250, 330))  # resizing img
bg_rect = bg.get_width()

# functions
car_val = CarClass(50, 270, 0, 0)  # x, y, changex, changey
moving_img_val = moving_img(0, 0, 0)
run = True
while run:
    clock.tick(120)
    for x in range(120):
        Screen.blit(ground_img, (x * ground_width + moving_img_val.scroll1 - ground_width, 330))
    for bg_x in range(120):
        Screen.blit(bg_img, (bg_x * bg_width + moving_img_val.scroll2 - bg_width, 0))  # position for img
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

        # controller
        if event.type == pygame.KEYDOWN:
            print("pressed")
            if event.key == pygame.K_LEFT:
                car_val.car_changex = -0.50
                print("pressed left")
            if event.key == pygame.K_RIGHT:
                car_val.car_changex = .50
                print("pressed right")
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_val.car_changex = 0

        if event.type == pygame.KEYDOWN:
            print("pressed")
            if event.key == pygame.K_UP:
                car_val.car_changey = -1
                print("pressed up")
            if event.key == pygame.K_DOWN:
                car_val.car_changey = 1
                print("pressed down")
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_val.car_changey = 0

        if event.type == spawnpipe:
            obs_list.extend(create_obs())

    # car
    car_val.limit_w_h(Screen)
    carfunc(car_val.car_x, car_val.car_y)
    # moving img
    moving_img_val.conditon_to_scrollIMg(Screen)
    # obs
    obs_list = move_obs(obs_list)
    draw_obs(obs_list)

    # title
    Screen.blit(title, (280, -140))
    pygame.display.flip()
pygame.quit
