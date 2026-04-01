class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inverter_lista(cabeca):
    anterior = None
    atual = cabeca

    while atual:
        proximo = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo

    return anterior


# Exemplo
cabeca = No(1)
cabeca.proximo = No(2)
cabeca.proximo.proximo = No(3)

cabeca = inverter_lista(cabeca)

# Impressão
atual = cabeca
while atual:
    print(atual.valor, end=" -> ")
    atual = atual.proximo
print("null")
