from random import randint
import matplotlib.pyplot as plt
import timeit


def geralista(tam):
    lista = []
    x = 0
    while x < tam:
        n = randint(1, tam)
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


def countingsort(lista, range):
    i = j = l = 0
    k = 1
    index = []
    output = []
    while i < (range + 1):
        index.append(0)
        i += 1
    while j < len(lista):
        output.append(0)
        index[lista[j]] += 1
        j += 1
    while k < (range + 1):
        index[k] += index[k - 1]
        k += 1
    while l < len(lista):
        output[index[lista[l]] - 1] = lista[l]
        index[lista[l]] -= 1
        l += 1
    return output


#print(countingsort(geralista(20), 20))


def desenhagrafico(x, y, z, xl = "Entrada", yl = "Saida"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("CountingSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 10000, 30000, 50000, 70000, 100000]
yg = []
zg = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("countingsort({}, {})".format(listacm, i), setup="from __main__ import countingsort", number=1)
    yg.append(val1)
    val2 = timeit.timeit("countingsort({}, {})".format(listapc, i), setup="from __main__ import countingsort", number=1)
    zg.append(val2)
    print(val1, val2)

desenhagrafico(xg, yg, zg, xl = "Tamanho da lista", yl = "Tempo")
