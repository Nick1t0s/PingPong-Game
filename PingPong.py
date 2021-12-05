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
WIDTH = 1000
HEIGHT = 1000
typ = 'multi'

window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption('Ping-Pong')
clock = pygame.time.Clock()

basicFont = pygame.font.SysFont(None, 70)

# sound
roket = mixer.Sound("data/roket.mp3")
wall = mixer.Sound("data/Desk.mp3")

# type move
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
dir = random.choice((DOWNRIGHT,DOWNLEFT,UPRIGHT,UPLEFT))
speed = 7
score = 0
# is move
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
sF = pygame.font.SysFont('arial',60)
score1 = 0
score2 = 0

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
            if event.pos[1] > 500:
                typ = 'multi'
            else:
                typ = 'single'
            print(typ)
        if event.type == MOUSEBUTTONDOWN and not start_game and not play and end_game:
            play = True
            end_game = False
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                if typ == 'single':
                    player2Left = True
                    player1Left = True
                if typ == 'multi':
                    player1Left = True

            if event.key == K_RIGHT:
                if typ == 'single':
                    player2Right = True
                    player1Right = True
                if typ == 'multi':
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



        if event.type == KEYUP:

            if event.key == K_LEFT:
                if typ == 'single':
                    player2Left = False
                    player1Left = False
                if typ == 'multi':
                    player1Left = False
            if event.key == K_RIGHT:
                if typ == 'single':
                    player2Right = False
                    player1Right = False
                if typ == 'multi':
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

    if not play and start_game:
        texts = sF.render("Одиночная игра",True,RED)
        window.blit(texts,(300,100))
        texts2 = sF.render("С другом", True, GREEN)
        window.blit(texts2, (400, 800))

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
        roket.play()
        if typ == 'multi':
            score1 += 1
        if typ == 'single':
            score += 1
        if dir == DOWNLEFT:
            dir = UPLEFT
        if dir == DOWNRIGHT:
            dir = UPRIGHT

    if ball.colliderect(player2):
        roket.play()
        if typ == 'multi':
            score2 += 1
        if typ == 'single':
            score += 1
        if dir == UPLEFT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = DOWNRIGHT

    if ball.left < 0:
        wall.play()
        if dir == DOWNLEFT:
            dir = DOWNRIGHT
        if dir == UPLEFT:
            dir = UPRIGHT

    if ball.right > WIDTH:
        wall.play()
        if dir == DOWNRIGHT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = UPLEFT


    if ball.top < 0:
        play = False
        end_game = True
        if typ == 'single':
            text = basicFont.render("Счет " + str(score),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'multi':
            text = basicFont.render("Победил игрок 1, счёт: " + str(score1),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery

    if ball.bottom > HEIGHT:
        play = False
        end_game = True
        if typ == 'single':
            text = basicFont.render("Счет " + str(score),RED,RED)
            textRect = text.get_rect()
            textRect.centerx = window.get_rect().centerx
            textRect.centery = window.get_rect().centery
        if typ == 'multi':
            text = basicFont.render("Победил игрок 2, счёт: " + str(score2), RED, RED)
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