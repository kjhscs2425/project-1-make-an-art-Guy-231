import turtle
 
turtle.tracer(00)
turtle.speed(0)
x=0
turtle.up()
turtle.forward(-200)
turtle.down()
turtle.color('yellow')



for x in range(150):
     turtle.forward(x+10)
     turtle.right(46)
     turtle.color('blue')
     if x >=50:
          turtle.color('purple')

turtle.up()
turtle.forward(400)
turtle.down()

for x in range(150):
     turtle.forward(x-2)
     turtle.right(91)
     turtle.color('yellow')
     if x >=50:
          turtle.color('orange')
     if x >=100:
        turtle.color('green')

turtle.right(-90)
turtle.up()
turtle.forward(300)
turtle.down()

for x in range(100):
     turtle.forward(x+45)
     turtle.right(170)
     turtle.color('yellow')
     if x >=25:
          turtle.color('orange')
     if x >=50:
        turtle.color('red')
        if x >=75:
            turtle.color('orange')

turtle.right(90)
turtle.up()
turtle.fd(200)
turtle.down()

for x in range(100):
     turtle.forward(x+45)
     turtle.right(201)
     turtle.color('yellow')
     if x >=25:
          turtle.color('orange')
     if x >=50:
        turtle.color('red')   



turtle.exitonclick()
