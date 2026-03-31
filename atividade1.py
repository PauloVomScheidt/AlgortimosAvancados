def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

valores = [1, 2, 3, 4]
resultado = soma_elementos(valores)
print(resultado)  