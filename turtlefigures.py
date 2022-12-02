import math

def tree(n, l,pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2,pen)
     pen.right(90)
     tree(n-1, l/2,pen)
     pen.left(45)
     pen.backward(l)

#end 
#------------------------------------------------------------------------------

def dandelion(n, l,pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2,pen)
     pen.right(60)
     dandelion(n-1, l/2,pen)
     pen.right(60)
     dandelion(n-1, l/2,pen)
     pen.right(60)
     dandelion(n-1, l/2,pen)
     pen.left(90)
     pen.backward(l)

#end
#------------------------------------------------------------------------------

def fern(n, l,pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(2*l/3)
     pen.left(45); fern(n-1, l/2,pen); pen.right(45)
     pen.forward(2*l/3)
     pen.right(40); fern(n-1, l/2,pen); pen.left(40)
     pen.forward(2*l/3)
     pen.left(10); fern(n-1, 0.8*l,pen); pen.right(10)
     pen.backward(2*l)
#end
#------------------------------------------------------------------------------

def koch(n, l,pen):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3,pen)
     pen.left(60)
     koch(n-1,l/3,pen)
     pen.right(120)
     koch(n-1,l/3,pen)
     pen.left(60)
     koch(n-1,l/3,pen)
#end

def snowflake(n, l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.right(120)
     #endfor
#end 
#-----------------------------------------------------------------------------

def koch(n, l,pen):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3,pen)
     pen.left(60)
     koch(n-1,l/3,pen)
     pen.right(120)
     koch(n-1,l/3,pen)
     pen.left(60)
     koch(n-1,l/3,pen)
#end
     
def antiflake(n, l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.left(120)
     #endfor
#end 
#------------------------------------------------------------------------------
          
#sierpinsky gasket
def gasket(n, l,pen):
     
     # termination
     if n==0 or l<2 :
          
          # draw an equilateral triangle
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          #end for
          return
     #end if

     #recursive definition
     for i in range(3):
          gasket(n-1, l/2,pen)
          pen.forward(l)
          pen.left(120)
     #end for
#end s
#------------------------------------------------------------------------------

#sierpinsky carpet
def carpet(n, l,pen):

     #termination
     if n==0 or l<2 :
          # draw a square
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #end for
          return
  
     #recursive definition
     for i in range(4):
          carpet(n-1, l/3,pen)
          pen.forward(l/3)
          carpet(n-1, l/3,pen)
          pen.forward(l/3)
          pen.forward(l/3)
          pen.left(90)
     #end for
#end swiss
#------------------------------------------------------------------------------

#pentagon
def pentagon(n, l,pen):

     #termination
     if n==0 or l<2:
           # draw a pentagon
           for i in range(5):
                pen.forward(l)
                pen.left(72)
           #end for
           return

     # recursive defintion
     for i in range(5):
          pentagon(n-1, l/2.95,pen)
          pen.forward(l)
          pen.left(72)
     #end for
#end 
#-------------------------------------------------------------------------------
 
#c curve
def curve(n, l,pen):
     if n==0:
          pen.forward(1)
          return
     #endif
     curve(n-1, l,pen)
     pen.right(90)
     curve(n-1, l,pen)
     pen.left(90)
#end
#------------------------------------------------------------------------------

#spiral
def spiral(n, l, pen):
     for i in range(50):
          pen.forward(i * 4)
          pen.left(90)
#end
#-------------------------------------------------------------------------------

#circlespiral
def cspiral(n, l, pen):
     for i in range(10):
          for colors in ["red", "yellow", "blue", "green", "pink", "orange", "white", "cyan", "lavender", "black"]:
               pen.color(colors)
               pen.circle(80)
               pen.forward(i * 4)
               pen.left(170)
#end
#-------------------------------------------------------------------------------
               
#star
def star(n, l, pen):

     #termination
     if n==0 or l<2:
          pen.forward(l)
          return
     #endif

     for i in range(5):
          pen.forward(l)
          star(n-1, l/3, pen)
          pen.left(216)
#end
#-------------------------------------------------------------------------------
def sun(n, l, pen):
     pen.color("yellow")
     for i in range(54):
          pen.forward(l)
          pen.left(170)
     
#end
#-------------------------------------------------------------------------------
def india(order, length, pen):

     pen.color("blue")
     pen.circle(50)

     pen.color("white")
     pen.forward(200)
     pen.left(90)
     pen.forward(100)
     pen.left(90)
     pen.forward(200)
     pen.forward(200)
     pen.left(90)
     pen.forward(100)
     pen.left(90)
     pen.forward(200)

     pen.penup()
     pen.forward(200)
     pen.pendown()

     pen.color("green")
     pen.begin_fill()
     pen.right(90)
     pen.forward(100)
     pen.right(90)
     pen.forward(400)
     pen.right(90)
     pen.forward(100)
     pen.end_fill()
     
     pen.penup()
     pen.forward(100)
     pen.pendown()

     pen.color("orange")
     pen.begin_fill()
     pen.forward(100)
     pen.right(90)
     pen.forward(400)
     pen.right(90)
     pen.forward(100)
     pen.end_fill()

     pen.penup()
     pen.right(90)
     pen.forward(203)
     pen.pendown()

     pen.left(90)
     
     pen.color("blue")
     for i in range(54):
          pen.forward(100)
          pen.left(170)
#end
