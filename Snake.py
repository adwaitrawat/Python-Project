import random, pygame 

size = width, height = 1000, 1000
pixel = 5
speed = [pixel,0]
head = [500,400]
food = [0,0]
eaten = [0]
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (0,255,255)
BLACK = (0,0,0)
fps=15

class tail(object):



	def __init__(self,*new_tail):

		self.tail = [new_tail[0],new_tail[1]]
		self.speed_tail = [new_tail[2],new_tail[3]]
		if self.speed_tail[0] >= 0 :
			self.tail[0] -= 2*pixel
		elif self.speed_tail[0] <= 0 : 
			self.tail[0] += 2*pixel
		elif self.speed_tail[1] >= 0 :
			self.tail[1] -= 2*pixel
		elif self.speed_tail[1] <= 0 :
			self.tail[1] += 2*pixel
		#graphics for the addition of new tail
		pass	

	def kill(self,head):
		if head == self.tail:
			return True
		else:
			return False

	def position(self,i):
		for j in range(0,2):
			self.speed_tail[j]=tails[i].speed_tail[j]
			self.tail[j]=tails[i].tail[j]
	pass

#------------------------------------------------------------class end

tails = [tail(490,400,pixel,0)]

def move():
	for i in range (0,2):
		display()
		head[i]+=speed[i]
		pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
		pygame.display.update()
		print(head)
	pass


def wall():
	if head[0] + pixel >= 1000 or head[1] + pixel >= 800 or head[0]  <= pixel*2 or head[1] + pixel <= pixel*2 :
		return 0
	else:
		return 1

def speed_update():
	for i in range(0,2): 
		if not speed[i] == 0 :
			speed[i]+=0.1*eaten[0]
	pass

def eat():
	if head[0] <= food[0] + pixel and head[1] <= food[1] + pixel and head[0] >= food[0] - pixel and head[1] >= food[1] - pixel:
		new_food()
		eaten[0]+=1
		print(eaten)
		speed_update()
		return True
	else :
		return False

def new_food():
	display()
	food[0]=random.randint(0,1000-pixel)
	food[1]=random.randint(0,800-pixel)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.display.update()
	pass

def direction():
	if event.type == pygame.KEYDOWN :
		if event.key == pygame.K_DOWN and speed[1] == 0 :
			temp = speed[0]
			speed[0] = 0
			speed[1] = temp
		if event.key == pygame.K_UP and speed[1] == 0 :
			temp = speed[0]
			speed[0] = 0
			speed[1] = -1*temp
		if event.key == pygame.K_RIGHT and speed[0] == 0 :
			temp = speed[1]
			speed[1] = 0
			speed[0] = temp
		if event.key == pygame.K_LEFT and speed[0] == 0:
			temp = speed[1]
			speed[1] = 0
			speed[0] = -1*temp
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
	pass

def display():
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,1000,800), pixel)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.display.update()

def score():
	#score board
	pass

def first_tail():
	if speed[0] == 0 :
		tails[0].tail[1] = head[1] - 2*pixel
	if speed[1] == 0 :
		tails[0].tail[0] = head[0] - 2*pixel

def tail_cut():
	for i in range(0,len(tails)) :
		if not tails[i].kill(head) :
			return False
		else :
			return True

#--------------------------------------------------------------------------------------
#main body
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.init()
display()
new_food()
move()
while wall() and tail_cut():
	clock.tick(15)
	direction()
	move()
	first_tail()
	for i in range(0,len(tails)-1) :
		tails[i+1].position(i)
	#if eat() :
	#	tails.append(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1])


#after exiting the game
#graphically show that the player lost

