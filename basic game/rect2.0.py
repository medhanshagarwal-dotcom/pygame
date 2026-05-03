import pygame

pygame.init()
SCREEEN_HEIGHT, SCREEN_WIDTH= 600, 500

win=pygame.display.set_mode(( SCREEN_WIDTH, SCREEEN_HEIGHT))
cap=pygame.display.set_caption('First image on pygame')



text=pygame.font.Font(None, 36).render("HEllO GUYS HOW ARE YOU",True, pygame.Color('white'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2, SCREEEN_HEIGHT//2 +150))

def game_loop():
    clock=pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pygame.draw.rect(win,(0, 125,255 ), pygame.Rect(150,200,70,60) )
        win.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
    game_loop()