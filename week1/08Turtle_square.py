# a small program to draw a square

# import the turtle module and give it the name t
# turtle is a module that allows us to draw shapes
import turtle as t

# set the length of the square to 40 units
length = 100
angle = 60

t.forward(length)   # move forward 40 units
t.left(angle)         # turn left 90 degrees
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)

t.exitonclick()     # exit the program when you click on the screen
