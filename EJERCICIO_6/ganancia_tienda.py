# Programa para calcular el precio de venta de un producto en una tienda 

# input
print("----------------------------------------")
print("------------Precio de venta-------------")
print("----------------------------------------")
p = int(input("Digite el precio de su producto: "))

# procesing
if p < 3000:
    g = p * 0.15
    c = p + g
else:
    if p > 6000:
        g = p * 0.25
        c = g + p
    else:
        c = p + 500

# output
print("------------------------------------------")
print("---------------Resultado------------------")
print("------------------------------------------")
print("El nuevo precio es: " + str(c))