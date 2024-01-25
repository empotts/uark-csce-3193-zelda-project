import pygame

class Sprite:
    def __init__(self, x, y, image_url):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_url)

class Link(Sprite):
    def __init__(self, x, y, url):
        super().__init__(x, y, url)
        self.w = 45
        self.h = 45
        self.prevX = x
        self.prevY = y
        self.numImages = 50
        self.currentImage = 0
        self.linkImages = []
        self.load_images()
        self.direction = 0

    def load_images(self):
        linkString = "Images/link"
        pngString = ".png"

        for i in range(1, 51):
            pathname = ""
            temp = pygame.image.load("")
            if i <= 9:
                pathname = linkString + "0" + str(i) + pngString
            else:
                pathname = linkString + str(i) + pngString
            temp = pygame.image.load(pathname)
            self.linkImages.append(temp)

    def update(self):
        self.image = self.linkImages[self.currentImage]

    def cycle_down(self):
        if self.currentImage < 5 or self.currentImage >= 12:
            self.currentImage = 5
        self.currentImage += 1
        self.direction = 0

    def cycle_left(self):
        if self.currentImage < 13 or self.currentImage >= 22:
            self.currentImage = 13
        self.currentImage += 1
        self.direction = 1

    def cycle_right(self):
        if self.currentImage < 29 or self.currentImage >= 37:
            self.currentImage = 29
        self.currentImage += 1
        self.direction = 3

    def cycle_up(self):
        if self.currentImage < 39 or self.currentImage >= 49:
            self.currentImage = 39
        self.currentImage += 1
        self.direction = 2

class Tile(Sprite):
    def __init__(self, x, y, url):
        super().__init__(x, y, url)
        self.w = 50
        self.h = 50

    def update(self):
        pass

class Boomerang(Sprite):
    def __init__(self, x, y, url, direction):
        super().__init__(x, y, url)
        self.w = 20
        self.h = 20
        self.is_active = True
        self.speed = 11
        self.direction = direction

    def update(self):
        if self.direction == 0:
            self.y += self.speed
        if self.direction == 1:
            self.x -= self.speed
        if self.direction == 2:
            self.y -= self.speed
        if self.direction == 3:
            self.x += self.speed

class Pot(Sprite):
    def __init__(self, x, y, url):
        super().__init__(x, y, url)
        self.w = 30
        self.h = 30
        self.sent = False
        self.speed = 11
        self.is_broke = False
        self.framesLeft = 20
        self.direction = None

    def send_pot(self, direction):
        self.sent = True
        self.direction = direction
        if direction == 0:
            self.y += self.speed
        if direction == 1:
            self.x -= self.speed
        if direction == 2:
            self.y -= self.speed
        if direction == 3:
            self.x+= self.speed













            import pygame
import time

from pygame.locals import*
from time import sleep

class Model():
	def __init__(self):
		self.dest_x = 0
		self.dest_y = 0

	def update(self):
		if self.rect.left < self.dest_x:
			self.rect.left += 1
		if self.rect.left > self.dest_x:
			self.rect.left -= 1
		if self.rect.top < self.dest_y:
			self.rect.top += 1
		if self.rect.top > self.dest_y:
			self.rect.top -= 1

	def set_dest(self, pos):
		self.dest_x = pos[0]
		self.dest_y = pos[1]

class View():
	def __init__(self, model):
		screen_size = (800,600)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.turtle_image = pygame.image.load("turtle.png")
		self.model = model
		self.model.rect = self.turtle_image.get_rect()

	def update(self):
		self.screen.fill([0,200,100])
		self.screen.blit(self.turtle_image, self.model.rect)
		pygame.display.flip()

class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True

	def update(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
			elif event.type == pygame.MOUSEBUTTONUP:
				self.model.set_dest(pygame.mouse.get_pos())
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.dest_x -= 1
		if keys[K_RIGHT]:
			self.model.dest_x += 1
		if keys[K_UP]:
			self.model.dest_y -= 1
		if keys[K_DOWN]:
			self.model.dest_y += 1

print("Use the arrow keys to move. Press Esc to quit.")
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