import pygame, sys, random

def move_char2():
    window.blit(char2, (-40, -50))
    window.blit(char2, (char2_move + 630, 500))


pygame.init()

window = pygame.display.set_mode((630, 500))
clock = pygame.time.Clock()
bg = pygame.image.load('image_game/bg_pix1.png').convert_alpha()
bg = pygame.transform.scale2x(bg)

char1 = pygame.image.load('image_game/New Piskel.png').convert_alpha()
char1 = pygame.transform.scale2x(char1)
char2 = pygame.image.load('image_game/char1_5.0xl.png').convert_alpha()
char2_move = 0
ground = pygame.image.load('image_game/bg_px1.png').convert_alpha()
ground = pygame.transform.scale2x(ground)

# variables for movement
move_left = False
move_right = False
move_down = False
move_up = False
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.blit(bg, (0, 0))
    window.blit(char1, (55, -200))
    window.blit(ground, (-200, -250))
    # char2
    move_char2()
    char2_move += 1
    if char2_move <= -650:
        char2_move = 0
    pygame.display.update()
    clock.tick(120)
