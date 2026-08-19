def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print(f"{0}°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"{100}°C = {celsius_to_fahrenheit(100):.1f}°F")
print(f"{72}°F = {fahrenheit_to_celsius(72):.1f}°C")