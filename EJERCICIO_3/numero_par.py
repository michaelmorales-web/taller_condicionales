# Programa para verificar si un número es par

# input
print("----------------------------------------")
print("------------Número par/impar-------------")
print("----------------------------------------")
x = int(input("Digite un número: "))

# procesing
mod = x%2
if (mod==0):
    rta= "PAR"
else:
    rta= "IMPAR"

# output
print("------------------------------------------")
print("---------------Resultado------------------")
print("------------------------------------------")
print("El número " + str(x) + " es " + rta)
