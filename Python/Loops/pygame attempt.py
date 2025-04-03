import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.draw.rect(window, (255, 0, 0), (100, 100, 200, 200))
    pygame.display.update()

pygame.quit()