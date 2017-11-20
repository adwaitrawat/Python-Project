import pygame, random, threading, os

pygame.init()
current = pygame.display.Info()
size = width, height = 100*(current.current_h//100), 100*(current.current_h//100)
ss = 10*(height//100)
pixel = 5
d = 2
pd = [2]
high_score = [0]
speed = [pixel*2,0]
head = [10*(width//20), 40*(height//100),0,0]
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
pygame.display.set_caption("Snakes")
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

tails = [tail(head[0]-2*pixel,head[1],pixel*2,0)]

def display():
	pygame.init()
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,width,40*(height//50)), pixel)
	pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
	pygame.draw.circle(screen, LIGHTBLUE, (food[0], food[1]), pixel)
	pygame.draw.circle(screen, GREEN, (tails[0].tail[0], tails[0].tail[1]), pixel)
	pygame.draw.rect(screen , RED ,[0,40*(height//50),10*(width//20),10*(height//50)] ,pixel)
	pygame.draw.rect(screen , RED ,[10*(width//20),40*(height//50),10*(width//20),10*(height//50)] ,pixel)
	text_display("SNAKES",30*(width//40), 90*(height//100),10*(height//100),GREEN)
	text_display("By - Adwait Rawat and Team",10*(3*(width//40)+(width//200)),90*(height//100) + 10*(height//200),10*(height//300),GREEN)
	if eaten[0] >= high_score[0] :
		text_display("SCORE : "+str(eaten[0]),10*(width//40),10*(4*(height//50) + (height//100)),3*ss//4,GREEN)
		text_display("HIGH SCORE : "+str(high_score[0]),10*(width//40),10*(4*(height//50) + (height//100)) + 3*ss//4,3*ss//4,GREEN)
	else :
		text_display("SCORE : "+str(eaten[0]),10*(width//40),10*(4*(height//50) + (height//100)),3*ss//4,WHITE)
		text_display("HIGH SCORE : "+str(high_score[0]),10*(width//40),10*(4*(height//50) + (height//100)) + 3*ss//4,3*ss//4,WHITE)
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
		keys = pygame.key.get_pressed()
		if keys[pygame.K_q] and keys[pygame.K_w]:
			cheat_eat(1)
		elif event.key == pygame.K_ESCAPE:
			text_display("QUITTING",10*(width//20),40*(height//100),10*(height//100),RED)
			pygame.display.update()
			pygame.time.wait(1000)
			pygame.quit()
		elif event.key == pygame.K_SPACE:
			text_display("PAUSING FOR 5 SEC", 10*(width//20), 40*(height//100), 10*(height//100),RED)
			pygame.display.update()
			pygame.time.wait(5000)
		elif event.key == pygame.K_a:
			cheat_speed(1)
		elif event.key == pygame.K_d:
				cheat_speed(-1)
		elif event.key == pygame.K_e:
			cheat_eat(-1)
		elif event.key == pygame.K_f:
			cheat_food()
		elif not (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_w or event.key == pygame.K_q) :  
			cheat()
def text_display(text,x,y,size,color):
	s= pygame.font.SysFont("comicsans",size)
	s_surface = s.render(text,True,color)
	surface_rect = s_surface.get_rect()
	surface_rect.centerx = x
	surface_rect.centery = y
	screen.blit(s_surface, surface_rect)
	

def move():
	for i in range (0,2):
		head[i+2] = head[i]
		head[i]+=speed[i]
	if head[0] >= width + pixel or head[1] >= (4*(height/5)) + pixel or head[0]  <= pixel  or head[1] <= pixel :
		text_display("BUMPED INTO THE WALL",10*(width//20),40*(height//100),10*(height//100),RED)
		pygame.display.update()
		pygame.time.wait(500)
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

def kill():
	if speed[0] == 0 :
		for i in range(1,len(tails)):
			if head[0] <= tails[i].tail[0] + d and head[1] <= tails[i].tail[1] + d and head[0] >= tails[i].tail[0] - d and head[1] >= tails[i].tail[1] - d :
				text_display("BIT YOURSELF TOO BAD",10*(width//20),40*(height//100),10*(height//100),RED)
				pygame.display.update()
				pygame.time.wait(500)
				pygame.quit()
			else :
				for j in range(len(tails)-1,i+1,-1):
					if tails[i].tail[0] <= tails[j].tail[0] + d and tails[i].tail[1] <= tails[j].tail[1] + d and tails[i].tail[0] >= tails[j].tail[0] - d and tails[i].tail[1] >= tails[j].tail[1] - d :
						text_display("BIT YOURSELF TOO BAD",10*(width//20),40*(height//100),10*(height//100),RED)
						pygame.display.update()
						pygame.time.wait(500)
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
	fps[0] += 2

def eat():
	if speed[0] > 0 or speed[1] > 0:
		if food[0] <= head[0] + pixel and food[1] <= head[1] + pixel and food[0] >= head[2] - pixel and food[1] >= head[3] - pixel :
			score()
			end = len(tails) - 1
			new_food(10*random.randint(2*pixel/10,10*(width//100)-(pixel*2/10)),10*random.randint(2*pixel/10,40*(height//500)-(pixel*2/10)))
			eaten[0] += 1
			tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
			pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
			pygame.display.update()
			if eaten[0]%2 == 0 :
				speed_update()
	elif speed[0] < 0 or speed[1] < 0:
		if food[0] <= head[2] + pixel and food[1] <= head[3] + pixel and food[0] >= head[0] - pixel and food[1] >= head[1] - pixel :
			score()
			end = len(tails) - 1
			new_food(10*random.randint(2*pixel/10,10*(width//100)-(pixel*2/10)),10*random.randint(2*pixel/10,40*(height//500)-(pixel*2/10)))
			eaten[0] += 1
			tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
			pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
			pygame.display.update()
			if eaten[0]%2 == 0 :
				speed_update()
	
def new_food(i,j):
	food[0] = i
	food[1] = j
	pygame.draw.circle(screen, LIGHTBLUE, (food[0], food[1]), pixel)
	pygame.display.update()

def score():
	high = open("score.dat","r")
	global high_score
	high_score = [int(high.read(10))]
	high.close()
	high = open("score.dat","w")
	if eaten[0] >= high_score[0] :
		high_score = eaten
		high.write(str(eaten[0]))
	else :
		high.write(str(high_score[0]))
	high.close()


def cheat_speed(i):
	if i < 0 :
		fps[0] -= 2
	else :
		speed_update()

def cheat_food():
	if head[0] < 10*(width//20) and head[1] < 40*(height//100) :
		new_food(10*random.randint(head[0]/10,10*(width//200)),10*random.randint(head[1]/10,40*(height//1000)))
	elif head[0] > 10*(width//20) and head[1] < 40*(height//100) :
		new_food(10*random.randint(10*(width//200),head[0]/10),10*random.randint(head[1]/10,40*(height//1000)))
	elif head[0] < 10*(width//20) and head[1] > 40*(height//100) :
		new_food(10*random.randint(head[0]/10,10*(width//200)),10*random.randint(40*(height//1000),head[1]/10))
	elif head[0] >= 10*(width//20) and head[1] >= 40*(height//100) :
		new_food(10*random.randint(10*(width//200),head[0]/10),10*random.randint(40*(height//1000),head[1]/10))

def cheat_eat(i):
	if i > 0 :
		end = len(tails) - 1
		new_food(10*random.randint(2*pixel/10,10*(width//100)-(pixel*2/10)),10*random.randint(2*pixel/10,(40*height//500)-(pixel*2/10)))
		eaten[0] += 1
		pd[0] += 1
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()
	else :
		end = len(tails) - 1
		new_food(10*random.randint(2*pixel/10,10*(width//100)-(pixel*2/10)),10*random.randint(2*pixel/10,(40*height//500)-(pixel*2/10)))
		pd[0] += 1
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()

def cheat():
	text_display("OOPS PRESSED",10*(width//20),40*(height//100),10*(height//100),RED)
	text_display("THE WRONG BUTTON",10*(width//20),10*(height//20),10*(height//100),RED)
	pygame.display.update()
	pygame.time.wait(1000)
	pygame.quit()


score()
new_food(10*random.randint(2*pixel/10,10*(width//100)-(pixel*2/10)),10*random.randint(2*pixel/10,(40*height//500)-(pixel*2/10)))
while True :
	display()
	clock.tick(fps[0])	
	threading.Thread(target = move).start()	
	eat()
	kill()
	for event in pygame.event.get():
		direction()
