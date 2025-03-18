##Exemplo Práticos de Aplicação

#Indexação em Bancos de Dados

class Arvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

raiz = Arvore(10)
raiz.esquerda = Arvore(5)
raiz.direita = Arvore(15)

print("Raiz:", raiz.chave)                                   #Saída: Raiz: 10
print("Esquerda da Raiz:", raiz.esquerda.chave)              #Saída: Esquerda da Raiz: 5
print("Direita da Raiz:", raiz.direita.chave)                #Saída: Direita da Raiz: 15
