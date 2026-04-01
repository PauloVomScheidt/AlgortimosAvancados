class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def detectar_ciclo(cabeca):
    lento = cabeca
    rapido = cabeca

    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

        if lento == rapido:
            return True

    return False


# Exemplo com ciclo
cabeca = No(1)
cabeca.proximo = No(2)
cabeca.proximo.proximo = No(3)

# criando ciclo
cabeca.proximo.proximo.proximo = cabeca.proximo

print(detectar_ciclo(cabeca))  # True
