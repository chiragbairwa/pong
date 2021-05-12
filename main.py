import pygame
clock = pygame.time.Clock()
from random import randint as RI
#variables
WIDTH = 1200
HEIGHT = 600
BORDER = 30

fgcolor = pygame.Color('Grey')
bgcolor = pygame.Color('black')
PCOLOR =  pygame.Color('Violet')
BCOLOR =  pygame.Color('Orange')
VELOCITY = 1
FRAMERATE = 400
takey = 0
#OBJECTS
class paddle:
    HEIGHT = 100
    WIDTH = 20
    def __init__(self,y):
        self.y = y
        takey = y

    def show(self,color):
        pygame.draw.rect(screen, color, pygame.Rect((WIDTH-25,self.y),(self.WIDTH,self.HEIGHT)))

    def update(self):
        takey = self.y
        newy = pygame.mouse.get_pos()[1]
        if newy < HEIGHT-BORDER-self.HEIGHT and newy > BORDER:
            self.show(bgcolor)
            self.y = newy
            self.show(PCOLOR)

class ball:
    RADIUS = 20
    def __init__(self,x,y,vx,vy):
        self.x=WIDTH//2
        self.y=HEIGHT//2
        self.vx = vx
        self.vy = vy
        
    def show(self,color):
        pygame.draw.circle(screen, color,(self.x,self.y),self.RADIUS)
        
    def update(self):
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
            
        elif newy < BORDER + self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
            
        elif newx > WIDTH-BORDER-15:
            self.vx = -self.vx
        else:
            self.show(bgcolor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(BCOLOR)

#DRAW
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

ball1 = ball(WIDTH-ball.RADIUS,HEIGHT//2 , -VELOCITY,RI(-1,2)) 
pad   = paddle(HEIGHT//2)

pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(BORDER,HEIGHT)) )
pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)) )
ball1.show(BCOLOR)
pad.show(PCOLOR)


while True:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    pygame.display.flip()
    ball1.update()
    pad.update()
    
pygame.quit()

