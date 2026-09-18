"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    nova_lista = []

    for i in range(len (lista)):
        if lista[i] > 0:
            nova_lista.append(lista[i])

    return nova_lista      


def inverte(lista):
    inicio = 0
    fim = len(lista) - 1
    troca = 0

    while inicio < fim:
        troca = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = troca
        inicio += 1
        fim -= 1
    return lista

def busca_binaria(lista, alvo):

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio 

        if lista[meio] < alvo:
            inicio = meio + 1

        else: fim = meio - 1

    return -1

def intercala(lista_a, lista_b):
    nova_lista = []

    for i in range(len(lista_a)):
        nova_lista.append(lista_a[i])
        nova_lista.append(lista_b[i])

    return nova_lista
        

def remove_repetidos(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista
