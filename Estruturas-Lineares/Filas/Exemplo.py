from collections import deque

##Filas

# Criando uma fila

fila = deque()

fila.append(1)  # Adiciona no final
fila.append(2)
fila.append(3)

# Remoção
print(fila.popleft())  # Remove e retorna o primeiro elemento              #Saída: 1

# Verificação de Vazio
print(len(fila) == 0)  # Verifica se a fila está vazia                     #Saída: False
                                                                                      

