import turtle as t

t.pensize(5)

COLORS = ["cyan", "teal", "beige", "crimson", "pink", "orange"]

# Nested Loop

# Drawing a triangle for 6 times
for y in range(6):
    # Switch colors based on indexing
    t.color("black", COLORS[y])
    # Fill with one of the colors
    t.begin_fill()
    # Drawing a single triangle
    for x in range(3):
        t.forward(100)
        t.left(120)
    # Take a left turn everytime we draw one
    t.left(60)
    t.end_fill()