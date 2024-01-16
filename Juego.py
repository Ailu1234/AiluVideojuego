#libraries
import pgzrun
from gpiozero import Button

#window settings
WIDTH = 1024
HEIGHT = 1024

#variablesDelJoystick
boton1 = Button(13)
boton2 = Button(19)
boton3 = Button(26)

#sprites
background = Actor('fondo')
alien = Actor('personaje')
alien.pos = 50, 200
platforms = []
for x in range(3):
    platform = Actor('plataforma')
    platform.pos = 170 + x*190, 385 -x*50
    platforms.append(platform)
door = Actor('meta')
door.pos = 580, 45
##face = Actor('face')
##face.pos = 300,250

#world variables
gravityForce = 2
speed = 2
jump = 10
jumpSwitch = False
winSwitch = False
banner = Rect((0,0),(600,500))

#functions
def gravity():
    global gravityForce, jumpSwitch
    alien.y += gravityForce

    if alien.y < 120:
        jumpSwitch = True
    if alien.y >= 375:
        alien.y = 375
        jumpSwitch = False
        
def movement():
    global speed, jump, jumpSwitch
    if keyboard.right:
        alien.x += speed
    elif keyboard.left:
        alien.x -= speed

    if keyboard.space:
        if jumpSwitch == False:
            alien.y -= jump

def joystick():
    global speed, jump, jumpSwitch
    if boton1.is_pressed:
        alien.x += speed

    if boton3.is_pressed:
        alien.x -= speed

    if boton2.is_pressed:
        if jumpSwitch == False:
            alien.y -= jump
        
def collision():
    global gravityForce, jumpSwitch

    if alien.colliderect(platforms[0]):
        gravityForce = 0
        jumpSwitch = False
    elif alien.colliderect(platforms[1]):
        gravityForce = 0
        jumpSwitch = False
    elif alien.colliderect(platforms[2]):
        gravityForce = 0
        jumpSwitch = False
    else:
        gravityForce = 2

def winGame():
    global winSwitch
    if alien.colliderect(door):
        print('U WIN!')
        winSwitch = True
        
                
def draw():
    screen.clear()
    background.draw()
    alien.draw()
    door.draw()
    for x in range(3):
        platforms[x].draw()
    if winSwitch:
        screen.clear()
        screen.draw.filled_rect(banner,(0,150,0))
        ##face.draw()

def update():
    gravity()
    movement()
    collision()
    winGame()
    joystick()
  
    #print(jumpSwitch)
pgzrun.go()
