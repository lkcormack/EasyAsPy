import turtle # the turtle drawing package
import platform

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

if platform.system() == "Darwin":
    print("Executing macOS-specific exit.")
    turtle.exitonclick()
elif platform.system() == "Windows":
    print("Executing Windows-specific exit.")
    turtle.Screen().exitonclick()
    # Windows-specific functionality
else:
    print(f"Sorry, I don't speak {platform.system()}.")
    print("Trying Darwin-specific exit.")
    turtle.exitonclick()
    
