# Programa para verificar si un número es positivo

# input
print("----------------------------------------")
print("------------Número positivo-------------")
print("----------------------------------------")
x = int(input("Digite un número: "))

# procesing
if (x>0):
    rta= "POSITIVO"
else:
    rta= "NEGATIVO O CERO"

# output
print("------------------------------------------")
print("---------------Resultado------------------")
print("------------------------------------------")
print("El número " + str(x) + " es " + rta)
