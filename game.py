# Ally Price ajp5nm


# imports
import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)

# game: build a burger!
# win each round by collecting all toppings
# lose by touching an enemy
# goal is to see how many rounds you can complete before you lose

# necessary: user input: arrow keys to move/jump (done)
# necessary: graphics: burger, toppings, enemies (done)
# necessary: start screen (done)
# necessary: small enough window (done)

# optional: enemies (fork and knife) (done)
# optional: collectibles (toppings) (done)
# optional: timer (done)
# optional: high score sheet (done)


# creating gameboxes:
platform1 = gamebox.from_color(0, 0, "dark green", 100000, 75)
platform1.bottom = camera.bottom

bunimage = "bottom bun.png"
bun = gamebox.from_image(100, 540, bunimage)
bun.scale_by(0.2)
bun.bottom = platform1.top

burgerimage = "burger.png"
burger = gamebox.from_image(random.randint(100, 700), 540, burgerimage)
burger.scale_by(0.2)
burger.bottom = platform1.top
cheeseimage = "cheese.png"
cheese = gamebox.from_image(random.randint(100, 700), 540, cheeseimage)
cheese.scale_by(0.2)
cheese.bottom = platform1.top
tomatoimage = "tomato.png"
tomato = gamebox.from_image(random.randint(100, 700), 540, tomatoimage)
tomato.scale_by(0.2)
tomato.bottom = platform1.top
topbunimage = "top bun.png"
topbun = gamebox.from_image(random.randint(100, 700), 540, topbunimage)
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
fork = gamebox.from_image(random.randint(200, 700), 475, forkimage)
fork.scale_by(0.1)
fork.bottom = platform1.top
knifeimage = "knife.png"
knife = gamebox.from_image(random.randint(400, 700), 475, knifeimage)
knife.scale_by(0.05)
knife.bottom = platform1.top
enemies = [fork, knife]

# gravity/initial speed
gravity = 0.6
fork.speedx = 5
knife.speedx = -5

# initial values for global variables
character = bun
time = 0
time = round(time, 2)
toppingcount = 0

touchburger = False
touchcheese = False
touchtomato = False
touchtop = False

play = False
win = False
lose = False
scoreboard = False

highscores = "highscores.csv"
name = ""
keysdict = {pygame.K_a: "A", pygame.K_b: "B", pygame.K_c: "C", pygame.K_d: "D", pygame.K_e: "E", pygame.K_f: "F",
            pygame.K_g: "G", pygame.K_h: "H", pygame.K_i: "I", pygame.K_j: "J", pygame.K_l: "L", pygame.K_m: "M",
            pygame.K_n: "N", pygame.K_o: "O", pygame.K_p: "P", pygame.K_q: "Q", pygame.K_r: "R", pygame.K_s: "S",
            pygame.K_t: "T", pygame.K_u: "U", pygame.K_v: "V", pygame.K_w: "W", pygame.K_x: "X", pygame.K_y: "Y",
            pygame.K_z: "Z", pygame.K_SPACE: " ", pygame.K_EXCLAIM: "!", pygame.K_0: "0", pygame.K_1: "1",
            pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5", pygame.K_6: "6", pygame.K_7: "7",
            pygame.K_8: "8", pygame.K_9: "9"}


# functions:
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
    """plays the game, runs all other functions when applicable"""
    global win, lose, play, time, scoreboard
    if scoreboard == True:
        tickscoreboard(keys)
    elif play == False:
        tickstartscreen(keys)
    elif play == True:
        if win == True:
            tickwin(keys)
        elif lose == True:
            ticklose(keys)
        else:
            tickplay(keys)


def tickstartscreen(keys):
    """starts the game with a start screen that explains the rules"""
    global play, scoreboard
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw(bun)
    camera.draw("Time: 0", 36, "red", 50, 50)
    camera.draw("Toppings: 0", 36, "red", 80, 20)
    for topping in toppings:
        camera.draw(topping)
    for enemy in enemies:
        camera.draw(enemy)
    camera.draw("Welcome to Build-A-Burger!", 36, "red", 400, 100)
    camera.draw("Controls: Arrow keys", 36, "red", 400, 175)
    camera.draw("Rules: Collect all toppings as quickly as possible", 36, "red", 400, 250)
    camera.draw("Avoid enemies (fork and knife) or you lose", 36, "red", 400, 300)
    camera.draw("Press space to start!", 36, "red", 400, 375)
    camera.draw("Press H to see high score board!", 36, "red", 400, 450)
    if pygame.K_h in keys:
        scoreboard = True
    if pygame.K_SPACE in keys:
        play = True
    camera.display()


def tickwin(keys):
    """displays a winner screen if you win a round, then lets you enter the next round"""
    global scoreboard, win, time, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw("Time:", 36, "red", 50, 50)
    timebox = gamebox.from_text(100, 50, str(round(time)), 36, "red")
    camera.draw(timebox)
    camera.draw("Toppings:", 36, "red", 80, 20)
    toppingcountbox = gamebox.from_text(155, 20, str(toppingcount), 36, "red")
    camera.draw(toppingcountbox)
    camera.draw("You win!!!", 36, "red", 400, 250)
    camera.draw("Press space to play another round!", 36, "red", 400, 350)
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
    """displays a loser screen if you lose, lets you play again or go to the scoreboard"""
    global name, scoreboard, lose, time, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw("Time:", 36, "red", 50, 50)
    timebox = gamebox.from_text(100, 50, str(round(time)), 36, "red")
    camera.draw("Toppings:", 36, "red", 80, 20)
    toppingcountbox = gamebox.from_text(155, 20, str(toppingcount), 36, "red")
    camera.draw(toppingcountbox)
    camera.draw(timebox)
    camera.draw("You lose :(", 36, "red", 400, 100)
    camera.draw("Type your name, then press enter to save your score!", 36, "red", 400, 300)
    camera.draw(name, 42, "red", 400, 350)
    # add player name and score to csv of scores, then take them to the high score board
    for each in keysdict:
        if each in keys:
            name += keysdict[each]
            keys.clear()
    if pygame.K_BACKSPACE in keys:
        name = name[0:len(name)-1]
        keys.clear()
    if pygame.K_RETURN in keys:
        with open(highscores, "a") as f:
            print(name + ", " + str(toppingcount) + ", " + str(round(time)), file=f)
        reset()
        scoreboard = True
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
        reset()
        lose = False
    camera.display()


def reset():
    """if the player wants to play again, resets everything to its initial values"""
    global name, toppingcount, win, lose, time, touchburger, touchcheese, touchtomato, touchtop, bun, burger, cheese, tomato, topbun, bunburger, bunburgercheese, bunburgercheesetomato, fullburger, fork, knife, toppings, enemies, character
    """prepares the game to start from the beginning"""
    # redrawing gameboxes in their initial locations
    bun.center = [100, 540]
    bun.bottom = platform1.top
    burger.center = [random.randint(100, 700), 540]
    burger.bottom = platform1.top
    cheese.center = [random.randint(100, 700), 540]
    cheese.bottom = platform1.top
    tomato.center = [random.randint(100, 700), 540]
    tomato.bottom = platform1.top
    topbun.center = [random.randint(100, 700), 540]
    topbun.bottom = platform1.top
    toppings = [burger, cheese, tomato, topbun]
    bunburger.center = [200, 520]
    bunburger.bottom = platform1.top
    bunburgercheese.center = [300, 520]
    bunburgercheese.bottom = platform1.top
    bunburgercheesetomato.center = [400, 510]
    bunburgercheesetomato.bottom = platform1.top
    fullburger.center = [500, 510]
    fullburger.bottom = platform1.top
    fork.center = [random.randint(200, 700), 475]
    fork.bottom = platform1.top
    knife.center = [random.randint(400, 700), 475]
    knife.bottom = platform1.top
    timebox = gamebox.from_text(100, 50, str(round(time)), 36, "red")
    enemies = [fork, knife]
    fork.speedx = 5
    knife.speedx = -5
    character = bun
    if lose == True:
        toppingcount = 0
        time = 0
    touchburger = False
    touchcheese = False
    touchtomato = False
    touchtop = False
    win = False
    lose = False
    name = ""


def tickscoreboard(keys):
    """displays the scoreboard"""
    global play, scoreboard
    camera.clear("light blue")
    camera.draw(platform1)
    camera.draw("High scores:", 36, "red", 400, 50)
    camera.draw("Press R to return to the main menu", 36, "red", 400, 500)
    # display csv of scores
    f = open(highscores, "r")
    listofscores = []
    for line in f:
        row = line.strip().split(",")
        namescore = [row[0], row[1], row[2]]
        listofscores.append(namescore)
    f.close()
    listofscores.sort(key=lambda x: int(x[2]))
    listofscores.sort(key=lambda x: int(x[1]), reverse=True)
    # sorts by score rather than name, with the highest score coming first
    if len(listofscores) > 12:
    # limits the number of scores printed if there are too many to fit on the screen
        for x in range(12):
            scorestring = str(listofscores[x][0]) + ", " + str(listofscores[x][1]) + " points, " + str(listofscores[x][2]) + " seconds"
            camera.draw(scorestring, 20, "red", 400, 100+(x*30))
    else:
        for x in range(len(listofscores)):
            scorestring = str(listofscores[x][0]) + ", " + str(listofscores[x][1]) + " points, " + str(listofscores[x][2]) + " seconds"
            camera.draw(scorestring, 20, "red", 400, 100+(x*30))
    if pygame.K_r in keys:
        scoreboard = False
        play = False
    camera.display()


def tickplay(keys):
    """runs the actual game and allows the user to play"""
    global character, toppings, time, touchburger, touchcheese, touchtomato, touchtop, win, toppingcount, lose
    camera.clear("light blue")
    # character controls:
    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    if pygame.K_UP in keys and character.bottom_touches(platform1):
        character.speedy = -10
    # keep character on screen
    if character.x < 0:
        character.x = 0
    if character.x > 800:
        character.x = 800
    # gravity:
    for thing in toppings + [character] + enemies:
        thing.speedy += gravity
        thing.move_speed()
    # timer and topping counter
    timebox = gamebox.from_text(100, 50, str(round(time)), 36, "red")
    toppingcountbox = gamebox.from_text(155, 20, str(toppingcount), 36, "red")
    # move to stop overlapping the platform:
    for each in toppings + [character] + enemies:
        each.move_to_stop_overlapping(platform1)
    # losing if you touch an enemy
    for enemy in enemies:
        if character.touches(enemy):
            lose = True
    # moving enemies:
    for enemy in enemies:
        if enemy.x < 0:
            enemy.speedx += 5
        elif enemy.x > 800:
            enemy.speedx -= 5
        enemy.move_speed()
    # changing character after picking up a topping
    if character.touches(burger):
        touchburger = True
        toppingcount += 1
        burger.move(1000000000000000, 10000000000000000)
        # this just moves the icon that we are done with way off the screen so it doesn't cause problems
        toppings = [tomato, cheese, topbun]
    if character.touches(cheese) and touchburger:
        touchcheese = True
        toppingcount += 1
        cheese.move(1000000000000000, 10000000000000000)
        toppings = [tomato, topbun]
    if character.touches(tomato) and touchburger and touchcheese:
        touchtomato = True
        toppingcount += 1
        tomato.move(1000000000000000, 10000000000000000)
        toppings = [topbun]
    if character.touches(topbun) and touchburger and touchcheese and touchtomato:
        touchtop = True
        toppingcount += 1
        topbun.move(1000000000000000, 10000000000000000)
        toppings = []
    # drawing everything
    camera.draw(platform1)
    drawcharacter()
    camera.draw("Time:", 36, "red", 50, 50)
    camera.draw(timebox)
    camera.draw("Toppings:", 36, "red", 80, 20)
    camera.draw(toppingcountbox)
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
