# author ：Li
import turtle as t
#中国国旗
t.up()
t.goto(-200,200)
t.down()
t.begin_fill()
t.fillcolor("red")
t.pencolor("red")
for i in range(2):
    t.forward(280)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

t.up()
t.goto(-170,145)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()

t.up()
t.goto(-100,180)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for i in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

t.up()
t.goto(-70,160)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for i in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

t.up()
t.goto(-70,120)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for x in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

t.up()
t.goto(-70,120)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for x in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

t.up()
t.goto(-100,100)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
for x in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()


t.hideturtle()#隐藏小海龟
#维持面板
t.done()


