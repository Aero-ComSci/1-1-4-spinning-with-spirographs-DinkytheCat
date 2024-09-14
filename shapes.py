import turtle as t

def setup_fixed_window():
    root = t.getcanvas().winfo_toplevel()
    root.geometry("800x800")
    root.resizable(False, False)

def draw_horizontal_shapes(num_shapes):
    if num_shapes <= 0 or num_shapes > 5:
        print("Number of shapes must be between 1 and 5.")
        return
    
    t.speed(0)
    t.bgcolor('black')
    screen_width = 800


    total_shape_width = num_shapes * 50
    total_spacing = screen_width - total_shape_width
    spacing_between_shapes = total_spacing / (num_shapes + 1)

    for i in range(num_shapes):
        x = -screen_width / 2 + (i + 1) * spacing_between_shapes + i * 50
        y = 0
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color('red')
        t.dot(50)
        
try:
    num_shapes = int(input("Enter the number of shapes (between 1 and 5): "))
    if 1 <= num_shapes <= 5:
        t.setup(800, 800)
        setup_fixed_window()
        draw_horizontal_shapes(num_shapes)
        t.done()
    else:
        print("Number of shapes must be between 1 and 5.")
except ValueError:
    print("Please enter a valid integer.")
