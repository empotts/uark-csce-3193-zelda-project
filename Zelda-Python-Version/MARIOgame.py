import pygame
import time
from pygame.locals import*
from time import sleep 
from pygame import mixer 
# Sprite class for our Mario, Goomba, Pipe
class Sprite():
    def __init__(self,x,y,w,h,image):
        self.x = x
        self.y = y
        self.h = h 
        self.w = w
        self.image = pygame.image.load(image)
# Model class to initiate collision and update all the things on the page
class Model():
    def __init__(self):
        self.sprites = []
        # Adding Pipes to page 
        self.sprites.append(Pipe(25,100,55,400))
        self.sprites.append(Pipe(325,350,55,400))
        self.sprites.append(Pipe(625,400,55,400))
        self.sprites.append(Pipe(925,350,55,400))
        self.sprites.append(Pipe(1225,100,55,400))
        self.sprites.append(Pipe(1425,350,55,400))
        self.sprites.append(Pipe(1625,350,55,400))
        self.sprites.append(Pipe(1825,100,55,400))
        # Adding blocks
        i = 5 
        while i < 1905:
            self.sprites.append(Block(i,500,12,12))
            i += 40 
        # Adding Goombas
        self.sprites.append(Goomba(100,455,45,37))
        self.sprites.append(Goomba(425,455,45,37))
        self.sprites.append(Goomba(700,455,45,37))
        #Adding Mario
        self.mario = Mario(325,100,60,95)
        self.sprites.append(self.mario)
    # update function
    def update(self):
        for i in self.sprites:
            if isinstance(i,Goomba):
                i.goombaOldPos()
                if i.burnTime > 40:
                    self.sprites.remove(i)
            i.update()
            for j in self.sprites:
                # If mario and a pipe collide
                if isinstance(i,Mario) and isinstance (j,Pipe):
                    if self.collide(i,j):
                        self.mario.outPipe(j)
                if isinstance(i,Goomba) and isinstance (j,Pipe):
                    if self.collide(i,j):
                        i.outPipe(j)
                if isinstance(i,Fireball) and isinstance (j,Goomba):
                    if self.collide(i,j):
                        j.death()
            if isinstance(i,Fireball):
                self.removeFireball(i)
    def collide(self,a,b):
        if a.x + a.w < b.x:
            return False
        if a.x > b.x + b.w: 
            return False
        if a.y + a.h < b.y:
            return False
        if a.y > b.y + b.h:
            return False
        return True

    def addFireball(self,x,y):
        self.fireball = Fireball(x,y,47,47)
        self.sprites.append(self.fireball)

    def removeFireball(self,f):
        for i in self.sprites:
            if isinstance(i,Mario):
                if f.x > i.x + 1000:
                    self.sprites.remove(f)

class Mario(Sprite):
    def __init__(self,x,y,w,h):
        # initial the sprite
        super().__init__(x,y,w,h,"mario1.png")
        # Intiate base values
        self.vertVelocity = 12
        self.marioCount = 0
        self.currentImage = 0
        self.prevX = self.x
        self.prevY = self.y 
        # Mario images 
        self.mario_images = [] 
        self.mario1 = pygame.image.load("mario1.png")
        self.mario2 = pygame.image.load("mario2.png")
        self.mario3 = pygame.image.load("mario3.png")
        self.mario4 = pygame.image.load("mario4.png")
        self.mario5 = pygame.image.load("mario5.png")
        #Pushing them into mario_images array
        self.mario_images.append(self.mario1)
        self.mario_images.append(self.mario2)
        self.mario_images.append(self.mario3)
        self.mario_images.append(self.mario4)
        self.mario_images.append(self.mario5)
        # Make first image current image
        self.image = self.mario_images[self.currentImage]

    def update(self):
        self.image = self.mario_images[self.currentImage]
        self.marioCount += 1
        self.vertVelocity += 12
        self.y += self.vertVelocity
        # grav
        if self.y > 405:
            self.vertVelocity = 0
            self.y = 405
            self.marioCount = 0
        if self.y < 0: 
            self.y = 0

    def changeImage(self):
        self.currentImage += 1
        if self.currentImage > 4:
            self.currentImage = 0

    def marioOldPos(self): 
        self.prevX = self.x
        self.prevY = self.y

    def jump(self): 
        if self.marioCount < 4:
            self.vertVelocity -= 24
    
    def outPipe(self,p):
        if self.x + self.w >= p.x and self.prevX + self.w < p.x: 
            self.x = p.x - self.w -1
        if self.x <= p.x + p.w and self.prevX > p.x + p.w: 
            self.x = p.x + p.w + 1
        if self.y + self.h >= p.y and self.prevY + self.h < p.y:
            self.vertVelocity = 0
            self.marioCount = 0
            self.y = p.y - self.h - 1
        if self.y <= p.y + p.h and self.prevY > p.y + p.h: 
            self.y = p.y + p.h + 1
            self.vertVelocity = 0

class Goomba(Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, "goomba.png")
        # Intialize values
        self.vertVelocity = 6
        self.hortVelocity = 3
        self.currentImage = 0
        self.burnTime = 0
        self.prevX = self.x
        self.prevY = self.y
        # Put goomba images into the array
        self.goombaImages = []
        self.goomba = pygame.image.load("goomba.png")
        self.goombaFire = pygame.image.load("goomba_fire.png")
        # Pushing into array 
        self.goombaImages.append(self.goomba)
        self.goombaImages.append(self.goombaFire)

    def update(self):
        self.image = self.goombaImages[self.currentImage]
        self.x = self.x + self.hortVelocity
        # If burning
        if self.currentImage == 1:
            self.burnTime += 1
        #grav 
        self.vertVelocity += 12
        self.y += self.vertVelocity
        if self.y > 455:
            self.vertVelocity = 0
            self.y = 455
        return True

    def goombaOldPos(self): 
        self.prevX = self.x
        self.prevY = self.y

    def outPipe(self,p):
        if self.x + self.w >= p.x and self.prevX + self.w < p.x: 
            self.x = p.x - self.w -1
            self.hortVelocity *= -1
        if self.x <= p.x + p.w and self.prevX > p.x + p.w: 
            self.x = p.x + p.w + 1
            self.hortVelocity *= -1
        if self.y + self.h >= p.y and self.prevY + self.h < p.y:
            self.vertVelocity = 0
            self.marioCount = 0
            self.y = p.y - self.h - 1
        if self.y <= p.y + p.h and self.prevY > p.y + p.h: 
            self.y = p.y + p.h + 1
            self.vertVelocity = 0

    def death(self):
        self.currentImage = 1
        self.hortVelocity = 0
        self.burnTime += 1

class Pipe(Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, "pipe.png")
    def update(self):
        return True

class Block(Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h,"block.png")
    def update(self):
        return True

class Fireball(Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h,"fireball.png")
        self.vertVelocity = 6
        self.hortVelocity = 12
    def update(self):
        self.x += self.hortVelocity
        self.vertVelocity += 6
        self.y += self.vertVelocity
        if self.y > 450:
            self.y = 450
            self.vertVelocity -= 60

class View():
    def __init__(self,model):
        screen_size = (800,540)
        self.screen = pygame.display.set_mode(screen_size,32) 
        self.background_image = pygame.image.load("background.png")
        mixer.music.load("RetroTuskNES.wav")
        mixer.music.set_volume(0.01)
        mixer.music.play(-1)
        self.model = model
    
    def update(self):
        self.screen.fill([173,216,230])
        self.screen.blit(self.background_image,(0,0))

        for sprite in self.model.sprites:
            if isinstance(sprite,Mario):
                self.screen.blit(sprite.image, (50, sprite.y))
            else:
                self.screen.blit(sprite.image, ((sprite.x - self.model.mario.x + 50), sprite.y))
        pygame.display.flip()

class Controller():
    def __init__(self,model): 
        self.model = model
        self.keep_going = True

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keep_going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keep_going = False
                if event.key == K_SPACE:
                    self.keep_going = True
                if event.key == K_LCTRL: 
                    self.fireball_press = True
            elif event.type == KEYUP:
                if event.key == K_LCTRL:
                    self.model.addFireball(self.model.mario.x + self.model.mario.w - 20, self.model.mario.y)
        keys = pygame.key.get_pressed()
        self.model.mario.marioOldPos()
        if keys[K_LEFT]:
            self.model.mario.x -= 8
            self.model.mario.changeImage()
        if keys[K_RIGHT]:
            self.model.mario.x += 8
            self.model.mario.changeImage()
        if keys[K_SPACE]:
            self.model.mario.jump()

print("Use the arrow keys to move and space to jump! Press Ctrl to shoot FIREBALLS! Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
    c.update()
    m.update()
    v.update()
    sleep(0.04)
print("Goodbye")