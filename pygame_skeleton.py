

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('This is a configurable title')

clock = pygame.time.Clock()

still_playing = True

while still_playing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_playing = False

        print(event)

    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()