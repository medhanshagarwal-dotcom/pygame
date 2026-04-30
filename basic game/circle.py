import pygame

pygame.init()

x=pygame.display.set_mode((700, 700))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(x, (123, 234, 0), (100, 100), 50, 3)
    pygame.draw.circle(x, (25, 255, 55), (300, 300), 50)
    pygame.display.flip()
