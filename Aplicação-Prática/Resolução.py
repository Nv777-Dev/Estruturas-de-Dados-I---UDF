##Resolução ultilizando Fila (Queue)

#Importando a biblioteca (Queue)
import queue

# Criação da fila usando a biblioteca (Queue)
fila = queue.Queue()

# Função para simular a chegada de um cliente 
def chegar_cliente(nome_cliente):
    fila.put(nome_cliente)
    print(f"{nome_cliente} entrou na fila.")

# Função para simular o atendimento de um cliente
def atender_cliente():
    if not fila.empty():
        cliente_atendido = fila.get()
        print(f"{cliente_atendido} foi atendido e saiu da fila.")
    else:
        print("Não há clientes na fila.")

# Chegada de clientes
chegar_cliente("Cliente 1")                      #Saída: Cliente 1 entrou na fila.              
chegar_cliente("Cliente 2")                      #Saída: Cliente 2 entrou na fila.
chegar_cliente("Cliente 3")                      #Saída: Cliente 3 entrou na fila.

# Atendimento aos clientes
atender_cliente()                                #Saída: Cliente 1 foi atendido e saiu da fila.
atender_cliente()                                #Saída: Cliente 2 foi atendido e saiu da fila.
atender_cliente()                                #Saída: Cliente 3 foi atendido e saiu da fila.
atender_cliente()                                #Saída: Não há clientes na fila.

