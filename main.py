import pygame
import random
import math
import time



#Sound
pygame.mixer.init()
pygame.mixer.set_num_channels(3)
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
playerImg=pygame.image.load("playerStopped.png")
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

#Score
Score=0
font=pygame.font.Font("joystix monospace.TTF",28)
textX=10
textY=650
def show_score(X,Y):
	score=font.render("Score: "+str(Score),True,(255,255,255))
	screen.blit(score,(X,Y))
#Dead
fontDead=pygame.font.Font("joystix monospace.TTF",35)
DeadX=140
DeadY=320
Death=False
#For the sound to be launched once
DeathSound = pygame.mixer.Sound("Explosion.wav")
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper
@run_once
def Explosion(DeathSound):
	pygame.mixer.Channel(0).play(DeathSound)








def show_Dead(X,Y):
	dead=fontDead.render("You are Dead",True,(255,255,255))
	screen.blit(dead,(X,Y))



running=True
while running:#game loop to make window always opened
	sound1.play(loops = -1)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		#if key clicked check whether left,right,up or down
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				playerX_change=-2.5
				playerImg=pygame.image.load("player.png")

			if event.key==pygame.K_RIGHT:
				playerX_change=2.5
				playerImg=pygame.image.load("player.png")

			if event.key==pygame.K_DOWN:
				playerY_change=2.5

			if event.key==pygame.K_UP:
				playerY_change=-2.5
				playerImg=pygame.image.load("player.png")

			if event.key==pygame.K_SPACE:
				if Bullet_state is "hidden":
					BulletY=playerY
					BulletX=playerX
					fire_Bullet(playerX,playerY)
					pygame.mixer.Channel(0).play(bulletSound)

			if event.key==pygame.K_UP and event.key==pygame.K_RIGHT:
				playerY_change=-2.5
				playerX_change=2.5
			if event.key==pygame.K_UP and event.key==pygame.K_LEFT:
				playerY_change=-2.5	
				playerX_change=-2.5		
			if event.key==pygame.K_DOWN and event.key==pygame.K_RIGHT:
				playerY_change=2.5	
				playerX_change=2.5
			if event.key==pygame.K_DOWN and event.key==pygame.K_LEFT:
				playerY_change=2.5	
				playerX_change=-2.5		





		if event.type==pygame.KEYUP:#key is released
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_UP:
				playerX_change=0
				playerY_change=0
				playerImg=pygame.image.load("playerStopped.png")








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
	#DestructionEnnemy1
	try:
		D=math.sqrt(math.pow(Ennemy1X-BulletX,2)+math.pow(Ennemy1Y-BulletY,2))
		if D<=25:
			Ennemy1Img=pygame.image.load("explosion.png")
			Ennemy1(Ennemy1X,Ennemy1Y)
			Score+=1
			print("Bingo!")
			Ennemy1Y=800
			BulletY=-5

	except:
		pass
	#Dead
	D2=math.sqrt(math.pow(Ennemy1X-playerX,2)+math.pow(Ennemy1Y-playerY,2))
	if D2<=40 :
		Death=True
	if Death is True:
		Explosion(DeathSound)
		show_Dead(DeadX,DeadY)
		Ennemy1Y=-5
		Ennemy1X=-5
		playerY=1000




	Ennemy1Img=pygame.image.load("ennemy1.png")
	Ennemy1(Ennemy1X,Ennemy1Y)
	player(playerX,playerY)
	if (Ennemy1Y>625)or (Ennemy1X>540):
		Ennemy1Y=100
		Ennemy1X=random.randint(200,650)
		Ennemy1(Ennemy1X,Ennemy1Y)
	show_score(textX,textY)


	pygame.display.update()
 