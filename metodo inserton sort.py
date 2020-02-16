#Implemente a solução de ordenamento INSERTION sort, calcule os tempos para
#ordenar, através do mesmo, séries de números aleatórios para os seguintes
#tamanhos [1000,10000,30000,60000]. Plote os gráficos de tempo x tamanho.

#Gerador de lista
import random
import timeit 
import sys

lista = list(range(60000))
random.shuffle(lista)

'''def ListaPiorCaso(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]

ListaPiorCaso(lista)'''


#Metodo de Ordenação
def insertionsort(lista):
    chave = 1
    while chave < len(lista):
        cont1 = chave
        cont2 = chave
        while cont1 > 0:
            cont1 -= 1
            if lista[cont2] < lista[cont1]:
                aux = lista[cont2]
                lista[cont2] = lista[cont1]
                lista[cont1] = aux
                cont2 -= 1
        chave += 1
    return lista
print ("Sorted array") 
    
insertionsort(lista)
#print(lista)
tempo =   timeit.timeit("insertionsort({})".format(lista), setup="from __main__ import insertionsort",number=1)
print(tempo)



    
