#! python
import math

def request_float(question:str, default:float = None):
    try:
        return float(input(question))
    except ValueError:
        if default == None: return default
        else: return float(default)
    except KeyboardInterrupt:
        if default == None: return default
        else: return float(default)

def request_positive_float(question:str, default:float = None):
    value = -1
    while value <= 0:
        value = request_float(question, default)
        if value <= 0: print("The value must be positive.")
    return value

def compute_area_square(side:float):
    return compute_area_rectangle(side, side)

def compute_area_rectangle(length:float, width:float = None):
    if width == None: return compute_area_square(length)
    return (length * width)

def compute_area_circle(radius:float):
    return math.pi * (radius ** 2)

def request_square():
    square_side = request_positive_float("Please enter the length of a side of the square: ", 0)
    print(f"The area of the square with a length of {square_side} is {compute_area_square(square_side):.2f}")

def request_rectangle():
    rectangle_length = request_positive_float("Please enter the length of a rectangle: ", 0)
    rectangle_width = request_positive_float("Please enter the width of a rectangle: ", 0)
    print(f"The area of the rectangle with a length of {rectangle_length} and width of {rectangle_width} is {compute_area_rectangle(rectangle_length, rectangle_width):.2f}")

def request_circle():
    circle_radius = request_positive_float("Please enter the radius of a circle: ", 0)
    print(f"The area of the circle with a radius of {circle_radius} is {compute_area_circle(circle_radius):.2f}")

def compute_area(shape:str, dimension:float):
    #match shape:
    #    case "square":
    #        pass
    #    case "circle":
    #        pass
    if shape == "square":
        return compute_area_square(dimension)
    elif shape == "circle":
        return compute_area_circle(dimension)
    else:
        raise Exception("unknown shape")

def calculate_area():
    reply = ""
    while reply != "quit":
        try:
            reply = input("\nWhat shape do you want to calculate (quit to exit): ").lower()
            match reply:
                case "square":
                    request_square()
                case "rectangle":
                    request_rectangle()
                case "circle":
                    request_circle()
                case _:
                    if reply != "quit": print(f"I do not recognize a shape of {reply}.")
        except KeyboardInterrupt:
            reply = "quit"

calculate_area()