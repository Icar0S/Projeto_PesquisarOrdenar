#Implemente a solução de ordenamento Quicksort, calcule os tempos para ordenar,
#através do mesmo, séries de números aleatórios para os seguintes
#tamanhos [100000,200000,300000,400000,500000].
#Plote os gráficos de tempo x tamanho.

#Bibliotecas
from random import randint
import matplotlib.pyplot as plt
import timeit

#Lista
def geralista(tam):
    lista = [100000, 200000, 300000, 400000, 500000]
    x = 0
    while x < tam:
        n = randint(1, 10*tam)
        lista.append(n)
        x += 1
    return lista

#Lista pior caso
def geralistapc(tam):
    lista = [100000, 200000, 300000, 400000, 500000]
    x = 0
    while x < tam:
        lista.append(tam)
        tam -= 1
    return lista


def escolhe_pivo(lis):
    if lis[0] > lis[len(lis)-1]:
        p = len(lis)-1
    else:
        p = 0
    return p


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = escolhe_pivo(lista)
    menor = []
    meio = []
    maior = []
    for i in range(len(lista)):
        if lista[i] < lista[pivo]:
            menor.append(lista[i])
        if lista[i] == lista[pivo]:
            meio.append(lista[i])
        if lista[i] > lista[pivo]:
            maior.append(lista[i])
    return quicksort(menor) + meio + quicksort(maior)


def desenhagrafico(x, y, z, xl = "Tamanho da lista", yl = "Tempo"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("QuickSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [10, 100, 300, 500, 700, 989]
yg = []
zg = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("quicksort({})".format(listacm), setup="from __main__ import quicksort", number=1)
    yg.append(val1)
    val2 = timeit.timeit("quicksort({})".format(listapc), setup="from __main__ import quicksort", number=1)
    zg.append(val2)
    print(val1, val2)

desenhagrafico(xg, yg, zg)
