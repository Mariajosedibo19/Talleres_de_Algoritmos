import turtle
tortuguita = turtle.Turtle()
fondo=turtle.Screen()
fondo.bgcolor("light pink")


# M
tortuguita.pencolor("red")
tortuguita.pensize(13)
tortuguita.shape("turtle")
tortuguita.left(90)
tortuguita.forward(100)
tortuguita.right(130)
tortuguita.forward(100)

tortuguita.left(100)
tortuguita.forward(100)
tortuguita.right(130)
tortuguita.forward(100)
a=tortuguita.pos()


#A
tortuguita.goto(a)
tortuguita.right(290)
tortuguita.pencolor("purple")
tortuguita.pensize(13)
tortuguita.shape("circle")
tortuguita.left(70)
tortuguita.forward(100)
tortuguita.right(130)
tortuguita.forward(60)
tortuguita.right(120)
tortuguita.forward(50)
tortuguita.right(180)
tortuguita.forward(50)
tortuguita.right(65)
tortuguita.forward(50)
b=tortuguita.pos()

#J
tortuguita.goto(b)
tortuguita.right(290)
tortuguita.pencolor("green")
tortuguita.pensize(13)
tortuguita.shape("circle")
tortuguita.forward(60)
tortuguita.left(90)
tortuguita.forward(100)
tortuguita.left(90)
tortuguita.forward(50)
tortuguita.right(180)
tortuguita.forward(100)
c=tortuguita.pos()

#O
tortuguita.goto(c)
tortuguita.right(180)
tortuguita.pencolor("light blue")
tortuguita.pensize(13)
tortuguita.shape("arrow")
tortuguita.left(90)
tortuguita.forward(90)
tortuguita.left(90)
tortuguita.forward(90)
tortuguita.left(90)
tortuguita.forward(90)
tortuguita.left(90)
tortuguita.forward(90)
d=tortuguita.pos()

#flor
medida = 8  
pen = turtle.Turtle()  
for i in range(medida * 2):
    pen.forward(i * 5) 
    pen.right(90)    
tortuguita.exitonclick()
