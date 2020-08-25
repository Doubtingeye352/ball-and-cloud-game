import turtle
import random
import time
import math


wn = turtle.Screen()
wn.title("ball and cloud")
wn.bgcolor("lightblue")
wn.setup(800,550)
wn.tracer(0)



score = 0



Gnd = -232


ground = turtle.Turtle()
ground.color("darkgreen")
ground.speed(0)
ground.shape("square")
ground.shapesize(stretch_wid=1, stretch_len=40)
ground.penup()
ground.goto(0,-250)


sun  = turtle.Turtle()
sun.color("yellow")
sun.speed(0)
sun.shape("circle")
sun.penup()
sun.goto(0,220)

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.width = 20
player.height = 20
player.dy = 0
player.dx = 0
player.state = "ready"
player.goto(-340, Gnd + player.height / 2)



enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(340, -225)

Mini_enemys = []

for _ in range(20):
    Mini_enemy = turtle.Turtle()
    Mini_enemy.shape("square")
    Mini_enemy.color("white")
    Mini_enemy.shapesize(stretch_wid=0.4, stretch_len=2, outline=None)
    Mini_enemy.penup()
    x = random.randint(-450, 450)
    y = random.randint(100, 200)
    Mini_enemy.setposition(x, y)
    Mini_enemys.append(Mini_enemy)

pen = turtle.Turtle()
player.hideturtle()
sun.hideturtle()
ground.hideturtle()
pen.write("Loading terrain", font=("arial", 26, "normal"))
time.sleep(2)
pen.clear()
pen.write("Done!", font=("arial", 26, "normal"))
time.sleep(1)
pen.clear()
player.showturtle()
sun.showturtle()
pen.hideturtle()
ground.showturtle()






def Collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False

enemyspeed = 10

playerspeed = 5

def jump():
    if player.state == "Ready":
        player.dy = 12
        player.state = "jumping"
        
        
def move_left():
        x = player.xcor()
        x = x - playerspeed
        if x < -400:
            x = -400
        player.setx(x)


def move_right():
        x = player.xcor()
        x = x + playerspeed
        if x > 400:
            x = 400
        player.setx(x)


Gravity = -0.8

wn.listen()
wn.onkeypress(jump, "space")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_left, "Left")

while True:
    wn.update()

    pen2 = turtle.Turtle()
    pen2.write(score, font=("arial", 26, "normal"))
    pen2.clear()
    pen2.penup()
    pen2.goto(0, 200)


    x = enemy.xcor()
    x = x - enemyspeed
    if x < -400:
        x = 345
        score += 1

    enemy.setx(x)



    if Collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()

        pen.write("Game Over", font=("Roboto", 26, "normal"))
        pen2.hideturtle()
        
        break




    for Mini_enemy in Mini_enemys:
        y = Mini_enemy.ycor()
        y -= 5
        Mini_enemy.sety(y)

        if Mini_enemy.ycor() < -250:
            x = random.randint(-450, 450)
            y = random.randint(100, 200)
            Mini_enemy.setposition(x, y)

        if Collision(player, Mini_enemy):
            player.hideturtle()
            Mini_enemy.hideturtle()

            pen.write("Game Over", font=("Roboto", 26, "normal"))
            pen2.hideturtle()
            break
            
            



  


    # Gravity
    player.dy += Gravity

    # Move the jumper
    y = player.ycor()
    y += player.dy
    player.sety(y)

    # Deal with the ground
    if player.ycor() < Gnd + player.height / 2:
       player.sety(Gnd + player.height / 2)
       player.dy = 0
       player.state = "Ready"



wn.mainloop()
