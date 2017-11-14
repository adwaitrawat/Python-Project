import pygame, random ,threading

size = width, height = 1000, 800
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
fps=20

def direction():
	if event.type == pygame.KEYDOWN :
		if speed[0] > 0 and speed[1] == 0 :
			if event.key == pygame.K_UP:
				temp = speed[0]
				speed[0] = 0
				speed[1] = -1*temp
			if event.key == pygame.K_DOWN :
				temp = speed[0]
				speed[0] = 0
				speed[1] = temp
		if speed[1] > 0 and speed[0] == 0 :
			if event.key == pygame.K_RIGHT :
				temp = speed[1]
				speed[1] = 0
				speed[0] = temp
			if event.key == pygame.K_LEFT : 
				temp = speed[1]
				speed[1] = 0
				speed[0] = -1*temp
		if speed[0] < 0 and speed[1] == 0 :
			if event.key == pygame.K_UP:
				temp = speed[0]
				speed[0] = 0
				speed[1] = temp
			if event.key == pygame.K_DOWN :
				temp = speed[0]
				speed[0] = 0
				speed[1] = -1*temp
		if speed[1] < 0 and speed[0] == 0 :
			if event.key == pygame.K_RIGHT :
				temp = speed[1]
				speed[1] = 0
				speed[0] = -1*temp
			if event.key == pygame.K_LEFT : 
				temp = speed[1]
				speed[1] = 0
				speed[0] = temp
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
	pass

def display():
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, (0,0,1000,800), pixel)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.display.update()

def move():
	for i in range (0,2):
		display()
		head[i]+=speed[i]
		pygame.draw.rect(screen, GREEN, (head[0]-pixel,head[1]-pixel,2*pixel,2*pixel), 0)
		pygame.display.update()
		print(head)
	pass


def wall():
	if head[0] + 2*pixel >= 1000 or head[1] + 2*pixel >= 800 or head[0]  <= 0 or head[1] <= 0 :
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
	food[0]=random.randint(0+pixel,1000-pixel)
	food[1]=random.randint(0+pixel,800-pixel)
	pygame.draw.circle(screen, YELLOW, (food[0], food[1]), pixel)
	pygame.display.update()
	pass

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 250) #Adds continuos mobility to the head
pygame.init()
display()
new_food()
move()
while wall() :
	for event in pygame.event.get():
		clock.tick(fps)
		move()
		direction()
		eat()
		
		
