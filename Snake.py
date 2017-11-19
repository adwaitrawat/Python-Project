import pygame, random, threading, os

size = width, height = 1000, 1000
pixel = 5
d = 2
pd = [2]
high_score = [0]
speed = [pixel*2,0]
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

tails = [tail(490,400,pixel*2,0)]

def display():
	pygame.init()
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,1000,800), pixel)
	pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
	pygame.draw.circle(screen, LIGHTBLUE, (food[0], food[1]), pixel)
	pygame.draw.circle(screen, GREEN, (tails[0].tail[0], tails[0].tail[1]), pixel)
	pygame.draw.rect(screen , RED ,[0,800,500,200] ,pixel)
	pygame.draw.rect(screen , RED ,[500,800,500,200] ,pixel)
	snake = pygame.font.SysFont("comicsans",150)
	snake_dis = snake.render(("SNAKES"),True,GREEN)
	snake_rect = snake_dis.get_rect()
	snake_rect.centerx = 750
	snake_rect.centery = 900
	screen.blit(snake_dis, snake_rect)
	by = pygame.font.SysFont("comicsans",20)
	by_dis = by.render(("By - Adwait Rawat and Team"),True,GREEN)
	by_rect = by_dis.get_rect()
	by_rect.centerx = 850
	by_rect.centery = 940
	screen.blit(by_dis, by_rect)
	if eaten[0] >= high_score[0] :
		s = pygame.font.SysFont("comicsans",50)
		score = s.render("SCORE : "+str(eaten[0]),True,GREEN)
		score_rect = score.get_rect()
		score_rect.centerx = 175
		score_rect.centery = 875
		screen.blit(score, score_rect)
		high_s = pygame.font.SysFont("comicsans",50)
		high_s = high_s.render("HIGH SCORE : "+str(high_score[0]),True,GREEN)
		hs_rect = high_s.get_rect()
		hs_rect.centerx = 175
		hs_rect.centery = 925
		screen.blit(high_s, hs_rect)
	else :
		s = pygame.font.SysFont("comicsans",50)
		score = s.render("SCORE : "+str(eaten[0]),True,WHITE)
		score_rect = score.get_rect()
		score_rect.centerx = 175
		score_rect.centery = 875
		screen.blit(score, score_rect)
		high_s = pygame.font.SysFont("comicsans",50)
		high_s = high_s.render("HIGH SCORE : "+str(high_score[0]),True,WHITE)
		hs_rect = high_s.get_rect()
		hs_rect.centerx = 175
		hs_rect.centery = 925
		screen.blit(high_s, hs_rect)
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
			e = pygame.font.SysFont("comicsans",100)
			esc = e.render("QUITTING",True,RED)
			esc_rect = esc.get_rect()
			esc_rect.centerx = 500
			esc_rect.centery = 400
			screen.blit(esc, esc_rect)
			pygame.display.update()
			pygame.time.wait(1000)
			pygame.quit()
		elif event.key == pygame.K_SPACE:
			p = pygame.font.SysFont("comicsans",100)
			pau = p.render("PAUSING FOR 5 SEC",True,RED)
			pau_rect = pau.get_rect()
			pau_rect.centerx = 500
			pau_rect.centery = 400
			screen.blit(pau, pau_rect)
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

def move():
	for i in range (0,2):
		head[i+2] = head[i]
		head[i]+=speed[i]
	if head[0] >= 1000 + pixel or head[1] >= 800 + pixel or head[0]  <= pixel  or head[1] <= pixel :
		h = pygame.font.SysFont("comicsans",100)
		hea = h.render("BUMPED INTO THE WALL",True,RED)
		hea_rect = hea.get_rect()
		hea_rect.centerx = 500
		hea_rect.centery = 400
		screen.blit(hea, hea_rect)
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
	pygame.display.update()

def kill():
	if speed[0] == 0 :
		for i in range(1,len(tails)):
			if head[0] <= tails[i].tail[0] + d and head[1] <= tails[i].tail[1] + d and head[0] >= tails[i].tail[0] - d and head[1] >= tails[i].tail[1] - d :
				k = pygame.font.SysFont("comicsans",100)
				kill = k.render("BIT YOURSELF TOO BAD",True,RED)
				kill_rect = kill.get_rect()
				kill_rect.centerx = 500
				kill_rect.centery = 400
				screen.blit(kill, kill_rect)
				pygame.display.update()
				pygame.time.wait(500)
				pygame.quit()
			else :
				for j in range(len(tails)-1,i+1,-1):
					if tails[i].tail[0] <= tails[j].tail[0] + d and tails[i].tail[1] <= tails[j].tail[1] + d and tails[i].tail[0] >= tails[j].tail[0] - d and tails[i].tail[1] >= tails[j].tail[1] - d :
						ki = pygame.font.SysFont("comicsans",100)
						killl = ki.render("BIT YOURSELF TOO BAD",True,RED)
						killl_rect = killl.get_rect()
						killl_rect.centerx = 500
						killl_rect.centery = 400
						screen.blit(killl, killl_rect)
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
			new_food(10*random.randint(2*pixel/10,100-(pixel*2/10)),10*random.randint(2*pixel/10,80-(pixel*2/10)))
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
			new_food(10*random.randint(2*pixel/10,100-(pixel*2/10)),10*random.randint(2*pixel/10,80-(pixel*2/10)))
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
	pygame.draw.rect(screen , RED ,[0,800,500,200] ,pixel)
	if eaten[0] >= high_score[0] :
		s = pygame.font.SysFont("comicsans",50)
		score = s.render("SCORE : "+str(eaten[0]),True,GREEN)
		score_rect = score.get_rect()
		score_rect.centerx = 175
		score_rect.centery = 875
		screen.blit(score, score_rect)
		high_score = eaten
		high.write(str(eaten[0]))
		high_s = pygame.font.SysFont("comicsans",50)
		high_s = high_s.render("HIGH SCORE : "+str(high_score[0]),True,GREEN)
		hs_rect = high_s.get_rect()
		hs_rect.centerx = 200
		hs_rect.centery = 925
		screen.blit(high_s, hs_rect)
		pygame.display.update()
	else :
		high.write(str(high_score[0]))
		s = pygame.font.SysFont("comicsans",50)
		score = s.render("SCORE : "+str(eaten[0]),True,WHITE)
		score_rect = score.get_rect()
		score_rect.centerx = 200
		score_rect.centery = 875
		screen.blit(score, score_rect)
		high_s = pygame.font.SysFont("comicsans",50)
		high_s = high_s.render("HIGH SCORE : "+str(high_score[0]),True,WHITE)
		hs_rect = high_s.get_rect()
		hs_rect.centerx = 175
		hs_rect.centery = 925
		screen.blit(high_s, hs_rect)
		pygame.display.update()
	high.close()


def cheat_speed(i):
	if i < 0 :
		fps[0] -= 2
	else :
		speed_update()

def cheat_food():
	if head[0] < 500 and head[1] < 400 :
		new_food(10*random.randint(head[0]/10,50),10*random.randint(head[1]/10,40))
	elif head[0] > 500 and head[1] < 400 :
		new_food(10*random.randint(50,head[0]/10),10*random.randint(head[1]/10,40))
	elif head[0] < 500 and head[1] > 400 :
		new_food(10*random.randint(head[0]/10,50),10*random.randint(40,head[1]/10))
	elif head[0] >= 500 and head[1] >= 400 :
		new_food(10*random.randint(50,head[0]/10),10*random.randint(40,head[1]/10))

def cheat_eat(i):
	if i > 0 :
		end = len(tails) - 1
		new_food(10*random.randint(2*pixel/10,100-(pixel*2/10)),10*random.randint(2*pixel/10,80-(pixel*2/10)))
		eaten[0] += 1
		pd[0] += 1
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()
	else :
		end = len(tails) - 1
		new_food(10*random.randint(2*pixel/10,100-(pixel*2/10)),10*random.randint(2*pixel/10,80-(pixel*2/10)))
		pd[0] += 1
		tails.append(tail(tails[end].tail[0],tails[end].tail[1],tails[end].speed_tail[0],tails[end].speed_tail[1]))
		pygame.draw.circle(screen, GREEN, (tails[end].tail[0], tails[end].tail[1]), pixel)
		pygame.display.update()

def cheat():
	c = pygame.font.SysFont("comicsans",100)
	cheat = c.render("OOPS PRESSED",True,RED)
	cheat_rect = cheat.get_rect()
	cheat_rect.centerx = 500
	cheat_rect.centery = 400
	screen.blit(cheat, cheat_rect)
	ch = pygame.font.SysFont("comicsans",100)
	cheatt = ch.render("THE WRONG BUTTON",True,RED)
	cheatt_rect = cheatt.get_rect()
	cheatt_rect.centerx = 500
	cheatt_rect.centery = 500
	screen.blit(cheatt, cheatt_rect)
	pygame.display.update()
	pygame.time.wait(1000)
	pygame.quit()


score()
new_food(10*random.randint(2*pixel/10,100-(pixel*2/10)),10*random.randint(2*pixel/10,80-(pixel*2/10)))
while True :
	display()
	clock.tick(fps[0])	
	threading.Thread(target = move).start()	
	eat()
	kill()
	for event in pygame.event.get():
		direction()
