import turtle
tao = turtle.Pen()
tao.shape('turtle')

tao.color("black","brown")
tao.begin_fill()
for i in range(2):
    tao.forward(10)
    tao.left(90)
    tao.forward(300)
    tao.left(90)
tao.end_fill()

tao.left(180)
tao.goto(0,230)

for i in range(14):
    for i in range(2):
        tao.forward(30)
        tao.right(90)
        tao.forward(3)
        tao.right(90)
    tao.right(90)
    tao.forward(5)
    tao.left(90)

turtle.done()