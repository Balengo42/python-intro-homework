def weather_fahrenheit(celsius_temp):
    f_temp= (celsius_temp * 9/5) +32
    print (f"{celsius_temp}°C = {f_temp:.1f}°F")



def weather_celsius(fahrenheit_temp):
    c_temp = (fahrenheit_temp -32) * 5/9
    print (f"{fahrenheit_temp}°F = {c_temp:.1f}°C")

weather_fahrenheit(0)
weather_fahrenheit(100)
weather_celsius(72)