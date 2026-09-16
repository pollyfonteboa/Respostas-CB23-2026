class _No:
    #inicia o nó com um valor que foi passado e já define (aponta) o próximo nó como None (vazio)
    def __init__(self, value):
        self.value = value
        self.next = None

class PilhaEncadeada:
    #inicia a pilha encadeada com head (a cabeça, ou seja, o primeiro elemento da pilha) como None (vazio) e contador de tamanho como 0 
    def __init__(self):
        self.head = None
        self.contador_tamanho = 0

#define o ultimo_node como um nó que recebe o valor passado, aponta o proximo nó como cabeça da pilha e insere o ultimo_node como a nova cabeça. Aumenta um no valor do contador de tamanho da pilha.
#complexidade de tempo O(1).
    def push(self, value):
        ultimo_node = _No(value)
        ultimo_node.next = self.head
        self.head = ultimo_node
        self.contador_tamanho += 1

#se a cabeça da pilha estiver vazia, gera o erro "Pilha vazia", caso tenha um elemento, define ele como item, coloca ele como vazio (self.head.next),ou seja, retira o elemento da pilha, diminui um no tamanho da pilha e retorna o valor do elemento retirado.
#complexiadade de tempo O(1).
    def pop(self):
        if self.head is None:
            raise IndexError("Pilha Vazia")
        else:
            item = self.head
            self.head = self.head.next 
            self.contador_tamanho -= 1  
            return item.value

#se a cabeça estiver vazia, gera o erro "Pilha Vazia", caso tenha um elemento, retorna o valor do elemnteo da cabeça.      
#complexidade de tempo O(1).
    def topo(self):
        if self.head is None:
            raise IndexError("Pilha Vazia")
        else:
            return self.head.value

#se a cabeça da pilha estiver vazia, retorna True, caso contrário, retorna False.
#complexidade de tempo O(1).
    def esta_vazia(self):
        return self.head is None

#a partir do contador de tamanho que foi atualizado nos metodos anteriores, retornamos o tamanho da pilha.  
# complexidade de tempo O(1).     
    def len(self):
        return self.contador_tamanho

#representa a pilha textualmente, como string, mostrando o valor de cada nó, começando pela cabeça até a base.
#complexidade de tempo O(n), onde n é o número de elementos na pilha. o representador passa em cada elemnto da pilha.
    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)
