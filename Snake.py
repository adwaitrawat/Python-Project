import random, pygame 
pygame.init()

size = width, height = 1000, 1000
pixel = 5
speed = [pixel,0]
head = [500,400]
food = []
eaten = 0
WHITE = (0,0,0)
RED = (255,0,0)
GREEN = (0,0,255)
BLUE = (0,255,0)
YELLOW = (0,255,255)
BLACK = (255,255,255)

class tail(object):

	self.tail = []
	self.speed_tail = []

	def __init__(self,*tail):
		for i in range(0,2):
			self.tail[i]=tail[i]
		self.speed_tail[0]=tail[2]
		self.speed_tail[0]=tail[3]
		if tail[2] >= 0 :
			self.tail[1] -= 2*pixel
		elif tail[2] <= 0 : 
			self.tail[1] += 2*pixel
		elif tail[3] >= 0 :
			self.tail[0] -= 2*pixel
		elif tail[3] <= 0 :
			self.tail[0] += 2*pixel
		self.tail=tail.speed_tail
		#graphics for the addition of new tail
		pass	

	def kill(self,head):
		if head == self.tail:
			return 0
		else:
			return 1

	def position(self,i):
		for j in range(0,2):
			self.speed_tail[j]=tails[i].speed_tail[j]
			self.tail[j]=tails[i].tail[j]
	pass

tails = []
tails[0].tail = [490,400]
tails[0].speed_tail = speed

def move(self):
	for i in range (0,2):
		head[i]+=speed[i]
	pass


def wall():
	if head[0] + pixel + 5 == 1000 or head[1] + pixel + 5 == 800 :
		return 0
	else:
		return 1

def speed_update():
	for i in range(0,2): 
		if not speed[i] == 0 :
			speed[i]+=speed[i]
	pass

def eat():
	if head == food :
		end = len(tails)-1
		new_food()
		eaten+=1
	return True

def new_food():
	food[0]=random.randint(0,1000-pixel)
	food[1]=random.randint(0,800-pixel)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pass

def esc():
	if pygame.key.get_pressed(K_ESCAPE) == True :
		return 0
	else : 
		return 1

def direction():
	if pygame.key.get_pressed(K_UP) == True and speed[1] == 0 :
		temp = speed[0]
		speed[0] = 0
		speed[1] = temp
	elif pygame.key.get_pressed(K_DOWN) == True and speed[1] == 0 :
		temp = -1*speed[0]
		speed[0] = 0
		speed[1] = temp
	elif pygame.key.get_pressed(K_RIGHT) == True and speed[0] == 0 :
		temp = speed[0]
		speed[0] = 0
		speed[1] = temp
	elif pygame.key.get_pressed(K_LEFT) == True and speed[0] == 0:
		temp = -1*speed[0]
		speed[0] = 0
		speed[1] = temp
	pass

def display():
	screen = pygame.display.set_mode(size)
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, [0, 0, 1000, 800], pixel)

def score():
	#score board
	pass

def turn():
	if speed[0] == 0 
		tails[0].tail[1] = head[1] - 2*pixel
	if speed[1] == 0 
		tails[0].tail[0] = head[0] - 2*pixel

clock = pygame.time.Clock()

#main body
while wall() and tail() and esc():
	clock.tick(15)
	display()
	turn()
	direction()
	move()
	turn()
	for i in range(0,len(tails)-1) :
		tails[i+1].position(i)
	if eat() :
		tails.append(tails[end].tail[0],tails[end].tail[1])
	if eaten%3==0 :
		speed_update()

#after exiting the game
#graphically show that the player lost

pygame.quit()
