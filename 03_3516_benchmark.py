import AulasPraticas.AP_03_ordenacao as ap3
import random
import time
import sys

#limita a memória que o computador pode usar 
sys.setrecursionlimit(10**6)

#define um caso aleátorio
def avg_case(N):
    #cria uma lista ordenada de 0 a n-1
    original = [x for x in range(N)]
    my_list = []
    while len(original):
            #sorteia o índice de um número na lista
            random_index = random.randint(0,len(original) - 1)
            #insere o número correspondente do índice sorteado na lista "my list"
            my_list.append(original[random_index])
            #remove o item sorteado da lista original
            original[random_index], original[-1] = original[-1], original[random_index]
            original.pop(-1)
    #retorna a lista embaralhada
    return my_list

#gera o pior caso no "case_quick", ele inverte a lista ordenada
def gera_worst_case_quick(N):
    return [x for x in range(N)][::-1]

#define a função que irá rodar os casos, passando como parâmetro: o tipo da função, o tamanho da lista, a quantidade de vezes que irá rodar o teste, e o pior caso (ou caso médio).
def perf_algo(sort_algo, N, k, worst_case_fun = None):
    #cria uma lista vazia
    times = []
    #repete a função k vezes
    for _ in range(k):
        #caso tenha-se passado o parâmetro worst_case, usa essa lista, caso contrário uma lista aleatória do avg_case
        my_list = worst_case_fun(N) if worst_case_fun else avg_case(N)
        #inicia a contagem de tempo
        start_t = time.perf_counter()
        #chama a função que passamos como parâmentro e a lista que passamos como parâmetro para ela
        sort_algo(my_list)
        #finaliza a contagem do tempo
        end_t = time.perf_counter()
        #coloca a contagem do tempo na lista times
        times.append(end_t - start_t)
    #faz a média dos k tempos e retorna o resultado
    return sum(times)/k

if __name__ == "__main__":
    print("-" * 64)
    print(f"{'Test N = 100':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 100, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 100, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort,100, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort,100, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort,100, 50)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort,100, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 500':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 500, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 500, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 500, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 500, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 500, 50)}ms")
    print(f"Pior tempo Selection Sort: { perf_algo(ap3.selection_sort, 500, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 1000':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 1000, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 1000, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 1000, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 1000, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 1000, 50)}ms")
    print(f"Pior tempo Selection Sort: { perf_algo(ap3.selection_sort, 1000, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 5000':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 5000, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 5000, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 5000, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 5000, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 5000, 50)}ms")
    print(f"Pior tempo Selection Sort: { perf_algo(ap3.selection_sort, 5000, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
