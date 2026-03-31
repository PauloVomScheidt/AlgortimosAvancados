def maior_elemento(lista):
    maior = lista[0]  
    
    for numero in lista:
        if numero > maior:
            maior = numero
    
    return maior

valores = [3, 7, 2, 9, 1]
resultado = maior_elemento(valores)
print(resultado)  