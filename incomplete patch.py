import pygame, random ,threading

size = width, height = 1000, 1000
pixel = 5
speed = [pixel,0]
head = [500,400,0,0]
food = [0,0]
eaten = [0]
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (0,255,255)
BLACK = (0,0,0)
fps=[10]
screen = pygame.display.set_mode(size)

class tail(object):



	def __init__(self,*new_tail):
		self.tail = [new_tail[0],new_tail[1],0,0]
		self.speed_tail = [new_tail[2],new_tail[3]]
		if self.speed_tail[0] >= 0 :
			self.tail[0] -= 2*pixel
		elif self.speed_tail[0] <= 0 : 
			self.tail[0] += 2*pixel
		elif self.speed_tail[1] >= 0 :
			self.tail[1] -= 2*pixel
		elif self.speed_tail[1] <= 0 :
			self.tail[1] += 2*pixel
		pass	

	def kill(self,head):
		if head == self.tail:
			return True
		else:
			return False

	def position(self,i):
		for j in range(0,2):
			self.speed_tail[j]=tails[i].speed_tail[j]
		if self.speed_tail[0] > 0 and self.speed_tail[1] == 0 :
			self.tail[2] = self.tail[0]
			self.tail[3] = self.tail[1]
			self.tail[0] = tails[i].tail[2] - pixel
			self.tail[1] = tails[i].tail[3]
		elif self.speed_tail[0] < 0 and self.speed_tail[1] == 0 :
			self.tail[2] = self.tail[0]
			self.tail[3] = self.tail[1]
			self.tail[0] = tails[i].tail[2] + pixel
			self.tail[1] = tails[i].tail[3]
		elif self.speed_tail[1] > 0 and self.speed_tail[0] == 0 :
			self.tail[2] = self.tail[0]
			self.tail[3] = self.tail[1]
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3] - pixel
		elif self.speed_tail[1] < 0 and self.speed_tail[0] == 0 :
			self.tail[2] = self.tail[0]
			self.tail[3] = self.tail[1]
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3] + pixel
		pass

tails = [tail(490,400,pixel,0)]

def display():
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,1000,800), pixel)
	pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.draw.circle(screen, GREEN, (tails[0].tail[0], tails[0].tail[1]), pixel)
	for i in range(1,len(tails)) :
		if tails[i].speed_tail[0] > 0 and tails[i].speed_tail[1] == 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[1] > 0 and tails[i].speed_tail[0] == 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[0] < 0 and tails[i].speed_tail[1] == 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[1] < 0 and tails[i].speed_tail[0] == 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
	pygame.display.update()

def direction():
	if event.type == pygame.KEYDOWN :
		if speed[0] > 0 and speed[1] == 0 :
			if event.key == pygame.K_UP:
				temp = speed[0]
				speed[0] = 0
				speed[1] = -1*temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
			if event.key == pygame.K_DOWN :
				temp = speed[0]
				speed[0] = 0
				speed[1] = temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
		if speed[1] > 0 and speed[0] == 0 :
			if event.key == pygame.K_RIGHT :
				temp = speed[1]
				speed[1] = 0
				speed[0] = temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
			if event.key == pygame.K_LEFT : 
				temp = speed[1]
				speed[1] = 0
				speed[0] = -1*temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
		if speed[0] < 0 and speed[1] == 0 :
			if event.key == pygame.K_UP:
				temp = speed[0]
				speed[0] = 0
				speed[1] = temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
			if event.key == pygame.K_DOWN :
				temp = speed[0]
				speed[0] = 0
				speed[1] = -1*temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
		if speed[1] < 0 and speed[0] == 0 :
			if event.key == pygame.K_RIGHT :
				temp = speed[1]
				speed[1] = 0
				speed[0] = -1*temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
			if event.key == pygame.K_LEFT : 
				temp = speed[1]
				speed[1] = 0
				speed[0] = temp
				for i in range(0,2):
					tails[0].speed_tail[i] = speed[i]
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
		if event.key == pygame.K_SPACE:
			pygame.time.wait(5000)
	pass



def move():
	for i in range (0,2):
		display()
		head[i+2] = head[i]
		head[i]+=speed[i]
		if head[0] >= 1000 + pixel or head[1] >= 800 + pixel or head[0]  <= pixel*2 - 2 or head[1] + pixel <= pixel*2 - 2 :
			pygame.quit()
		else :
			if speed[0] > 0 :
				tails[0].tail[2] = tails[0].tail[0]
				tails[0].tail[3] = tails[0].tail[1]
				tails[0].tail[0] = head[2] - pixel
				tails[0].tail[1] = head[3]
			elif speed[0] < 0:
				tails[0].tail[2] = tails[0].tail[0]
				tails[0].tail[3] = tails[0].tail[1]
				tails[0].tail[0] = head[2] + pixel
				tails[0].tail[1] = head[3]
			elif speed[1] > 0 :
				tails[0].tail[2] = tails[0].tail[0]
				tails[0].tail[3] = tails[0].tail[1]
				tails[0].tail[0] = head[2]
				tails[0].tail[1] = head[3] - pixel
			elif speed[1] < 0:
				tails[0].tail[2] = tails[0].tail[0]
				tails[0].tail[3] = tails[0].tail[1]
				tails[0].tail[0] = head[2]
				tails[0].tail[1] = head[3] + pixel
			for j in range(1,len(tails)) :
				tails[j].position(j-1)
		for j in range(0,len(tails)):
			print(tails[j].tail)
	pygame.display.update()
	pass


def wall():
	if head[0] + pixel >= 1000 or head[1] + pixel >= 800 or head[0]  <= pixel*2 - 2 or head[1] + pixel <= pixel*2 - 2 :
		return 0
	else:
		return 1

def speed_update(): 
	if speed[1] > 0 :
		speed[1] += 1
	elif speed[1] > 0 :
		speed[1] += 1
	elif speed[0] > 0 :
		speed[0] += 1
	elif speed[0] > 0 :
		speed[0] += 1
	elif speed[1] < 0 :
		speed[1] -= 1
	elif speed[1] < 0 :
		speed[1] -= 1
	elif speed[0] < 0 :
		speed[0] -= 1
	elif speed[0] < 0 :
		speed[0] -= 1
	pass

def eat():
	if head[0] <= food[0] + pixel*2 and head[1] <= food[1] + pixel*2 and head[0] >= food[0] - pixel*2 and head[1] >= food[1] - pixel*2 :
		end = len(tails) - 1
		new_food()
		eaten[0]+=1
		print(eaten)
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()
		print(head)
		print(tails[end+1].tail)
		print(head)
		print(end)
		if eaten[0]%1 == 0 :
			speed_update()
	pass

def new_food():
	display()
	food[0]=random.randint(pixel,1000-pixel*2)
	food[1]=random.randint(pixel,800-pixel*2)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.display.update()
	pass


clock = pygame.time.Clock()
pygame.init()
display()
new_food()
while wall() :
	clock.tick(fps[0])	
	threading.Thread(target = move).start()
	eat()
	for event in pygame.event.get():
		direction()
