FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return C


def convert_to_fahrenheit(celsius):
    F = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return F
def main():
    try:
        entered_value = float(input("Enter the temperature to convert: "))
        CorF = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if CorF == "F":
            print(f"{entered_value}°F is {convert_to_celsius(entered_value)}°C")
        elif CorF == "C":
            print(f"{entered_value}°C is {convert_to_fahrenheit(entered_value)}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()