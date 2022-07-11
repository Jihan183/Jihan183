from turtle import *
color('blue', 'yellow')
begin_fill()
while True:
    forward(300)
    left(50)
    if abs(pos()) < 1:
        break
end_fill()
done()
