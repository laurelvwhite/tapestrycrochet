from argparse import ArgumentParser
from graphics import *
from PIL import ImageGrab

parser = ArgumentParser()
parser.add_argument('--height', type=int, default=10,
                     help='Number of rows of stitches. Default is 10.')
parser.add_argument('--width', type=int, default=20,
                     help='Number of stitches per row. Default is 20.')
parser.add_argument('--magnification', type=int, default=20,
                     help='Side length of each stitch in grid in pixels')
parser.add_argument('--filename', type=str, default='pattern.png',
                     help='File to save pattern image to. Default is '
                     '"pattern.png" in pwd.')
parser.add_argument('--background', type=str, default='white',
                     choices=['red', 'orange', 'yellow', 'green', 'blue',
                     'purple', 'pink', 'gray', 'black', 'white', 'brown'],
                     help='Color to auto-fill stitches. Default is white.')
parser.add_argument('--first_color', type=str, default='red',
                     choices=['red', 'orange', 'yellow', 'green', 'blue',
                     'purple', 'pink', 'gray', 'black', 'white', 'brown'],
                     help='A stitch color. Default is red.')
parser.add_argument('--second_color', type=str, default='yellow',
                     choices=['red', 'orange', 'yellow', 'green', 'blue',
                     'purple', 'pink', 'gray', 'black', 'white', 'brown'],
                     help='A stitch color. Default is yellow.')
parser.add_argument('--third_color', type=str, default='blue',
                     choices=['red', 'orange', 'yellow', 'green', 'blue',
                     'purple', 'pink', 'gray', 'black', 'white', 'brown'],
                     help='A stitch color. Default is blue.')
opts = parser.parse_args()

height=opts.height
width=opts.width
mag=opts.magnification
filename=opts.filename
background=opts.background
first_color=opts.first_color
second_color=opts.second_color
third_color=opts.third_color
color=first_color

win = GraphWin('Pattern', width*mag, height*mag+2*mag)
win.setBackground('white')

for i in range(width):
    for j in range(height):
        rect = Rectangle(Point(i*mag,2*mag+j*mag),Point(i*mag+mag,2*mag+j*mag+mag))
        rect.draw(win)
        rect.setFill(background)

first_rect = Rectangle(Point(win.getWidth()/2-2.0*mag,mag),Point(win.getWidth()/2-1.0*mag,2*mag))
first_rect.draw(win)
first_rect.setFill(first_color)

second_rect = Rectangle(Point(win.getWidth()/2-1.0*mag,mag),Point(win.getWidth()/2-0.0*mag,2*mag))
second_rect.draw(win)
second_rect.setFill(second_color)

third_rect = Rectangle(Point(win.getWidth()/2+0.0*mag,mag),Point(win.getWidth()/2+1.0*mag,2*mag))
third_rect.draw(win)
third_rect.setFill(third_color)

background_rect = Rectangle(Point(win.getWidth()/2+1.0*mag,mag),Point(win.getWidth()/2+2.0*mag,2*mag))
background_rect.draw(win)
background_rect.setFill(background)

message = Text(Point(win.getWidth()/2, mag/2), 'Click here to quit and save.')
message.draw(win)

while (True):
    p = win.getMouse()
    if p.y < mag:
        break
    if p.y > mag and p.y < 2*mag:
        if (p.x > win.getWidth()/2-2.0*mag) and (p.x < win.getWidth()/2-1.0*mag):
            color = first_color
            continue
        elif (p.x > win.getWidth()/2-1.0*mag) and (p.x < win.getWidth()/2-0.0*mag):
            color = second_color
            continue
        elif (p.x > win.getWidth()/2+0.0*mag) and (p.x < win.getWidth()/2+1.0*mag):
            color = third_color
            continue
        elif (p.x > win.getWidth()/2+1.0*mag) and (p.x < win.getWidth()/2+2.0*mag):
            color = background
            continue
        else:
            continue
    x = p.x - p.x%mag
    y = p.y - p.y%mag
    stitch = Rectangle(Point(x,y),Point(x+mag,y+mag))
    stitch.draw(win)
    stitch.setFill(color)

ImageGrab.grab().save(filename)
win.close()
