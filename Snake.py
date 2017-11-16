import pygame, random ,threading

size = width, height = 1000, 1000
pixel = 5
d = 2 #d as in delta
speed = [pixel,0]
head = [500,400,0,0]
food = [0,0]
eaten = [0]
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHTBLUE = (0,255,255)
BLACK = (0,0,0)
fps=[10]
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class tail(object):



	def __init__(self,*new_tail):
		self.tail = [new_tail[0],new_tail[1],0,0]
		self.speed_tail = [new_tail[2],new_tail[3]]
		if self.speed_tail[0] >= 0 :
			self.tail[0] -= pixel
		elif self.speed_tail[0] <= 0 : 
			self.tail[0] += pixel
		elif self.speed_tail[1] >= 0 :
			self.tail[1] -= pixel
		elif self.speed_tail[1] <= 0 :
			self.tail[1] += pixel	

	def position(self,i):
		for j in range(0,2):
			self.speed_tail[j]=tails[i].speed_tail[j]
		self.tail[2] = self.tail[0]
		self.tail[3] = self.tail[1]
		if self.speed_tail[0] > 0 :
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3]
		elif self.speed_tail[0] < 0 :
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3]
		elif self.speed_tail[1] > 0 :
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3]
		elif self.speed_tail[1] < 0 :
			self.tail[0] = tails[i].tail[2]
			self.tail[1] = tails[i].tail[3]

tails = [tail(490,400,pixel,0)]

def display():
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,1000,800), pixel)
	pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
	pygame.draw.circle(screen, LIGHTBLUE, (food[0], food[1]), pixel)
	pygame.draw.circle(screen, GREEN, (tails[0].tail[0], tails[0].tail[1]), pixel)
	for i in range(1,len(tails)) :
		if tails[i].speed_tail[0] > 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[1] > 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[0] < 0 :
			pygame.draw.circle(screen, GREEN, (tails[i].tail[0], tails[i].tail[1]), pixel)
		if tails[i].speed_tail[1] < 0 :
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
		if event.key == pygame.K_a:
			cheat_speed(1)
		if event.key == pygame.K_s:
			cheat_speed(-1)
		if event.key == pygame.K_e:
			cheat_eat()
		if event.key == pygame.K_f:
			cheat_food()

def move():
	display()
	for i in range (0,2):
		head[i+2] = head[i]
		head[i]+=speed[i]
	if head[0] >= 1000 + pixel or head[1] >= 800 + pixel or head[0]  <= pixel  or head[1] <= pixel :
		pygame.quit()	
	else :
		tails[0].tail[2] = tails[0].tail[0]
		tails[0].tail[3] = tails[0].tail[1]
		if speed[0] > 0 :
			tails[0].tail[0] = head[2] 
			tails[0].tail[1] = head[3]
		elif speed[0] < 0:
			tails[0].tail[0] = head[2] 
			tails[0].tail[1] = head[3]
		elif speed[1] > 0 :
			tails[0].tail[0] = head[2]
			tails[0].tail[1] = head[3] 
		elif speed[1] < 0:
			tails[0].tail[0] = head[2]
			tails[0].tail[1] = head[3] 
		for j in range(1,len(tails)) :
			tails[j].position(j-1)
		for j in range(0,len(tails)):
			print(tails[j].tail)	
	pygame.display.update()

def kill():
	if speed[0] == 0 :
		for i in range(1,len(tails)):
			if head[0] <= tails[i].tail[0] + d and head[1] <= tails[i].tail[1] + d and head[0] >= tails[i].tail[0] - d and head[1] >= tails[i].tail[1] - d :
				pygame.quit()
			else :
				for j in range(len(tails)-1,i+1,-1):
					if tails[i].tail[0] <= tails[j].tail[0] + d and tails[i].tail[1] <= tails[j].tail[1] + d and tails[i].tail[0] >= tails[j].tail[0] - d and tails[i].tail[1] >= tails[j].tail[1] - d :
						pygame.quit()
	else : 
		for i in range(1,len(tails)):
			if head[0] <= tails[i].tail[0] + d and head[1] <= tails[i].tail[1] + d and head[0] >= tails[i].tail[0] - d and head[1] >= tails[i].tail[1] - d :
				pygame.quit()
			else :
				for j in range(len(tails)-1,i+1,-1):
					if tails[j].tail[0] <= tails[i].tail[0] + d and tails[j].tail[1] <= tails[i].tail[1] + d and tails[j].tail[0] >= tails[i].tail[0] - d and tails[j].tail[1] >= tails[i].tail[1] - d :
						pygame.quit()

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

def eat():
	if head[0] <= food[0] + 2*pixel and head[1] <= food[1] + 2*pixel and head[2] >= food[0] - 2*pixel and head[3] >= food[1] - 2*pixel :
		end = len(tails) - 1
		new_food(random.randint(2*pixel,1000-pixel*2),random.randint(2*pixel,800-pixel*2))
		eaten[0] += 1
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()
		speed_update()
	for i in range(0,len(tails)):
		if tails[i].tail[0] <= food[0] + 2*pixel and tails[i].tail[1] <= food[1] + 2*pixel and tails[i].tail[2] >= food[0] - 2*pixel and tails[i].tail[3] >= food[1] - 2*pixel :
			end = len(tails) - 1
			new_food(random.randint(2*pixel,1000-pixel*2),random.randint(2*pixel,800-pixel*2))
			eaten[0]+=1
			tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
			pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
			pygame.display.update()
	
def new_food(i,j):
	display()
	food[0] = i
	food[1] = j
	pygame.draw.circle(screen, LIGHTBLUE, (food[0], food[1]), pixel)
	pygame.display.update()

def cheat_speed(i):
	if i < 0 :
		if speed[1] > 0 :
			speed[1] -= 1
		elif speed[1] > 0 :
			speed[1] -= 1
		elif speed[0] > 0 :
			speed[0] -= 1
		elif speed[0] > 0 :
			speed[0] -= 1
		elif speed[1] < 0 :
			speed[1] += 1
		elif speed[1] < 0 :
			speed[1] += 1
		elif speed[0] < 0 :
			speed[0] += 1
		elif speed[0] < 0 :
			speed[0] += 1
	else :
		speed_update()

def cheat_food():
	if head[0] < 500 and head[1] < 400 :
		new_food(random.randint(head[0],500),random.randint(head[1],400))
	elif head[0] > 500 and head[1] < 400 :
		new_food(random.randint(500,head[0]),random.randint(head[1],400))
	elif head[0] < 500 and head[1] > 400 :
		new_food(random.randint(head[0],500),random.randint(400,head[1]))
	elif head[0] >= 500 and head[1] >= 400 :
		new_food(random.randint(500,head[0]),random.randint(400,head[1]))

def cheat_eat():
	end = len(tails) - 1
	new_food(random.randint(2*pixel,1000-pixel*2),random.randint(2*pixel,800-pixel*2))
	eaten[0] += 1
	tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
	pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
	pygame.display.update()

display()
new_food(random.randint(2*pixel,1000-pixel*2),random.randint(2*pixel,800-pixel*2))
while True :
	clock.tick(fps[0])	
	threading.Thread(target = move).start()	
	eat()
	kill()
	for event in pygame.event.get():
		direction()
