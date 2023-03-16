import turtle
from turtle import *
import pygame
from pygame import *
import random
import time
turtle.title("Space Invaders")
turtle.bgcolor("black") 

#turtle properties
player = turtle.Turtle()
player2 = player.clone()
shot = 7
enemy = turtle.Turtle()
enemy2 = enemy.clone()
enemy3 = enemy.clone()
enemy4 = enemy.clone()
enemy5 = enemy.clone()
enemy6 = enemy.clone()
enemy.penup()
enemy.color("green")
enemy.shapesize(2, 2, 2)
enemy2.penup()
enemy2.color("green")
enemy2.shapesize(2, 2, 2)
enemy3.shapesize(2, 2, 2)
enemy3.color("green")
enemy3.penup()
enemy4.penup()
enemy4.color("green")
enemy4.shapesize(2, 2, 2)
enemy5.penup()
enemy5.color("green")
enemy5.shapesize(2, 2, 2)
enemy6.penup()
enemy6.color("green")
enemy6.shapesize(2, 2, 2)
player.pensize(1)
player.speed(10)
player.shapesize(2,2,2)
player.shape("square")
player.color("yellow", "green")
player.penup()
enemy2.shape("square")
enemy3.shape("square")
enemy4.shape("square")
enemy5.shape("square")
enemy6.shape("square")
enemy.shape("square")
e = 0
global var
var = True
player2.color("black")
#Player Movement
def right(): 
    player.forward(20)
    global var
    var = True
    if var == True:
        bullet.forward(20)
        bullet2.forward(20)
        bullet3.forward(20)
def left():
    player.backward(20)
    if var == True:
        bullet.backward(20)
        bullet2.forward(20)
        bullet3.forward(20)
player.goto(0,-300)
player2.goto(0,300)
enemy.goto(-420,350)
enemy2.goto(-360,350) 
enemy3.goto(-300, 350)
enemy4.goto(-240, 350)
enemy5.goto(-180, 350)
enemy6.goto(-120, 350)

turtle.listen()
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
bullet = turtle.Turtle()
bullet2 = turtle.Turtle()
bullet3 = turtle.Turtle()
bullet.penup()
bullet.color("green")
def shoot():         
    bullet.left(90)           
    bullet.penup()
    bullet.shape("circle")
    bullet.color("green", "yellow")
    bullet.penup()
    bullet.shapesize(.5, .5)
    global shot
    shot = 5
    bullet.showturtle()
    var = False

turtle.onkey(shoot, 'space')
turtle.listen()
def quitThis():
    Turtle.bye()
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 40 and abs(a.ycor() - b.ycor()) < 40 
def follow_runner(): 
    if is_collided_with(bullet, enemy):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy.color("black")
        bullet.reset
        enemy.reset
        shot = 4
        global e
        e = e+1
        bullet = False
    if is_collided_with(bullet, enemy2):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy2.color("black")
        bullet.reset
        enemy2.reset
        shot = 4
        e=e+1
        bullet = False
    if is_collided_with(bullet, enemy3):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy3.color("black")
        bullet.reset
        enemy3.reset
        shot = 4
        e=e+1
        bullet = False
    if is_collided_with(bullet, enemy4):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy4.color("black")
        bullet.reset
        enemy4.reset
        shot = 4
        e=e+1
        bullet = False
    if is_collided_with(bullet, enemy5):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy5.color("black")
        bullet.reset
        enemy5.reset
        shot = 4
        e=e+1
        bullet = False
    if is_collided_with(bullet, enemy6):
        bullet.color("black")
        score = 0
        score = score + 50
        print(score)
        enemy6.color("black")
        bullet.reset
        enemy6.reset
        shot = 4
        e=e+1
        bullet = False
def move():
    enemy.fd(10)
    enemy2.fd(10)
    enemy3.fd(10)
    enemy4.fd(10)
    enemy5.fd(10)
    enemy6.fd(10)
def turnr():
    enemy.right(90)
    enemy2.right(90)
    enemy3.right(90)
    enemy4.right(90)
    enemy5.right(90)
    enemy6.right(90)
def turnl():
    enemy.left(90)
    enemy2.left(90)
    enemy3.left(90)
    enemy4.left(90)
    enemy5.left(90)
    enemy6.left(90)
def gob():
    if shot == 435:
        print("the heck")
turtle.listen()
follow_runner() 

#bullet.color("black")

while True:
    for i in range(55):
        follow_runner() 
        move()
        follow_runner() 
        if shot == 5:
            bullet.forward(10)
            follow_runner() 
        else:
            gob()
        time.sleep(.05)
        if shot == 5:
            bullet.forward(10)
            follow_runner() 
        else:
            gob()
        time.sleep(.05)
    if shot == 5:
        bullet.forward(10)
        follow_runner() 
    else:
            gob()
    turnr()
    if shot == 5:
        bullet.forward(10)
        follow_runner() 
    else:
            gob()
    if shot == 5:
        bullet.forward(10)
        follow_runner() 
    move()
    move()
    if shot == 5:
        bullet.forward(10)
        follow_runner() 
    else:
            gob()
    turnr()
    if shot == 5:
        bullet.forward(10)
        follow_runner()
    else:
            gob()
    if shot == 5:
        bullet.forward(10)
        follow_runner() 
    else:
            gob()
    for i in range (55):
        if bullet.pos() == enemy.pos():
            bullet.hideturtle()
            enemy.hideturtle()
            follow_runner() 
        else:
            gob()
        move()
        if shot == 5:
            bullet.forward(10)
        time.sleep(.05)
    else:
            gob()
    if shot == 5:
        bullet.forward(10)
    else:
            gob()
    time.sleep(.05)
    turnl()
    if shot == 5:
        bullet.forward(10)
    else:
            gob()
    if shot == 5:
           bullet.forward(10)
    else:
            gob()
    move()
    move()
    if shot == 5:
           bullet.forward(10)
    else:
            gob()
    turnl()
    if shot == 5:
           bullet.forward(10)
    else:
            gob()
turtle.mainloop()