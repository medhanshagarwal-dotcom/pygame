import pygame
import random

sw, sh = 500, 500
ms=3
fs=72

pygame.init()
img=pygame.transform.scale(pygame.image.load('C:/medhansh/python/advanced/pygame/images and stuff/bg.jpg'), (sh, sw))

f=pygame.font.SysFont("Times New Roman", fs)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, c, h, w):
        super().__init__()
        self.image=pygame.Surface([w, h])
        self.image.fill("Dodgerblue")
        pygame.draw.rect(self.image ,c, pygame.Rect(0,0,h, w))
        self.rect = self.image.get_rect()
    def move(self, x_c , y_c):
        self.rect.x=x_c
        self.rect.y=y_c
        self.rect.x=min(max(0,self.rect.x), self.rect.w-sw)
        self.rect.y=min(max(0,self.rect.y), self.rect.h-sh)

screen=pygame.display.set_mode((sw, sh))
pygame.display.set_caption('sprite collision')

all_sprite=pygame.sprite.Group()

sp1=Sprite(pygame.Color('Black'),20 ,30)
sp1.rect.x=random.randint(0, 480)
sp1.rect.y=random.randint(0, 370)
all_sprite.add(sp1)
sp2=Sprite(pygame.Color('Red'),20 ,30)
sp2.rect.x=random.randint(0, 480)
sp2.rect.y=random.randint(0, 370)
all_sprite.add(sp2)
running=True
won=False
c=pygame.time.Clock()

# Main game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
      running = False

  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * ms
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * ms
    sp1.move(x_change, y_change)

    if sp1.rect.colliderect(sp2.rect):
      all_sprite.remove(sp2)
      won = True
    screen.blit(img, (0, 0))
    all_sprite.draw(screen)
    if won:
       t=f.render("You win", True, pygame.Color('Black'))
       screen.blit(t, (30, 30))
    pygame.display.flip()
    c.tick(90)
pygame.quit()