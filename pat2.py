from turtle import*
speed('fastest')
bgcolor('black')
color =['red', 'orange', 'yellow',
         'green', 'blue', 'purple']
i=0
while True:
    pencolor(color[i%6])
    fd(10+i)
    lt(100)
    i +=1
mainloop()