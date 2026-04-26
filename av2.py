import pygame

pygame.init()
SCREEEN_HEIGHT, SCREEN_WIDTH= 600, 500

win=pygame.display.set_mode(( SCREEN_WIDTH, SCREEEN_HEIGHT))
cap=pygame.display.set_caption('First image on pygame')

img=pygame.transform.scale(pygame.image.load('C:/medhansh/python/advanced/pygame/images and stuff/download (1).jpg').convert_alpha(), (200,200))
img2=pygame.transform.scale(pygame.image.load('C:/medhansh/python/advanced/pygame/images and stuff/images.jpg').convert(), (SCREEEN_HEIGHT, SCREEN_WIDTH))

img_rect=img.get_rect(center=(SCREEN_WIDTH//2, SCREEEN_HEIGHT//2 -30))

text=pygame.font.Font(None, 36).render("HEllO GUYS HOW ARE YOU",True, pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2, SCREEEN_HEIGHT//2 +150))

def game_loop():
    clock=pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        win.blit(img2,(0,0))
        win.blit(img,img_rect)
        win.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
    game_loop()

