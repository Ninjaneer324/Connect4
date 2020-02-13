import pygame
from pygame.locals import *
from circle import *

width = 800
height = 800

rad = 25

window = pygame.display.set_mode((width, height))
pygame.font.init()

pygame.display.set_caption("Connect 4")

#bigger font
myfont = pygame.font.SysFont("Comic Sans MS", 50)
#smaller font
myfont1 = pygame.font.SysFont("Comic Sans MS", 30)
#even smaller font
font2 = pygame.font.SysFont("Comic Sans MS", 20)

red = False
yellow = False

a = [[circle(255, 255, 255, 100, 100) for c in range(7)] for r in range(6)]

color = (255, 0, 0)


pos = (100, 100)

play = True

instruct = True

#checks that r and c values given don't exceed array boundries
def inRange(r, c):
    if r > -1 and r < len(a) and c > -1 and c < len(a[r]):
        return True
    return False

for r in range(len(a)):
    for c in range(len(a[r])):
        a[r][c] = circle(255, 255, 255, 100, 100)

"""Next 8 methods: check in each direction from 
a[x][y] don't exceed boundries and give a win for the color in argument
"""
def checkNorth(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x, y-i):
            if not (a[x][y-i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkSouth(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x, y + i):
            if not (a[x][y + i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkEast(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x + i, y):
            if not (a[x + i][y].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkWest(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x - i, y):
            if not (a[x - i][y].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkNorthEast(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x + i, y - i):
            if not (a[x + i][y - i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkNorthWest(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x - i, y - i):
            if not (a[x - i][y - i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkSouthEast(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x + i, y + i):
            if not (a[x + i][y + i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkSouthWest(x, y, r, g, b):
    for i in range(1,4):
        if inRange(x - i, y + i):
            if (not a[x - i][y + i].color() == (r, g, b)):
                return False
        else:
            return False
    return True

def checkWin(r, c):
    if checkNorth(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or checkSouth(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or checkEast(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or \
            checkWest(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or checkNorthEast(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or \
            checkNorthWest(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or checkSouthEast(r, c, a[r][c].red, a[r][c].green, a[r][c].blue) or \
            checkSouthWest(r, c, a[r][c].red, a[r][c].green, a[r][c].blue):
        return True
    return False


#Next 2 methods check who wins
def checkRedWin():
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c].color() == (255, 0, 0):
                if checkWin(r, c):
                    return True

    return False

def checkYellowWin():
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c].color() == (255, 255, 0):
                if checkWin(r,c):
                    return True
    return False

#Checks if checkerboard is filled in case of draw
def allDone():
    for r in range(len(a)):
        for c in range(len(a[r])):
            if not a[r][c].done:
                return False
    return True

#Instructions window
while instruct:
    window.fill((0, 0, 0))
    inst = font2.render("Intructions:", True, (255, 255, 255))
    i_1 = font2.render("-Press right and left arrow to move chip", True, (255, 255, 255))
    i_2 = font2.render("-Press space to move it down", True, (255, 255, 255))
    i_3 = font2.render("Have fun! :D Press Space to Start!", True, (255, 255, 255))
    window.blit(inst, (350, 200))
    window.blit(i_1, (240, 230))
    window.blit(i_2, (285, 260))
    window.blit(i_3, (250, 320))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                instruct = False
    pygame.display.update()


#Actual game itself :)
while True:
    if play:
        main = circle(color[0],color[1],color[2], pos[0],pos[1])
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if main.x - 100 >= 100:
                        main.moveLeft()
                        pos = main.pos()
                if event.key == K_RIGHT:
                    if main.x + 100 <= 700:
                        main.moveRight()
                        pos = main.pos()
                if event.key == pygame.K_SPACE:
                    c = (main.x-100)//100
                    times = 1
                    for r in range(len(a)):
                        if not a[len(a) - 1 - r][c].done:
                            a[len(a) - 1 - r][c].done = True
                            a[len(a) - 1 - r][c].red = main.red
                            a[len(a) - 1 - r][c].green = main.green
                            a[len(a) - 1 - r][c].blue = main.blue
                            if color == (255,255,0):
                                color = (255, 0, 0)
                            else:
                                color = (255, 255, 0)
                            break
        #Drawing and redrawing of board
        window.fill((0, 0, 255))
        for r in range(len(a)):
            for c in range(len(a[r])):
                a[r][c].x = c * 100 + 100
                a[r][c].y = r * 100 + 200
                pygame.draw.circle(window, a[r][c].color(), a[r][c].pos(), rad)
        pygame.draw.circle(window, main.color(), main.pos(), rad)

        pygame.display.update()
        pygame.time.delay(115)

        if checkRedWin():
            #print("Red Won!")
            red = True
            play = False

        elif checkYellowWin():
            yellow = True
            play = False
        elif allDone():
            play = False
    else:
        #Drawing of who wins or draw screen when game is over
        #print("Reached")
        while True:
            window.fill((0, 0, 255))
            textsurface = myfont.render("Draw", True, (255, 255, 255))
            if red:
                textsurface = myfont.render("Red Wins", True, (255, 0, 0))
            elif yellow:
                textsurface = myfont.render("Yellow Wins", True, (255, 255, 0))

            window.blit(textsurface, (300, 300))

            #Play again option
            temp = myfont1.render("Play again? Press Backspace", True, (255, 255, 255))
            window.blit(temp, (250, 350))
            get_out = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        play = True
                        red = False
                        yellow = False
                        a = [[circle(255, 255, 255, 100, 100) for c in range(7)] for r in range(6)]
                        color = (255, 0, 0)
                        pos = (100, 100)
                        get_out = True
                        break
            #gets out of this while true loop to restart game
            pygame.display.update()
            if get_out:
                break
pygame.display.update()