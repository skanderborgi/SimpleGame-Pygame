import pygame
import random


#Sound
pygame.mixer.init()
pygame.mixer.set_num_channels(2)
sound1 = pygame.mixer.Sound("bgmusic.ogg")


#Initialization 
pygame.init()
screen=pygame.display.set_mode((600,700))#screen creation
#Background Image:
bg = pygame.image.load("space.png")
#Title:
pygame.display.set_caption("Meteor")
#Icon:
icon=pygame.image.load("asteroid.png")
pygame.display.set_icon(icon)
#Player:
playerImg=pygame.image.load("player.png")
playerX=280
playerY=500
playerX_change=0
playerY_change=0
def player(X,Y):
	screen.blit(playerImg,(X,Y))
#Ennemy
Ennemy1Img=pygame.image.load("ennemy1.png")
Ennemy1X=random.randint(200,650)
Ennemy1Y=100
def Ennemy1(X,Y):
	screen.blit(Ennemy1Img,(X,Y))
#Bullet
BulletImg=pygame.image.load("bullet.png")
bulletSound = pygame.mixer.Sound("bullet.wav")


Bullet_state="hidden" #no bullet lanched /"fire" if it's lanched
def fire_Bullet(X,Y):
	global Bullet_state
	Bullet_state="fire"
	screen.blit(BulletImg,(X+16,Y+10))






running=True
while running:#game loop to make window always opened
	sound1.play(loops = -1)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		#if key clicked check whether left,right,up or down
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				playerX_change=-1

			if event.key==pygame.K_RIGHT:
				playerX_change=1
			if event.key==pygame.K_DOWN:
				playerY_change=1

			if event.key==pygame.K_UP:
				playerY_change=-1
			if event.key==pygame.K_SPACE:
				if Bullet_state is "hidden":
					BulletY=playerY
					BulletX=playerX
					fire_Bullet(playerX,playerY)
					pygame.mixer.Channel(0).play(bulletSound)

			if event.key==pygame.K_UP and event.key==pygame.K_RIGHT:
				playerY_change=-1	
				playerX_change=1
			if event.key==pygame.K_UP and event.key==pygame.K_LEFT:
				playerY_change=-1	
				playerX_change=-1		
			if event.key==pygame.K_DOWN and event.key==pygame.K_RIGHT:
				playerY_change=1	
				playerX_change=1
			if event.key==pygame.K_DOWN and event.key==pygame.K_LEFT:
				playerY_change=1	
				playerX_change=-1		





		if event.type==pygame.KEYUP:#key is released
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_UP:
				playerX_change=0
				playerY_change=0







	screen.blit(bg, (-130, -80))
	playerX +=playerX_change 
	playerY +=playerY_change


	Ennemy1Y+=2
	Ennemy1X+=random.choice([-1.5, 1.5])

	if Bullet_state is "fire":
		fire_Bullet(BulletX,BulletY)
		BulletY-=5
		if BulletY<=0 :
			Bullet_state="hidden"
	if playerX<=0 :
		playerX=0
	if playerX>=540:
		playerX=540
	if playerY<=10 :
		playerY=10
	if playerY>=625:
		playerY=625
	Ennemy1(Ennemy1X,Ennemy1Y)
	player(playerX,playerY)
	if (Ennemy1Y>625)or (Ennemy1X>540):
		Ennemy1Y=100
		Ennemy1X=random.randint(200,650)
		Ennemy1(Ennemy1X,Ennemy1Y)

	#Destruction
	
	pygame.display.update()
 