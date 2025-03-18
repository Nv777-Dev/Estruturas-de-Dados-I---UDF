# ⚜️ **Gerenciamento de Fila em um Caixa de Supermercado**

### 🟢 **Descrição do Problema:** Imagine um supermercado onde há várias caixas de pagamento. Em cada caixa, os clientes chegam, fazem suas compras e, em seguida, pagam. O supermercado quer garantir que os clientes sejam atendidos na ordem em que chegaram, ou seja, o primeiro a chegar será o primeiro a ser atendido. Para isso, precisamos de uma estrutura de dados que permita adicionar clientes à fila e retirar o cliente que está sendo atendido de forma eficiente.

## ⚜️ **Estrutura de Dados Escolhida**

### 🟢 **Fila (Queue):** Uma fila é a estrutura de dados mais adequada para resolver esse problema, pois ela segue o princípio FIFO (First In, First Out), que é exatamente o que precisamos para gerenciar a ordem de atendimento dos clientes no caixa.

## ⚜️ **Como a Fila (Queue) Pode Ajudar Nesse Problema**

### 🟢 **Enfileirar:** Cada vez que um cliente chega ao caixa, ele é adicionado ao final da fila. Isso é feito com a operação de enfileiramento.

### 🟢 **Desenfileirar:** O cliente que está no início da fila (ou seja, o primeiro a chegar) é o próximo a ser atendido e, portanto, é removido da fila. Essa operação é chamada de desenfileiramento.

## ⚜️ **Passos para Resolução**

### 🟢 **Inicialização da Fila:** Criamos uma fila vazia para começar.

### 🟢 **Chegada de Clientes:** Quando um cliente chega, ele é colocado no final da fila, A fila cresce à medida que novos clientes chegam.

### 🟢 **Atendimento dos Clientes:**  O cliente na frente da fila (primeiro a chegar) é atendido e removido da fila, O cliente na frente da fila (primeiro a chegar) é atendido e removido da fila.

## ⚜️ **Exemplo de Funcionamento**

#### ◼️ **Fila inicial(vazia): []

#### ◼️ **Cliente 1 chega e entra na fila: [Cliente 1]

#### ◼️ **Cliente 2 chega e entra na fila: [Cliente 1, Cliente 2]

#### ◼️ **Cliente 3 chega e entra na fila: [Cliente 1, Cliente 2, Cliente 3]

#### ◼️ **Cliente 1 é atendido e sai da fila: [Cliente 2, Cliente 3]

#### ◼️ **Cliente 2 é atendido e sai da fila: [Cleinte 3]

#### ◼️ **Cliente 3 é atendido e sai da fila: []

# ⚜️ **Conclusão**
## 🟢 **A fila é uma excelente escolha para esse problema, pois sua natureza FIFO é ideal para modelar processos que requerem ordem de chegada, como no caso de atendimento a clientes em caixas de supermercado. Ela garante que os clientes sejam atendidos de forma justa e eficiente.**

# ⚜️ **Referências**

#### Livro: Data Structures & Algorithms in Python
#### Autores: Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
