import math


def Convert(temp_in, temp_degree):
    celsius = 0
    fahrenheit = 0
    if temp_in.upper() == 'C':  # Celsius
        fahrenheit = round(float(temp_degree) * 9/5 + 32, 3)
        return f"Temperature in Fahrenheit is: {fahrenheit} °F"
    elif temp_in.upper() == 'F':  # Fahrenheit
        celsius = round((float(temp_degree) - 32) * 5/9, 3)
        return f"Temperature in Celsius is: {celsius} °C"


result = Convert('F', 25)
print(result)
