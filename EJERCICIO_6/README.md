# EJERCICIO_6: ganancia_tienda
- Programa en Python para calcular en que precio se debe vender un producto para tener un ganancia de acuerdo con el precio del producto

## Análisis

### Variables de entrada
- $p$ (Precio)

### Proceso
- $p > 3000$
- true:
   - $G = p * 0.15$
   - $c = p + G$
- False:
   - $p > 6000$
   - True:
      - $G = p * 0.25$
      - $c = p + G$
   - False:
      - $c = p + 500$

### Variable de salida
- c

## Diseño
![diagram de flujo](diagrama.png)

## Construcción
- codigo implementado en el archivo ganancia_tienda.py
