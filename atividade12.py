def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    
    pilha = []

    while numero > 0:
        resto = numero % 2
        pilha.append(resto)
        numero = numero // 2

    binario = ""
    while pilha:
        binario += str(pilha.pop())

    return binario

print(decimal_para_binario(13))  
print(decimal_para_binario(10))  
print(decimal_para_binario(1))   