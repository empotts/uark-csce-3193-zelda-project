#Ethan Potts
#CSCE 3193 Assignment 8
#05-04-2023
#Assignment Description: This assignment creates the Zelda game using Python


import pygame
import time

from pygame.locals import*
from time import sleep


class Sprite:
    def __init__(self, x, y, url):
        self.x = x
        self.y = y
        self.url = url
    def update(self):
        pass

class Link(Sprite):
    def __init__(self, x, y, image_url):
        super().__init__(x, y, image_url)
        self.image = pygame.image.load(self.url)
        self.prevX = x
        self.prevY = y
        self.numLinkImages = 50
        self.currentLinkImage = 0
        self.linkImages = []
        self.w = 45
        self.h = 45
        self.direction = 0

        for i in range(1,51):
            if(i<10):
                pathname = "Images/link0" + str(i) + ".png"
                tempImage = pygame.image.load(pathname)
                tempImage = pygame.transform.scale(tempImage,(50,50))
                self.linkImages.append(tempImage)
            if(i>=10):
                pathname = "Images/link" + str(i) + ".png"
                tempImage = pygame.image.load(pathname)
                tempImage = pygame.transform.scale(tempImage,(50,50))
                self.linkImages.append(tempImage)

    def update(self):
        self.image = self.linkImages[self.currentLinkImage]
        self.prevX = self.x
        self.prevY = self.y
    
    def cycleDown(self):
        if(self.currentLinkImage < 5 or self.currentLinkImage >= 12):
            self.currentLinkImage = 5
        self.currentLinkImage += 1
        self.direction = 0

    def cycleLeft(self):
        if(self.currentLinkImage < 13 or self.currentLinkImage >= 22):
            self.currentLinkImage = 13
        self.currentLinkImage += 1
        self.direction = 1

    def cycleRight(self):
        if(self.currentLinkImage < 29 or self.currentLinkImage >= 37):
            self.currentLinkImage = 29
        self.currentLinkImage += 1
        self.direction = 3

    def cycleUp(self):
        if(self.currentLinkImage < 39 or self.currentLinkImage >= 49):
            self.currentLinkImage = 39
        self.currentLinkImage += 1
        self.direction = 2
    

class Tile(Sprite):
    def __init__(self, x, y, url):
        super().__init__(x, y, url)
        self.w = 50
        self.h = 50
        self.image = pygame.image.load(self.url)
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
    def update(self):
        pass

class Pot(Sprite):
    def __init__(self, x, y, url):
        super().__init__(x, y, url)
        self.w = 30
        self.h = 30
        self.sent = False
        self.isBroke = False
        self.framesLeft = 20
        self.direction = 0
        self.speed = 11
        self.image = pygame.image.load(self.url)
        self.image = pygame.transform.scale(self.image,(self.w,self.h))

    def sendPot(self, direction):
        self.sent = True
        self.direction = direction
        
    def update(self):
        if self.isBroke:
            self.image = pygame.image.load("Images/pot_broken.png")
            self.framesLeft -= 1
            self.speed = 0;
        if self.sent:
            if self.direction == 0:
                self.y += self.speed
            if self.direction == 1:
                self.x -= self.speed
            if self.direction == 2:
                self.y -= self.speed
            if self.direction == 3:
                self.x += self.speed

class Boomerang(Sprite):
    def __init__(self, x, y, url,direction):
        super().__init__(x, y, url )
        self.w = 20
        self.h = 20
        self.isActive = True
        self.speed = 11
        self.direction = direction
        self.image = pygame.image.load(self.url)
        self.image = pygame.transform.scale(self.image,(self.w,self.h))

    def update(self):
        if self.direction == 0:
            self.y += self.speed
        if self.direction == 1:
            self.x -= self.speed
        if self.direction == 2:
            self.y -= self.speed
        if self.direction == 3:
            self.x += self.speed

class Model():
    def __init__(self):
        self.sprites = []
        self.link = Link(100,100,"Images/link01.png")
        self.sprites.append(self.link)
        tileURL = "Images/tile.jpg"
        potURL = "Images/pot.png"
        self.sprites.append( Tile( 0, 0,tileURL)); self.sprites.append( Tile( 50, 0,tileURL)); self.sprites.append( Tile( 100, 0,tileURL)); self.sprites.append( Tile( 150, 0,tileURL)); self.sprites.append( Tile( 200, 0,tileURL)); self.sprites.append( Tile( 250, 0,tileURL)); self.sprites.append( Tile( 300, 0,tileURL)); self.sprites.append( Tile( 350, 0,tileURL)); self.sprites.append( Tile( 400, 0,tileURL)); self.sprites.append( Tile( 450, 0,tileURL)); self.sprites.append( Tile( 500, 0,tileURL)); self.sprites.append( Tile( 550, 0,tileURL)); self.sprites.append( Tile( 600, 0,tileURL)); self.sprites.append( Tile( 650, 0,tileURL)); self.sprites.append( Tile( 0, 50,tileURL)); self.sprites.append( Tile( 0, 100,tileURL)); self.sprites.append( Tile( 0, 150,tileURL)); self.sprites.append( Tile( 0, 200,tileURL)); self.sprites.append( Tile( 0, 250,tileURL)); self.sprites.append( Tile( 0, 350,tileURL)); self.sprites.append( Tile( 0, 300,tileURL)); self.sprites.append( Tile( 0, 400,tileURL)); self.sprites.append( Tile( 0, 450,tileURL)); self.sprites.append( Tile( 0, 500,tileURL)); self.sprites.append( Tile( 0, 550,tileURL)); self.sprites.append( Tile( 0, 600,tileURL)); self.sprites.append( Tile( 0, 650,tileURL)); self.sprites.append( Tile( 0, 700,tileURL)); self.sprites.append( Tile( 0, 750,tileURL)); self.sprites.append( Tile( 0, 800,tileURL)); self.sprites.append( Tile( 0, 850,tileURL)); self.sprites.append( Tile( 0, 900,tileURL)); self.sprites.append( Tile( 0, 950,tileURL)); self.sprites.append( Tile( 50, 950,tileURL)); self.sprites.append( Tile( 100, 950,tileURL)); self.sprites.append( Tile( 150, 950,tileURL)); self.sprites.append( Tile( 200, 950,tileURL)); self.sprites.append( Tile( 250, 950,tileURL)); self.sprites.append( Tile( 300, 950,tileURL)); self.sprites.append( Tile( 350, 950,tileURL)); self.sprites.append( Tile( 400, 950,tileURL)); self.sprites.append( Tile( 450, 950,tileURL)); self.sprites.append( Tile( 500, 950,tileURL)); self.sprites.append( Tile( 550, 950,tileURL)); self.sprites.append( Tile( 600, 950,tileURL)); self.sprites.append( Tile( 650, 950,tileURL)); self.sprites.append( Tile( 650, 900,tileURL)); self.sprites.append( Tile( 600, 900,tileURL)); self.sprites.append( Tile( 500, 900,tileURL)); self.sprites.append( Tile( 550, 900,tileURL)); self.sprites.append( Tile( 450, 900,tileURL)); self.sprites.append( Tile( 350, 900,tileURL)); self.sprites.append( Tile( 400, 900,tileURL)); self.sprites.append( Tile( 300, 900,tileURL)); self.sprites.append( Tile( 200, 900,tileURL)); self.sprites.append( Tile( 250, 900,tileURL)); self.sprites.append( Tile( 150, 900,tileURL)); self.sprites.append( Tile( 100, 900,tileURL)); self.sprites.append( Tile( 50, 900,tileURL)); self.sprites.append( Tile( 700, 950,tileURL)); self.sprites.append( Tile( 750, 950,tileURL)); self.sprites.append( Tile( 850, 950,tileURL)); self.sprites.append( Tile( 1050, 950,tileURL)); self.sprites.append( Tile( 1000, 950,tileURL)); self.sprites.append( Tile( 900, 950,tileURL)); self.sprites.append( Tile( 950, 950,tileURL)); self.sprites.append( Tile( 800, 950,tileURL)); self.sprites.append( Tile( 700, 900,tileURL)); self.sprites.append( Tile( 750, 900,tileURL)); self.sprites.append( Tile( 800, 900,tileURL)); self.sprites.append( Tile( 850, 900,tileURL)); self.sprites.append( Tile( 900, 900,tileURL)); self.sprites.append( Tile( 1000, 900,tileURL)); self.sprites.append( Tile( 950, 900,tileURL)); self.sprites.append( Tile( 1050, 900,tileURL)); self.sprites.append( Tile( 1100, 900,tileURL)); self.sprites.append( Tile( 1100, 950,tileURL)); self.sprites.append( Tile( 1150, 900,tileURL)); self.sprites.append( Tile( 1150, 950,tileURL)); self.sprites.append( Tile( 1200, 900,tileURL)); self.sprites.append( Tile( 1200, 950,tileURL)); self.sprites.append( Tile( 1250, 900,tileURL)); self.sprites.append( Tile( 1250, 950,tileURL)); self.sprites.append( Tile( 1300, 900,tileURL)); self.sprites.append( Tile( 1300, 950,tileURL)); self.sprites.append( Tile( 1350, 950,tileURL)); self.sprites.append( Tile( 1350, 900,tileURL)); self.sprites.append( Tile( 1350, 850,tileURL)); self.sprites.append( Tile( 1350, 800,tileURL)); self.sprites.append( Tile( 1350, 750,tileURL)); self.sprites.append( Tile( 1350, 700,tileURL)); self.sprites.append( Tile( 1350, 600,tileURL)); self.sprites.append( Tile( 1350, 650,tileURL)); self.sprites.append( Tile( 1350, 550,tileURL)); self.sprites.append( Tile( 1350, 500,tileURL)); self.sprites.append( Tile( 1350, 450,tileURL)); self.sprites.append( Tile( 1350, 400,tileURL)); self.sprites.append( Tile( 1350, 350,tileURL)); self.sprites.append( Tile( 1350, 300,tileURL)); self.sprites.append( Tile( 1350, 250,tileURL)); self.sprites.append( Tile( 1350, 200,tileURL)); self.sprites.append( Tile( 1350, 150,tileURL)); self.sprites.append( Tile( 1350, 100,tileURL)); self.sprites.append( Tile( 1350, 50,tileURL)); self.sprites.append( Tile( 1350, 0,tileURL)); self.sprites.append( Tile( 1250, 0,tileURL)); self.sprites.append( Tile( 1300, 0,tileURL)); self.sprites.append( Tile( 1200, 0,tileURL)); self.sprites.append( Tile( 1150, 0,tileURL)); self.sprites.append( Tile( 1050, 0,tileURL)); self.sprites.append( Tile( 1100, 0,tileURL)); self.sprites.append( Tile( 1000, 0,tileURL)); self.sprites.append( Tile( 900, 0,tileURL)); self.sprites.append( Tile( 950, 0,tileURL)); self.sprites.append( Tile( 850, 0,tileURL)); self.sprites.append( Tile( 800, 0,tileURL)); self.sprites.append( Tile( 750, 0,tileURL)); self.sprites.append( Tile( 700, 0,tileURL)); self.sprites.append( Tile( 50, 400,tileURL)); self.sprites.append( Tile( 100, 400,tileURL)); self.sprites.append( Tile( 150, 400,tileURL)); self.sprites.append( Tile( 200, 400,tileURL)); self.sprites.append( Tile( 250, 400,tileURL)); self.sprites.append( Tile( 400, 400,tileURL)); self.sprites.append( Tile( 450, 400,tileURL)); self.sprites.append( Tile( 500, 400,tileURL)); self.sprites.append( Tile( 550, 400,tileURL)); self.sprites.append( Tile( 600, 400,tileURL)); self.sprites.append( Tile( 650, 400,tileURL)); self.sprites.append( Tile( 650, 350,tileURL)); self.sprites.append( Tile( 650, 300,tileURL)); self.sprites.append( Tile( 650, 50,tileURL)); self.sprites.append( Tile( 650, 100,tileURL)); self.sprites.append( Tile( 700, 50,tileURL)); self.sprites.append( Tile( 700, 100,tileURL)); self.sprites.append( Tile( 700, 300,tileURL)); self.sprites.append( Tile( 700, 350,tileURL)); self.sprites.append( Tile( 700, 400,tileURL)); self.sprites.append( Tile( 750, 400,tileURL)); self.sprites.append( Tile( 50, 450,tileURL)); self.sprites.append( Tile( 100, 450,tileURL)); self.sprites.append( Tile( 150, 450,tileURL)); self.sprites.append( Tile( 200, 450,tileURL)); self.sprites.append( Tile( 250, 450,tileURL)); self.sprites.append( Tile( 400, 450,tileURL)); self.sprites.append( Tile( 450, 450,tileURL)); self.sprites.append( Tile( 500, 450,tileURL)); self.sprites.append( Tile( 550, 450,tileURL)); self.sprites.append( Tile( 600, 450,tileURL)); self.sprites.append( Tile( 650, 450,tileURL)); self.sprites.append( Tile( 700, 450,tileURL)); self.sprites.append( Tile( 750, 450,tileURL)); self.sprites.append( Tile( 800, 450,tileURL)); self.sprites.append( Tile( 800, 400,tileURL)); self.sprites.append( Tile( 850, 450,tileURL)); self.sprites.append( Tile( 850, 400,tileURL)); self.sprites.append( Tile( 900, 400,tileURL)); self.sprites.append( Tile( 900, 450,tileURL)); self.sprites.append( Tile( 950, 450,tileURL)); self.sprites.append( Tile( 950, 400,tileURL)); self.sprites.append( Tile( 1100, 400,tileURL)); self.sprites.append( Tile( 1100, 450,tileURL)); self.sprites.append( Tile( 1150, 400,tileURL)); self.sprites.append( Tile( 1150, 450,tileURL)); self.sprites.append( Tile( 1200, 400,tileURL)); self.sprites.append( Tile( 1200, 450,tileURL)); self.sprites.append( Tile( 1250, 400,tileURL)); self.sprites.append( Tile( 1250, 450,tileURL)); self.sprites.append( Tile( 1300, 400,tileURL)); self.sprites.append( Tile( 1300, 450,tileURL)); self.sprites.append( Tile( 1300, 500,tileURL)); self.sprites.append( Tile( 1250, 500,tileURL)); self.sprites.append( Tile( 1200, 500,tileURL)); self.sprites.append( Tile( 1150, 500,tileURL)); self.sprites.append( Tile( 1100, 500,tileURL)); self.sprites.append( Tile( 950, 500,tileURL)); self.sprites.append( Tile( 900, 500,tileURL)); self.sprites.append( Tile( 850, 500,tileURL)); self.sprites.append( Tile( 700, 500,tileURL)); self.sprites.append( Tile( 800, 500,tileURL)); self.sprites.append( Tile( 750, 500,tileURL)); self.sprites.append( Tile( 650, 850,tileURL)); self.sprites.append( Tile( 650, 800,tileURL)); self.sprites.append( Tile( 50, 500,tileURL)); self.sprites.append( Tile( 150, 500,tileURL)); self.sprites.append( Tile( 100, 500,tileURL)); self.sprites.append( Tile( 200, 500,tileURL)); self.sprites.append( Tile( 250, 500,tileURL)); self.sprites.append( Tile( 400, 500,tileURL)); self.sprites.append( Tile( 450, 500,tileURL)); self.sprites.append( Tile( 500, 500,tileURL)); self.sprites.append( Tile( 550, 500,tileURL)); self.sprites.append( Tile( 600, 500,tileURL)); self.sprites.append( Tile( 650, 500,tileURL)); self.sprites.append( Tile( 650, 550,tileURL)); self.sprites.append( Tile( 650, 600,tileURL)); self.sprites.append( Tile( 700, 550,tileURL)); self.sprites.append( Tile( 700, 600,tileURL)); self.sprites.append( Tile( 700, 850,tileURL)); self.sprites.append( Tile( 700, 800,tileURL)); self.sprites.append( Tile( 950, 150,tileURL)); self.sprites.append( Tile( 950, 200,tileURL)); self.sprites.append( Tile( 950, 250,tileURL)); self.sprites.append( Tile( 1000, 250,tileURL)); self.sprites.append( Tile( 1000, 200,tileURL)); self.sprites.append( Tile( 1000, 150,tileURL)); self.sprites.append( Tile( 1050, 150,tileURL)); self.sprites.append( Tile( 1050, 200,tileURL)); self.sprites.append( Tile( 1050, 250,tileURL)); self.sprites.append( Tile( 1100, 250,tileURL)); self.sprites.append( Tile( 1100, 200,tileURL)); self.sprites.append( Tile( 1100, 150,tileURL)); self.sprites.append( Tile( 1300, 850,tileURL)); self.sprites.append( Tile( 1300, 800,tileURL)); self.sprites.append( Tile( 1250, 800,tileURL)); self.sprites.append( Tile( 1250, 850,tileURL)); self.sprites.append( Tile( 1200, 850,tileURL)); self.sprites.append( Tile( 1250, 750,tileURL)); self.sprites.append( Tile( 1300, 700,tileURL)); self.sprites.append( Tile( 1300, 750,tileURL)); self.sprites.append( Tile( 750, 800,tileURL)); self.sprites.append( Tile( 750, 850,tileURL)); self.sprites.append( Tile( 800, 850,tileURL)); self.sprites.append( Tile( 750, 600,tileURL)); self.sprites.append( Tile( 800, 550,tileURL)); self.sprites.append( Tile( 750, 550,tileURL)); self.sprites.append( Tile( 1250, 550,tileURL)); self.sprites.append( Tile( 1300, 600,tileURL)); self.sprites.append( Tile( 1300, 550,tileURL)); self.sprites.append( Tile( 1300, 650,tileURL)); self.sprites.append( Tile( 1200, 550,tileURL)); self.sprites.append( Tile( 1250, 600,tileURL)); self.sprites.append( Tile( 1250, 650,tileURL)); self.sprites.append( Tile( 1250, 700,tileURL)); self.sprites.append( Tile( 850, 550,tileURL)); self.sprites.append( Tile( 800, 600,tileURL)); self.sprites.append( Tile( 800, 800,tileURL)); self.sprites.append( Tile( 850, 850,tileURL)); self.sprites.append( Tile( 1000, 700,tileURL)); self.sprites.append( Tile( 1000, 750,tileURL)); self.sprites.append( Tile( 1050, 750,tileURL)); self.sprites.append( Tile( 1050, 700,tileURL)); self.sprites.append( Tile( 1000, 650,tileURL)); self.sprites.append( Tile( 1050, 650,tileURL)); self.sprites.append( Tile( 250, 550,tileURL)); self.sprites.append( Tile( 250, 600,tileURL)); self.sprites.append( Tile( 250, 850,tileURL)); self.sprites.append( Tile( 250, 800,tileURL)); self.sprites.append( Tile( 200, 800,tileURL)); self.sprites.append( Tile( 200, 600,tileURL)); self.sprites.append( Tile( 400, 550,tileURL)); self.sprites.append( Tile( 400, 600,tileURL)); self.sprites.append( Tile( 450, 600,tileURL)); self.sprites.append( Tile( 400, 850,tileURL)); self.sprites.append( Tile( 400, 800,tileURL)); self.sprites.append( Tile( 450, 800,tileURL)); self.sprites.append( Tile( 250, 200,tileURL)); self.sprites.append( Tile( 300, 200,tileURL)); self.sprites.append( Tile( 350, 200,tileURL)); self.sprites.append( Tile( 400, 200,tileURL)); self.sprites.append( Tile( 300, 150,tileURL)); self.sprites.append( Tile( 350, 150,tileURL)); self.sprites.append( Tile( 300, 250,tileURL)); self.sprites.append( Tile( 350, 250,tileURL));
        self.sprites.append(Pot(310,310,potURL)); self.sprites.append(Pot(360,310,potURL)); self.sprites.append(Pot(310,360,potURL)); self.sprites.append(Pot(360,360,potURL));
    def update(self):
        for sprite in self.sprites:
            for sprite2 in self.sprites:
                if(self.collision(sprite, sprite2)):
                    if isinstance(sprite,Link) and isinstance(sprite2,Tile):
                        self.link.x = self.link.prevX
                        self.link.y = self.link.prevY
                    if isinstance(sprite,Link) and isinstance(sprite2,Pot):
                        sprite2.sendPot(self.link.direction)
                    if isinstance(sprite,Tile) and isinstance(sprite2,Pot):
                        sprite2.isBroke = True
                    if isinstance(sprite,Boomerang) and isinstance(sprite2,Pot):
                        sprite.isActive = False
                        sprite2.isBroke = True
                    if isinstance(sprite,Tile) and isinstance(sprite2,Boomerang):
                        sprite2.isActive = False
            sprite.update()
        
        tempList = self.sprites.copy()
        for sp in self.sprites:
            if(isinstance(sp,Pot)):
                if(sp.framesLeft<=0):
                    tempList.remove(sp)
            if(isinstance(sp,Boomerang)):
                if(sp.isActive == False):
                    tempList.remove(sp)

        self.sprites = tempList
                      

    def collision(self,a,b):
        aR = a.x + a.w   
        aL = a.x
        bR = b.x + b.w
        bL = b.x
        aU = a.y
        aD = a.y + a.h
        bU = b.y
        bD= b.y + b.h
		
        if(aR -5 < bL):
            return False
        if(aL +5 > bR):
            return False
        if(aD - 5 < bU):
            return False
        if(aU+ 5>bD):
            return False
        return True
    
    def addBoomer(self):
        temp = Boomerang(self.link.x+15, self.link.y+15,"Images/boomerang1.png",self.link.direction)
        self.sprites.append(temp)
        

class View():
    def __init__(self,model):
        screen_size = (700,500)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Assignment 8: Python Zelda')
        self.model = model
        self.viewX = 0
        self.viewY = 0
        
        
    def update(self):
        self.screen.fill([0,255,255])

        for sprite in self.model.sprites:
                if isinstance(sprite,Link):
                    self.screen.blit(sprite.image, (sprite.x-self.viewX, sprite.y-self.viewY))
                else:
                    self.screen.blit(sprite.image, ((sprite.x-self.viewX, sprite.y-self.viewY)))
        pygame.display.flip()

        
        

class Controller():
    def __init__(self, model,view):
        self.model = model
        self.view = view
        self.keepGoing = True

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keepGoing = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keepGoing = False
                elif event.key == K_LCTRL:
                    self.model.addBoomer()
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.model.link.x -= 10
            self.model.link.cycleLeft()
        if keys[K_RIGHT]:
            self.model.link.x += 10
            self.model.link.cycleRight()
        if keys[K_UP]:
            self.model.link.y -= 10
            if (not(keys[K_LEFT] or keys[K_RIGHT])):
                self.model.link.cycleUp()
        if keys[K_DOWN]:
            self.model.link.y += 10
            if (not(keys[K_LEFT] or keys[K_RIGHT])):
                self.model.link.cycleDown()
        if keys[K_q]:
            self.keepGoing = False
            

        if self.model.link.x + 25 > 700:
            self.view.viewX = 700
        if self.model.link.x + 25 < 700:
            self.view.viewX = 0
        if self.model.link.y + 25 > 500:
            self.view.viewY = 500
        if self.model.link.y+ 25 < 500:
            self.view.viewY = 0

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m,v)
while c.keepGoing:
    c.update()
    m.update()
    v.update()
    sleep(0.04)
print("Goodbye")