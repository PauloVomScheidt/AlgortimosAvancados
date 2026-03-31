def remover_duplicatas(lista):
    resultado = []
    
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    
    return resultado

valores = [1, 2, 2, 3, 1, 4]
print(remover_duplicatas(valores))  