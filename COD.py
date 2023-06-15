import turtle

#Creating the Turtle Screen#
screen = turtle.Screen()
screen.bgcolor("black")

#Creating the Object#
cod = turtle.Turtle()
cod.color("gold")

#set fill color to yellow
cod.fillcolor("gold")

#Setting The Cursor to the middle of the screen
cod.penup()
cod.backward(223)
cod.pendown()

#Start Filling the object
cod.begin_fill()
cod.right(-40)
cod.forward(70)

#Bend
cod.right(70)
cod.forward(100)

#Bridge
cod.penup()
cod.forward(20)
cod.pendown()
cod.forward(90)

#Bend
cod.left(60)
cod.forward(90)

#Bridge
cod.penup()
cod.forward(20)
cod.pendown()
cod.forward(100)

#Bend
cod.right(70)
cod.forward(70)

#Bend
cod.right(50)
cod.forward(400)

#Bend
cod.right(60)
cod.forward(70)

#Bend
cod.right(70)
cod.forward(101)

#Bend
cod.right(50)
cod.forward(369)

cod.penup()
cod.left(130)
cod.forward(22)
cod.pendown()

#Bend
cod.right(-50)
cod.forward(250)

#Bend
cod.left(130)
cod.backward(100)

#Bend
cod.left(110)
cod.forward(100)

#Bend
cod.right(61)
cod.forward(265)

cod.penup()
cod.left(65)
cod.forward(20)
cod.left(115)
cod.pendown()
cod.forward(369)

#Bend
cod.right(50)
cod.forward(100)
cod.right(70)
cod.forward(70)
cod.right(60)
cod.forward(405)

#Stop Filling the Object
cod.end_fill()

screen.exitonclick()