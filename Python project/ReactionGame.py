#Project Name: Split Screen Reaction Game

#Author: Eric

#readme:
#1. basics >>
# Make a game, where a ball can fall from left or right.
# User has to press correct mouse button(left or right) to gain point (1 point per good click)
# wrong btn = lose point(-2 per bad click)
# ball hit ground = game over
# if point < 0, game over
# if point = 20, win
# note that the ball speed increases as the game goes on. ballspeed = 5(score+1)
# note that all "print" and texts in the console are for testing
# note that touchpad also work, two finger tap = right click on mouse

#2. advanced(if enough time) >>
#gameover screen
#show score on normal screen and on gameover screen
#show the reason for losing on game over screen, landed/score<0

#3. extra/bonus animations(if enough time) >>
#ball turn red and shake after wrong click
#turn green after right click.

#game start test log:
print("Game Starting...")


#import biuld-in functions, libraries...
from turtle import *
import time
import random




#background
root = Screen()
root.title("Reaction Game")
root.bgcolor("blue")
root.setup(500,600)


#draw split line
line = Turtle()
line.shape("circle")
line.hideturtle
line.color("lightblue")
line.shapesize(1,1)
line.width(20)
line.goto(0,300)
line.goto(0,-300)
line.goto(0,-280)
line.goto(-300, -280)
line.goto(300, -280)
line.penup()
line.hideturtle()


#Sprite(ball)
ball = Turtle()
ball.hideturtle()
ball.shape("circle")
ball.color("yellow")
ball.shapesize(3,3)
ball.penup()


#Sprite(score keeper)
pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(-200, 260)
pen.pendown()
pen.color("white")
pen.write(0, font=("Calibri", 20, "bold"))


#Sprite(Game over)
penLose = Turtle()
penLose.penup()
penLose.hideturtle()
penLose.goto(-150, 0)
penLose.pendown()
penLose.color("lightblue")


#Sprite(Game over score)
penLose1 = Turtle()
penLose1.penup()
penLose1.hideturtle()
penLose1.goto(-150, -100)
penLose1.pendown()
penLose1.color("lightblue")


#Sprite(Win)
penWin = Turtle()
penWin.penup()
penWin.hideturtle()
penWin.goto(-150, 0)
penWin.pendown()
penWin.color("darkblue")

#Sprite(Win score)
penWin1 = Turtle()
penWin1.penup()
penWin1.hideturtle()
penWin1.goto(-150, -100)
penWin1.pendown()
penWin1.color("darkblue")

#First initializations
score = 0
speed = score+5
pos = [(-125, 300), (125, 300)]


#funtions for click detect
def clickRightCorrect(x,y):
    global score
    print("right")
    score += 1
    clickRightCorrect.has_been_called = True

def clickLeftCorrect(x,y):
    global score
    print("left")
    score += 1
    clickLeftCorrect.has_been_called = True

def clickRightWrong(x,y):
    global score
    print("right(wrong)")
    clickRightWrong.has_been_called = True
    score -= 2

def clickLeftWrong(x,y):
    global score
    print("left(wrong)")
    clickLeftWrong.has_been_called = True
    score -= 2


#initiallize, default(funtion not called)
clickRightCorrect.has_been_called = False
clickLeftCorrect.has_been_called = False
clickRightWrong.has_been_called = False
clickLeftWrong.has_been_called = False

# turn ball to face north
ball.left(90)


#while loop to keep the game running
while(True):

    def topOfLoop():
        global score
        global speed


        # initiallize, default(funtion not called)
        clickRightCorrect.has_been_called = False
        clickLeftCorrect.has_been_called = False
        clickRightWrong.has_been_called = False
        clickLeftWrong.has_been_called = False


        #check if player already won or lose
        if score >= 50:
            print("Win!")
            root.clear()
            root.bgcolor("lightgreen")
            penWin.write("🎉Nice Reaction Skill!🎉", font=("Calibri", 25, "bold"))
            penWin1.write("Score = " + str(score), font=("Calibri", 25, "bold"))
            time.sleep(5)
            exit()

        if score < 0:
            print("Lose!")
            root.clear()
            root.bgcolor("red")
            penLose.write("🥺Score Too Low!🥺", font=("Calibri", 25, "bold"))
            penLose1.write("Score = " + str(score), font=("Calibri", 25, "bold"))
            time.sleep(5)
            exit()



        ball.hideturtle()


        # move to dropping position:
        posTop = random.choice(pos)
        ball.goto(posTop)
        print(posTop)

        # start showing turtle:
        ball.showturtle()


        while (True):

            speed = (score+1)*5


            # fall:
            ball.backward(speed)
            time.sleep(0.01)


            # User input(click) check, using if else statement
            if (ball.xcor() == -125):
                root.onscreenclick(clickLeftCorrect, 1)
                root.onscreenclick(clickRightWrong, 3)

                if(clickLeftCorrect.has_been_called):
                    print(score)
                    pen.clear()
                    pen.write(score, font=("Calibri", 20, "bold"))
                    print("speed = " + str(speed))
                    topOfLoop()

                if (clickRightWrong.has_been_called):
                    print(score)
                    pen.clear()
                    pen.write(score, font=("Calibri", 20, "bold"))
                    print("speed = " + str(speed))
                    topOfLoop()

            if (ball.xcor() == 125):
                root.onscreenclick(clickLeftWrong, 1)
                root.onscreenclick(clickRightCorrect, 3)

                if(clickRightCorrect.has_been_called):
                    print(score)
                    pen.clear()
                    pen.write(score, font=("Calibri", 20, "bold"))
                    print("speed = " + str(speed))
                    topOfLoop()

                if (clickLeftWrong.has_been_called):
                    print(score)
                    pen.clear()
                    pen.write(score, font=("Calibri", 20, "bold"))
                    print("speed = " + str(speed))
                    topOfLoop()

            # check if landed
            if (ball.ycor() <= (-280)):
                print("Crash! You lost.")
                root.clear()
                root.bgcolor("red")
                penLose.write("🥺Ball Landed!🥺", font=("Calibri", 25, "bold"))
                penLose1.write("Score = " + str(score), font=("Calibri", 25, "bold"))
                time.sleep(5)
                exit()


    #first drop(call topOfLoop function before any input), note that this function is a recursion
    topOfLoop()


mainloop()
