
from graphics import *
def main():
    win = GraphWin()
    for row in range(2):
        for column in range(2):
            rect = Rectangle(Point(row*100,column*100),Point((row+1)*100,(column+1)*100))
            fillColor = "blue" if row == column else "red"
            rect.setFill(fillColor)
            rect.setOutline("black")
            rect.draw(win)
            insideRect = Rectangle(Point(row*150 + 25,column*150 + 25),Point((row+1)*50 + 25,(column+1)*50 + 25))
            fillInsideColor = "red" if row == column else "blue"
            insideRect.setFill(fillInsideColor)
            insideRect.setOutline("black")
            insideRect.draw(win)
    win.getMouse()
    win.close()
main()
