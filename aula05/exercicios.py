def bubble_sort(lista):
    nova = lista.copy()
    for fim in range(len(nova) - 1, 0, -1):
        for j in range(fim):
            if nova[j] > nova[j + 1]:
                nova[j], nova[j + 1] = nova[j + 1], nova[j]
    return nova


def selection_sort(lista):
    nova = lista.copy()
    for i in range(0, len(nova)):
        menor = i
        for j in range(i + 1, len(nova)):
            if nova[j] < nova[menor]:
                menor = j
        nova[i], nova[menor] = nova[menor], nova[i]
    return nova


def insertion_sort(lista):
    a = lista.copy()
    for i in range(1, len(a)):
        valor = a[i]
        j = i - 1
        while j >= 0 and a[j] > valor:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = valor
    return a

def quicksort(lista):
        if len(lista) <= 1:
            return lista.copy() 
        
        maior = []
        menor = []
        meio = []
        pivo = lista[len(lista) // 2]

        for i in range(len(lista)):
            if lista[i] > pivo:
                maior.append(lista[i])
            elif lista[i] < pivo:
                menor.append(lista[i])
            else:
                meio.append(lista[i])
        return quicksort(menor) + meio + quicksort(maior)


    
