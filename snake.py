import random
import pygame
import sys


class snakePart(object):
	"""docstring for snakePart"""
	rows = 20 
	width = 500
	snake_part1 = pygame.image.load('snake_sprites/snake_part1.png')
	snake_part2 = pygame.image.load('snake_sprites/snake_part2.png')
	snake_part3 = pygame.image.load('snake_sprites/snake_part3.png')
	snake_part4 = pygame.image.load('snake_sprites/snake_part4.png')
	snake_head1 = pygame.image.load('snake_sprites/snake_head1.png')
	snake_head2 = pygame.image.load('snake_sprites/snake_head2.png')
	snake_head3 = pygame.image.load('snake_sprites/snake_head3.png')
	snake_head4 = pygame.image.load('snake_sprites/snake_head4.png')
	snack_image = pygame.image.load('snake_sprites/snack.png')
	snake_tail1 = pygame.image.load('snake_sprites/snake_tail1.png')
	snake_tail2 = pygame.image.load('snake_sprites/snake_tail2.png')
	snake_tail3 = pygame.image.load('snake_sprites/snake_tail3.png')
	snake_tail4 = pygame.image.load('snake_sprites/snake_tail4.png')
	snake_tail5 = pygame.image.load('snake_sprites/snake_tail5.png')
	snake_tail6 = pygame.image.load('snake_sprites/snake_tail6.png')
	snake_tail7 = pygame.image.load('snake_sprites/snake_tail7.png')
	snake_tail8 = pygame.image.load('snake_sprites/snake_tail8.png')

	def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
		self.pos = start
		self.dirnx = dirnx
		self.dirny = dirny
		self.color = color

	def move(self, dirnx, dirny):
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

	def draw(self, surface, eyes = False, snack = False, tail = False):
		spacing = self.width // self.rows
		i = self.pos[0]
		j = self.pos[1]

		if snack: 
			surface.blit(self.snack_image, (i*spacing + 1, j*spacing + 1 ))

		elif eyes:

			if self.dirnx == 1 and self.dirny == 0:
				surface.blit(self.snake_head1, (i*spacing + 1, j*spacing + 1 ))
			elif self.dirnx == -1 and self.dirny == 0:
				surface.blit(self.snake_head2, (i*spacing + 1, j*spacing + 1))
			elif self.dirnx == 0 and self.dirny == 1:
				surface.blit(self.snake_head4, (i*spacing + 1, j*spacing + 1))
			else:
				surface.blit(self.snake_head3, (i*spacing + 1, j*spacing + 1))

		elif tail:

			if self.dirnx == 1 and self.dirny == 0:
				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:
					surface.blit(self.snake_tail3, (i*spacing + 1, j*spacing + 1))

				else:
					surface.blit(self.snake_tail4, (i*spacing + 1 , j*spacing + 1))

			elif self.dirnx == -1 and self.dirny == 0:
				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:
					surface.blit(self.snake_tail1, (i*spacing + 1, j*spacing + 1))

				else:
					surface.blit(self.snake_tail2, (i*spacing + 1 , j*spacing + 1))

			elif self.dirnx == 0 and self.dirny == 1:
				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:
					surface.blit(self.snake_tail5, (i*spacing + 1, j*spacing + 1))

				else:
					surface.blit(self.snake_tail6, (i*spacing + 1 , j*spacing + 1))

			else:
				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:
					surface.blit(self.snake_tail7, (i*spacing + 1, j*spacing + 1))

				else:
					surface.blit(self.snake_tail8, (i*spacing + 1 , j*spacing + 1))




		else:

			if self.dirnx != 0:

				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:

					surface.blit(self.snake_part1, (i*spacing + 1, j*spacing + 1))

				else:

					surface.blit(self.snake_part2, (i*spacing + 1 , j*spacing + 1))

			else:

				if i % 2 != 0 and j % 2 != 0 or i % 2 == 0 and j % 2 == 0:

					surface.blit(self.snake_part3, (i*spacing + 1, j*spacing + 1))

				else:

					surface.blit(self.snake_part4, (i*spacing + 1 , j*spacing + 1))


		#pygame.draw.rect(surface, self.color, (i*spacing + 1, j*spacing + 1, spacing - 2, spacing - 2))

class obstacle(object):
	"""docstring for obstacle"""

	rows = 20 
	width = 500
	def __init__(self, coordites, color = (170, 170, 255)):

		self.coordites = coordites
		self.color = color

	def draw(self, surface):

		spacing = self.width // self.rows
		for position in self.coordites:
			i = position[0]
			j = position[1]

			pygame.draw.rect(surface, self.color, (i*spacing + 1, j*spacing + 1, spacing, spacing))


class snake(object):
	"""docstring for snake"""

	body = []
	turns = {}
	def __init__(self, color, pos):

		self.color = color
		self.head = snakePart(pos)
		self.tail = snakePart((pos[0] -2, pos[1]))
		self.body.append(self.head)
		self.body.append(snakePart((pos[0] - 1, pos[1])))
		self.body.append(self.tail)
		# movement direction
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				if keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				if keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				if keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1 
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


		for i, part in enumerate(self.body):
			p = part.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				part.move(turn[0], turn[1])
				if i == len(self.body) -1:
					self.turns.pop(p) 

			else:
				if part.dirnx == -1 and part.pos[0] <= 0:
					part.pos = (part.rows - 1, part.pos[1])
				elif part.dirnx == 1 and part.pos[0] >= part.rows -1:
					part.pos = (0, part.pos[1])
				elif part.dirny == 1 and part.pos[1] >= part.rows -1:
					part.pos = (part.pos[0], 0)
				elif part.dirny == -1 and part.pos[1] <= 0:
					part.pos = (part.pos[0], part.rows - 1)
				else:
					part.move(part.dirnx, part.dirny)


	def reset(self, pos):
		self.head = snakePart(pos)
		self.tail = snakePart((pos[0]-2, pos[1]))
		self.body = []
		self.body.append(self.head)
		self.body.append(snakePart((pos[0] - 1, pos[1])))
		self.body.append(self.tail)
		self.turns = {}
		self.dirnx = 0
		self.dirny = 1

	def addPart(self):
		tail = self.body[-1]
		dirnx, dirny = tail.dirnx, tail.dirny

		if dirnx == 1 and dirny == 0:
			self.body.append(snakePart((tail.pos[0]-1,tail.pos[1])))
		elif dirnx == -1 and dirny == 0:
			self.body.append(snakePart((tail.pos[0]+1,tail.pos[1])))
		elif dirnx == 0 and dirny == 1:
			self.body.append(snakePart((tail.pos[0],tail.pos[1]-1)))
		elif dirnx == 0 and dirny == -1:
			self.body.append(snakePart((tail.pos[0],tail.pos[1]+1)))
 
		self.body[-1].dirnx = dirnx
		self.body[-1].dirny = dirny
		
	def draw(self, surface):
		for i, part in enumerate(self.body):
			if i == 0:
				part.draw(surface, eyes = True)
			elif i == len(self.body) -1:
				part.draw(surface, tail = True)
			else:
				part.draw(surface)


def drawGrid(surface, rows):

	width, height = surface.get_width(), surface.get_height()
	spacing = width // rows

	x = 0
	y = 0

	for l in range(rows):
		x += spacing
		y += spacing
		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, height))
		pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

def spawnSnack(rows, item):

	positions = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
			continue
		else:
			break

	return (x,y)

def redrawWindow(surface, snake, snack, obstacle ,rows):

	width, height = surface.get_width(), surface.get_height() 
	surface.fill((255, 255, 255))
	#drawGrid(surface, rows)
	snake.draw(surface)
	snack.draw(surface, snack = True)
	obstacle.draw(surface)
	pygame.display.update()

def main():

	width = 500
	height = 500
	rows = 20
	pygame.init()
	win = pygame.display.set_mode((width, height))
	s = snake((255, 0, 0), (10, 10))
	barrier = obstacle([(0, 0)])			#([(4,4), (4,5), (5,4), (5,5)])
	snack = snakePart(spawnSnack(rows, s), color = (0, 0, 255)) 
	game = True
	clock = pygame.time.Clock() 


	while game:
		pygame.time.delay(10)
		clock.tick(10) # game speed
		s.move()
		if s.body[0].pos == snack.pos:
			s.addPart()
			snack = snakePart(spawnSnack(rows, s), color = (0, 0, 255))

		for x in range(len(s.body)):
			if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])) or s.body[0].pos in barrier.coordites:
				print('Score: ', len(s.body))
				s.reset((10,10))
				break

		redrawWindow(win, s, snack, barrier, rows)

main() 

