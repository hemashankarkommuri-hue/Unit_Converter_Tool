def meter_to_km(m):
    return m / 1000

def km_to_meter(km):
    return km * 1000

def gram_to_kg(g):
    return g / 1000

def kg_to_gram(kg):
    return kg * 1000

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("===== UNIT CONVERTER =====")
print("1. Meter to Kilometer")
print("2. Kilometer to Meter")
print("3. Gram to Kilogram")
print("4. Kilogram to Gram")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Result:", meter_to_km(value), "km")
elif choice == 2:
    print("Result:", km_to_meter(value), "m")
elif choice == 3:
    print("Result:", gram_to_kg(value), "kg")
elif choice == 4:
    print("Result:", kg_to_gram(value), "g")
elif choice == 5:
    print("Result:", celsius_to_fahrenheit(value), "°F")
elif choice == 6:
    print("Result:", fahrenheit_to_celsius(value), "°C")
else:
    print("Invalid Choice")