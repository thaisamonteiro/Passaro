import pygame

pygame.init()
window = pygame.display.set_mode(size=(500, 700))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # end pygame