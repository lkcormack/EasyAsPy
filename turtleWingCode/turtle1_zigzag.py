import turtle # the turtle drawing package

t = turtle.Turtle() 

print(f"Default heading is {t.heading()} (right)")
t.setheading(270) # down 

# Draw a line 
t.forward(100)  # Move forward by 100 units

# zig
t.right(90)     # Turn right by 90 degrees

# Draw a line 
t.forward(100)  # Move forward by 100 units

# zag
t.left(90)

# Draw a line 
t.forward(100)  # Move forward by 100 units

turtle.exitonclick()