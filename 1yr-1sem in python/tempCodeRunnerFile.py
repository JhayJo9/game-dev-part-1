
    Screen.blit(ground, [0,Screen_height+j])
    if j == Screen_height:
        j = 0
        j += 1
    pygame.display.update()
    clock.tic