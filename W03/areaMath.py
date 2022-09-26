"""
    filname:  areaMath.py
    inputs:  a floating point decimal to represent the length from the user to the question "What is the length of a side of the square? "
    inputs:  a floating point decimal to represent the length from the user to the question "What is the length of the rectangle? "
    inputs:  a floating point decimal to represent the width from the user to the question "What is the width of the rectangle? "
    inputs:  a floating point decimal to represent the radius from the user to the question "What is the radius of the circle? "
    output:  the results of the math calculations for each of the input responses as below:
        The area of the square is:  {square_length ** 2}.
        The area of the rectangle is:  {rectangle_length * rectangle_width}.
        The area of the circle is:  {(circle_radius ** 2) * 3.14}.
    additional requirements for output:
        1)  needs to be able to handle decimal input as well as whole number input.
    author:  Tracy Mann
    version:  1.0
    date:  9/21/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
    version 1.1:
        date:  9/27/2022
            1)  Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module.
            2)  Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius,
                and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.
            3)  For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters.
                Then, display the resulting area in both square centimeters and square meters.
                Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.

            input update:
                inputs:  a floating point decimal to represent the length from the user to the question "What is the length of a side of the square in centimeters? "
                inputs:  a floating point decimal to represent the length from the user to the question "What is the length of the rectangle in centimeters? "
                inputs:  a floating point decimal to represent the width from the user to the question "What is the width of the rectangle in centimeters? "
                inputs:  a floating point decimal to represent the radius from the user to the question "What is the radius of the circle in centimeters? "
                new input:  a floating point decimal to represent the length from the user to the question "What is a length for the common shapes in centimeters? "
            output update:
                The area of the square is:  {square_length ** 2} sq cm or {(square_length/centimeters_in_meter) ** 2} sq m.
                The area of the rectangle is:  {rectangle_length * rectangle_width} sq cm or {(rectangle_length/centimeters_in_meter) * (rectangle_width/centimeters_in_meter)} sq m.
                The area of the circle is:  {(circle_radius ** 2) * math.pi} sq cm or {((circle_radius/centimeters_in_meter) ** 2) * math.pi} sq m.
                The area of the common square is:  {length ** 2} sq cm or {(length/centimeters_in_meter) ** 2} sq m.
                The area of the common circle is:  {(length ** 2) * math.pi} sq cm or {((length/centimeters_in_meter) ** 2) * math.pi} sq m.
                The area of the common cube is:  {length ** 3} cu cm or {(length/centimeters_in_meter) ** 3} cu m.
            ref:  https://www.w3schools.com/python/ref_math_pi.asp for python pi use
    
"""

#added in version 1.1
import math
#added in version 1.1
centimeters_in_meter = 100
#changed in version 1.1
#square_length = float(input("What is the length of a side of the square? "))
#print(f"The area of the square is:  {square_length ** 2}.")
square_length = float(input("What is the length of a side of the square in centimeters? "))
print(f"The area of the square is:  {square_length ** 2} sq cm. or {(square_length/centimeters_in_meter) ** 2} sq m.")
#changed in version 1.1
#rectangle_length = float(input("What is the length of the rectangle? "))
#rectangle_width = float(input("What is the width of the rectangle? "))
#print(f"The area of the rectangle is:  {rectangle_length * rectangle_width}.")
rectangle_length = float(input("What is the length of the rectangle in centimeters? "))
rectangle_width = float(input("What is the width of the rectangle in centimeters? "))
print(f"The area of the rectangle is:  {rectangle_length * rectangle_width} sq cm or {(rectangle_length/centimeters_in_meter) * (rectangle_width/centimeters_in_meter)} sq m.")
#changed in version 1.1
#circle_radius = float(input("What is the radius of the circle? "))
#print(f"The area of the circle is:  {(circle_radius ** 2) * 3.14}.")
circle_radius = float(input("What is the radius of the circle in centimeters? "))
print(f"The area of the circle is:  {(circle_radius ** 2) * math.pi} sq cm or {((circle_radius/centimeters_in_meter) ** 2) * math.pi} sq m.")
#added in version 1.1
length = float(input("What is a length for the common shapes in centimeters? "))
print(f"The area of the common square is:  {length ** 2} sq cm or {(length/centimeters_in_meter) ** 2} sq m.")
print(f"The area of the common circle is:  {(length ** 2) * math.pi} sq cm or {((length/centimeters_in_meter) ** 2) * math.pi} sq m.")
print(f"The area of the common cube is:  {length ** 3} cu cm or {(length/centimeters_in_meter) ** 3} cu m.")
