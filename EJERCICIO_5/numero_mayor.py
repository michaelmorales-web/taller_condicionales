# Programa para comparar tres números enteros y determiar cual es el mayor

# input
print("----------------------------------------")
print("------------Ultimos digitos iguales-------------")
print("----------------------------------------")
n1 = int(input("1. "))
n2 = int(input("2. "))
n3 = int(input("3. "))

# procesing
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            rta = str(n1) + ", " + str(n2) + ", " + str(n3)
        else:
            rta = str(n1) + ", " + str(n3) + ", " + str(n2)
    else:
        rta = str(n2) + ", " + str(n1) + ", " + str(n3)
else:
    if n2 > n3:
        if n1 > n3:
            rta = str(n2) + ", " + str(n1) + ", " + str(n3)
        else:
            rta = str(n2) + ", " + str(n3) + ", " + str(n1)
    else:
        rta = str(n3) + ", " + str(n2) + ", " + str(n1)

# output
print("------------------------------------------")
print("---------------Resultado------------------")
print("------------------------------------------")
print()
print("Sus números, de mayor a menor son: " + rta)

print()
input("(Presione enter para salir)")