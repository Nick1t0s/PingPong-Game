def ult():
    global s,speed,score,score1,score2
    if (s == False and ((player1Left or player1Right) and ball.colliderect(player1))):
        score1 += 3
        score += 3
        s = True
        speed = 13
        ul.play()
    elif (s == False and ((player2Left or player2Right) and ball.colliderect(player2))):
        score2 += 3
        score += 3
        s = True
        speed = 13
        ul.play()
    else:
        s = False
        speed = 8
    roket.play()

import pygame, sys,random,tkinter.filedialog
from pygame.locals import *
from pygame import mixer

# init
pygame.init()
mixer.init()
root = tkinter.Tk()
root.withdraw()
# data
musicPlay = True
WIDTH = 900
HEIGHT = 800
typ = 'multi'

window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption('Ping-Pong')
clock = pygame.time.Clock()

basicFont = pygame.font.SysFont(None, 70)

# sound
roket = mixer.Sound("data/roket.mp3")
wall = mixer.Sound("data/Desk.mp3")
ul = mixer.Sound("data/Kiya.mp3")

pr = 20
s = False

# type move
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
dir = random.choice((DOWNRIGHT,DOWNLEFT,UPRIGHT,UPLEFT))
speed = 8
score = 0
# is move
player1Left = False
player1Right = False
player2Left = False
player2Right = False
scr = 'start'


YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

backIm =  pygame.image.load('data/Background.png')
back_r = backIm.get_rect()
sF = pygame.font.SysFont('arial',60)
score1 = 0
score2 = 0

ball = pygame.Rect(490,490,40,40)

player1 = pygame.Rect(450,700,200,10)
player2 = pygame.Rect(450,100,200,10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and scr == 'start':
            score1 = 0
            score2 = 0
            score = 0
            scr = 'play'
            if event.pos[1] <= 255:
                typ = 'single'
            elif event.pos[1] >255 and event.pos[1] < 475:
                typ = 'bot'
            else:
                typ = 'multi'
            print(typ)

        if event.type == MOUSEBUTTONDOWN and scr == 'end':
            scr = 'start'
            score = 0
            score1 = 0
            score2 = 0
            ball.centerx = 500
            ball.centery = 500
            player1.centerx = 500
            player2.centerx = 500

        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                if typ == 'single':
                    player2Left = True
                    player1Left = True
                if typ == 'multi':
                    player1Left = True
                if typ == 'bot':
                    player1Left = True

            if event.key == K_RIGHT:
                if typ == 'single':
                    player2Right = True
                    player1Right = True
                if typ == 'multi':
                    player1Right = True
                if typ == 'bot':
                    player1Right = True

            if event.key == K_a:
                if typ == 'single':
                    player2Left = True
                    player1Left = True
                if typ == 'multi':
                    player2Left = True

            if event.key == K_d:
                if typ == 'single':
                    player2Right = True
                    player1Right = True
                if typ == 'multi':
                    player2Right = True
            if event.key == K_F3:
                pygame.quit()
                sys.exit()



        if event.type == KEYUP:

            if event.key == K_LEFT:
                if typ == 'single':
                    player2Left = False
                    player1Left = False
                if typ == 'multi':
                    player1Left = False
                if typ == 'bot':
                    player1Left = False
            if event.key == K_RIGHT:
                if typ == 'single':
                    player2Right = False
                    player1Right = False
                if typ == 'multi':
                    player1Right = False
                if typ == 'bot':
                    player1Right = False

            if event.key == K_a:
                if typ == 'single':
                    player2Left = False
                    player1Left = False
                if typ == 'multi':
                    player2Left = False

            if event.key == K_d:
                if typ == 'single':
                    player2Right = False
                    player1Right = False
                if typ == 'multi':
                    player2Right = False

            if event.key == K_F1:
                if musicPlay:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                musicPlay = not musicPlay
            if event.key == K_F2:
                mixer.music.load(tkinter.filedialog.askopenfilename())
                mixer.music.play(-1,0.0)

    window.fill((255,255,255))
    window.blit(backIm, back_r)

    if scr == 'start':
        texts = sF.render("?????????????????? ????????",True,RED)
        window.blit(texts,(300,100))
        textsb = sF.render("?? ??????????",True,YELLOW)
        window.blit(textsb,(375,350))
        texts2 = sF.render("?? ????????????", True, GREEN)
        window.blit(texts2, (375, 600))

    if scr =='play':
        if player1Left and player1.left > 0:
           player1.left -= 15
        if player1Right and player1.right < WIDTH:
            player1.left += 15

        if player2Left and player2.left > 0:
            player2.left -= 15
        if player2Right and player2.right < WIDTH:
            player2.left += 15

    if ball.colliderect(player1) and scr =='play':
        ult()
        if typ == 'multi' or typ == 'bot':
            score1 += 1
        if typ == 'single':
            score += 1
        if dir == DOWNLEFT:
            dir = UPLEFT
        if dir == DOWNRIGHT:
            dir = UPRIGHT

    if ball.colliderect(player2) and scr =='play':
        ult()
        if typ == 'multi' or typ == 'bot':
            score2 += 1
        if typ == 'single':
            score += 1
        if dir == UPLEFT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = DOWNRIGHT

    if ball.left < 0 and scr =='play':
        wall.play()
        if dir == DOWNLEFT:
            dir = DOWNRIGHT
        if dir == UPLEFT:
            dir = UPRIGHT

    if ball.right > WIDTH and scr =='play':
        wall.play()
        if dir == DOWNRIGHT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = UPLEFT


    if ball.top < 0:
        scr = 'end'
        if typ == 'single':
            text = basicFont.render("???????? " + str(score),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'multi':
            text = basicFont.render("?????????????? ?????????? 1, ????????: " + str(score1),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'bot':
            text = basicFont.render("?????????????? ??????????, ????????: " + str(score1),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery

    if ball.bottom > HEIGHT:
        scr = 'end'
        if typ == 'single':
            text = basicFont.render("???????? " + str(score),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'multi':
            text = basicFont.render("?????????????? ?????????? 2, ????????: " + str(score2), RED, RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'bot':
            text = basicFont.render("?????????????? ??????, ????????: " + str(score2), RED, RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery

    if scr =='end':
        window.blit(text, textRect)

    if scr =='play':
        if dir == DOWNLEFT:
            ball.left -= speed
            ball.top += speed
        if dir == DOWNRIGHT:
            ball.left += speed
            ball.top += speed
        if dir == UPLEFT:
            ball.left -= speed
            ball.top -= speed
        if dir == UPRIGHT:
            ball.left += speed
            ball.top -= speed

        pygame.draw.ellipse(window, YELLOW, ball)
        pygame.draw.rect(window,RED,player1)
        pygame.draw.rect(window, GREEN, player2)

    if scr == 'play' and typ == 'bot':
        if player1Left and player1.left > 0:
           player1.left -= 15
        if player1Right and player1.right < WIDTH:
            player1.left += 15

        if player2.right < WIDTH or (dir in (DOWNLEFT,UPLEFT) and ball.right<740 ):
            player2.left = ball.left


    pygame.display.update()
    clock.tick(500)
