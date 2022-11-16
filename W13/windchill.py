#! python
import math
#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

wind_mph_list = [*range(5, 65, 5)]
temp_f_list = [*range(40, -50, -5)]

def toMPH(kph: float):
    mph = kph / 1.609
    return mph

def toKPH(mph: float):
    kph = mph * 1.609
    return kph

def toFahrenheit(celsius: float):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fromFahrenheit(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def wind_chill(temperature:float, wind_speed:float, isFahrenheit=True):
    if isFahrenheit:  # use abs to get the magnitude of the velocity without direction of positive or negative
        return 35.74 + (0.6215 * temperature) - (35.75 * (math.fabs(wind_speed) ** 0.16)) + (0.4275 * temperature * (math.fabs(wind_speed) ** 0.16))
    else:  #if you pass metric you must be all in metric, so KPH with ºC
        return fromFahrenheit(wind_chill(toFahrenheit(temperature), toMPH(math.fabs(wind_speed))))

def main():
    temperature = float(input("What is the Temperature? "))
    f_or_c = input("Fahrenheit or Celsius (F/C)? ").lower()
    e_or_m = input("Display in English or Metric (E/M)? ").lower()
    if f_or_c == "c": temperature = toFahrenheit(temperature)
    for mph in range(5, 65, 5):
        if e_or_m == "m":            
            print(f"At temperature {fromFahrenheit(temperature):.1f}C, and wind speed {toKPH(mph):.0f} kph, the windchill is: {wind_chill(fromFahrenheit(temperature), toKPH(mph), False):.2f}C")
        else:
            print(f"At temperature {temperature:.1f}F, and wind speed {mph:.0f} mph, the windchill is: {wind_chill(temperature, mph):.2f}F")

main()