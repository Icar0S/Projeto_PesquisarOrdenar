from random import randint
import matplotlib.pyplot as plt
import timeit


def geralista(tam):
    lista = [30000,40000,50000,60000,70000]
    x = 0
    while x < tam:
        n = randint(1, 10*tam)
        lista.append(n)
        x += 1
    #print(lista)
    return lista

def geralistapc(tam):
    lista = []
    x = 0
    while x < tam:
        lista.append(tam)
        tam -= 1
    #print(lista)
    return lista


def shellsort(lista):
    cont = 0
    val = 1
    while val > 0:
        for i in range(val, len(lista)):
            aux = lista[i]
            j = i
            cont += 1
            while j >= val and aux < lista[j - val]:
                lista[j] = lista[j - val]
                j = j - val
                lista[j] = aux
        val = 0
    #return lista
    return cont


#print(shellsort(geralista(10)))


def desenhagrafico(x, y, z, xl = "Entrada", yl = "Saida"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("ShellSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 10000, 30000, 50000, 70000, 100000]
yg = []
yg2 = []
zg = []
zg2 = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("shellsort({})".format(listacm), setup="from __main__ import shellsort", number=1)
    yg.append(val1)
    yg2.append(shellsort(listacm))
    val2 = timeit.timeit("shellsort({})".format(listapc), setup="from __main__ import shellsort", number=1)
    zg.append(val2)
    zg2.append(shellsort(listapc))
    print(val1, val2)

desenhagrafico(xg, yg, zg, xl = "Tamanho da lista", yl = "Tempo")
