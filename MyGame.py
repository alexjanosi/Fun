import pygame

# create the game
pygame.init()

# create window for game
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Sans Time")

# upload sprites
walkRight = [pygame.image.load('Sans/Walk/Right1.png'), 
pygame.image.load('Sans/Walk/Right2.png'), pygame.image.load('Sans/Walk/Right3.png'), 
pygame.image.load('Sans/Walk/Right4.png')]
walkLeft = [pygame.image.load('Sans/Walk/Left1.png'), 
pygame.image.load('Sans/Walk/Left2.png'), pygame.image.load('Sans/Walk/Left3.png'), 
pygame.image.load('Sans/Walk/Left4.png')]
bg = pygame.image.load('Sans/bg.jpg')
char = [pygame.image.load('Sans/Poses/SansLaught1.png')] * 3 + [pygame.image.load("Sans/Poses/SansEyeClosed.png")]
sleep = [pygame.image.load("Sans/Sleep/Sleep1.png"), pygame.image.load("Sans/Sleep/Sleep2.png")]

# run a clock
clock = pygame.time.Clock()

# class of character you control
class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.left = False
		self.right = False
		self.stand = True
		self.standCount = 0
		self.standing = 0
		self.walkCount = 0
		self.jumpCount = 10

	# update movements on window
	def draw(self, win):

		if self.walkCount + 1 >= 20:
			self.walkCount = 0

		if self.standCount + 1 >= 100:
			self.standCount = 0
			self.standing += 1

		if self.left:
			win.blit(walkLeft[self.walkCount//5], (self.x,self.y))
			self.walkCount += 1
			self.standCount = 0
			self.standing = 0

		elif self.right:
			win.blit(walkRight[self.walkCount//5], (self.x,self.y))
			self.walkCount += 1
			self.standCount = 0
			self.standing = 0

		else:
		
			if self.standing <= 5:
				win.blit(char[self.standCount//25], (self.x, self.y))
			else:
				win.blit(sleep[self.standCount//50], (self.x, self.y))

			self.standCount += 1
			self.walkCount = 0

class projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing

	def draw(win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# redraws the window
def redrawGameWindow():

	win.blit(bg, (0,0))  
	man.draw(win)
	pygame.display.update() 
	
# create a character and start main loop
man = player(50, 390, 70, 60)
run = True

while run:
	clock.tick(20)

	# exit correctly
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# get keys pressed
	keys = pygame.key.get_pressed()
	
	# update according to actions
	if keys[pygame.K_LEFT] and man.x > man.vel: 
		man.x -= man.vel
		man.left = True
		man.right = False
		man.standCount = 0

	elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:  
		man.x += man.vel
		man.left = False
		man.right = True
		man.standCount = 0
		
	else: 
		man.walkCount = 0
		
	if not(man.isJump):
		if keys[pygame.K_UP]:
			man.isJump = True
			man.walkCount = 0
			man.standCount = 0
	else:
		if man.jumpCount >= -10:
			man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
			man.jumpCount -= 1
		else: 
			man.jumpCount = 10
			man.isJump = False

	redrawGameWindow() 
	
	
pygame.quit()