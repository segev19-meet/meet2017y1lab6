import turtle
turtle.penup()
turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
square.goto(0,0)
square.pendown()
square.goto(0,100)
square.stamp()
square.goto(100,100)
square.stamp()
square.goto(100,0)
square.stamp()
square.goto(0,0)
square.stamp()


triangle=turtle.clone()
triangle.shape("triangle")
triangle.penup()
triangle.goto(-100,-100)
triangle.pendown()

triangle.goto(-100,0)
triangle.stamp()
triangle.goto(-50,-50)
triangle.stamp()
triangle.goto(-100,-100)
triangle.stamp()


turtle.mainloop()


