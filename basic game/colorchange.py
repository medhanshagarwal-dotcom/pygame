import pygame

def main():
    pygame.init()
    h, w= 500, 500
    s=pygame.display.set_mode((h,w))
    pygame.display.set_caption('Second caption on pygame')
    color={'red':pygame.Color('red'),
           'green':pygame.Color('green'),
           'yellow':pygame.Color('yellow'),
           'blue':pygame.Color('blue'),
           'orange':pygame.Color('orange')}
    current_color= color['yellow']
    x, y=30,30
    sw,sh=60,60
    c=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        p=pygame.key.get_pressed()
        if p[pygame.K_LEFT]: 
            x-=3
        if p[pygame.K_RIGHT]: 
            x+=3
        if p[pygame.K_UP]: 
            y-=3
        if p[pygame.K_DOWN]: 
            y+=3
        
        x=min(max(0,x), w-sw)
        y=min(max(0,y), h-sh)
        
        if x==0:
            current_color=color['red']
        elif x==w-sw:
            current_color=color['green']
        elif y==0:
            current_color=color['blue']
        elif y==h-sh:
            current_color=color['orange']
        else:
            current_color=color['yellow']
        
        s.fill((0,0,0))
        pygame.draw.rect(s, current_color, (x, y, sw, sh))
        pygame.display.flip()
        c.tick(90)
    pygame.quit()
if __name__=='__main__':
    main()