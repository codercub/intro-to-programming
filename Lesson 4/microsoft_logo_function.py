# microsoft_logo.py

# Written by @zmagsar
# Nov 17, 2020
# Function ashiglasan huvilbar

import turtle as t

t.title("Microsoft Corporation")
t.speed(0)

# Dorvoljing ogogdson ongoor zurah function
def square(color):
    t.color(color, color)
    t.begin_fill()
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

# Uzgiig x, y tseg ruu avaachih function
def move_pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Undsen function
def main():
    # Ongonuudiig hadgalah list
    colors = [["orange red", "deep sky blue"], ["yellow green", "gold"]]
    # x tseguudiig hadgalah list
    x = [-450, -340]
    # y tseguudiig hadgalah list
    y = [5, -105]
    # Mor moroor n dorvoljin zurah davtalt
    for i in range(2):
        # Bagana baganaar n dorvoljin zurah davtalt
        for j in range(2):
            # Uzgiig x mor, y baganad avaachih
            move_pen(x[i % 2], y[j % 2])
            # Tuhain ongoor dorvoljing zurah
            square(colors[i][j])
    
    move_pen(-200, -100)
    # Uzegnii ongiig saaral bolgoh
    t.pencolor("grey")
    # Tuhain zaasan font, hemjee, helbereer bichih
    t.write("Microsoft", font = ("Segoe UI", 80, "normal"))
    
    t.hideturtle()
    
main()