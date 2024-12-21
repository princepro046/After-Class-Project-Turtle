import turtle

# Create turtle
t = turtle.Turtle()

# Draw rectangle
for _ in range(2):
    t.forward(200)  # Draw width
    t.left(90)
    t.forward(100)  # Draw height
    t.left(90)

turtle.done()  # Finish drawing
