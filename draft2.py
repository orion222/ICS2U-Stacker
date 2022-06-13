from graphics import *
import threading
import winsound
import threading
import time

screen = "newGame"
hotkey = "space"
ending = "none"

while screen == "newGame":
    print("made it")
    if ending == "win":
        winScreen = GraphWin("WINNER WINNER CHICKEN DINNER", 500, 500)
        winText = Text(Point(250, 200), "YOU WIN")
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
    titleScreen = GraphWin("Stacker", 600, 600, autoflush=False)
    title = Text(Point(300, 75), "S T A C K E R")
    title.draw(titleScreen)
    title.setSize(30)
    classic = Text(Point(300, 230), "Classic Mode")
    classic.draw(titleScreen)
    classic.setSize(20)
    classRect = Rectangle(Point(215, 220), Point(385, 240))
    classRect.draw(titleScreen)
    endless = Text(Point(300, 285), "Endless Mode")
    endless.draw(titleScreen)
    endless.setSize(20)
    endRect = Rectangle(Point(215, 275), Point(385, 295))
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
    screen = "title"
    while screen == "title":
        print("title")
        click = titleScreen.getMouse()

        sizes = [114, 76, 38]
        blocks = [
            "3block.gif",
            "2block.gif",
            "1block.gif"
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

        if 385 >= click.getX() >= 215 and 295 >= click.getY() >= 275:  # if user wants to endless
            endless = True
            click = Point(385, 240)

        if 385 >= click.getX() >= 215 and 240 >= click.getY() >= 220:  # if user clicks on classic
            titleScreen.close()
            gameScreen = GraphWin("Stacker", 1200, 900, autoflush=False)
            winsound.PlaySound("gameMusic", winsound.SND_ASYNC | winsound.SND_LOOP)

            if not endless:
                modeText = Text(Point(800, 850), "Mode: Classic")
            else:
                modeText = Text(Point(800, 850), "Mode: Endless")

            modeText.setSize(15)
            modeText.draw(gameScreen)

            scoreText = Text(Point(800, 50), "Score: " + str(level))

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
                print("while stacking")

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

                drawnblock = Image(Point(position, 792 - height * 76), block)
                drawnblock.draw(gameScreen)
                draw = True
                placing = True

                if endless:
                    scoreText.undraw()
                    scoreText = Text(Point(800, 50), "Score: " + str(level))
                    scoreText.draw(gameScreen)
                    update()

                while placing:
                    timeEnd = time.time() + 0.5  # 0.75 - 0.05 * level
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

                            if prevPosition - position >= size * 2 or position - prevPosition >= size * 2:
                                end = True
                                print("GAME OVER, You lose")
                                ending = "lose"

                            elif force == "force1":
                                if prevPosition - 38 == position:
                                    prevPosition = position
                                elif prevPosition + 38 == position:
                                    prevPosition = position
                                else:
                                    end = True
                                    print("GAME OVER, You lose")
                                    ending = "lose"
                                force = "none"

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

                            drawnblocks.append(drawnblock)
                            print(drawnblocks)
                            print("Previous Position:", prevPosition, "New Position:", position)

                            if starter == "left":
                                starter = "right"
                            else:
                                starter = "left"

                            level += 1
                            height += 1
                            print(level)  # test code

                            if end:
                                stacking = False
                                placing = False
                                draw = False
                                # Trying to make the failed/winning block flicker
                                winsound.PlaySound(None, winsound.SND_PURGE)
                                if ending == "lose":
                                    winsound.PlaySound("losingSoundEffect", winsound.SND_ASYNC)
                                elif ending == "win":
                                    winsound.PlaySound("winningSoundEffect", winsound.SND_ASYNC)

                                for z in range(3):
                                    drawnblock.undraw()
                                    update()
                                    time.sleep(0.5)
                                    drawnblock = Image(Point(position, 792 - (height - 1) * 76), block)
                                    drawnblock.draw(gameScreen)
                                    update()
                                    time.sleep(0.5)
                                screen = "newGame"
                                gameScreen.close()

                            elif (level == 10 or (level - 10) % 9 == 0 and not level == 1) and endless is True:  # if it hits the top block
                                for i in drawnblocks:
                                    i.undraw()
                                height = 1
                                prevBlock = Image(Point(prevPosition, 792), block)
                                prevBlock.draw(gameScreen)
                                drawnblocks = [prevBlock]
                                print("went thru")

                    if draw:  # the physical moving of the block
                        drawnblock.move(76 * direction, 0)
                        position += 76 * direction
                        if position - size <= 184 or position + size >= 716:
                            direction *= -1

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
                    rule2 = Text(Point(250, 150),
                                 "2. You will be given power ups randomly to help you on your endless journey")
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    pg2.append(rule2)

                    rule3 = Text(Point(175, 175), "* Slow-mo: Slow down the speed for your")
                    rule3.setSize(10)
                    rule3.draw(rulesScreen)

                    rule6 = Text(Point(225, 190), "your next block at a random speed")
                    rule6.setSize(10)
                    rule6.draw(rulesScreen)

                    rule4 = Text(Point(225, 225), "* Extended block: Extends your current block by 1 to get a")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)

                    rule5 = Text(Point(268, 240), "higher chance of stacking it correctly")
                    rule5.setSize(10)
                    rule5.draw(rulesScreen)

                    rule5 = Text(Point(250, 350), "ALSO, ENDLESS STACKING >:)")
                    rule5.setOutline("black")
                    rule5.setFill("PURPLE")
                    rule5.setSize(25)
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

            # insert about info

            click = aboutScreen.getMouse()
            while True:
                if 425 <= click.getX() <= 475 and 435 <= click.getY() <= 465:
                    aboutScreen.close()
                    break
                click = aboutScreen.getMouse()
