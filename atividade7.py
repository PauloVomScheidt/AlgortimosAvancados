class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def contar_nos(cabeca):
    contador = 0
    atual = cabeca
    while atual:
        contador += 1
        atual = atual.proximo
    return contador


# Exemplo
cabeca = No(1)
cabeca.proximo = No(2)
cabeca.proximo.proximo = No(3)

print(contar_nos(cabeca))  # 3
