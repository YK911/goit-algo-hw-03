import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size):
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor("lightblue")
    screen.title("Koch Snowflake")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.setpos(-size / 2, size / 2)
    snowflake_turtle.color("white")
    snowflake_turtle.speed(10)
    snowflake_turtle.width(4)

    for _ in range(4):
        koch_snowflake(snowflake_turtle, order, size)
        snowflake_turtle.right(90)

    screen.mainloop()


draw_koch_snowflake(order=3, size=300)
