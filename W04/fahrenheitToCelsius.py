"""
    filname:  fahrenheitToCelsius.py
    inputs:  a floating point decimal to represent the temperature in Fahrenheit from the user to the question "What is the temperature in Fahrenheit? "
    process:
        temperature_celsius = (temperature_fahrenheit - 32) * (5 / 9)
    output:  the results of the math calculations for the input responses as below:
        The temperature in Celsius is {temperature_celsius} degrees.
    additional requirements for output:
        1)  result is to be displayed to 1 point of precision.
    author:  Tracy Mann
    version:  1.0
    date:  9/24/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
    
"""

temperature_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
temperature_celsius = (temperature_fahrenheit - 32) * (5 / 9)
print(f"The temperature in Celsius is {temperature_celsius:.1f} degrees.")
