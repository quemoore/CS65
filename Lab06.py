# Quentin Moore
# CS65 Section 1
# 09-29-2025

from graphics import *
import random

num = int(input("How many retangles do you want: "))

win = GraphWin("Squares", 600, 600)

for i in range(num):
    
    # random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # random size
    x0 = random.randint(0, 600)
    y0 = random.randint(0, 600)
    x1 = random.randint(0, 600)
    y1 = random.randint(0, 600)
    
    rect = Rectangle(Point(x0, y0), Point(x1, y1))
    rect.setFill(color_rgb(r, g, b))
    rect.setOutline(color_rgb(r, g, b))
    rect.draw(win)
    
# code for the rest of lab 6
'''
# window
win = GraphWin("hello World", 1000, 800)


# point
p = Point(300, 300)
p.draw(win)

# moves point
p.move(100, 100)

# circle
circ = Circle(p, 50)
circ.setOutline("red")
circ.draw(win)

p.move(100, 200)

circ1 = Circle(Point(200, 200), 50)
circ1.setOutline("blue")
circ1.setFill("blue")
circ1.draw(win)

text = Text(Point(100, 100), "hello world")
text.setSize(22)
text.setTextColor("green")
text.draw(win)

rect = Rectangle(Point(600, 40), Point(800, 200))
rect.setFill("yellow")
rect.draw(win)


# main circ
circ = Circle(Point(500, 425), 200)
circ.setFill("yellow")
circ.draw(win)

# eyes
circ = Circle(Point(410, 350), 40)
circ.setFill("black")
circ.draw(win)

circ = Circle(Point(590, 350), 40)
circ.setFill("black")
circ.draw(win)

# mouth
circ = Circle(Point(500, 480), 70)
circ.setFill("black")
circ.draw(win)

rect = Rectangle(Point(400, 400), Point(600, 450))
rect.setFill("yellow")
rect.setOutline("yellow")
rect.draw(win)
'''