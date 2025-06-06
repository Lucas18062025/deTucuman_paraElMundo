temperatura = float(input("ingrese temperatura:"))
escala = input("Es Fahrenheit(f) o es Celsius(C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    Fahrenheit = temperatura * 1.8 + 32
    print(Fahrenheit)
else:
    print ("Escala Incorrecta")