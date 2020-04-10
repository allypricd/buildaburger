# Ally Price ajp5nm

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# game: build a burger
# goal is to get with all toppings

# necessary: user input: arrow keys to move/jump
# necessary: graphics: burger, toppings, enemies
# necessary: start screen
# necessary: small enough window

# optional: enemies (fork and knife)
# optional: collectables (toppings)
# optional: timer
# optional: high score sheet?
# optional: maybe multiple levels?


# current problems:
# how to make it more complex?


platform1 = gamebox.from_color(0, 0, "dark green", 100000, 75)
platform1.bottom = camera.bottom

bunimage = "bottom bun.png"
bun = gamebox.from_image(100,540, bunimage)
bun.scale_by(0.2)
bun.bottom = platform1.top

burgerimage = "burger.png"
burger = gamebox.from_image(random.randint(200,700), 540, burgerimage)
burger.scale_by(0.2)
burger.bottom = platform1.top
cheeseimage = "cheese.png"
cheese = gamebox.from_image(random.randint(200,700), 540, cheeseimage)
cheese.scale_by(0.2)
cheese.bottom = platform1.top
tomatoimage = "tomato.png"
tomato = gamebox.from_image(random.randint(200,700), 540, tomatoimage)
tomato.scale_by(0.2)
tomato.bottom = platform1.top
topbunimage = "top bun.png"
topbun = gamebox.from_image(random.randint(200,700), 540, topbunimage)
topbun.scale_by(0.2)
topbun.bottom = platform1.top
toppings = [burger, cheese, tomato, topbun]

bunburgerimage = "bun burger.png"
bunburger = gamebox.from_image(200, 520, bunburgerimage)
bunburger.scale_by(0.2)
bunburger.bottom = platform1.top
bunburgercheeseimage = "bun burger cheese.png"
bunburgercheese = gamebox.from_image(300, 520, bunburgercheeseimage)
bunburgercheese.scale_by(0.2)
bunburgercheese.bottom = platform1.top
bunburgercheesetomatoimage = "bun burger cheese tomato.png"
bunburgercheesetomato = gamebox.from_image(400, 510, bunburgercheesetomatoimage)
bunburgercheesetomato.scale_by(0.2)
bunburgercheesetomato.bottom = platform1.top
fullburgerimage = "full burger.png"
fullburger = gamebox.from_image(500, 510, fullburgerimage)
fullburger.scale_by(0.2)
fullburger.bottom = platform1.top

forkimage = "fork.png"
fork = gamebox.from_image(random.randint(200,700), 475, forkimage)
fork.scale_by(0.1)
fork.bottom = platform1.top
knifeimage = "knife.png"
knife = gamebox.from_image(random.randint(200,700), 475, knifeimage)
knife.scale_by(0.05)
knife.bottom = platform1.top
enemies = [fork, knife]


gravity = 0.5

for enemy in enemies:
    enemy.speedx = 5

character = bun

time = 0
time = round(time, 2)

touchburger = False
touchcheese = False
touchtomato = False
touchtop = False

play = False

win = False
lose = False


def drawcharacter():
    """determines which version of the character to draw"""
    global touchburger, touchcheese, touchtomato, touchtop, character
    if touchtop:
        fullburger.center = character.center
        character = fullburger
    elif touchtomato:
        bunburgercheesetomato.center = character.center
        character = bunburgercheesetomato
    elif touchcheese:
        bunburgercheese.center = character.center
        character = bunburgercheese
    elif touchburger:
        bunburger.center = character.center
        character = bunburger
    else:
        character = bun
    camera.draw(character)


def tick(keys):
    global win, lose, play, time
    if play == False:
        tickstartscreen(keys)
    elif play == True:
        if win == True:
            tickwin(keys)
        elif lose == True:
            ticklose(keys)
        else:
            tickplay(keys)


def tickstartscreen(keys):
    global play
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw(bun)
    camera.draw("Time: 0", 36, "red", 40, 20)
    for topping in toppings:
        camera.draw(topping)
    for enemy in enemies:
        camera.draw(enemy)
    camera.draw("Welcome to Build-A-Burger!", 36, "red", 400, 100)
    camera.draw("Controls: Arrow keys", 36, "red", 400, 175)
    camera.draw("Rules: Collect all toppings in order to win", 36, "red", 400, 250)
    camera.draw("Avoid enemies (fork and knife) or you lose", 36, "red", 400, 300)
    camera.draw("Press space to start!", 36, "red", 400, 375)
    if pygame.K_SPACE in keys:
        play = True
    camera.display()

def tickwin(keys):
    global win, time, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw("Time:", 36, "red", 40, 20)
    timebox = gamebox.from_text(100, 20, str(round(time)), 36, "red")
    camera.draw(timebox)
    camera.draw("You win!!!", 36, "red", 400, 250)
    camera.draw("Press space to play again!", 36, "red", 400, 450)
    drawcharacter()
    for topping in toppings:
        camera.draw(topping)
    for enemy in enemies:
        camera.draw(enemy)
    if pygame.K_SPACE in keys:
        win = False
        reset()
    camera.display()

def ticklose(keys):
    global lose, time, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw("Time:", 36, "red", 40, 20)
    timebox = gamebox.from_text(100, 20, str(round(time)), 36, "red")
    camera.draw(timebox)
    camera.draw("You lose :(", 36, "red", 400, 250)
    camera.draw("Press space to play again!", 36, "red", 400, 450)
    drawcharacter()
    if touchburger == False:
        camera.draw(burger)
    elif touchcheese == False:
        camera.draw(cheese)
    elif touchtomato == False:
        camera.draw(tomato)
    elif touchtop == False:
        camera.draw(topbun)
    for enemy in enemies:
        camera.draw(enemy)
    if pygame.K_SPACE in keys:
        lose = False
        reset()
    camera.display()


def reset():
    global win, lose, time, touchburger, touchcheese, touchtomato, touchtop, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    """prepares the game to start from the beginning"""
    # redrawing gameboxes in their initial locations
    bun.center = [100,540]
    bun.bottom = platform1.top
    burger.center = [random.randint(200,700),540]
    burger.bottom = platform1.top
    cheese.center = [random.randint(200,700),540]
    cheese.bottom = platform1.top
    tomato.center = [random.randint(200,700),540]
    tomato.bottom = platform1.top
    topbun.center = [random.randint(200,700),540]
    topbun.bottom = platform1.top
    toppings = [burger, cheese, tomato, topbun]
    bunburger.center = [200,520]
    bunburger.bottom = platform1.top
    bunburgercheese.center = [300,520]
    bunburgercheese.bottom = platform1.top
    bunburgercheesetomato.center = [400,510]
    bunburgercheesetomato.bottom = platform1.top
    fullburger.center= [500,510]
    fullburger.bottom = platform1.top
    fork.center = [600,475]
    fork.bottom = platform1.top
    knife.center = [350,475]
    knife.bottom = platform1.top
    timebox = gamebox.from_text(100, 20, str(round(time)), 36, "red")
    enemies = [fork, knife]
    for enemy in enemies:
        enemy.speedx = 5
    character = bun
    time = 0
    time = round(time, 2)
    touchburger = False
    touchcheese = False
    touchtomato = False
    touchtop = False
    win = False
    lose = False



def tickplay(keys):
    global character, toppings, time, pause, touchburger, touchcheese, touchtomato, touchtop, win, lose
    camera.clear("light blue")
    # character controls:
    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    if pygame.K_DOWN in keys:
        character.y += 10
    if pygame.K_UP in keys and character.bottom_touches(platform1):
        character.speedy = -10
    # gravity:
    for thing in toppings + [character] + enemies:
        thing.speedy += gravity
        thing.move_speed()
    # timer
    timebox = gamebox.from_text(100, 20, str(round(time)), 36, "red")
    # move to stop overlapping the platform:
    for each in toppings + [character] + enemies:
        each.move_to_stop_overlapping(platform1)
    # losing if you touch an enemy
    for enemy in enemies:
        if character.touches(enemy):
            lose = True
    # moving enemies:
    for enemy in enemies:
        if enemy.x < 100:
            enemy.speedx += 5
        elif enemy.x > 700:
            enemy.speedx -= 5
        enemy.move_speed()
    # changing character after picking up a topping
    if character.touches(burger):
        touchburger = True
        burger.move(1000000000000000, 10000000000000000)
        # this just moves the icon that we are done with way off the screen so it doesn't cause problems
        toppings = [tomato, cheese, topbun]
    if character.touches(cheese) and touchburger:
        touchcheese = True
        cheese.move(1000000000000000, 10000000000000000)
        toppings = [tomato, topbun]
    if character.touches(tomato) and touchburger and touchcheese:
        touchtomato = True
        tomato.move(1000000000000000, 10000000000000000)
        toppings = [topbun]
    if character.touches(topbun) and touchburger and touchcheese and touchtomato:
        touchtop = True
        topbun.move(1000000000000000, 10000000000000000)
        toppings = []
    # drawing everything
    camera.draw(platform1)
    drawcharacter()
    camera.draw("Time:", 36, "red", 40, 20)
    camera.draw(timebox)
    if touchburger == False:
        camera.draw(burger)
    elif touchcheese == False:
        camera.draw(cheese)
    elif touchtomato == False:
        camera.draw(tomato)
    elif touchtop == False:
        camera.draw(topbun)
    for enemy in enemies:
        camera.draw(enemy)
    if touchtop == True:
        win = True
    # display
    camera.display()
    # increase the timer
    time += (1/30)


gamebox.timer_loop(30, tick)
