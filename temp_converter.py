def convert_temperature(value, unit):
    if unit == "C":
        f = (value * 9/5) + 32
        k = value + 273.15
        print(f"\nFahrenheit: {f:.2f} °F")
        print(f"Kelvin: {k:.2f} K")

    elif unit == "F":
        c = (value - 32) * 5/9
        k = c + 273.15
        print(f"\nCelsius: {c:.2f} °C")
        print(f"Kelvin: {k:.2f} K")

    elif unit == "K":
        c = value - 273.15
        f = (c * 9/5) + 32
        print(f"\nCelsius: {c:.2f} °C")
        print(f"Fahrenheit: {f:.2f} °F")

    else:
        print("❌ Invalid unit! Use C, F, or K")


print("=== Temperature Converter ===")

try:
    value = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F/K): ").upper()

    convert_temperature(value, unit)

except:
    print("❌ Please enter a valid number!")