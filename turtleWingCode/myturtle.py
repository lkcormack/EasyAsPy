# myturtle.py

def draw_box(t, width, height):
    # Draw a box with the given width and height below the turtle
    t.left(90)
    t.forward(int(width/2))
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(int(width/2))

def draw_zigzag_left(t, width, height):
    # Draw a zigzag with the given width and height below the turtle
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
   
def draw_zigzag_right(t, width, height):
    # Draw a zigzag with the given width and height below the turtle
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

def make_label(t, label):
    # Write the given label below the turtle
    t.penup()
    t.forward(20)
    t.write(label, font=("Arial", 12, "normal"))
    t.backward(20)
    t.pendown()
