# Names: Jacky and Orion
# Project Choice: Stacker
# Stacker is a game where the user tries to align (aka stack) blocks vertically. The blocks will be moving left and
# right while the user is stacking. When the user inputs the specified key, the moving block will stop and hopefully be
# aligned with previous stacked blocks. If the stacked newly stacked block is only partially aligned with previous blocks, the
# misaligned portion of blocks will disappear and the user will be stacking with a smaller block than before;
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
    # print("made it")
    if ending == "win":  # screen if you win (only for classic mode)
        winScreen = GraphWin("WINNER WINNER CHICKEN DINNER", 500, 500)
        youWin = Image(Point(250, 250), "culmimages/youWin.gif")
        youWin.draw(winScreen)
        time.sleep(3)
        winScreen.close()
        screen = "title"
        # Old graphics:
        # winText = Text(Point(250, 200), "YOU WIN")
        # winText.setFill("lightgreen")
        # winText.draw(winScreen)
        # winText.setSize(35)
        # newGame = Text(Point(250, 300), "New Game")
        # newGame.draw(winScreen)
        # newGame.setSize(15)
        # rect1 = Rectangle(Point(200, 290), Point(300, 310))
        # rect1.draw(winScreen)
        # exitGame = Text(Point(250, 340), "Exit Game")
        # exitGame.draw(winScreen)
        # exitGame.setSize(15)
        # rect2 = Rectangle(Point(200, 330), Point(300, 350))
        # rect2.draw(winScreen)
        # while screen == "newGame":
        #     click = winScreen.getMouse()
        #     if 300 >= click.getX() >= 200 and 310 >= click.getY() >= 290:
        #         winScreen.close()
        #         screen = "title"
        #     elif 300 >= click.getX() >= 200 and 350 >= click.getY() >= 330:
        #         quit()

    elif ending == "lose":  # screen if you lose (only for classic mode)
        loseScreen = GraphWin("Wow so sad you lost", 500, 500)
        gameOver = Image(Point(250, 250), "culmimages/gameOver.gif")
        gameOver.draw(loseScreen)

        coverWatermark = Rectangle(Point(175, 455), Point(355, 480))
        coverWatermark.setFill("black")
        coverWatermark.draw(loseScreen)

        while screen == "newGame":  # if statements to see if user wants to quit or new game
            click = loseScreen.getMouse()
            if 217 >= click.getX() >= 154 and 410 >= click.getY() >= 380:
                loseScreen.close()
                screen = "title"
            elif 346 >= click.getX() >= 296 and 410 >= click.getY() >= 380:
                quit()

    elif ending == "finalscore":  # screen when user loses in endless
        winScreen = GraphWin("im dying from writing code", 500, 500)
        highscoreBackground = Image(Point(250, 250), "culmimages/highscoreBackground.gif")
        highscoreBackground.draw(winScreen)
        finalText = Image(Point(250, 50), "culmimages/finalText.gif")
        finalText.draw(winScreen)

        nobodywillcheckthisvariablename = Text(Point(250, 130), str(tempScore))
        nobodywillcheckthisvariablename.setSize(35)
        nobodywillcheckthisvariablename.setFill("Green")
        nobodywillcheckthisvariablename.draw(winScreen)

        newGameText = Image(Point(250, 220), "culmimages/newGameText.gif")
        newGameText.draw(winScreen)

        exitGameText = Image(Point(250, 270), "culmimages/exitGameText.gif")
        exitGameText.draw(winScreen)

        while screen == "newGame":  # if statements to check if user wants to quit or new game
            click = winScreen.getMouse()
            if 338 >= click.getX() >= 163 and 241 >= click.getY() >= 200:
                winScreen.close()
                screen = "title"
            elif 345 >= click.getX() >= 155 and 291 >= click.getY() >= 250:
                quit()

    titleScreen = GraphWin("Stacker", 600, 600, autoflush=False)
    titleBackground = Image(Point(300, 300), "culmimages/titleBackground.gif")
    titleBackground.draw(titleScreen)
    stackerTitle = Image(Point(300, 75), "culmimages/stackerTitle.gif")
    stackerTitle.draw(titleScreen)

    classic = Image(Point(300, 230), "culmimages/classic.gif")
    classic.draw(titleScreen)
    # dimension of image: 300 x 30

    endless = Image(Point(300, 285), "culmimages/endless.gif")
    endless.draw(titleScreen)

    hotkeyTitle = Image(Point(300, 400), "culmimages/hotkeyTitle.gif")
    hotkeyTitle.draw(titleScreen)

    rules = Image(Point(300, 447), "culmimages/rules.gif")
    rules.draw(titleScreen)
    # rules = Text(Point(300, 447), "Rules")
    # rules.draw(titleScreen)

    leaveText = Text(Point(550, 550), "Quit")
    leaveText.setSize(20)
    leaveText.setTextColor("light grey")
    leaveText.draw(titleScreen)
    # leaveRect = Rectangle(Point(520, 535), Point(580, 565))
    # leaveRect.draw(titleScreen)

    aboutText = Text(Point(50, 550), "About")
    aboutText.setSize(20)
    aboutText.setTextColor("light grey")
    aboutText.draw(titleScreen)
    # aboutRect = Rectangle(Point(10, 535), Point(90, 565))
    # aboutRect.draw(titleScreen)

    resetScore = Text(Point(410, 550), "Reset score")
    resetScore.setSize(13)
    resetScore.setTextColor("light grey")
    resetScore.draw(titleScreen)
    # resetRect = Rectangle(Point(360, 540), Point(460, 560))
    # resetRect.draw(titleScreen)

    screen = "title"

    highscoreimg = Image(Point(300, 525), "culmimages/highscore.gif")
    highscoreimg.draw(titleScreen)

    #  ^^^^ all visuals for the menu
    while screen == "title":

        undrawScore.undraw()

        with open("highscore.txt",
                  "r") as highscorefile:  # context manager "highscorefile" is the var that stores the .txt
            contents = highscorefile.readline()
            # looks at local highscore and saves it in a variable

        highscoreText = Text(Point(300, 561), contents)
        undrawScore = highscoreText
        highscoreText.setSize(20)
        highscoreText.setFill("red")
        highscoreText.draw(titleScreen)
        localhighscore = int(contents)

        update()

        # print("title")
        click = titleScreen.getMouse()

        # images used consistently
        sizes = [114, 76, 38]
        blocks = [
            "culmimages/3block.gif",
            "culmimages/2block.gif",
            "culmimages/1block.gif",
        ]

        buttons = [
            "culmimages/add1.gif",
            "culmimages/slowspeed.gif",
            "culmimages/scoremultiply.gif"
        ]

        blackbuttons = [
            "culmimages/add1black.gif",
            "culmimages/slowspeedblack.gif",
            "culmimages/scoremultiplyblack.gif"
        ]
        # hotkey = "space"  -  defined this at the top now
        # all algorithm variables
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
        addBlock = False

        if 450 >= click.getX() >= 150 and 300 >= click.getY() >= 270:  # if user wants to endless
            endless = True
            click = Point(385, 240)

        if 450 >= click.getX() >= 150 and 245 >= click.getY() >= 215:  # if user clicks on classic
            titleScreen.close()
            if endless:  # gamescreen will be bigger if endless mode is chosen
                gameScreen = GraphWin("Stacker", 1200, 900, autoflush=False)
                endlessBackground = Image(Point(600, 450), "culmimages/endlessBackground.gif")
                endlessBackground.draw(gameScreen)
            else:  # gamescreen will be smaller if classic mode is chosen
                gameScreen = GraphWin("Stacker", 900, 900, autoflush=False)
                classicBackground = Image(Point(450, 450), "culmimages/classicBackground.gif")
                classicBackground.draw(gameScreen)

            # winsound.PlaySound("culmsounds/gameMusic", winsound.SND_ASYNC | winsound.SND_LOOP)

            if not endless:  # visuals to tell you what mode you chose
                modeText = Text(Point(450, 40), "Classic Mode")
                modeText.setSize(35)
            else:
                modeText = Text(Point(950, 50), "ENDLESS MODE")
                modeText.setSize(30)
                square = Rectangle(Point(800, 150), Point(1100, 670))
                square.draw(gameScreen)
                square.setFill("white")

                for x in range(3):
                    bruh = Image(Point(950, 200 + x * 200), blackbuttons[x])
                    bruh.draw(gameScreen)
                    temp.append(bruh)

                # more visuals
                addText = Text(Point(950, 260), "Press 1: Add One Block")
                addText.draw(gameScreen)
                addTextBottom = Text(Point(950, 275), "* Only for 1 and 2 blocks to increase chance of stacking *")
                addTextBottom.draw(gameScreen)
                addTextBottom.setSize(8)

                slowText = Text(Point(950, 450), "Press 2: Slow Down For One Level")
                slowText.draw(gameScreen)
                multiplierText = Text(Point(950, 650), "Press 3: Double Score for 3 Levels")
                multiplierText.draw(gameScreen)

                george = Text(Point(950, 130), "*** Power ups only work when lit up ***")
                george.setSize(15)
                george.draw(gameScreen)

            modeText.draw(gameScreen)

            scoreText = Text(Point(450, 50), "Score: " + str(score))

            base = Line(Point(184, 832), Point(716, 832))
            base.setWidth(5)
            # added 2 to the heights to account for the width
            border2 = Line(Point(181, 70), Point(181, 835))
            # subtracted 3 to the x values to account for width
            border3 = Line(Point(718, 70), Point(718, 835))
            # added 2 to the x values to account for width

            # added 5 to border y values for second points to account for the base's width

            base.draw(gameScreen)
            border2.draw(gameScreen)
            border2.setWidth(5)
            border3.draw(gameScreen)
            border3.setWidth(5)

            # This was the grid that we used to help visualize where the blocks were.
            # verticals = []
            # for i in range(6):
            #     s = Line(Point(260 + 76 * i, 70), Point(260 + 76 * i, 830))
            #     verticals.append(s)
            #     s.draw(gameScreen)
            #
            # horizontals = []
            # for i in range(9):
            #     s = Line(Point(184, 146 + 76 * i), Point(716, 146 + 76 * i))
            #     horizontals.append(s)
            #     s.draw(gameScreen)

            update()

            drawnblocks = []

            while stacking:
                if bop == 5:
                    # bop is the counter to see if you've placed 5 blocks-
                    # without a power up, this will set powerups to true when it is 5
                    # this counter will only start when you use a powerup, so you
                    # can save powerups for future levels
                    powerupping = True
                    bop = 0

                if not endless:
                    if level == 4 and n == 0:
                        n = 1
                        force = "force2"
                        block = blocks[n]
                        size = sizes[n]
                    elif level == 7 and n == 1:
                        n = 2
                        force = "force1"
                        block = blocks[n]
                        size = sizes[n]

                # these if statements lets the computer know on which side to place
                # the next block, so that the user cannot spam place on one side
                # and go up many levels in a short period of time
                if starter == "left":
                    position = 184 + size
                    direction = 1
                elif starter == "right":
                    position = 184 + 532 - size
                    direction = -1

                # this condition here "lights up" the buttons
                # when appropriate (when you stack 5 blocks after using the powerups)
                if endless:
                    if powerupping:
                        for x in range(len(temp)):
                            if x == 0:
                                if n == 0:
                                    continue
                            temp[x].undraw()

                        for x in range(3):
                            if x == 0:
                                if n == 0:
                                    temp = temp[:1]
                                    continue
                                else:
                                    temp = []
                            bruh = Image(Point(950, 200 + x * 200), buttons[x])
                            bruh.draw(gameScreen)
                            temp.append(bruh)

                # this block right here is the block that is first drawn either
                # in the right side or the left side
                drawnblock = Image(Point(position, 792 - height * 76), block)
                drawnblock.draw(gameScreen)
                placing = True

                # this updates the score
                if endless:
                    scoreText.undraw()
                    scoreText = Text(Point(450, 50), "Score: " + str(score))
                    scoreText.draw(gameScreen)
                    scoreText.setSize(25)
                    update()

                # this changes the speed back to normal, as the powerup only slows down for 1 level
                if slowed == 2:
                    slowed = 1

                while placing:
                    draw = True
                    classicEnd = time.time() + (0.75 - 0.075 * level)
                    endlessEnd = time.time() + ((0.75 - 0.01 * level) * slowed)
                    timeEnd = 0

                    # these 2 if and else statements differentiates the time restraints to place
                    # a block depending if you are doing classic mode or endless mode
                    # classic mode is faster, endless mode is slower
                    if endless:
                        timeEnd = endlessEnd
                    else:
                        timeEnd = classicEnd

                    # while the current time is equal to the current time + whatever the speed is set to
                    while time.time() < timeEnd:  # time for input

                        # algorithm to check keys you pressed
                        key = gameScreen.checkKey()
                        if key == hotkey:

                            # if you placed a block, all the code under this will run
                            # set placing to false and drawing to false because we don't
                            # want it to move when it is already placed
                            placing = False
                            draw = False

                            # - - - Hit Reg - - - -

                            if level == 0:
                                prevPosition = position
                            elif not endless:
                                if level == 9 and prevPosition == position and n == 2:
                                    # print("WINNER WINNER CHICKEN DINNER")
                                    end = True
                                    ending = "win"

                            # - - - - - - - - - - - - - - - Hit Reg Added Block - - - - - - - - - - - - - - - - - - -

                            if endless and addBlock is True:
                                if n == 0:
                                    # if the block is a three block
                                    if (position + 38 == prevPosition) or (position - 38 == prevPosition):
                                        n = 1
                                        block = blocks[n]
                                        size = sizes[n]
                                        drawnblock.undraw()
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)
                                    elif (position + 114 == prevPosition) or (position - 114 == prevPosition):
                                        n = 2
                                        block = blocks[n]
                                        size = sizes[n]
                                        if position < prevPosition:
                                            prevPosition = prevPosition - 38
                                        else:
                                            prevPosition = prevPosition + 38
                                        drawnblock.undraw()
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)
                                    else:
                                        end = True
                                        ending = "lose"
                                else:
                                    # if the block is a two block
                                    if (position + 38 == prevPosition) or (position - 38 == prevPosition):
                                        n = 2
                                        block = blocks[n]
                                        size = sizes[n]
                                        drawnblock.undraw()
                                        drawnblock = Image(Point(prevPosition, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)
                                    else:
                                        end = True
                                        ending = "lose"

                            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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
                                    # print("GAME OVER, You lose")
                                    ending = "lose"
                                force = "none"

                            if (prevPosition - position >= size * 2 or position - prevPosition >= size * 2) \
                                    and not addBlock:
                                # when the stocked block is completely misaligned
                                end = True
                                # print("GAME OVER, You lose")
                                ending = "lose"
                                if endless:
                                    ending = "finalscore"

                            elif (position != prevPosition) and (force == "none") and (addBlock is False):
                                if (n == 0 or n == 1) and (position + 76 == prevPosition
                                                           or position - 76 == prevPosition):
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
                                    # print("yep")
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

                            addBlock = False
                            if end:
                                winsound.PlaySound(None, winsound.SND_PURGE)
                                stacking = False
                                placing = False
                                draw = False

                                # plays either winning or losing sound depending on outcome
                                if ending == "lose" or ending == "finalscore":
                                    winsound.PlaySound("culmsounds/losingSoundEffect", winsound.SND_ASYNC)
                                elif ending == "win":
                                    winsound.PlaySound("culmsounds/winningSoundEffect", winsound.SND_ASYNC)

                                # Makes the block flicker 3 times
                                for z in range(3):
                                    drawnblock.undraw()
                                    update()
                                    time.sleep(0.5)
                                    drawnblock = Image(Point(position, 792 - (height * 76)), block)
                                    drawnblock.draw(gameScreen)
                                    update()
                                    time.sleep(0.5)
                                screen = "newGame"

                                # checks if your endless score beat the local score and saves it
                                if endless:
                                    with open("highscore.txt", "w") as highscorefile:
                                        if score > localhighscore:
                                            highscorefile.write(str(score))
                                            newHighscore = True
                                        else:
                                            highscorefile.write(str(localhighscore))

                                gameScreen.close()
                                tempScore = score
                                break

                            drawnblocks.append(drawnblock)
                            # print(drawnblocks)
                            # print("Previous Position:", prevPosition, "New Position:", position)

                            # changes the start position to the opposite side for the next block
                            if starter == "left":
                                starter = "right"
                            else:
                                starter = "left"

                            score += 1
                            level += 1
                            height += 1
                            if not powerupping:
                                bop += 1

                            # a power up that multiplies your score for the next 5 blocks by 2 when placed
                            if multiplier:
                                if not count == 5:
                                    score += 1  # adds more 1 more score, 1 + 1 = 2 for next 5 blocks
                                    count += 1
                                else:
                                    count = 0
                                    multiplier = False

                            # print("level = " + str(level))  # test code

                            # checks if the block placed was at the very top, then it clears the grid and keeps the
                            # recently placed block at the bottom
                            if (level == 10 or (level - 10) % 9 == 0 and not level == 1) and endless:
                                # if it hits the top block
                                for i in drawnblocks:
                                    i.undraw()
                                height = 1
                                prevBlock = Image(Point(prevPosition, 792), block)
                                prevBlock.draw(gameScreen)
                                drawnblocks = [prevBlock]
                                # print("went thru")

                        # checks if the keys are any hotkeys for powerups
                        elif endless:
                            if powerupping:
                                if key == "":
                                    continue
                                elif key == "1":  # adds 1 block
                                    # if you still have a 3 block, then this will not do anything
                                    if n == 0:
                                        continue

                                    # adds 1 block to your current block
                                    else:
                                        if (position - 184) > (716 - position):
                                            position = position - 38
                                        else:
                                            position = position + 38
                                        # this elif and elif statement is here so that the updated block will be
                                        # aligned with the grid

                                        n = n - 1
                                        block = blocks[n]
                                        size = sizes[n]
                                        drawnblock.undraw()
                                        drawnblock = Image(Point(position, 792 - height * 76), block)
                                        drawnblock.draw(gameScreen)
                                        addBlock = True

                                # slows down the speed only for the current block
                                elif key == "2":  # slow the speed down
                                    slowed = 2

                                # sets the score of the next 5 blocks for 2
                                elif key == "3":  # score multiplier
                                    multiplier = True

                                # sets powerupping to false after you use it
                                powerupping = False
                                draw = False
                                for x in temp:
                                    x.undraw()

                                # grey out all the images to indicate you do not have any powerups available
                                temp = []
                                for x in range(3):
                                    bruh = Image(Point(950, 200 + x * 200), blackbuttons[x])
                                    bruh.draw(gameScreen)
                                    temp.append(bruh)

                    # moves the block left and right forever until it has been placed
                    if draw:  # the physical moving of the block
                        drawnblock.move(76 * direction, 0)
                        update()
                        position += 76 * direction
                        if position - size <= 184 or position + size >= 716:
                            direction *= -1

        elif 360 <= click.getX() <= 460 and 540 <= click.getY() <= 560:  # if user clicks resets score
            # overwrites the text file used with "0"
            with open("highscore.txt", "w") as highscorefile:
                highscorefile.write("0")

        elif 463 >= click.getX() >= 137 and 415 >= click.getY() >= 385:  # if user clicks on hotkey
            titleScreen.close()

            # visuals
            hotkeyScreen = GraphWin("Hot Key Edit", 500, 500, autoflush=False)
            hotkeyBackground = Image(Point(250, 250), "culmimages/hotkeyBackground.gif")
            hotkeyBackground.draw(hotkeyScreen)

            screen = "hotkey fix"

            currentHotkey = Text(Point(250, 450), "Current Hotkey: " + hotkey.upper())
            currentHotkey.draw(hotkeyScreen)
            currentHotkey.setSize(17)
            currentHotkey.setFill("white")

            changeKey = Image(Point(250, 275), "culmimages/hotkeyText1.gif")
            changeKey.draw(hotkeyScreen)

            confirmChange = Image(Point(250, 325), "culmimages/hotkeyText2.gif")
            confirmChange.draw(hotkeyScreen)

            # lets user choose options
            while screen == "hotkey fix":
                click = hotkeyScreen.getMouse()
                if 395 >= click.getX() >= 105 and 292 >= click.getY() >= 258:  # if user chooses to change hotkey
                    changeKey.undraw()
                    selectKey = Image(Point(250, 275), "culmimages/hotkeyText3.gif")
                    selectKey.draw(hotkeyScreen)

                    confirmChange.undraw()

                    update()

                    # sets hotkey to whatever typed
                    hotkey = hotkeyScreen.getKey()
                    if hotkey == "1" or hotkey == "2" or hotkey == "3":  # invalid hotkeys
                        hotkey = "space"

                        # flashes an error message if they choose 1 2 or 3 because those keys are used for
                        # powerups
                        for i in range(3):
                            errorText = Text(Point(350, 50), "Hotkeys cannot be 1, 2, or 3!")
                            errorText.setSize(15)
                            errorText.setFill("red")
                            errorText.setSize(13)
                            errorText.draw(hotkeyScreen)
                            update()
                            time.sleep(0.5)
                            errorText.undraw()
                            update()
                            time.sleep(0.5)

                    currentHotkey.undraw()
                    selectKey.undraw()
                    currentHotkey = Text(Point(250, 450), "Current Hotkey: " + hotkey.upper())
                    currentHotkey.draw(hotkeyScreen)
                    currentHotkey.setSize(17)
                    currentHotkey.setFill("lightgrey")

                    changeKey = Image(Point(250, 275), "culmimages/hotkeyText1.gif")
                    changeKey.draw(hotkeyScreen)

                    confirmChange = Image(Point(250, 325), "culmimages/hotkeyText2.gif")
                    confirmChange.draw(hotkeyScreen)

                elif 89 <= click.getX() <= 411 and 338 >= click.getY() >= 312:
                    # exits the hotkey change tab
                    hotkeyScreen.close()
                    screen = "newGame"
                    ending = "none"
                    continue

        elif 335 >= click.getX() >= 265 and 460 >= click.getY() >= 435:  # if user clicks on rules
            rulesScreen = GraphWin("Rules", 500, 500, autoflush=False)
            rulesscreenBackground = Image(Point(250, 250), "culmimages/rulesBackground.gif")
            rulesscreenBackground.draw(rulesScreen)
            skip = False
            while True:
                page1 = True
                page2 = False

                # these lists store the elements of their pages so we can undraw them
                # when we switch to the previous or next page
                pg1 = []
                pg2 = []
                if skip:
                    cont = True
                    break
                if page1:

                    # visuals
                    text1 = Text(Point(250, 25), "Classic Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg1.append(text1)

                    rule1 = Text(Point(250, 125),
                                 "1. You will be given a starter 3x1 block to stack that is constantly moving")
                    rule1.setSize(10)
                    rule1.draw(rulesScreen)
                    rule1.setFill("white")
                    pg1.append(rule1)
                    rule2 = Text(Point(250, 162), "2. The default hot key to stack is space, try to stack all "
                                                  "blocks on your previous one")
                    pg1.append(rule2)
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    rule2.setFill("white")

                    pg1.append(rule2)
                    rule3 = Text(Point(250, 200),
                                 "3. Everytime you misalign your new block with the previous block under it, \n"
                                 "you will lose the misaligned blocks, making a smaller base for you to stack on")
                    rule3.setSize(10)
                    rule3.draw(rulesScreen)
                    rule3.setFill("white")

                    pg1.append(rule3)
                    rule4 = Text(Point(250, 250),
                                 "4. Speeds of the block constantly moving will \nincrease after each level")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)
                    rule4.setFill("white")

                    pg1.append(rule4)
                    rule5 = Text(Point(250, 300), "5. If you make it to level 4 with 3 block\n"
                                                  " remaining, you will be forced to lose one block")
                    rule5.setSize(10)
                    rule5.draw(rulesScreen)
                    rule5.setFill("white")

                    pg1.append(rule5)
                    rule6 = Text(Point(250, 350), "6. If you make it to level 7 with more than one block remaining, \n "
                                                  "you will also be forced to lose one block")
                    rule6.setSize(10)
                    rule6.draw(rulesScreen)
                    rule6.setFill("white")

                    pg1.append(rule6)

                    blackbox = Rectangle(Point(130, 390), Point(370, 410))
                    blackbox.setFill("black")
                    blackbox.draw(rulesScreen)
                    pg1.append(blackbox)
                    rule7 = Text(Point(250, 400), "7. Once you stack to the top, you win!")
                    rule7.setSize(10)
                    rule7.draw(rulesScreen)
                    rule7.setFill("white")

                    pg1.append(rule7)

                    rule8 = Text(Point(250, 450), "TL;DR \n Time each placement of blocks on top of the \n"
                                                  "previous one, when you hit the top you win!")
                    rule8.setSize(13)
                    rule8.setFill("white")
                    rule8.draw(rulesScreen)
                    rule8.setFill("white")

                    pg1.append(rule8)

                    exittext = Text(Point(475, 485), "Next")
                    exittext.setFill("red")
                    exittext.draw(rulesScreen)
                    pg1.append(exittext)

                    click = rulesScreen.getMouse()

                    # only allows you to click next so you read the endless rules
                    while True:
                        if 460 <= click.getX() <= 490 and 480 <= click.getY() <= 490:
                            page2 = True
                            page1 = False
                            for i in pg1:
                                i.undraw()
                            break
                        click = rulesScreen.getMouse()

                if page2:
                    # when "next" is clicked

                    # visuals
                    text1 = Text(Point(250, 50), "Endless Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg2.append(text1)

                    rule1 = Text(Point(250, 100), "1. Same as classic mode but..")
                    rule1.setSize(10)
                    rule1.setFill("white")
                    rule1.draw(rulesScreen)
                    pg2.append(rule1)

                    rule123 = Text(Point(250, 150), "2. Speed will increase slower than classic mode")
                    rule123.setSize(10)
                    rule123.setFill("white")
                    rule123.draw(rulesScreen)
                    pg2.append(rule123)

                    rule2 = Text(Point(250, 200),
                                 "3. You will be given power ups every 3 blocks you stack (these can be saved)")
                    rule2.setSize(10)
                    rule2.setFill("white")

                    rule2.draw(rulesScreen)
                    pg2.append(rule2)

                    rule3 = Text(Point(250, 250), "* Slow-mo: Slow down the speed \nfor your next block by 2x")
                    rule3.setSize(10)
                    rule3.setFill("white")

                    rule3.draw(rulesScreen)
                    pg2.append(rule3)

                    rule4 = Text(Point(250, 300), "* Extended block: Extends your current \n block by 1 to get a"
                                                  "higher chance of \n stacking it correctly")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)
                    rule4.setFill("white")

                    pg2.append(rule4)

                    rule7 = Text(Point(250, 350), "* Score multiplier: Your next 3 blocks have a \n"
                                                  "score of 3 if stacked properly")
                    rule7.setSize(10)
                    rule7.draw(rulesScreen)
                    rule7.setFill("white")

                    pg2.append(rule7)

                    rule5 = Text(Point(250, 450), "ALSO, ENDLESS STACKING >:)")
                    rule5.setFill("white")
                    rule5.setSize(25)
                    rule5.setFill("white")

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
                        # either allows you to go back to classic rules (page 1) or quit the rules tab
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

        elif 520 <= click.getX() <= 580 and 535 <= click.getY() <= 565:  # if user wants to quit from menu
            quit()

        elif 10 <= click.getX() <= 90 and 535 <= click.getY() <= 565:  # if user wants to go to the about screen
            aboutScreen = GraphWin("About", 500, 500)

            # visuals
            aboutscreenBackground = Image(Point(250, 250), "culmimages/aboutBackground.gif")
            aboutscreenBackground.draw(aboutScreen)

            exitAbout = Text(Point(450, 450), "Exit")
            exitAbout.setSize(20)
            exitAbout.draw(aboutScreen)

            contrib = Text(Point(250, 70), "Contributors: Jacky and Orion")
            contrib.draw(aboutScreen)

            aboutGame = Text(Point(250, 125), "About the Game:")
            aboutGame.draw(aboutScreen)
            aboutGame.setSize(20)

            aboutGameText = Text(Point(250, 225), "Stacker is a game where the user tries to align (aka stack) blocks\n"
                                                  "vertically. The blocks will be moving "
                                                  "left and right while the user\n"
                                                  "is stacking. When the user inputs the "
                                                  "specified key, the moving block\n"
                                                  " will stop and hopefully be aligned with previous stacked blocks.\n"
                                                  "After every level, the speed of the moving blocks will increase.\n"
                                                  "If the stacked newly block is only "
                                                  "partially aligned with previous blocks,\n"
                                                  "the misaligned portion of blocks blocks will "
                                                  "disappear and the user\n"
                                                  "will be stacking with a smaller block than before; increases the\n"
                                                  "difficulty for future stacking.")
            aboutGameText.draw(aboutScreen)
            version = Text(Point(250, 25), "Version 1.0.0")
            version.draw(aboutScreen)

            features = Text(Point(250, 350), "Our Additional Features:")
            features.draw(aboutScreen)
            features.setSize(15)
            featuresText = Text(Point(250, 380), "Endless mode, power ups (slow speed, add block, score multiplier),\n"
                                                 "achievements, hot key switch")
            featuresText.draw(aboutScreen)

            eggText = Image(Point(50, 450), "culmimages/eastereggsmall.gif")
            eggText.draw(aboutScreen)

            easteregg = False
            click = aboutScreen.getMouse()
            while True:
                # either allows you to leave rules and go back to the menu ORRRR
                # lets you discover a SECRET EASTER EGG!! POG
                if 425 <= click.getX() <= 475 and 435 <= click.getY() <= 465:
                    aboutScreen.close()
                    break
                elif 25 <= click.getX() <= 75 and 425 <= click.getY() <= 475:
                    easteregg = True
                    break
                click = aboutScreen.getMouse()

            if easteregg:  # if you click on the easteregg
                aboutScreen.close()

                # visuals
                easterwin = GraphWin("can't believe its all over", 400, 400)

                egg = Image(Point(200, 110), "culmimages/easteregg.gif")
                egg.draw(easterwin)

                smiley1 = Image(Point(75, 350), "culmimages/smiley.gif")
                smiley2 = Image(Point(325, 350), "culmimages/smiley.gif")
                smiley1.draw(easterwin)
                smiley2.draw(easterwin)

                text2 = Text(Point(200, 300), "Hi Ms Wong. We would like to thank you for\n"
                                              "teaching us very well and being a cool teacher.\n"
                                              "We enjoyed the course a lot and wish \n"
                                              "you the best in your future in teaching.\n"
                                              "\n See you in grade 11!")
                text2.draw(easterwin)
                text3 = Text(Point(200, 380), "Sincerely, Orion and Jacky")
                text3.draw(easterwin)
                easterwin.getMouse()
                easterwin.close()  # thanks for the fun we both had in class!, btw exactly 1000 lines 😳😳 <- flushed


