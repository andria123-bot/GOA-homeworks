from turtle import *
speed (999999999)
width (2)
bgcolor ("light blue")


#castle wall


penup()
goto (0, -100)
pendown()
backward (150)
begin_fill ()
color ("gray")
forward (260)
left (90)
forward (220)
left (90)
forward (260)
left (90)
forward (220)
end_fill()


#black line on castle wall


color ("black")
penup ()
goto (0, -100)
pendown()
left (90)
backward (150)
forward (260)
left (90)
forward (220)
left (90)
forward (260)
left (90)
forward (220)

#castle pillarN1 left side


begin_fill ()
color ("gray")
right (90)
forward (70)
right (90)
forward (300)
right (90)
forward (70)
right (90)
forward (300)
end_fill ()
color ("black")
right (90)
forward (70)
right (90)
forward (300)
right (90)
forward (70)
right (90)
forward (300)
backward (300)
begin_fill()
color ("gray")
right (270)
forward (20)
left (90)
forward (50)
left (90)
forward (100)
penup ()
backward (100)
right (90)
backward (50)
right (90)
backward (89)
left (180)
pendown ()
forward (20)
right (90)
forward (50)
right (90)
forward (109)
right (90)
forward (50)
end_fill()

#frame of pillar N1

color ("black")
right (90)
forward (110)
right (90)
forward (50)
right (90)
forward (110)
right (90)
forward (50)

#pillar roof N1


backward (30)
begin_fill()
color ("dark red")
left (90)
forward (35)
left (120)
forward (180)
left (120)
forward (180)
left (120)
forward (150)
end_fill ()

#pillar N2

penup()
goto (110, -100)
begin_fill ()
color ("gray")
pendown()
forward (70)
left (90)
forward (300)
left (90)
forward (70)
left (90)
forward (300)
end_fill ()

#pillan N2 black frame

color ("black")
left (90)
forward (70)
left (90)
forward (300)
left (90)
forward (70)
left (90)
forward (300)

#pillan N2 roof

penup ()
goto (110, -100)
backward (300)
pendown ()
begin_fill ()
color ("gray")
right (90)
forward (25)
backward (95)
right (180)
forward (25)
left (90)
forward (40)
left (90)
forward (120)
left (90)
forward (40)
end_fill()

#pillar frame black

color ("black")

left (90)
forward (120)
left (90)
forward (40)
left (90)
forward (120)
left (90)
forward (40)

#N2 pillar flag

backward (40)
left (90)
forward (80)
width (1.5)
left (90)
forward (50)
begin_fill ()
color ("white")
forward (100)
right (90)
forward (200)
right (90)
forward (100)
right (90)
forward (200)
end_fill ()


#GOA name


color ("black")
penup ()
backward (15)
left (90)
backward (45)
write ("GOAL ORIENTED ACADEMY", font=("arial",10,"normal"))

#castle door

penup ()
goto (110,0)
forward (100)
right (90)
forward (70)
pendown()
right (90)
forward (120)
left (60)
forward (60)
backward (60)
right (60)
backward (120)
left (90)
forward (190)
left (180)
forward (70)
pendown()
left (90)
forward (120)
right (60)
forward (60)
right (30)
forward (16)
penup ()
left (90)
backward (150)
right (90)
forward (52)
pendown()

backward (10)
left (90)
forward (126)
backward (126)
left (90)
forward (10)
right (90)
forward (130)

backward (130)
left (90)
forward (10)
right (90)
forward (136)

backward (136)
left (90)
forward (10)
right (90)
forward (143)

backward (143)
left (90)
forward (10)
right (90)
forward (149)

backward (149)
left (90)
forward (10)
right (90)
forward (149)

backward (149)
left (90)
forward (10)
right (90)
forward (149)

backward (149)
left (90)
forward (10)
right (90)
forward (143)

backward (143)
left (90)
forward (10)
right (90)
forward (136)

backward (136)
left (90)
forward (10)
right (90)
forward (130)

backward (130)
left (90)
forward (10)
right (90)
forward (126)

#windows N1 pillar N2

penup()
goto (100,170)
right (90)
forward (15)
forward (10)
pendown()
begin_fill ()
color ("Black")
forward (40)
right (90)
forward (50)
right (90)
forward (40)
right (90)
forward (50)
end_fill()

#window N2 pillan N1

begin_fill ()
color ("Black")
penup ()
goto (-150, 170)
left (90)
forward (15)
pendown()
forward (40)
left (90)
forward (50)
left (90)
forward (40)
left (90)
forward (50)
end_fill()


#blocks


penup ()
right (90)
forward (15)
right (90)
forward (32)
pendown()
begin_fill ()
color ("gray")
left (90)
forward (50)
right (90)
forward (18)
right (90)
forward (50)
end_fill()
color ("black")
right (90)
forward (18)
right (90)
forward (50)
right (90)
forward (18)
right (90)
forward (50)
right (90)
forward (18)
backward (18)
left (90)
backward (50)
left (90)
backward (18)
left (90)
penup()
forward (55) # aaqqqaa
pendown()
begin_fill ()
color ("gray")
right (90)
forward (18)
backward (18)
left (90)
forward (50)
right (90)
forward (18)
right (90)
forward (50)
end_fill()
color ("black")
right (90)
forward (18)
right (90)
forward (50)
right (90)
forward (18)
right (90)
forward (50)

penup()

goto (110, 125)
right (90)

begin_fill()
color ("gray")
pendown ()
forward (13)
left (90)
forward (50)
left (90)
forward (18)
left (90)
forward (50)
end_fill()
color ("black")
left (90)
forward (18)
left (90)
forward (50)
left (90)
forward (18)
left (90)
forward (50)


#stickman N1


penup ()

backward (55)
left (105)
pendown()
forward (25)
left (150)
forward (25)
backward (25)
right (165)
forward (25)
right (90)
circle (7)
right (90)
forward (5)
left (20)
forward (20)
backward (20)
right (40)
forward (20)

#stickman N2

penup()

goto (-50, 120)

right (145)

pendown()

forward (25)
left (150)
forward (25)
backward (25)
right (165)
forward (25)
right (90)
circle (7)
right (90)
forward (5)
left (20)
forward (20)
backward (20)
right (40)
forward (20)

#tower left side N1

penup ()

right (70)
forward (158)
left (90)
forward (60)

pendown()

begin_fill()
color ("gray")
right (85)
forward (130)
left (85)
forward (173)
left (90)
forward (130)
end_fill ()

#frame of tower left side N1

color ("black")

backward (130)
right (90)
backward (173)
right (85)
backward (131)

left (85)
forward (40)
right (90)
penup ()
forward (30)
pendown()
begin_fill ()
color ("black")
forward (75)
left (90)
forward (30)
left (90)
forward (75)
left (90)
forward (30)
end_fill()














































































































































































































exitonclick()