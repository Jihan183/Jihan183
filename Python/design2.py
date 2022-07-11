from turtle import *
color('green', 'black')
begin_fill()
while True:
    forward(250)
    left(125)
    if abs(pos()) < 1:
        break
end_fill()
done()
