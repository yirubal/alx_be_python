# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main script
try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if scale == 'C':
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted}°F")
elif scale == 'F':
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted}°C")
else:
    raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
