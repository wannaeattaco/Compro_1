import turtle
from turtle import Turtle
import time
import random
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bon appetit!")
screen.setup(800, 600)
screen.tracer(0)


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Game(Turtle):

    def __init__(self, score=0, plate=3):
        self.score = score
        self.plate = plate
        self.bell_pepper = bell_pepper
        self.mushroom = mushroom
        self.salami = salami
        self.cheese = cheese
        self.spoon = spoon
        self.fork = fork
        self.knife = knife

    def collect(self):
        x = random.randint(-350, 350)
        y = random.randint(300, 400)
        if self.bell_pepper.distance(player) < 20:
            self.bell_pepper.goto(x, y)
            self.score += 1
            print(f'score {self.score}')
            font = ("Courier", 24, "normal")
            self.write(f'Score: {self.score}', align="left", font=font)
        if self.mushroom.distance(player) < 20:
            self.mushroom.goto(x, y)
            self.score += 3
            print(f'score {self.score}')
            font = ("Courier", 24, "normal")
            self.write(f'Score: {self.score}', align="left", font=font)
        if self.salami.distance(player) < 20:
            self.salami.goto(x, y)
            self.score += 5
            print(f'score {self.score}')
            font = ("Courier", 24, "normal")
            self.write(f'Score: {self.score}', align="left", font=font)
        if self.cheese.distance(player) < 20:
            self.cheese.goto(x, y)
            self.score += 5
            print(f'score {self.score}')
            font = ("Courier", 24, "normal")
            self.write(f'Score: {self.score}', align="left", font=font)

    def hurt(self):
        if self.spoon.distance(player) < 20:
            x = random.randint(-350, 350)
            y = random.randint(300, 400)
            self.spoon.goto(x, y)
            self.plate -= 1
            print(f'live {self.plate}')
        if self.fork.distance(player) < 20:
            x = random.randint(-350, 350)
            y = random.randint(300, 400)
            self.fork.goto(x, y)
            self.plate -= 1
            print(f'live {self.plate}')
        if self.knife.distance(player) < 20:
            x = random.randint(-350, 350)
            y = random.randint(300, 400)
            self.knife.goto(x, y)
            self.plate -= 1
            print(f'live {self.plate}')

    def set_score(self, score, plate):
        self.score = score
        self.plate = plate
        Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        font = ("Courier", 24, "normal")
        self.write(f'Score: {self.score}', align="left", font=font)


class Stage(Turtle):

    def __init__(self):
        self.game = Game
        self.item = Items
        self.spoon = Spoon

    def set_score(self, score, plate):
        self.game.score = score
        self.game.plate = plate
        Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        font = ("Courier", 24, "normal")
        self.write(f'Score: {self.game.score}', align="left", font=font)


class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, -250)
        self.speed(0)

    def go_left(self):
        self.shape('square')
        move_to_x = player.xcor() - 15
        move_to_y = player.ycor()
        self.setheading(180)
        self.goto(move_to_x, move_to_y)
        # if player.xcor() == -300:

    def go_right(self):
        self.shape('square')
        move_to_x = player.xcor() + 15
        move_to_y = player.ycor()
        self.setheading(0)
        self.goto(move_to_x, move_to_y)


class Items(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('green')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 10)

    def fall(self):
        self.shape('circle')
        y = self.ycor()
        y -= 2
        self.sety(y)

        if y < -300:
            x = random.randint(-350, 350)
            y = random.randint(300, 400)
            self.goto(x, y)


class BellPepper(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('green')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(280, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 10)


class Mushroom(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('white')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(300, 380)
        self.goto(x, y)
        self.speed = random.randint(1, 10)


class Salami(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('#7f2f26')
        self.penup()
        x = random.randint(-350, 360)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 10)


class Cheese(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        x = random.randint(-340, 350)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 15)


class Fork(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(5, 10)


class Spoon(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('blue')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 10)


class Knife(Items):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.color('grey')
        self.penup()
        x = random.randint(-350, 350)
        y = random.randint(300, 400)
        self.goto(x, y)
        self.speed = random.randint(1, 10)


player = Player()
stage = Stage()
items = Items()
bell_pepper = BellPepper()
mushroom = Mushroom()
salami = Salami()
cheese = Cheese()
spoon = Spoon()
fork = Fork()
knife = Knife()
game = Game()
screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")

while True:
    screen.update()
    time.sleep(0.01)
    BellPepper.fall(bell_pepper)
    Mushroom.fall(mushroom)
    Salami.fall(salami)
    Cheese.fall(cheese)
    Spoon.fall(spoon)
    Fork.fall(fork)
    Knife.fall(knife)
    Game.collect(game)
    Game.hurt(game)
# screen.mainloop()


