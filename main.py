'''
    breadth first search:
    Na teoria dos grafos, busca em largura (ou busca em amplitude, também conhecido em inglês por Breadth-First Search - BFS)
    é um algoritmo de busca em grafos utilizado para realizar uma busca ou travessia num grafo e estrutura de dados do tipo árvore.
    Intuitivamente, você começa pelo vértice raiz e explora todos os vértices vizinhos. Então, para cada um desses vértices mais
    próximos, exploramos os seus vértices vizinhos inexplorados e assim por diante, até que ele encontre o alvo da busca.
    Fonte(WIKIPEDIA)

    depth first search:
    Na teoria dos grafos, busca em profundidade (ou busca em profundidade-primeiro, também conhecido em inglês por Depth-First Search - DFS)
    é um algoritmo usado para realizar uma busca ou travessia numa árvore, estrutura de árvore ou grafo. Intuitivamente, o algoritmo começa
    num nó raiz (selecionando algum nó como sendo o raiz, no caso de um grafo) e explora tanto quanto possível cada um dos seus ramos,
    antes de retroceder(backtracking).
    FONTE(WIKIPEDIA)

    Greedy Best First Search:
    O algoritmo de busca melhor-primeiro[1] ou "best-first" usa a função heurística F(n)=h(n) de procura ao nó de destino.
    Esta procura expandir o nó que é mais próximo ao objetivo, implicando numa condução rápida até o nó destino.

    A*:
    Algoritmo A* (Lê-se: A-estrela) é um algoritmo para Busca de Caminho. Ele busca o caminho em um grafo de um vértice inicial até um
    vértice final. Ele é a combinação de aproximações heurísticas como do algoritmo Breadth First Search (Busca em Largura) e da formalidade
    do Algoritmo de Dijkstra.

    Código de Gustavo Yoshimi Yamashita.
    Use livremente, mas não esqueça de me mencionar :)
    O código pode ser melhorado, por favor, caso tenha alguma sugestão me envie uma mensagem por uma das redes sociais abaixo.

    LinkedIn: https://www.linkedin.com/in/gustavo-yamashita/
    github: https://github.com/GustavoYoshimiYamashita
    Youtube: https://www.youtube.com/c/RobotizandoCanal

'''

import pygame


class Labirinto():

    def __init__(self, linha, coluna, formato, parentes, fronteira, algoritmo, preencher):
        self.linha = linha
        self.coluna = coluna
        self.formato = formato
        self.parentes = parentes
        self.fronteira = fronteira
        self.algoritmo = algoritmo
        self.preencher = preencher

    # Atualizando o print(labirinto) para imprimir o labirinto 2x2 ao invés do enderço de memória do objeto
    def __str__(self):
        tamanho_coluna = len(self.formato)
        for x in range(0, tamanho_coluna):
            for y in range(0, tamanho_coluna):
                if (x == self.linha and y == self.coluna):
                    print("() ", end="")
                else:
                    print(str(self.formato[x][y]) + " ", end="")
            print("")
        return ""

    # O agente representa o personagem dentro do labirinto que irá se movimentar,
    # esse método sempre inicia o agente no lado esquerdo inferior do labirinto
    # independente do tamanho do labirinto em si
    def inicio_agente(self):
        # tamanho do lado do labirinto, assumindo que é sempre um quadrado equilátero
        tamanho_coluna = len(self.formato)
        return tamanho_coluna - 2

    def get_linha(self):
        return self.linha

    def get_coluna(self):
        return self.coluna

    def set_linha(self, nova_linha):
        self.linha = nova_linha

    def set_linha(self, nova_coluna):
        self.linha = nova_coluna

    def mover_agente(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    # Verifica se existe parede no norte do agente
    def norte_livre(self):
        if not self.formato[self.linha - 1][self.coluna] != pd:
            return False
        else:
            return True

    # Verifica se existe parede no sul do agente
    def sul_livre(self):
        if not self.formato[self.linha + 1][self.coluna] != pd:
            return False
        else:
            return True

    # Verifica se existe parede no leste do agente
    def leste_livre(self):
        if not self.formato[self.linha][self.coluna + 1] != pd:
            return False
        else:
            return True

    # Verifica se existe parede no oeste do agente
    def oeste_livre(self):
        if not self.formato[self.linha][self.coluna - 1] != pd:
            return False
        else:
            return True

    '''
     Basicamente os parentes representam céluas no qual o agente já se movimentou.
     Toda célula nova é armazenada dento de uma lista. O motivo disso é para
     verificar se aquela célula do labirinto já foi explorada pelo agente ou não.
     Isso permite por exemplo evitar que o agente entre em um loop de ficar se 
     movendo em células que já foram visitadas.
    '''

    def get_parentes(self):
        return self.parentes

    # Verifica se a célula já está dentro da lista parentes
    def verifica_parentes(self, x, y):
        try:
            return parentes.index((x, y)) != -1
        except:
            return False

    def adicionar_parentes(self, x, y):
        if self.verifica_parentes(x, y):
            pass
        else:
            self.parentes.append((x, y))

    def imprimir_parentes(self):
        print(self.parentes)

    '''
    A fronteira é basicamente uma lista com todas células inexploradas pelo agente,
    cada célula não verificada é armazenada na memória para posteriormente ser explorada.
    '''

    def get_fronteira(self, indicex, indicey):
        return self.fronteira[indicex][indicey]

    def verifica_fronteira(self, x, y):
        try:
            return fronteira.index((x, y)) != -1
        except:
            return False

    def adicionar_fronteira(self, x, y):
        if self.verifica_fronteira(x, y) or self.verifica_parentes(x, y):
            pass
        else:
            self.fronteira.append((x, y))

    def remover_fronteira(self, x, y):
        self.fronteira.remove((x, y))

    def reseta_fronteira(self):
        self.fronteira = []

    # p(0,0) p(2,3)
    # p1(x1, y1) e p2(x2, y2), distancia igual a |(x2-x1)| + |(y2-y1)|
    def distancia_manhattan(self, x1, y1, x2, y2):
        distancia = abs((x2 - x1)) + abs((y2 - y1))
        return distancia

    def menor_valor(self, lst):
        i = float("inf")
        for nr in lst:
            for x in range(len(lst)):
                if nr < i:
                    i = nr
        return i

    def posicao_menor_valor(self, lst, valor):
        try:
            return lst.index(valor)
        except:
            return False

    def valor_com_passos(self, x, y, passo):
        return self.formato[x][y] + passo


# Caminho livre
cl = 10
# Objetivo final
fi = -2
# Parede
pd = -1

# Exemplo de labirinto 1
labirinto1 = [[pd, pd, pd, pd, pd, pd],
              [pd, cl, cl, cl, cl, pd],
              [pd, cl, pd, pd, cl, pd],
              [pd, cl, cl, cl, cl, pd],
              [pd, cl, pd, pd, fi, pd],
              [pd, pd, pd, pd, pd, pd]]

# Mude aqui pra escolher o algoritmo que deseja testar

'''
Opcoes disponíveis: dfs -> Depth First Search        | 
                    bfs -> Breadth First Search      | 
                    gbfs -> Greedy Best First Search | 
                    a* -> A*                         |

'''
algoritmo = "gbfs"

# Exemplo de labirinto 2
labirinto2 = [[pd, pd, pd, pd, pd, pd, pd, pd, pd, pd, pd, pd],
              [pd, pd, cl, cl, cl, cl, cl, cl, cl, cl, fi, pd],
              [pd, pd, cl, pd, pd, pd, pd, cl, pd, pd, cl, pd],
              [pd, pd, cl, cl, cl, cl, cl, cl, cl, cl, cl, pd],
              [pd, pd, cl, pd, pd, cl, pd, pd, pd, pd, cl, pd],
              [pd, pd, cl, cl, cl, cl, cl, cl, cl, pd, cl, pd],
              [pd, pd, pd, cl, pd, pd, pd, pd, cl, cl, cl, pd],
              [pd, cl, cl, cl, cl, cl, cl, cl, cl, pd, cl, pd],
              [pd, cl, pd, cl, pd, cl, pd, cl, pd, pd, cl, pd],
              [pd, cl, pd, cl, pd, cl, pd, pd, pd, pd, cl, pd],
              [pd, cl, pd, cl, pd, cl, cl, cl, cl, cl, cl, pd],
              [pd, pd, pd, pd, pd, pd, pd, pd, pd, pd, pd, pd]]

parentes = []

fronteira = []

# True para preencher com cor azul por onde o agente já se movimentou e False para não
preencher = True

# Criando objeti do tipo labirinto, observação: o 0, 1 utilizado no começo é a posição inicial do agente,
# você pode passar qualquer valor, pois depois isso é corrigido.
labirinto = Labirinto(0, 1, labirinto2, parentes, fronteira, algoritmo, preencher)
# Corrigindo início do agente, você pode alterar por aqui também
labirinto.mover_agente(labirinto.inicio_agente(), 1)

# Booleano para o while do labirinto
jogo = True

# Inicializando tela no pygame
tamanho_coluna = len(labirinto.formato)
vertical = 50 * tamanho_coluna
horizontal = 50 * tamanho_coluna
surface = pygame.display.set_mode((horizontal, vertical))
tamanho_quadrado_coluna = int(horizontal / tamanho_coluna)
tamanho_quadrado_linha = int(vertical / tamanho_coluna)
print(tamanho_quadrado_linha)
contador = 0

# Inicializando cor
red = (255, 0, 0)
green = (0, 255, 0)
blue = (100, 200, 255)
black = (0, 0, 0)

# Desenhando labirinto
for x in range(0, tamanho_coluna):
    for y in range(0, tamanho_coluna):
        if (labirinto.formato[x][y]) == -1:
            pygame.draw.rect(surface, red, pygame.Rect(y * 50, x * 50, 50, 50))
        if (labirinto.formato[x][y] == -2):
            pygame.draw.rect(surface, green, pygame.Rect(y * 50, x * 50, 50, 50))
        pygame.draw.rect(surface, red, pygame.Rect(y * 50, x * 50, 50, 50), 1)
        pygame.display.flip()
        contador += 50
pygame.draw.rect(surface, blue, pygame.Rect(labirinto.get_coluna() * 50, labirinto.get_linha() * 50, 50, 50))

print("INICIANDO O LABIRINTO\n")
print(labirinto)
print("/////////////////////\n")

# Quantidade de passos dado pelo agente
passos = 0

while jogo:

    # Inicializando pygame
    pygame.init()

    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            exit()

    for x in range(tamanho_coluna):
        for y in range(tamanho_coluna):
            if labirinto.formato[x][y] == cl:
                labirinto.formato[x][y] = labirinto.distancia_manhattan(x, y, 1, 10)
            else:
                pass

    # Se o agente ainda não encontrou o objetivo, então:
    if not (labirinto.formato[labirinto.get_linha()][labirinto.get_coluna()] == fi):
        # Se o norte estiver livre e não for uma célula já visitada, faça:
        if labirinto.norte_livre() and not labirinto.verifica_parentes(labirinto.get_linha() - 1,
                                                                       labirinto.get_coluna()):
            labirinto.adicionar_fronteira(labirinto.get_linha() - 1, labirinto.get_coluna())
            labirinto.adicionar_parentes(labirinto.get_linha(), labirinto.get_coluna())

        if labirinto.sul_livre() and not labirinto.verifica_parentes(labirinto.get_linha() + 1, labirinto.get_coluna()):
            # Se o sul estiver livre e não for uma célula já visitada, faça:
            labirinto.adicionar_fronteira(labirinto.get_linha() + 1, labirinto.get_coluna())
            labirinto.adicionar_parentes(labirinto.get_linha(), labirinto.get_coluna())

        if labirinto.leste_livre() and not labirinto.verifica_parentes(labirinto.get_linha(),
                                                                       labirinto.get_coluna() + 1):
            # Se o leste estiver livre e não for uma célula já visitada, faça:
            labirinto.adicionar_fronteira(labirinto.get_linha(), labirinto.get_coluna() + 1)
            labirinto.adicionar_parentes(labirinto.get_linha(), labirinto.get_coluna())

        if labirinto.oeste_livre() and not labirinto.verifica_parentes(labirinto.get_linha(),
                                                                       labirinto.get_coluna() - 1):
            # Se o oeste estiver livre e não for uma célula já visitada, faça:
            labirinto.adicionar_fronteira(labirinto.get_linha(), labirinto.get_coluna() - 1)
            labirinto.adicionar_parentes(labirinto.get_linha(), labirinto.get_coluna())

        valor = []
        valor_com_passos = []

        for x in range(len(labirinto.fronteira)):
            valor.append(labirinto.formato[labirinto.fronteira[x][0]][labirinto.fronteira[x][1]])
            valor_com_passos.append(
                labirinto.valor_com_passos(labirinto.fronteira[x][0], labirinto.fronteira[x][1], passos))

        menor_valor = labirinto.menor_valor(valor)
        posicao_menor_valor = labirinto.posicao_menor_valor(valor, menor_valor)
        menor_valor_passos = labirinto.menor_valor(valor_com_passos)
        posicao_menor_valor_passos = labirinto.posicao_menor_valor(valor_com_passos, menor_valor_passos)

        print("fronteira: ", fronteira)
        print("parentes: ", parentes)
        print("passo atual: ", passos)
        print("valor: ", valor)
        print("menor valor: ", menor_valor)
        print("posicao menor valor: ", posicao_menor_valor)
        print("valor com passos: ", valor_com_passos)
        print("menor valor com passos: ", menor_valor_passos)
        print("posicao menor valor e passos: ", posicao_menor_valor_passos)
        print(labirinto)

        if labirinto.algoritmo == "bfs":
            # Movendo o agente para a nova célula
            labirinto.mover_agente(labirinto.get_fronteira(0, 0), labirinto.get_fronteira(0, 1))
            passos += 1
            # Removendo a primeira célula da fronteira
            labirinto.remover_fronteira(labirinto.get_fronteira(0, 0), labirinto.get_fronteira(0, 1))
        elif labirinto.algoritmo == "dfs":
            # Movendo o agente para a nova célula
            labirinto.mover_agente(labirinto.get_fronteira(-1, 0), labirinto.get_fronteira(-1, 1))
            passos += 1
            # Removendo a última célula da fronteira
            labirinto.fronteira.pop()
        elif labirinto.algoritmo == "gbfs":
            # Movendo o agente para a nova célula
            labirinto.mover_agente(labirinto.get_fronteira(posicao_menor_valor, 0),
                                   labirinto.get_fronteira(posicao_menor_valor, 1))
            passos += 1
            # Removendo todas as células da fronteira
            labirinto.reseta_fronteira()
        elif labirinto.algoritmo == "a*":
            # Movendo o agente para a nova célula
            labirinto.mover_agente(labirinto.get_fronteira(posicao_menor_valor_passos, 0),
                                   labirinto.get_fronteira(posicao_menor_valor_passos, 1))
            passos += 1
            # Removendo a célula com o menor valor
            labirinto.remover_fronteira(labirinto.get_fronteira(posicao_menor_valor_passos, 0),
                                        labirinto.get_fronteira(posicao_menor_valor_passos, 1))
        else:
            raise ValueError("O algoritmo selecionado não está cadastrado!")

        # Desenhando o agente
        pygame.draw.rect(surface, blue, pygame.Rect(labirinto.get_coluna() * 50, labirinto.get_linha() * 50, 50, 50))
        # Atualizando a tela do pygame
        pygame.display.flip()

        # Esse 'for in range' faz o papel de um delay(), justamente para deixar lente o programa, facilitando a visualização
        # do agente se movimentando pelo labirinto, essa parte pode ser retirada se quiser.
        for i in range(0, 10000000):
            pass

        if labirinto.preencher:
            pygame.draw.rect(surface, blue,
                             pygame.Rect(labirinto.get_coluna() * 50, labirinto.get_linha() * 50, 50, 50))
        else:
            pygame.draw.rect(surface, black,
                             pygame.Rect(labirinto.get_coluna() * 50, labirinto.get_linha() * 50, 50, 50))
            pygame.draw.rect(surface, red,
                             pygame.Rect(labirinto.get_coluna() * 50, labirinto.get_linha() * 50, 50, 50, ), 1)

    # Finaliza o jogo
    else:
        jogo = False

print("Quantidade de passos realizados: ", passos)
