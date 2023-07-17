from turtle import*
speed('fastest')
color = ['red','green',]
for i in range (6):
    pencolor('red')
    fd(50)
    for i in range (6):
        pencolor('blue')
        fd(25)
        fillcolor(color[i%2])
        begin_fill()
        for i in range(6):
           pencolor('green')
           fd(25)
           lt(360/6)
        end_fill()
    lt(360/6)
lt(360/6)
mainloop()


