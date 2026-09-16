from P06_3516_pilha_encadeada import PilhaEncadeada 
    
class FilaEncadeada:

    #inicia a fila encadeada com duas pilhas, uma de entrada (onde os itens são enfileirados) e outra de saída (onde eles são colocados de trás pra frente, e de onde irão sair)
    def __init__(self):
        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

#insere o elemento que chegou no final da fila, ou seja, na pilha de entrada.
#complexidade de tempo O(1).
    def enfileirar(self, value):
        self.pilha_entrada.push(value)

#se as duas pilhas estiverem vazias, gera o erro "Fila Vazia". Caso a pilha de saída estiver vazia e a de entrada não, passa todos os itens da entrada pra saida e tira o elemento topo da lista de saida. Caso a lista de saida não esteja vazia, remove e retorna o elemento do topo.
#complexidade de tempo O(1) amortizado.
    def desenfileirar(self):
        if self.pilha_saida.esta_vazia():
            if self.pilha_entrada.esta_vazia():
                raise IndexError("Fila Vazia")
            else:
                while not self.pilha_entrada.esta_vazia():
                    item = self.pilha_entrada.pop()
                    self.pilha_saida.push(item)
                return self.pilha_saida.pop()
        else:
            return self.pilha_saida.pop()

#se a pilha de saída estiver vazia e a de entrada também, gera o erro "Fila Vazia". Caso a pilha de saída estiver vazia e a de entrada não, passa todos os itens da entrada pra saida e retorna o elemento topo da lista de saida. Caso a lista de saida não esteja vazia, retorna o elemento do topo.     
#complexidade de tempo O(1) amortizado.
    def frente(self):
        if self.pilha_saida.esta_vazia():
            if self.pilha_entrada.esta_vazia():
                raise IndexError("Fila Vazia")
            else:
                while not self.pilha_entrada.esta_vazia():
                    item = self.pilha_entrada.pop()
                    self.pilha_saida.push(item)
                return self.pilha_saida.topo()
        else:
            return self.pilha_saida.topo()

#se a ambas as pilhas estiverem vazias, returna True, caso contrário, retorna False.
#complexidade de tempo O(1).
    def esta_vazia(self):
        return self.pilha_saida.esta_vazia() and self.pilha_entrada.esta_vazia()

#retorna o tamanho da fila, que é a soma do tamanho das duas pilhas.
#complexidade de tempo O(1).
    def len(self):
        return self.pilha_entrada.len() + self.pilha_saida.len()

#representa a fila textualmente, como string, mostrando o valor de cada nó, começando pela pilha de saída (que é a que tem os elementos mais antigos) e depois a pilha de entrada (que tem os elementos mais recentes).
#complexidade de tempo O(n), onde n é o número de elementos na fila. o representador passa em cada elemento da fila.
    def __repr__(self):
        saida = str(self.pilha_saida)
        entrada = str(self.pilha_entrada)
        values = []
        if saida:
            values.append(saida)
        if entrada:
            values.append(entrada)
        if not values:
            return "Fila Vazia"
        return ' -> '.join(values)
            
    

