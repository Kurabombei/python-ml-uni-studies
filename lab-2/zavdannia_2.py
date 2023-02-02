from graphics import *
def main():
    win = GraphWin()
    for i in range(6):
        size = 8
        rect = Rectangle(Point(i*size,0),Point((i+1)*size,size))
        fillColor = "green" if i < 3 else "white"
        outline = "white" if i < 3 else "black"
        rect.setFill(fillColor)
        rect.setOutline(outline)
        rect.draw(win)
    win.getMouse()
    win.close()
main()
