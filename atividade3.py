def inverter_lista(lista):
    invertida = []
    
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    
    return invertida

valores = [1, 2, 3]
resultado = inverter_lista(valores)
print(resultado)  