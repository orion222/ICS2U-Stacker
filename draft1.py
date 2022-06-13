# Names: Jacky and Orion
# Proect Choice: Stacker
# Stacker is a game where the user tries to align (aka stack) blocks vertically. The blocks will be moving left and
# right while the user is stacking. When the user inputs the specified key, the moving block will stop and hopefully be
# aligned with previous stacked blocks. If the stacked newly block is only partially aligned with previous blocks, the
# misaligned portion of blocks blocks will disappear and the user will be stacking with a smaller block than before;
# increases the difficulty for future stacking.

from graphics import *
import winsound
import time

screen = "newGame"
hotkey = "space"
ending = "none"

localhighscore = 0
undrawScore = Text(Point(100, 100), "hi")
tempScore = 0
while screen == "newGame":
    print("made it")
    if ending == "win":
        winScreen = GraphWin("WINNER WINNER CHICKEN DINNER", 500, 500)
        winText = Text(Point(250, 200), "YOU WIN")
        winText.setFill("lightgreen")
        winText.draw(winScreen)
        winText.setSize(35)
        newGame = Text(Point(250, 300), "New Game")
        newGame.draw(winScreen)
        newGame.setSize(15)
        rect1 = Rectangle(Point(200, 290), Point(300, 310))
        rect1.draw(winScreen)
        exitGame = Text(Point(250, 340), "Exit Game")
        exitGame.draw(winScreen)
        exitGame.setSize(15)
        rect2 = Rectangle(Point(200, 330), Point(300, 350))
        rect2.draw(winScreen)
        while screen == "newGame":
            click = winScreen.getMouse()
            if 300 >= click.getX() >= 200 and 310 >= click.getY() >= 290:
                winScreen.close()
                screen = "title"
            elif 300 >= click.getX() >= 200 and 350 >= click.getY() >= 330:
                quit()
    elif ending == "lose":
        loseScreen = GraphWin("Wow so sad you lost", 500, 500)
        loseText = Text(Point(250, 200), "YOU LOSE")
        loseText.setFill("red")
        loseText.draw(loseScreen)
        loseText.setSize(35)
        newGame = Text(Point(250, 300), "New Game")
        newGame.draw(loseScreen)
        newGame.setSize(15)
        rect1 = Rectangle(Point(200, 290), Point(300, 310))
        rect1.draw(loseScreen)
        exitGame = Text(Point(250, 340), "Exit Game")
        exitGame.draw(loseScreen)
        exitGame.setSize(15)
        rect2 = Rectangle(Point(200, 330), Point(300, 350))
        rect2.draw(loseScreen )
        while screen == "newGame":
            click = loseScreen.getMouse()
            if 300 >= click.getX() >= 200 and 310 >= click.getY() >= 290:
                loseScreen.close()
                screen = "title"
            elif 300 >= click.getX() >= 200 and 350 >= click.getY() >= 330:
                quit()

    elif ending == "finalscore":
        winScreen = GraphWin("im dying from writing code", 500, 500)
        winText = Text(Point(250, 100), "YOUR FINAL SCORE WAS")
        winText.draw(winScreen)
        winText.setSize(20)
        nobodywillcheckthisvariablename = Text(Point(250, 200), str(tempScore))
        nobodywillcheckthisvariablename.setSize(35)
        nobodywillcheckthisvariablename.setFill("Green")
        nobodywillcheckthisvariablename.draw(winScreen)
        newGame = Text(Point(250, 300), "New Game")
        newGame.draw(winScreen)
        newGame.setSize(15)
        rect1 = Rectangle(Point(200, 290), Point(300, 310))
        rect1.draw(winScreen)
        exitGame = Text(Point(250, 340), "Exit Game")
        exitGame.draw(winScreen)
        exitGame.setSize(15)
        rect2 = Rectangle(Point(200, 330), Point(300, 350))
        rect2.draw(winScreen)
        while screen == "newGame":
            click = winScreen.getMouse()
            if 300 >= click.getX() >= 200 and 310 >= click.getY() >= 290:
                winScreen.close()
                screen = "title"
            elif 300 >= click.getX() >= 200 and 350 >= click.getY() >= 330:
                quit()

    titleScreen = GraphWin("Stacker", 600, 600, autoflush=False)
    title = Text(Point(300, 75), "S T A C K E R")
    title.draw(titleScreen)
    title.setSize(30)
    classic = Text(Point(300, 230), "Classic Mode")
    classic.draw(titleScreen)
    classic.setSize(20)
    classRect = Rectangle(Point(215, 215), Point(385, 245))
    classRect.draw(titleScreen)
    endless = Text(Point(300, 285), "Endless Mode")
    endless.draw(titleScreen)
    endless.setSize(20)
    endRect = Rectangle(Point(210, 270), Point(388, 300))
    endRect.draw(titleScreen)
    hotkeyTitle = Text(Point(300, 400), "Change HotKey")
    hotkeyTitle.draw(titleScreen)
    hotkeyTitle.setSize(17)
    keyRect = Rectangle(Point(215, 390), Point(385, 410))
    keyRect.draw(titleScreen)
    rules = Text(Point(300, 447), "Rules")
    rules.draw(titleScreen)
    rules.setSize(20)
    rulesRect = Rectangle(Point(265, 460), Point(335, 435))
    rulesRect.draw(titleScreen)

    leaveText = Text(Point(550, 550), "Quit")
    leaveText.setSize(20)
    leaveRect = Rectangle(Point(520, 535), Point(580, 565))
    leaveRect.draw(titleScreen)
    leaveText.draw(titleScreen)

    aboutText = Text(Point(50, 550), "About")
    aboutText.setSize(20)
    aboutRect = Rectangle(Point(10, 535), Point(90, 565))
    aboutText.draw(titleScreen)
    aboutRect.draw(titleScreen)

    resetScore = Text(Point(410, 550), "Reset score")
    resetScore.setSize(13)
    resetScore.draw(titleScreen)

    resetRect = Rectangle(Point(360, 540), Point(460, 560))
    resetRect.draw(titleScreen)

    screen = "title"

    highscoreimg = Image(Point(rulesRect.getCenter().getX(), 525), "images/highscore.gif")
    highscoreimg.draw(titleScreen)

    while screen == "title":

        undrawScore.undraw()

        with open("highscore.txt",
                  "r") as highscorefile:  # context manager "highscorefile" is the var that stores the .txt
            contents = highscorefile.readline()

        highscoreText = Text(Point(rulesRect.getCenter().getX(), 561), contents)
        undrawScore = highscoreText
        highscoreText.setSize(20)
        highscoreText.setFill("red")
        highscoreText.draw(titleScreen)
        localhighscore = int(contents)

        update()

        print("title")
        click = titleScreen.getMouse()

        sizes = [114, 76, 38]
        blocks = [
            "images/3block.gif",
            "images/2block.gif",
            "images/1block.gif",
        ]

        buttons = [
            "images/add1.gif",
            "images/slowspeed.gif",
            "images/scoremultiply.gif"
        ]

        blackbuttons = [
            "images/add1black.gif",
            "images/slowspeedblack.gif",
            "images/scoremultiplyblack.gif"
        ]
        # hotkey = "space"  -  defined this at the top now
        level = 0
        n = 0
        block = blocks[n]
        starter = "left"
        position = 0
        size = sizes[n]
        placing = True
        stacking = True
        end = False
        direction = 1
        prevPosition = 0
        endless = False
        height = 0
        force = "none"
        powerupping = False
        temp = []
        score = 0
        count = 0
        multiplier = False
        slowed = 1
        bop = 0

        if 385 >= click.getX() >= 215 and 295 >= click.getY() >= 275:  # if user wants to endless
            endless = True
            click = Point(385, 240)

        if 385 >= click.getX() >= 215 and 240 >= click.getY() >= 220:  # if user clicks on classic
            titleScreen.close()
            if endless:
                gameScreen = GraphWin("Stacker", 1200, 900, autoflush=False)
            else:
                gameScreen = GraphWin("Stacker", 900, 900, autoflush=False)

            # winsound.PlaySound("sounds/gameMusic", winsound.SND_ASYNC | winsound.SND_LOOP)

            if not endless:
                modeText = Text(Point(800, 850), "Mode: Classic")
                classicSpeed = 5
            else:
                modeText = Text(Point(800, 850), "Mode: Endless")
                for x in range(3):
                    bruh = Image(Point(950, 200 + x * 200), blackbuttons[x])
                    bruh.draw(gameScreen)
                    temp.append(bruh)

                # visuals
                addText = Text(Point(950, 260), "Press 1: Add One Block\n* Only for 1 and 2 blocks *")
                addText.draw(gameScreen)
                slowText = Text(Point(950, 450), "Press 2: Slow Down For One Level")
                slowText.draw(gameScreen)
                multiplierText = Text(Point(950, 650), "Press 3: Multiply Score for 3 Levels")
                multiplierText.draw(gameScreen)

                square = Rectangle(Point(800, 150), Point(1100, 670))
                square.draw(gameScreen)
                george = Text(Point(950, 130), "Powerups")
                george.setSize(15)
                george.draw(gameScreen)
                bailey = Text(Point(950, 700), "*** Power ups only work when lit up ***")
                bailey.setSize(15)
                bailey.draw(gameScreen)
                classicSpeed = 1

            modeText.setSize(15)
            modeText.draw(gameScreen)

            scoreText = Text(Point(800, 50), "Score: " + str(score))

            base = Line(Point(184, 830), Point(716, 830))
            border2 = Line(Point(184, 70), Point(184, 830))
            border3 = Line(Point(716, 70), Point(716, 830))
            base.draw(gameScreen)
            border2.draw(gameScreen)
            border3.draw(gameScreen)

            verticals = []
            for i in range(6):
                s = Line(Point(260 + 76 * i, 70), Point(260 + 76 * i, 830))
                verticals.append(s)
                s.draw(gameScreen)

            horizontals = []
            for i in range(9):
                s = Line(Point(184, 146 + 76 * i), Point(716, 146 + 76 * i))
                horizontals.append(s)
                s.draw(gameScreen)

            update()

            drawnblocks = []

            while stacking:
                if bop == 5:
                    powerupping = True
                    bop = 0

                if not endless:
                    if level == 4 and n == 0:
                        n = 1
                        force = "force2"
                        block = blocks[n]
                        size = sizes[n]
                    elif level == 8 and n == 1:
                        n = 2
                        force = "force1"
                        block = blocks[n]
                        size = sizes[n]

                if starter == "left":
                    position = 184 + size
                    direction = 1
                elif starter == "right":
                    position = 184 + 532 - size
                    direction = -1

                if endless:
                    if powerupping:
                        for x in temp:
                            x.undraw()

                        temp = []
                        for x in range(3):
                            bruh = Image(Point(950, 200 + x * 200), buttons[x])
                            bruh.draw(gameScreen)
                            temp.append(bruh)

                drawnblock = Image(Point(position, 792 - height * 76), block)
                drawnblock.draw(gameScreen)
                placing = True

                scoreText.undraw()
                scoreText = Text(Point(800, 50), "Score: " + str(score))
                if endless:
                    scoreText = Text(Point(850, 50), "Score: " + str(score))

                scoreText.setSize(20)
                scoreText.draw(gameScreen)
                update()

                if slowed == 2:
                    slowed = 1

                while placing:
                    draw = True
                    classicEnd = time.time() + (0.75 - 0.05 * level)
                    endlessEnd = time.time() + ((0.75 - 0.01 * level) * slowed)
                    timeEnd = 0
                    if endless:
                        timeEnd = endlessEnd
                    else:
                        timeEnd = classicEnd
                    while time.time() < timeEnd:  # time for input

                        key = gameScreen.checkKey()
                        if key == hotkey:

                            placing = False
                            draw = False

                            # - - - Hit Reg - - - -

                            if level == 0:
                                prevPosition = position
                            elif not endless:
                                if level == 9 and prevPosition == position and n == 2:
                                    print("WINNER WINNER CHICKEN DINNER")
                                    end = True
                                    ending = "win"

                            if force == "force2":
                                if prevPosition + 38 == position:
                                    prevPosition = position
                                elif prevPosition - 38 == position:
                                    prevPosition = position
                                else:
                                    if prevPosition + 114 == position:
                                        prevPosition = position - 38
                                    elif prevPosition - 114 == position:
                                        prevPosition = position + 38
                                    n = 2
                                    block = blocks[2]
                                    size = sizes[n]
                                    drawnblock.undraw()
                                    drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                    drawnblock.draw(gameScreen)
                                force = "none"

                            elif force == "force1":
                                if prevPosition + 38 == position:
                                    prevPosition = position
                                elif prevPosition - 38 == position:
                                    prevPosition = position
                                else:
                                    end = True
                                    print("GAME OVER, You lose")
                                    ending = "lose"
                                force = "none"

                            if prevPosition - position >= size * 2 or position - prevPosition >= size * 2:
                                end = True
                                print("GAME OVER, You lose")
                                ending = "lose"
                                if endless:
                                    ending = "finalscore"

                            elif (position != prevPosition) and (force == "none"):
                                if (n == 0 or n == 1) and (position + 76 == prevPosition or position - 76 == prevPosition):
                                    n = n + 1
                                    block = blocks[n]
                                    size = sizes[n]
                                    drawnblock.undraw()
                                    if prevPosition > position:
                                        prevPosition = position + 38
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)

                                    elif prevPosition < position:
                                        prevPosition = position - 38
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)

                                elif n == 0 and position + 152 == prevPosition or position - 152 == prevPosition:
                                    print("yep")
                                    n = 2
                                    block = blocks[n]
                                    size = sizes[n]
                                    drawnblock.undraw()

                                    if prevPosition > position:
                                        prevPosition = position + 76
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)

                                    elif prevPosition < position:
                                        prevPosition = position - 76
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)
                            # - - - - - - - - - - -

                            if end:
                                winsound.PlaySound(None, winsound.SND_PURGE)
                                stacking = False
                                placing = False
                                draw = False
                                # Trying to make the failed/winning block flicker

                                if ending == "lose" or ending == "finalscore":
                                    winsound.PlaySound("sounds/losingSoundEffect", winsound.SND_ASYNC)
                                elif ending == "win":
                                    winsound.PlaySound("sounds/winningSoundEffect", winsound.SND_ASYNC)

                                if not endless:
                                    scoreText.undraw()
                                    scoreText = Text(Point(800, 50), "Score: " + str(score + 1))
                                    scoreText.draw(gameScreen)
                                    update()

                                for z in range(3):
                                    drawnblock.undraw()
                                    update()
                                    time.sleep(0.5)
                                    drawnblock = Image(Point(position, 792 - (height * 76)), block)
                                    drawnblock.draw(gameScreen)
                                    update()
                                    time.sleep(0.5)
                                screen = "newGame"

                                if endless:
                                    with open("highscore.txt", "w") as highscorefile:
                                        if score > localhighscore:
                                            highscorefile.write(str(score))
                                        else:
                                            highscorefile.write(str(localhighscore))

                                gameScreen.close()
                                tempScore = score
                                break



                            drawnblocks.append(drawnblock)
                            print(drawnblocks)
                            print("Previous Position:", prevPosition, "New Position:", position)

                            if starter == "left":
                                starter = "right"
                            else:
                                starter = "left"

                            score += 1
                            level += 1
                            height += 1
                            if not powerupping:
                                bop += 1

                            if multiplier:
                                if not count == 5:
                                    score += 1  # adds more 1 more score, 1 + 1 = 2 for next 5 blocks
                                    count += 1
                                else:
                                    count = 0
                                    multiplier = False

                            print("level = " + str(level))  # test code

                            if (level == 10 or (level - 10) % 9 == 0 and not level == 1) and endless:  # if it hits the top block
                                for i in drawnblocks:
                                    i.undraw()
                                height = 1
                                prevBlock = Image(Point(prevPosition, 792), block)
                                prevBlock.draw(gameScreen)
                                drawnblocks = [prevBlock]
                                print("went thru")

                        elif endless:
                            if powerupping:
                                if key == "":
                                    continue
                                elif key == "1":  # adds 1 block
                                    if n == 0:
                                        continue
                                    else:
                                        n -= 1

                                elif key == "2":  # slow the speed down
                                    slowed = 2

                                elif key == "3":  # score multiplier
                                    multiplier = True

                                powerupping = False
                                draw = False
                                for x in temp:
                                    x.undraw()

                                temp = []
                                for x in range(3):
                                    bruh = Image(Point(950, 200 + x * 200), blackbuttons[x])
                                    bruh.draw(gameScreen)
                                    temp.append(bruh)

                    if draw:  # the physical moving of the block
                        drawnblock.move(76 * direction, 0)
                        update()
                        position += 76 * direction
                        if position - size <= 184 or position + size >= 716:
                            direction *= -1

        elif 360 <= click.getX() <= 460 and 540 <= click.getY() <= 560:
            with open("highscore.txt", "w") as highscorefile:
                highscorefile.write("0")

        elif 385 >= click.getX() >= 215 and 410 >= click.getY() >= 390:  # if user clicks on hotkey
            titleScreen.close()
            hotkeyScreen = GraphWin("Hot Key Edit", 500, 500, autoflush=False)
            screen = "hotkey fix"

            currentHotkey = Text(Point(175, 150), "Current Hotkey: " + hotkey)
            currentHotkey.draw(hotkeyScreen)
            currentHotkey.setSize(17)

            changeKeyRect = Rectangle(Point(50, 250), Point(350, 300))
            changeKeyRect.draw(hotkeyScreen)
            changeKey = Text(Point(200, 275), "Click Here to Change Key")
            changeKey.draw(hotkeyScreen)

            confirmChangeRect = Rectangle(Point(50, 300), Point(350, 350))
            confirmChangeRect.draw(hotkeyScreen)
            confirmChange = Text(Point(200, 325), "Confirm Change and/or Exit")
            confirmChange.draw(hotkeyScreen)

            while screen == "hotkey fix":
                click = hotkeyScreen.getMouse()
                if 350 >= click.getX() >= 50 and 300 >= click.getY() >= 250:
                    changeKey.undraw()
                    selectKey = Text(Point(200, 275), "Select New Key")
                    selectKey.draw(hotkeyScreen)

                    confirmChangeRect.undraw()
                    confirmChange.undraw()

                    hotkey = hotkeyScreen.getKey()
                    currentHotkey.undraw()
                    currentHotkey = Text(Point(175, 150), "Current Hotkey: " + hotkey)
                    currentHotkey.draw(hotkeyScreen)
                    currentHotkey.setSize(17)

                    selectKey.undraw()
                    changeKey = Text(Point(200, 275), "Click Here to Change Key")
                    changeKey.draw(hotkeyScreen)
                    confirmChangeRect = Rectangle(Point(50, 300), Point(350, 350))
                    confirmChangeRect.draw(hotkeyScreen)
                    confirmChange = Text(Point(200, 325), "Confirm Change and/or Exit")
                    confirmChange.draw(hotkeyScreen)

                elif 350 >= click.getX() >= 50 and 350 >= click.getY() >= 300:
                    hotkeyScreen.close()
                    screen = "newGame"
                    ending = "none"
                    continue

        elif 335 >= click.getX() >= 265 and 460 >= click.getY() >= 435:  # if user clicks on rules
            rulesScreen = GraphWin("Rules", 500, 500, autoflush=False)
            skip = False
            while True:
                page1 = True
                page2 = False
                pg1 = []
                pg2 = []
                if skip:
                    cont = True
                    break
                if page1:
                    text1 = Text(Point(250, 50), "Classic Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg1.append(text1)

                    rule1 = Text(Point(250, 100),
                                 "1. You will be given a starter 3x1 block to stack that is constantly moving")
                    rule1.setSize(10)
                    rule1.draw(rulesScreen)
                    pg1.append(rule1)
                    rule2 = Text(Point(250, 150), "2. The default hot key to stack is space, try to stack all "
                                                  "blocks on your previous one")
                    pg1.append(rule2)
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    pg1.append(rule2)
                    rule3 = Text(Point(250, 200),
                                 "3. Everytime you misalign your new block with the previous block under it, \n"
                                 "you will lose the misaligned blocks, making a smaller base for you to stack on")
                    rule3.setSize(10)
                    rule3.draw(rulesScreen)
                    pg1.append(rule3)
                    rule4 = Text(Point(250, 250),
                                 "4. Speeds of the block constantly moving will increase after each level")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)
                    pg1.append(rule4)
                    rule5 = Text(Point(250, 300), "5. If you make it to level 4 with more than two blocks \n"
                                                  " remaining, you will be forced to lose one block")
                    rule5.setSize(10)
                    rule5.draw(rulesScreen)
                    pg1.append(rule5)
                    rule6 = Text(Point(250, 350), "6. If you make it to level 7 with more than one block remaining, \n "
                                                  "you will also be forced to lose one block")
                    rule6.setSize(10)
                    rule6.draw(rulesScreen)
                    pg1.append(rule6)
                    rule7 = Text(Point(250, 400), "7. Once you stack to the top, you win!")
                    rule7.setSize(10)
                    rule7.draw(rulesScreen)
                    pg1.append(rule7)

                    rule8 = Text(Point(250, 450), "TL;DR \n Time each placement of blocks on top of the \n"
                                                  "previous one, when you hit the top you win!")
                    rule8.setSize(13)
                    rule8.setFill("green")
                    rule8.draw(rulesScreen)
                    pg1.append(rule8)

                    exittext = Text(Point(475, 485), "Next")
                    exittext.setFill("red")
                    exittext.draw(rulesScreen)
                    pg1.append(exittext)

                    click = rulesScreen.getMouse()
                    while True:
                        if 460 <= click.getX() <= 490 and 480 <= click.getY() <= 490:
                            page2 = True
                            page1 = False
                            for i in pg1:
                                i.undraw()
                            break
                        click = rulesScreen.getMouse()

                if page2:

                    text1 = Text(Point(250, 50), "Endless Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg2.append(text1)

                    rule1 = Text(Point(250, 100), "1. Same as classic mode but..")
                    rule1.setSize(10)
                    rule1.draw(rulesScreen)
                    pg2.append(rule1)

                    rule123 = Text(Point(250, 150), "2. Speed will increase slower than classic mode")
                    rule123.setSize(10)
                    rule123.draw(rulesScreen)
                    pg2.append(rule123)

                    rule2 = Text(Point(250, 200),
                                 "3. You will be given power ups every 3 blocks you stack (these can be saved)")
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    pg2.append(rule2)

                    rule3 = Text(Point(175, 225), "* Slow-mo: Slow down the speed for your")
                    rule3.setSize(10)
                    rule3.draw(rulesScreen)
                    pg2.append(rule3)

                    rule6 = Text(Point(185, 240), "your next block by 2x")
                    rule6.setSize(10)
                    rule6.draw(rulesScreen)
                    pg2.append(rule6)

                    rule4 = Text(Point(225, 275), "* Extended block: Extends your current block by 1 to get a")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)
                    pg2.append(rule4)

                    rule5 = Text(Point(268, 290), "higher chance of stacking it correctly")
                    rule5.setSize(10)
                    rule5.draw(rulesScreen)
                    pg2.append(rule5)

                    rule7 = Text(Point(200, 325), "* Score multiplier: Your next 3 blocks have a score")
                    rule7.setSize(10)
                    rule7.draw(rulesScreen)
                    pg2.append(rule7)

                    rule8 = Text(Point(225, 340), "of 3 if stacked properly")
                    rule8.draw(rulesScreen)
                    rule8.setSize(10)
                    pg2.append(rule8)

                    rule5 = Text(Point(250, 400), "ALSO, ENDLESS STACKING >:)")
                    rule5.setOutline("black")
                    rule5.setFill("PURPLE")
                    rule5.setSize(25)
                    pg2.append(rule5)
                    rule5.draw(rulesScreen)

                    exittext = Text(Point(475, 485), "Exit")
                    exittext.setFill("red")
                    exittext.draw(rulesScreen)
                    pg2.append(exittext)

                    backtext = Text(Point(25, 485), "Back")
                    backtext.setFill("red")
                    backtext.draw(rulesScreen)
                    pg2.append(backtext)

                    click = rulesScreen.getMouse()
                    while True:
                        if 460 <= click.getX() <= 490 and 480 <= click.getY() <= 490:  # quit
                            page2 = False
                            page1 = False
                            skip = True
                            rulesScreen.close()
                            break
                        elif 10 <= click.getX() <= 40 and 480 <= click.getY() <= 490:  # back
                            for i in pg2:
                                i.undraw()
                            page1 = True
                            page2 = False
                            break
                        click = rulesScreen.getMouse()

        elif 520 <= click.getX() <= 580 and 535 <= click.getY() <= 565:  # if user wants to quit
            quit()

        elif 10 <= click.getX() <= 90 and 535 <= click.getY() <= 565:
            aboutScreen = GraphWin("About", 500, 500)

            exitAbout = Text(Point(450, 450), "Exit")
            exitAbout.setSize(20)
            exitRect = Rectangle(Point(425, 435), Point(475, 465))
            exitRect.draw(aboutScreen)
            exitAbout.draw(aboutScreen)

            contrib = Text(Point(250, 70), "Contributors: Jacky and Orion")
            contrib.draw(aboutScreen)

            aboutGame = Text(Point(250, 125), "About the Game:")
            aboutGame.draw(aboutScreen)
            aboutGame.setSize(20)

            aboutGameText = Text(Point(250, 225), "Stacker is a game where the user tries to align (aka stack) blocks\n"
                                                  "vertically. The blocks will be moving left and right while the user\n"
                                                  "is stacking. When the user inputs the specified key, the moving block\n"
                                                  " will stop and hopefully be aligned with previous stacked blocks.\n"
                                                  "After every level, the speed of the moving blocks will increase."
                                                  "If the stacked newly block is only partially aligned with previous blocks,\n"
                                                  "the misaligned portion of blocks blocks will disappear and the user\n"
                                                  "will be stacking with a smaller block than before; increases the\n"
                                                  "difficulty for future stacking.")
            aboutGameText.draw(aboutScreen)
            version = Text(Point(250, 25), "Version 1.0.0")
            version.draw(aboutScreen)

            features = Text(Point(250, 325), "Our Additional Features:")
            features.draw(aboutScreen)
            features.setSize(15)
            featuresText = Text(Point(250, 360), "Endless mode, power ups (slow speed, add block, score multiplier),\n"
                                                 "achievements, hot key switch")
            featuresText.draw(aboutScreen)

            click = aboutScreen.getMouse()

            # insert about info

            while True:
                if 425 <= click.getX() <= 475 and 435 <= click.getY() <= 465:
                    aboutScreen.close()
                    break
                click = aboutScreen.getMouse()
