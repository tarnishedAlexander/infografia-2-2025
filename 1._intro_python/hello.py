edad = 19
estatura = 1.9
nombre = "juan"
print("hola a todos, mi nombre es " + nombre + ", tengo " + str(edad) + " y mido " + str(estatura) + "m.")
print(f"hola a todos, mi nombre es {nombre}, tengo {edad} y mido {estatura}m.")

try:
    edad2 = float(input("ingrese edad: "))
    print(edad2, type(edad2))
except ValueError:
    print("ingrese un numero decimal valido")