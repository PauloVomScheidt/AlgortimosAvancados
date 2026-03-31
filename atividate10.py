class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.topo = -1

    def push(self, valor):
        if self.topo == self.capacidade - 1:
            print("Erro: Pilha cheia (overflow)")
            return
        
        self.topo += 1
        self.dados[self.topo] = valor

    def pop(self):
        if self.topo == -1:
            print("Erro: Pilha vazia (underflow)")
            return None
        
        valor = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return valor

    def peek(self):
        if self.topo == -1:
            print("Pilha vazia")
            return None
        
        return self.dados[self.topo]

    def esta_vazia(self):
        return self.topo == -1

    def __str__(self):
        return str(self.dados[:self.topo + 1])

pilha = Pilha(5)

pilha.push(10)
pilha.push(20)
pilha.push(30)

print("Pilha:", pilha)
print("Topo:", pilha.peek())
print("Removido:", pilha.pop())
print("Pilha após pop:", pilha)
print("Está vazia?", pilha.esta_vazia())