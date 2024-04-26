numero = 0
print(numero)

siguiente = 1
print(siguiente)

for _ in range(10):  # Generar 10 números de la secuencia (puedes cambiar este número según sea necesario)
    numero, siguiente = siguiente, numero + siguiente
    print(siguiente)
