def validar_parenteses(expressao):
    pilha = []

    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expressao:
        if char in '({[':
            pilha.append(char)

        elif char in ')}]':
            if not pilha:
                return False  
            
            topo = pilha.pop()

            if topo != pares[char]:
                return False  

    return len(pilha) == 0

print(validar_parenteses("({[]})"))  
print(validar_parenteses("([)]"))    
print(validar_parenteses("((()))"))  
print(validar_parenteses("((())"))   