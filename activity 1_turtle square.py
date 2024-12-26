import turtle
turtle.Screen().bgcolor("white")
sc=turtle.Screen()
sc.setup(400,400)
turtle.title("welcome to turtle world")
board=turtle.Turtle()
for i in range(4):
  board.forward(100)
  board.left(90)
turtle.mainloop()

