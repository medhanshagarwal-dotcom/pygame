import pygame
import random

pygame.init()
h, w= 400, 500
sprite_color_change_event=pygame.USEREVENT+1
background_color_change_event=pygame.USEREVENT+2

blue= pygame.Color('blue')
green=pygame.Color('green')
red=pygame.Color('red')

yellow=pygame.Color('yellow')
black=pygame.Color('black')
white=pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.vel= [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):

        self.rect.move_ip(self.vel)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.vel[0]= -self.vel[0]
            boundary_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.vel[1]= -self.vel[1]
            boundary_hit=True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))
    def change_color(self):
        self.image.fill(random.choice([yellow, black, white]))

def change_background_color():
    global bg_color
    bg_color=random.choice([red, green, blue])

all_sprite_list=pygame.sprite.Group()
spl=Sprite(white, 20 ,30)
spl.rect.x=random.randint(0, 480)
spl.rect.y=random.randint(0, 370)
all_sprite_list.add(spl)

screen=pygame.display.set_mode((500, 400))
pygame.display.set_caption('Bouncing sprite')

bg_color=red
screen.fill(bg_color)
exit=False

clock=pygame.time.Clock()
x, y=30,30
sw,sh=60,60
while not exit:
    color={'red':pygame.Color('red'),
           'green':pygame.Color('green'),
           'yellow':pygame.Color('yellow'),
           'blue':pygame.Color('blue'),
           'orange':pygame.Color('orange')}
    current_color= color['yellow']
    c=pygame.time.Clock()
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            elif event.type==sprite_color_change_event:
                spl.change_color()
            elif event.type==background_color_change_event:
                change_background_color()
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
            change_background_color()
            x+=3
    elif x==w-sw:
            current_color=color['green']
            change_background_color()
            x-=3
    elif y==0:
            current_color=color['blue']
            change_background_color()
            y+=3
    elif y==h-sh:
            current_color=color['orange']
            change_background_color()
            y-=3
    else:
            current_color=color['yellow']
    screen.fill(bg_color)
    pygame.draw.rect(screen, current_color, (x, y, sw, sh))
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()