import pygame, sys,random
from pygame.locals import *


pygame.init()
musicPlay = True
WIDTH = 1000
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption('ПингПонг')
clock = pygame.time.Clock()

basicFont = pygame.font.SysFont(None, 70)


DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
dir = random.choice((DOWNRIGHT,DOWNLEFT,UPRIGHT,UPLEFT))
speed = 7
score = 0

player1Left = False
player1Right = False
player2Left = False
player2Right = False
play = False
start_game = True
end_game = False


YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

backIm =  pygame.image.load('data/Background.png')
back_r = backIm.get_rect()


ball = pygame.Rect(490,490,40,40)

player1 = pygame.Rect(450,890,200,10)
player2 = pygame.Rect(450,100,200,10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and start_game:
            play = True
            start_game = False
        if event.type == MOUSEBUTTONDOWN and not start_game and not play and end_game:
            play = True
            end_game = False
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                player2Left = True
                player1Left = True

            if event.key == K_RIGHT:
                player2Right = True
                player1Right = True



        if event.type == KEYUP:

            if event.key == K_LEFT:
                player2Left = False
                player1Left = False
            if event.key == K_RIGHT:
                player2Right = False
                player1Right = False
            if event.key ==K_s:
                if musicPlay:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                musicPlay = not musicPlay


    window.fill((255,255,255))
    window.blit(backIm, back_r)

    if not play and start_game:
        texts = basicFont.render("Кликните чтобы начать игру",RED,RED)
        textsRect = texts.get_rect()
        textsRect.centerx = window.get_rect().centerx
        textsRect.centery = window.get_rect().centery
        window.blit(texts,textsRect)

    if play:
        if player1Left and player1.left > 0:
           player1.left -= 30
        if player1Right and player1.right < WIDTH:
            player1.left += 30

        if player2Left and player2.left > 0:
            player2.left -= 30
        if player2Right and player2.right < WIDTH:
            player2.left += 30

    if ball.colliderect(player1):
        score += 1
        if dir == DOWNLEFT:
            dir = UPLEFT
        if dir == DOWNRIGHT:
            dir = UPRIGHT

    if ball.colliderect(player2):
        score += 1
        if dir == UPLEFT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = DOWNRIGHT

    if ball.left < 0:
        if dir == DOWNLEFT:
            dir = DOWNRIGHT
        if dir == UPLEFT:
            dir = UPRIGHT

    if ball.right > WIDTH:
        if dir == DOWNRIGHT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = UPLEFT


    if ball.top < 0:
        play = False
        end_game = True
        text = basicFont.render("Счет " + str(score),RED,RED)
        textRect = text.get_rect()
        textRect.centerx = window.get_rect().centerx
        textRect.centery = window.get_rect().centery
        recRect = text.get_rect()
        recRect.centerx = window.get_rect().centerx
        recRect.centery = window.get_rect().centery

    if ball.bottom > HEIGHT:
        play = False
        end_game = True
        text = basicFont.render("Счет " + str(score),RED,RED)
        textRect = text.get_rect()
        textRect.centerx = window.get_rect().centerx
        textRect.centery = window.get_rect().centery
    if play == False and end_game:
        window.blit(text, textRect)

    if play:
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


    pygame.display.update()
    clock.tick(500)
