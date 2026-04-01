class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inserir_inicio(cabeca, valor):
    novo_no = No(valor)
    novo_no.proximo = cabeca
    return novo_no


# Exemplo de uso
cabeca = No(2)
cabeca.proximo = No(3)

cabeca = inserir_inicio(cabeca, 1)

# Impressão
atual = cabeca
while atual:
    print(atual.valor, end=" -> ")
    atual = atual.proximo
print("null")
