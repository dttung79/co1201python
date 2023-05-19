# draw a square without a top

import turtle as t

# # draw base line
# t.forward(100)
# t.left(90)
# # draw left side
# t.forward(100)
# t.left(90)
# # lift pen and move to right side
# t.penup()
# t.forward(100)
# # put pen down and draw right side
# t.pendown()
# t.left(90)
# t.forward(100)
# t.left(90)

# t.exitonclick()

angle = 90
length = 100

t.left(angle)
t.forward(length)
t.right(angle)
t.forward(length)
t.right(angle)
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)
t.forward(length)

t.exitonclick()