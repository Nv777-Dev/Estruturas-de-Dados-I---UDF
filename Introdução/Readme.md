# **Apresentação às Estruturas de Dados**

# **O que caracterizam as estruturas de dados?**

As estruturas de dados são métodos estruturados para guardar e administrar informações em sistemas informáticos, possibilitando operações eficazes como a inserção, pesquisa, eliminação e alteração de dados.  Elas atuam como elementos essenciais na elaboração de algoritmos, maximizando a utilização de recursos como tempo de processamento e memória.  No livro Data Structures and Algorithms in Python (Michael T. Goodrich, Roberto Tamassia e Michael H. Goldwasser), elas são destacadas como instrumentos cruciais para solucionar questões complexas através de métodos sistemáticos e escalonáveis.

# **Importância na Ciência da Computação**
 
Eficácia de Algoritmos: A seleção da estrutura apropriada tem um impacto direto no rendimento. Por exemplo, uma tabela de hash possibilita pesquisas com tempo fixo (0(1)), ao passo que uma lista encadeada pode demandar tempo linear (0(n)).
Gestão de Memória: Estruturas como árvores binárias balanceadas (AVL) minimizam o desperdício de espaço e aprimoram a velocidade de acesso.
Escalabilidade: Soluções para grandes volumes de dados e sistemas em tempo real requerem estruturas como grafos e filas de prioridade para lidar com grandes quantidades de informação.

# **Exemplos de Aplicação no Mundo Real**
## **Tabelas de Hash**
### **Exemplo: Sistemas de Login e Armazenamento de Senhas (Google e Facebook)**
#### (Google): O Google utiliza tabelas de hash em seu sistema de indexação e pesquisa para otimizar a recuperação de informações. Quando você faz uma pesquisa, o sistema usa hashing para armazenar e buscar rapidamente os dados indexados na sua base de dados.

#### (Facebook): No Facebook, as tabelas de hash são usadas para armazenar e verificar as senhas dos usuários de maneira eficiente. Quando você faz login no Facebook, sua senha é processada por um algoritmo de hash antes de ser comparada ao valor armazenado no banco de dados. Isso permite que a plataforma verifique a senha sem precisar armazená-la diretamente, melhorando a segurança.
