def rotacionar_array(arr, k):
    n = len(arr)
    
    k = k % n  
    
    parte_final = arr[-k:]
    parte_inicial = arr[:-k]
    
    return parte_final + parte_inicial

array = [1, 2, 3, 4, 5]
k = 2

resultado = rotacionar_array(array, k)
print(resultado)