from tkinter import *
from tkinter import ttk
import turtlefigures
import turtle


root = Tk()
root.title("Turtle Application")
root.geometry("1000x750+400+30")
root.resizable(False, False)
root["background"]="#000000"

label = Label(root, text = "Turtle Generator", bg = "#000000", fg = "white", bd = 6, font = "georgia", relief= "flat")
label.pack()

frame1 = Frame(root, relief = "flat", bg = '#000000', width = 600, height = 650)
frame1.pack(side = LEFT, padx = 10, pady = 10)

canvas = Canvas(frame1, highlightbackground = "#0099cc", width = 650, height = 650)
canvas.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)

pen.color("#66d6ff")
pen.speed(0)
pen.width(0)
pen.shape("turtle")

screen.bgcolor("#004b66")

frame2 = Frame(root, relief = "flat", bg = '#000000', width = 300, height = 650)
frame2.pack(side = LEFT, padx = 10)
frame2.pack_propagate(0)

controlPanel = Frame(frame2, relief = "flat", bg = "#00394d", width = 300, height = 200)
controlPanel.pack(side = TOP, padx = 2, pady = 2)
controlPanel.pack_propagate(0)

frame3 = Frame(controlPanel, bg = "#00394d" )
frame3.pack(fill = X)

lengthLabel = Label(frame3, text = "LENGTH:", bg = '#00394d', fg = '#0099cc')
lengthLabel.pack(side = LEFT, padx = 4, pady = 4)
 
lengthStr = StringVar()
lengthEntry = Entry(frame3, textvariable = lengthStr, bg = "#8cb3d9")
lengthEntry.pack(fill = X, padx = 4, expand = "yes")
lengthEntry.focus()

frame4 = Frame(controlPanel, bg = "#00394d")
frame4.pack(fill = X)

orderLabel = Label(frame4, text = "ORDER:", bg = '#00394d', fg = '#0099cc')
orderLabel.pack(side = LEFT, padx = 4, pady = 4) 
orderStr = StringVar()
orderEntry = Entry(frame4, textvariable = orderStr, bg = "#8cb3d9")
orderEntry.pack(fill = X, padx = 4, expand = "yes")


#draw turtle figures
def drawF():
       # get order and length
       length = int(lengthStr.get())
       order = int(orderStr.get()) 
 
       # get the figure id from OptionMenu
       figure = figureStr.get()
       figureId = figureList.index(figure)
 
       # if check to see what to draw
       
       if figureId == 0:# draw binary tree  
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws binary tree
              turtlefigures.tree(order, length, pen)
              
       elif figureId == 1:# draw quad tree       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws quad tree
              turtlefigures.dandelion(order, length, pen)
              
       elif figureId == 2:# draw a fern       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws fern
              turtlefigures.fern(order, length, pen)
              
       elif figureId == 3:# draw a snowflake       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws snowflake
              turtlefigures.snowflake(order, length, pen)
                    
       elif figureId == 4:# draw antiflake       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws antiflake
              turtlefigures.antiflake(order, length, pen)
              
       elif figureId == 5:# draw a s-gasket       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws s-gasket
              turtlefigures.gasket(order, length, pen)
              
       elif figureId == 6:# draw a carpet     
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws carpet
              turtlefigures.carpet(order, length, pen)
              
       elif figureId == 7:# draw a pentagon       
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws pentagon
              turtlefigures.pentagon(order, length, pen)
              
       elif figureId == 8:# draw a c-curve      
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws curve
              turtlefigures.curve(order, length, pen)
       
       elif figureId == 9:# draw a spiral      
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws spiral
              turtlefigures.spiral(order, length, pen)

       elif figureId == 10:# draw a cspiral      
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws cspiral
              turtlefigures.cspiral(order, length, pen)    

       elif figureId == 11:# draw a star      
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws stars
              turtlefigures.star(order, length, pen)

       elif figureId == 12:# draw a sun      
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws sun
              turtlefigures.sun(order, length, pen)

       elif figureId == 13:# draw INDIAN FLAG
              # move pen to a better position
              pen.up(); pen.backward(length);pen.down()
              # pen draws indianflag
              turtlefigures.india(order, length, pen)              
#end              


frame5 = Frame(controlPanel, bg = "#00394d")
frame5.pack(fill = X)
#make a drop down box for the figures
figureList = ["Binary Tree", "Dandelion", "Fern", "Snow Flake", "Anti Flake", "Sierpinsky Gasket", "Sierpinsky Carpet", "Penatgon", "C-Curve", "Square Spiral", "Spiral", "Star", "Sun", "Indian-Flag"]
figureStr = StringVar()
figure = OptionMenu(frame5, figureStr, *figureList)
figure.config(bg = "#6699cc", relief = "raised")
figure["menu"].config(bg = "black", fg = "white")
figure.pack(side = TOP, padx = 4, pady = 4)
figureStr.set("Turtle Figures")


#canvas background colors
def color(color):
       color = colorStr.get()
       colorId = colorList.index(color)

       if colorId == 0:
              screen.bgcolor("white")
       elif colorId == 1:
              screen.bgcolor("darkred")     
       elif colorId == 2:
              screen.bgcolor("indigo")
       elif colorId == 3:
              screen.bgcolor("steelblue")
       elif colorId == 4:
              screen.bgcolor("darkgreen")
       elif colorId == 5:
              screen.bgcolor("coral")
       elif colorId == 6:
              screen.bgcolor("purple")
       elif colorId == 7:
              screen.bgcolor("black")
#end

frame6 = Frame(controlPanel, bg = "#00394d")
frame6.pack(fill = X)
#make a drop down box for colors
colorList = ["White", "DarkRed", "Indigo", "SteelBlue", "DarkGreen", "Coral", "Purple", "Black"]
colorStr = StringVar()
colors = OptionMenu(frame6, colorStr, *colorList, command = color)
colors.config(bg = "#6699cc", relief = "raised")
colors["menu"].config(bg = "black", fg = "white")
colors.pack(side = TOP, padx = 2, pady = 2)
colorStr.set('Background Colors')


#frame 7 for pen color, shape and speed

frame7 = Frame(controlPanel, bg = "#00394d")
frame7.pack(fill = X)
#pen color change
def pencolor(pencolor):
       pencolor = pencolorStr.get()
       pencolorId = pencolorList.index(pencolor)

       if pencolorId == 0:
              pen.color("white")
       elif pencolorId == 1:
              pen.color("darkred")     
       elif pencolorId == 2:
              pen.color("indigo")
       elif pencolorId == 3:
              pen.color("steelblue")
       elif pencolorId == 4:
              pen.color("darkgreen")
       elif pencolorId == 5:
              pen.color("coral")
       elif pencolorId == 6:
              pen.color("purple")
       elif pencolorId == 7:
              pen.color("black")
#end

#make a drop down box for colors
pencolorList = ["White", "DarkRed", "Indigo", "SteelBlue", "DarkGreen", "Coral", "Purple", "Black"]
pencolorStr = StringVar()
pencolors = OptionMenu(frame7, pencolorStr, *pencolorList, command = pencolor)
pencolors.config(bg = "#6699cc", relief = "raised")
pencolors["menu"].config(bg = "black", fg = "white")
pencolors.pack(side = RIGHT, padx = 2, pady = 2)
pencolorStr.set('Color')

#turtle pen shape
def shape(shape):
       shape = shapeStr.get()
       shapeId = shapeList.index(shape)

       if shapeId == 0:
              pen.shape("classic")
       elif shapeId == 1:
              pen.shape("arrow")
       elif shapeId == 2:
              pen.shape("turtle")
       elif shapeId == 3:
              pen.shape("circle")
       elif shapeId == 4:
              pen.shape("square")
       elif shapeId == 5:
              pen.shape("triangle")
#end
#make a drop down box for shapes
shapeList = ["Classic", "Arrow", "Turtle", "Circle", "Square", "Triangle"]
shapeStr = StringVar()
shape = OptionMenu(frame7, shapeStr, *shapeList, command = shape)
shape.config(bg = "#6699cc", relief = "raised")
shape["menu"].config(bg = "black", fg = "white")
shape.pack(side = LEFT, padx = 2, pady = 2)
shapeStr.set('Shape')


#pen speed
def speed(speed):
       speed = speedStr.get()
       speedId = speedList.index(speed)

       if speedId == 0:
              pen.speed(0)
       if speedId == 1:
              pen.speed(10)
       if speedId == 2:
              pen.speed(6)
       if speedId == 3:
              pen.speed(3)
       if speedId == 4:
              pen.speed(1)
#end
#make a drop down box for speed
speedList = ["Fastest", "Fast", "Normal", "Slow", "Slowest"]
speedStr = StringVar()
speed = OptionMenu(frame7, speedStr, *speedList, command = speed)
speed.config(bg = "#6699cc", relief = "raised")
speed["menu"].config(bg = "black", fg = "white")
speed.pack(side = TOP, padx = 2, pady = 2)
speedStr.set("Speed")

#frame 8 for clear screen and draw command

frame8 = Frame(controlPanel, bg = "#00394d")
frame8.pack(fill = BOTH)
#clear command
def clearT():
       lengthStr.set("")
       orderStr.set("")
       screen.reset()
       
clearButton = Button(frame8, text = "CLEAR", command = clearT, relief = "raised", bg = '#0099cc', fg = '#00394d')
clearButton.pack(side = RIGHT, fill = NONE, padx = 5, pady = 5)

#draw command
drawButton = Button(frame8, text = "DRAW", command = drawF, relief = "raised", bg = '#0099cc', fg = '#00394d')
drawButton.pack(side = LEFT, fill = NONE, padx = 5, pady = 5)


#add a information box
message = '''Follow the steps below to get
started:

STEP 1
Select a type of turtle figure
from the list on the control
panel.

STEP 2
Enter your desired order and
length for the figures to be
drawn.

STEP 3
As you input order and length,
you will see the turtle pen
on the canvas starts to move
creating beautiful figures.

STEP 4
You may also choose a different
background color for the canvas

STEP 5
Below the background color
menu there are three options
for pen-shape, pen-speed &
pen-color.

STEP 6
Once you get a figure fully
drawn you can clear the screen
and proceed with another
figure.

Note -
For the figures Spiral, Sun &
Indian Flag no matter which
color you choose for the turtle
pen, it will be generated with
the color it is originally
specified in.

Tip #1 : Set the pen-speed
everytime you clear the
screen or else the turtle
is going to take forever to
generate a figure.

Tip #2 : Try white background
for the Indian Flag.


ENJOY....
'''

textbox = Text(frame2, height = 70, width = 300, bg = '#00394d', fg = '#b3d9ff', font = ("consolas","11"))
textbox.pack(fill = "both", expand = "yes", padx = 2, pady = 2)
textbox.insert('end', message)
textbox.config(state = 'disabled')

scrollbar = ttk.Scrollbar(textbox, orient = "vertical",  cursor = "arrow", command = textbox.yview)
scrollbar.pack(side = RIGHT, fill = Y)

textbox["yscrollcommand"] = scrollbar.set



