import pygame

pygame.init()

x=pygame.display.set_mode((300, 300))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(x,(0, 125,255 ), pygame.Rect(30,30,70,60) )
    
    pygame.display.flip()