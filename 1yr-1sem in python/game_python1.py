import pygame, sys, random

def funcroad():
    windows.blit(road, (road_pos, 170))
    windows.blit(road, (road_pos + 600, 170))

pygame.init()

windows = pygame.display.set_mode((600, 650))
clock = pygame.time.Clock()
title = pygame.image.load('image_game/New Piskel-1.png (4).png')
title = pygame.transform.scale2x(title).convert_alpha()

# bg_window = pygame.image.load('image_game/bg.png').convert()
# bg_window = pygame.transform.scale2x(bg_window)

road = pygame.image.load('image_game/New Piskel-1.png (7).png').convert_alpha()
road = pygame.transform.scale2x(road)
road_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # windows.blit(bg_window, (0, 0))
    windows.blit(title, (-50, -80))

    road_pos += 1.11
    funcroad()
    if road_pos <= -600:
        road_pos = 0

    pygame.display.update()
    clock.tick(120)

