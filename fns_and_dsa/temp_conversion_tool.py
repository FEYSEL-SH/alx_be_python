FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return C
def convert_to_fahrenheit(celsius):
    F = celsius * (9 / 5) + 32
    return F

enteredValue = int(input("inter your Enter the temperature to convert:"))
if type(enteredValue) == int:
    CorF = str(input("Is this temperature in Celsius or Fahrenheit?").upper())
    if CorF == "F":
        print(f"{enteredValue}°F is {convert_to_celsius(enteredValue)}°C")
    elif CorF == "C":
         print(f"{enteredValue}°C is {convert_to_fahrenheit(enteredValue)}°F")
    else:
        print("insert appropraite symbol")
else:
    print("“Invalid temperature. Please enter a numeric value.")