import turtle
turtle.Screen().bgcolor("white")
sc=turtle.Screen()
sc.setup(400,400)
turtle.title("welcome to turtle world")
board=turtle.Turtle()
board.forward(100)
for i in range(2):
  board.left(120)
  board.forward(100)
turtle.penup()
turtle.goto(10,60)
turtle.pendown()
turtle.forward()
for i in range(2):
  board.right(120)
  board.forward(100)
turtle.mainloop()
