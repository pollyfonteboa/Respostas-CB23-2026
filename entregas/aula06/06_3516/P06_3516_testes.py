import unittest
from P06_3516_pilha_encadeada import PilhaEncadeada
from P06_3516_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):
#define a criação de uma pilha encadeada para ser usada nos testes
    def setUp(self):
        self.pilha = PilhaEncadeada()

#testa se o último a entrar é o primeiro a sair. Coloca 3 elemntos na pilha e retia eles um a um, verificando se a ordem de saída é a inversa da ordem de entrada.
    def test_ordem_lifo(self):
        self.pilha.push(10)
        self.pilha.push(20)
        self.pilha.push(30)
        
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(self.pilha.pop(), 20)
        self.assertEqual(self.pilha.pop(), 10)

#chama a pilha vazia e vê se ela retorna o Index Error nos dois casos.
    def test_pop_e_topo_em_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()

#adiciona e retira elementos da pilha, testando se o tamanho continua correto.
    def test_coerencia_de_len(self):
        self.assertEqual(self.pilha.len(), 0)
        self.pilha.push("A")
        self.assertEqual(self.pilha.len(), 1)
        self.pilha.push("B")
        self.assertEqual(self.pilha.len(), 2)
        self.pilha.pop()
        self.assertEqual(self.pilha.len(), 1)
        self.pilha.pop()
        self.assertEqual(self.pilha.len(), 0)

#alterna operações de push e pop, verificando se o topo da pilha está correto a cada operação.
    def test_alternancia_de_operacoes(self):
        self.pilha.push(1)
        self.assertEqual(self.pilha.topo(), 1)
        self.pilha.push(2)
        self.assertEqual(self.pilha.pop(), 2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.topo(), 3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 1)

#testa se a pilha aceita tipos diferentes de elementos (str, int, float, None) e se eles são retirados na ordem correta.
    def test_tipos_diferentes_repetidos_e_none(self):
        self.pilha.push(100)
        self.pilha.push(100)
        self.pilha.push("texto")
        self.pilha.push(None)
        self.pilha.push(3.14)

        self.assertEqual(self.pilha.pop(), 3.14)
        self.assertIsNone(self.pilha.pop())
        self.assertEqual(self.pilha.pop(), "texto")
        self.assertEqual(self.pilha.pop(), 100)
        self.assertEqual(self.pilha.pop(), 100)


class TestFilaEncadeada(unittest.TestCase):

#define a criação de uma fila encadeada para ser usada nos testes.
    def setUp(self):
        self.fila = FilaEncadeada()

#testa a ordem FIFO (first in, first out) em sequência de enfileirar e desenfileirar. Coloca 3 elementos na fila e retira eles um a um, verificando se a ordem de saída é a mesma da ordem de entrada.
    def test_ordem_fifo(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

#testa a intercalação entre enfileirar e desenfileirar, verificando se a ordem de saída continua correta.
    def test_intercalacao_operacoes(self):
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.assertEqual(self.fila.desenfileirar(), "A")
        
        self.fila.enfileirar("C")
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")

#testa esvaziar totalmente a fila e voltar a usar a mesma instância.
    def test_esvaziar_e_reutilizar(self):
        self.fila.enfileirar(10)
        self.fila.enfileirar(20)
        self.assertEqual(self.fila.desenfileirar(), 10)
        self.assertEqual(self.fila.desenfileirar(), 20)
        self.assertTrue(self.fila.esta_vazia())

        # Reutilizando a mesma instância.
        self.fila.enfileirar(30)
        self.assertFalse(self.fila.esta_vazia())
        self.assertEqual(self.fila.frente(), 30)
        self.assertEqual(self.fila.desenfileirar(), 30)
        self.assertTrue(self.fila.esta_vazia())

#testa se a fila retorna o erro correto (Fila Vazia)quando se tenta desenfileirar ou acessar a frente de uma fila vazia.
    def test_desenfileirar_e_frente_em_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_de_len(self):
#Testa o tamanho da fila após operações na fila.
        self.assertEqual(self.fila.len(), 0)
        self.fila.enfileirar(100)
        self.assertEqual(self.fila.len(), 1)
        self.fila.enfileirar(200)
        self.assertEqual(self.fila.len(), 2)
        self.fila.desenfileirar()
        self.assertEqual(self.fila.len(), 1)
        self.fila.desenfileirar()
        self.assertEqual(self.fila.len(), 0)
        
if __name__ == "__main__":
    unittest.main()