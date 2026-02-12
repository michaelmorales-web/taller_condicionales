# Programa para calcular el costo de una llamada

# input
print("----------------------------------")
print("-----------Costo llamada----------")
print("----------------------------------")
min = int(input("Digite la duracion de la llamda en minutos: "))

# procesing
if (min <= 3):
    costo_llamada = 500
else:
    costo_llamada = 500 + (min - 3)*100

# output
print("--------------------------------------")
print("-------------Resultado----------------")
print("--------------------------------------")
print("Duracion de la llamada: " + str(min) + "minutos")
print("Costo de la llamada: " + str(costo_llamada))