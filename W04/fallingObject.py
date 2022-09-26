#import input
import math

class Error(Exception):
    """Raised when the item is unknown"""
    pass

class MissingDimension(Error):
    """Raised when the item is unknown"""
    pass

class UndefinedShape(Error):
    """Raised when the item is unknown"""
    pass

class UndefinedOrientation(Error):
    """Raised when the item is unknown"""
    pass

def triangle_area(base, height):
    try:
        return (1 / 2) * (float(base) * float(height))
    except ValueError:
        try:
            float(base)
            raise MissingDimension(f"Missing the height dimension for the triangle!", "triangle", "height")
        except ValueError:
            raise MissingDimension(f"Missing the base dimension for the triangle!", "triangle", "base")

#Cross sectional area of the projectile shape
def A(shape, dimensions = {}):
    if shape.lower() in geometry_constants["shape"].keys():
        return geometry_constants["shape"][shape.lower()]["crossSectionalArea"](dimensions)
    else:
        raise UndefinedShape(f"Shape type {shape} is undefined in the constants dictionary!")

def request_fluid_density(type = "air"):
    try:
        return physics.fluid_density(type)
    except physics.UndefinedFluidType:
        if type != "":
            return input.request_valid_float(f"What is the density of the fluid {type}? ", "A density must be positive!", -0.1, 0.0, "")
        else:
            return input.request_valid_float("What is the density of the fluid (in kg/m^3, 1.3 for air, 1000 for water)? ", "A density must be positive!", -0.1, 0.0, "")

def request_C(shape, shape_orientation = "default"):
    try:
        return physics.C(shape, shape_orientation)
    except UndefinedOrientation:
        if shape != "":
            return input.request_valid_float(f"What is the drag force constant for a {shape} at {shape_orientation} orientation? ", "A drag force constant must be positive!", -0.1, 0.0, "")
        else:
            return input.request_valid_float(f"What is the drag force constant at {shape_orientation} orientation (0.5 for sphere, 1.1 for cylinder)? ", "A drag force constant must be positive!", -0.1, 0.0, "")
    except UndefinedShape:
        if shape != "":
            return input.request_valid_float(f"What is the drag force constant for a {shape}? ", "A drag force constant must be positive!", -0.1, 0.0, "")
        else:
            return input.request_valid_float("What is the drag force constant (0.5 for sphere, 1.1 for cylinder)? ", "A drag force constant must be positive!", -0.1, 0.0, "")

def request_A(shape, dimensions = {}):
    try:
        return A(shape, dimensions)
    except MissingDimension as err:
        msg, shape, dimension = err.args
        dimensions[dimension] = input.request_valid_float(f"What is the {dimension} (in m) of the {shape}? ", f"A {dimension} must be positive!", -0.1, 0.0, "")
        return request_A(shape, dimensions)
    except UndefinedShape:
        if shape != "":
            return input.request_valid_float(f"What is the cross sectional area (in m^2) of the {shape}? ", "A cross sectional area must be positive!", -0.1, 0.0, "")
        else:
            return input.request_valid_float("What is cross sectional area (in m^2) of the projectile shape? ", "A cross sectional area must be positive!", -0.1, 0.0, "")

def request_c(type_of_fluid, shape, shape_dimensions = {}, shape_orientation = "default"):
    return 1 / 2 * request_fluid_density(type_of_fluid) * request_A(shape, shape_dimensions) * request_C(shape, shape_orientation)

def request_v(t, m, shape, shape_dimensions = {}, shape_orientation = "default", type_of_fluid = "air", location = "earth"):
    _c = request_c(type_of_fluid, shape, shape_dimensions, shape_orientation)
    _g = physics.g(location)
    return math.sqrt(m * _g / _c) * (1 - math.exp(-1 * math.sqrt(m * _g * _c) / m * t))

tst_fluid = "air"
tst_shape = "cylinder"
tst_dimensions = {"l":2, "w":3}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
tst_time = 2
tst_mass = 10
print(f"c = {x:.4f}")
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "sphere"
tst_dimensions = {"r":2}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_fluid = "air"
tst_shape = "cylinder"
tst_dimensions = {"l":2, "w":3}
x = request_c(tst_fluid, tst_shape, tst_dimensions, "")
tst_time = 2
tst_mass = 10
print(f"c = {x:.4f}")
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, "undefined", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "sphere"
tst_dimensions = {"r":2}
x = request_c(tst_fluid, tst_shape, tst_dimensions, "")
print(f"c = {x:.4f}")
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, "undefined", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "cylinder"
tst_dimensions = {"l":2}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {"l":2}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "cylinder"
tst_dimensions = {"w":2}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {"w":2}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "cylinder"
tst_dimensions = {}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = "sphere"
tst_dimensions = {}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_shape = ""
tst_dimensions = {}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

tst_fluid = ""
tst_dimensions = {}
x = request_c(tst_fluid, tst_shape, tst_dimensions)
print(f"c = {x:.4f}")
tst_dimensions = {}
y = request_v(tst_time, tst_mass, tst_shape, tst_dimensions, shape_orientation = "default", type_of_fluid = tst_fluid)
print(f"v = {y:.4f}")

"""
Welcome to the velocity calculator. Please enter the following:

Mass (in kg): 5
Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
Time (in seconds): 10
X Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
X Cross sectional area (in m^2): 0.01
X Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5

The inner value of c is: 0.003
The velocity after 10.0 seconds is: 67.512 m/s
"""
"""
Try determining the velocity for a few different objects that you know. For example, you might try a bowling ball, a loaf of bread, and a skydiver.

Hints: You can find the cross sectional area of a bowling ball by using its radius and calculating the area (pi*r^2). You can approximate the drag constant
     for a loaf of bread by thinking about it as a cylinder. Do your best to estimate the cross sectional area of a skydiver. Are they falling head first or
     lying flat? You can look up values for the drag constant of a skydiver.

Compare the difference in velocities for two different gravity values (Earth and Jupiter), assuming everything else is the same.

For one of the objects you picked, see if you can determine how long it takes to reach "terminal velocity" which is the fastest that the object will travel,
    by entering different values for "t" to see where it stops increasing.

Check your guess for the terminal velocity by using Python to compute the terminal velocity, which can be found by determining the velocity v(t) as time t
    approaches infinity. This results in the equation for terminal velocity:

v_terminal = sqrt(mg/c)
"""