from Graphics.graphics import *
import winsound
from random import randint
import threading
import time

gameScreen = GraphWin("window", 900, 900, autoflush=False)

blocks = [
"images/3block.gif",
"images/2block.gif",
"images/1block.gif"
]

base = Line(Point(188, 825), Point(713, 825))
border2 = Line(Point(188, 75), Point(188, 825))
border3 = Line(Point(713, 75), Point(713, 825))
base.draw(gameScreen)
border2.draw(gameScreen)
border3.draw(gameScreen)

verticals = []

for i in range(6):
    s = Line(Point(263 + 75 * i, 75), Point(263 + 75 * i, 825))
    verticals.append(s)
    s.draw(gameScreen)

horizontals = []

for i in range(9):
    s = Line(Point(188, 150 + 75 * i,), Point(713, 150 + 75 * i))
    horizontals.append(s)
    s.draw(gameScreen)


sizes = [112, 75, 37]
hotkey = "space"
level = 0
n = 0
block = blocks[n]
starter = "left"
position = 0
size = sizes[n]
placing = True
stacking = True
direction = 1


class classicMode (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global position
        global hotkey
        global level
        global size
        global block
        global stacking
        global placing
        global starter
        global direction
        while stacking:
            if starter == "left":
                position = 188 + size
                direction = 1
            elif starter == "right":
                position = 188 + 525 - size
                direction = -1

            drawnblock = Image(Point(position, 788 - level * 75), block)
            drawnblock.draw(gameScreen)

            placing = True
            update()
            draw = True
            while placing:
                end = time.time() + 0.75 - 0.05 * level
                while time.time() < end:
                    key = gameScreen.checkKey()
                    if key == hotkey:
                        placing = False
                        stacking = False
                        draw = False
                        if starter == "left":
                            starter = "right"
                        else:
                            starter = "left"
                        level += 1
                        print(level)
                        stacking = True
                if draw:
                    drawnblock.move(75 * direction, 0)
                    position += 75 * direction
                    if position - (size + 1) <= 188 or position + size + 1 >= 713:  # + 1 because its 1 pixel off
                        direction *= -1


thread1 = classicMode()
thread1.start()

gameScreen.mainloop()

