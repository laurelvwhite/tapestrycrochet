from argparse import ArgumentParser
from graphics import *
from PIL import ImageGrab
import math

# Define arguments
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
parser.add_argument('--stitch_colors', type=str, nargs='+', default=
                     ['red','yellow','blue','black'],
                     help='A list of colors to use for the stitches')

# Parse arguments
opts = parser.parse_args()
height=opts.height
width=opts.width
mag=opts.magnification
filename=opts.filename
background=opts.background
stitch_colors=opts.stitch_colors
stitch_colors.append(background) # Add the background color to the list of available stitch colors
ncolors=len(stitch_colors) # Determine number of stitch colors
current_color=stitch_colors[0] # Start coloring with first color

# If there are more colors than can fit in one row, throw out the ones at the end
if ncolors > width:
    print('Too many colors. Limiting to %d colors'%width)
    stitch_colors = stitch_colors[:width]

# Create graphics window
win = GraphWin('Pattern', width*mag, height*mag+2*mag)
win.setBackground('white')

# Draw grid with given number of rows and stitches per row
for i in range(width):
    for j in range(height):
        rect = Rectangle(Point(i*mag,2*mag+j*mag),Point(i*mag+mag,2*mag+j*mag+mag))
        rect.draw(win)
        rect.setFill(background)

# Put the stitch colors along the top of the grid
color_bin_left_edges = []
for i in range(ncolors):
    color_bin_left_edges.append(win.getWidth()/2-(ncolors/2)*mag+i*mag)
    color_rect = Rectangle(Point(color_bin_left_edges[i],mag),Point(color_bin_left_edges[i]+mag,2*mag))
    color_rect.draw(win)
    color_rect.setFill(stitch_colors[i])

# Put "quit" message along top of window
message = Text(Point(win.getWidth()/2, mag/2), 'Click here to quit and save.')
message.draw(win)

while True:
    # Take user input
    p = win.getMouse()
    # If user clicks along top, break loop and jump to save & exi
    if p.y < mag:
        break
    # If user clicks on one of the stitch colors, change the current color and wait for further input
    if p.y > mag and p.y < 2*mag:
        if p.x > color_bin_left_edges[0] and p.x < color_bin_left_edges[ncolors-1]+mag:
            index = math.floor((p.x-color_bin_left_edges[0])/mag)
            current_color = stitch_colors[index]
            continue
        else:
            continue
    # If user has clicked on a stitch box, fill the box with the current color
    x = p.x - p.x%mag
    y = p.y - p.y%mag
    stitch = Rectangle(Point(x,y),Point(x+mag,y+mag))
    stitch.draw(win)
    stitch.setFill(current_color)

# Save the image and close the window
ImageGrab.grab().save(filename)
win.close()
