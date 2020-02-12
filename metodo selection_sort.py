#Implemente a solução de ordenamento selection sort,
#calcule os tempos para ordenar, através do mesmo,
#séries de números aleatórios para os seguintes tamanhos [1000,10000,30000,60000].
#Repita a operação desta vez usando séries totalmente invertidas (Ordenadas de forma descendente).
#Plote os gráficos de tempo x tamanho.


#Gerador de lista
import random
import timeit 
import sys

lista = list(range(60000))
random.shuffle(lista)

def ListaPiorCaso(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]

ListaPiorCaso(lista)
#print(lista)


#ordenador de lista
def selectionsort(lista):
    for i in range(0, len(lista)):
        mini = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[mini]:
                mini = j
        if lista[i] != lista[mini]:
            aux = lista[i]
            lista[i] = lista[mini]
            lista[mini] = aux
    return lista
print ("Sorted array") 
    
selectionsort(lista)
print(lista)
tempo =   timeit.timeit("selectionsort({})".format(lista), setup="from __main__ import selectionsort",number=1)
print(tempo)













