import turtle

def  draw_recursive_pentagram(size):
    count = 1                   #计数器
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 50
    if size <= 500:
        draw_recursive_pentagram(size)

# def draw_pentagram(size):
#     count = 1
#     while count <= 5:
#         turtle.forward(size)
#         turtle.right(144)
#         count = count + 1

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    # size <= 100:
        #绘制五角星
        # draw_pentagram(size)
    draw_recursive_pentagram(size)
    #    size += 10

    turtle.exitonclick()

if __name__ == '__main__':
    main()

# turtle.penup()  抬起画笔,之后移动画笔不绘制形状
# turtle.pendown()    落下画笔,之后移动画笔绘制形状
# turtle.pensize()    设置画笔宽度
# turtle.pencolor()   设置画笔颜色
# 常用颜色：white black darkgreen gold violet purple