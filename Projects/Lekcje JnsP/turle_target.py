import turtle

# stałe nazwane
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# konfiguracja okna
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# narysowanie okna
turtle.hideturtle()
turtle.speed()
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# umieszczenie żółwia na środku ekranu`j`
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# pobranie od gracza wartości kąta i siły
angle = float(input("Podaj kąt: "))
force = float(input("Podaj siłe: "))

# obliczenie odległości
distance = force*FORCE_FACTOR

# określenie kierunku
turtle.setheading(angle)

# wystrzelenie pocisku
turtle.pendown()
turtle.forward(distance)

# czy cel został trafiony
if (turtle.xcor() >= TARGET_LEFT_X and
    turtle.xcor() <= (TARGET_LEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LEFT_Y and
        turtle.ycor() <= (TARGET_LEFT_Y + TARGET_WIDTH)):
    print("Trafiony")
else:
    print("Próbuj dalej")
