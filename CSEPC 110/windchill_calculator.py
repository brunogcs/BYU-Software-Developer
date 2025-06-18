while True:
    try:
        temperature = float(input("What is the temperature? "))  # Tenta converter a entrada para float
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

while True:
    type_temperature = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if type_temperature in ['F', 'C']:
        break  # Sai do loop se a entrada for válida
    else:
        print("Entrada inválida. Por favor, digite 'F' para Fahrenheit ou 'C' para Celsius.")

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
    return wind_chill

if type_temperature.upper() == "C":
    fahrenheit = convert_temperature(temperature)
elif type_temperature.upper() == "F":
    fahrenheit = temperature

wind_speed = 5

while wind_speed <= 60:
    wind_chill = calculate_wind_chill(fahrenheit, wind_speed)
    print(f"At temperature {fahrenheit}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
    wind_speed += 5