from turtle import *
width (2)
bgcolor("light blue")
speed (10000)

#green field


begin_fill ()
color ("green")
forward (1000)
right (90)
forward (300)
right (90)
forward (2000)
right (90)
forward (300)
right (90)
forward (1000)
end_fill ()

#castle middle part

begin_fill ()
color ("gray")
backward (150)
left (90)
forward (200)
right (90)
forward (250)
right (90)
forward (200)
right (90)
forward (150)
end_fill ()

#castle middle part frame

color ("black")
backward (150)
right (90)
forward (200)
left (90)
forward (250)
left (90)
forward (200)
left (90)
forward (150)

#tower N1 left side

backward (150)
begin_fill ()
color ("gray")
backward (50)
left (90)
forward (250)
left (90)
forward (30)
right (90)
forward (30)
right (90)
forward (30)
forward (50)
forward (30)
right (90)
forward (30)
right (90)
forward (30)
left (90)
forward (250)
end_fill()

#tower N1 left side frame

color ("black")
right (270)
backward (50)
left (90)
forward (250)
left (90)
forward (30)
right (90)
forward (30)
right (90)
forward (30)
forward (50)
forward (30)
right (90)
forward (30)
right (90)
forward (30)
left (90)
forward (250)
backward (250)
right (90)
forward (50)
forward (30)
right (90)
forward (15)

#left side pillar roof

left (90)
forward(20)
begin_fill ()
color ("darkred")
right (120)
forward (150)
backward (150)
left (120)
backward (20)
backward (30)
backward (50)           #აქ შეკრება არ მინდოდა რადგან დანიშნული 
backward (30)           # მაქვს ყველაფრის სიგრძე სიგანე ყველაფრის
backward (20)
right (60)
forward (150)
end_fill()

#left side tower N1

penup()
begin_fill ()
color ("gray")
goto (-200,0)
pendown()
right (30)
forward (140)
left (90)
forward (200)
left (90)
forward (140)
left (90)
forward (200)
end_fill()

#left side tower N1 frame

goto (-200,0)
left (90)

color ("black")
forward (140)
left (90)
forward (200)
left (90)
forward (140)
left (90)
forward (200)

#left side tower N1 windows

left (90)
forward (120)
penup()
left (90)
forward (15)
pendown()
forward (20)
left (90)
forward (70)
left (90)
forward (20)
left (90)
forward (70)
left (90)
forward (20)

#window N2

penup ()
forward(30)
pendown ()
forward (20)
left (90)
forward (70)
left (90)
forward (20)
left (90)
forward (70)
left (90)
forward (20)

#window N3

penup ()
forward(30)
pendown ()
forward (20)
left (90)
forward (70)
left (90)
forward (20)
left (90)
forward (70)
left (90)
forward (20)

#window N4

penup ()
forward(30)
pendown ()
forward (20)
left (90)
forward (70)
left (90)
forward (20)
left (90)
forward (70)
left (90)
forward (20)

#left side tower N2

penup()
forward (15)
left (90)
forward (120)
pendown()
begin_fill ()
color ("gray")
right (90)
forward (30)
right (90)
forward (200)
right (90)
forward (30)
right (90)
forward (200)
end_fill()
color ("black")
right (90)
forward (30)
right (90)
forward (200)
right (90)
forward (30)
right (90)
forward (200)
backward (200)

#left side pillar N2 roof

right (270)
forward (15)
begin_fill ()
color ("darkred")
left (110)
forward (85)
backward (85)
right (110)
backward (15)
backward (30)                #აქ შეკრება არ მინდოდა რადგან დანიშნული 
backward (15)                # მაქვს ყველაფრის სიგრძე სიგანე ყველაფრის
left (70)
forward (86.3)
end_fill()

#right pillar N2

penup()
goto (100,0)
pendown()
begin_fill ()
color ("gray")
right (70)
forward (50)
left (90)
forward (250)
left (90)
forward (50)
left (90)
forward (250)
end_fill()

#right pillan N2 frame

color ("gray")
left (90)
forward (50)
left (90)
forward (250)
left (90)
forward (50)
left (90)
forward (250)
backward (250)
right (90)
forward (30)
right (90)
begin_fill()
color ("gray")
forward (30)
right (90)
forward (110)
right(90)
forward (30)
right (90)
forward (110)
end_fill()

#upper plate of pillan N2 right side

right (90)
color ("black")
forward (30)
right (90)
forward (110)
right(90)
forward (30)
right (90)
forward (110)

#right side N2 pillar frame 

penup()
goto (100, 0)
pendown()
right (180)

forward (50)
left (90)
forward (250)
left (90)
forward (50)
left (90)
forward (250)

#right side pillar roof

left (90)
forward(20)
backward (20)
left (90)
forward (250)
left (90)
forward (30)
right (90)
forward (15)

#right side pillar N1 roof

penup()
right (90)
forward (110)
pendown()
forward (15)
begin_fill ()
color ("dark red")
left (120)
forward (145)
backward (145)
left (60)
forward (140)
right(118)
forward (145)
end_fill()

#right side pillan N2 with block house

penup()
goto (100, 0)
pendown()
color ("black")
left (28)
forward (140)
penup()
right (90)
forward (50)
pendown()

begin_fill()
color ("gray")
forward (200)
right (90)
forward (140)
right (90)
forward (200)
end_fill()

color ("black")
right (90)
forward (140)
right (90)
forward (200)
right (90)
forward (140)
right (90)
forward (200)




#left side tower N1 windows

#window N1 right side pillar N2


right (90)
forward (120)
penup()
right (90)
forward (18)
pendown ()
forward (20)
right (90)
forward (70)
right (90)
forward (20)
right (90)
forward (70)
backward (70)
left (90)
backward (20)
left (90)
backward (70)
left (90)

#window N2

penup()
forward (30)
pendown ()
forward (20)
right (90)
forward (70)
right (90)
forward (20)
right (90)
forward (70)
backward (70)
left (90)
backward (20)
left (90)
backward (70)
left (90)

#window N3

penup()
forward (30)
pendown ()
forward (20)
right (90)
forward (70)
right (90)
forward (20)
right (90)
forward (70)
backward (70)
left (90)
backward (20)
left (90)
backward (70)
left (90)

#window N4

penup()
forward (30)
pendown ()
forward (20)
right (90)
forward (70)
right (90)
forward (20)
right (90)
forward (70)
backward (70)
left (90)
backward (20)
left (90)
backward (70)
left (90)

#right side pillar N2

penup()
goto (350,0)
pendown()


begin_fill ()
color ("gray")
forward (30)
left (90)
forward (200)
left (90)
forward (30)
left (90)
forward (200)
end_fill ()

left (90)
color ("black")
forward (30)
left (90)
forward (200)
left (90)
forward (30)
left (90)
forward (200)

#left side pillan N2 roof

backward (200)
forward (15)
right (90)
forward (15)
begin_fill ()
color ("darkred")
right (110)
forward (87)
backward (87)
right (70)
forward (60)
left (110)
forward (87)
end_fill()

#door 

penup()
goto (0,0)

left (70)
backward (100)
color ("black")
forward (75)
pendown()
right (90)
forward (100)
left (30)
forward (50)
backward (50)
right (30)
backward (100)
left (90)
forward (150)
right (180)
forward (50)
left (90)
forward (100)
right (30)
forward (50)
right (60)
forward (50)

#door bars

penup()
goto (25,0)
pendown()
backward (10)
left (90)
for i in range (9):
    forward (100)
    backward (100)
    left (90)
    forward (10)
    right (90)
right (90)
forward (10)
left (90)
forward (118)
backward (118)
right (90)
forward (10)
left (90)
forward (134)
backward (134)
right (90)
forward (10)
left (90)
forward (144)
backward (144)   
right (90)
forward (10)
left (90)
forward (143)
backward (143)
right (90)
forward (10)
left (90)
forward (143)
backward (143)
right (90)
forward (10)
left (90)
forward (143)
backward (143)
right (90)
forward (10)
left (90)
forward (143)
backward (143)
right (90)
forward (10)
left (90)
forward(134)
backward (134)
right (90)
forward (10)
left (90)
forward (118)
backward (118)

#blocks on middle part


penup()
forward (200)
right (90)
forward (85)

left (90)
forward (20)
















exitonclick()   