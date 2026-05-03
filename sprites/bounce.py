import pygame
import random

pygame.init()

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
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==sprite_color_change_event:
            spl.change_color()
        elif event.type==background_color_change_event:
            change_background_color()
    all_sprite_list.update()
    screen.fill(bg_color)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()