numeros = [1,2,3,4,5,6,7,8,9]

# Números impares
impares = filter(lambda num: num % 2 != 0, numeros)

# Al cuadrado
cuadrado = map(lambda num: num**2, numeros)

print(list(impares))
print(list(cuadrado))

