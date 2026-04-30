import turtle
import winsound
wn=turtle.Screen()
wn.title("Subham")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

winning_score=1


#Left bar
bar_a=turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("green")
bar_a.shapesize(stretch_wid=6,stretch_len=1)
bar_a.penup()
bar_a.goto(-350,0)

#Right bar
bar_b=turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("green")
bar_b.shapesize(stretch_wid=6,stretch_len=1)
bar_b.penup()
bar_b.goto(+350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
# ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-(0.1)

#Score bar
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

#left bar moving
def bar_a_up():
    y=bar_a.ycor()
    y+=20
    bar_a.sety(y)

def bar_a_down():
    y=bar_a.ycor()
    y-=20
    bar_a.sety(y)

#right bar moving
def bar_b_up():
    y=bar_b.ycor()
    y+=20
    bar_b.sety(y)

def bar_b_down():
    y=bar_b.ycor()
    y-=20
    bar_b.sety(y)

#keyword pressing
wn.listen()
wn.onkeypress(bar_a_up,"w")
wn.onkeypress(bar_a_down,"s")

wn.onkeypress(bar_b_up,"Up")
wn.onkeypress(bar_b_down,"Down")

#game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.Beep(1000, 90)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.Beep(1000, 90)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
  

    #functions of bars
    # Left paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
        (ball.ycor() < bar_a.ycor() + 60 and ball.ycor() > bar_a.ycor() - 60):
        ball.setx(-340)     
        ball.dx *= -1        

# Right paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
        (ball.ycor() < bar_b.ycor() + 60 and ball.ycor() > bar_b.ycor() - 60):
        ball.setx(340)     
        ball.dx *= -1       

    # Left player wins
       
    if score_a >= winning_score:
        ball.hideturtle()
        bar_a.hideturtle()
        bar_b.hideturtle()
        wn.bgcolor("black")

        pen.clear()
        pen.goto(0, 0)
        pen.color("white")
        pen.write(f"Left Player Wins!\nScore: {score_a}", align="center", font=("Arial", 30, "bold"))
        wn.update()   # important: update screen after writing
        turtle.done()
        break

    # Right player wins
    if score_b >= winning_score:
        ball.hideturtle()
        bar_a.hideturtle()
        bar_b.hideturtle()
        wn.bgcolor("black")

        pen.clear()
        pen.goto(0, 0)
        pen.color("white")
        pen.write(f"Right Player Wins!\nScore: {score_b}", align="center", font=("Arial", 30, "bold"))
        wn.update()
        turtle.done()  
        break
