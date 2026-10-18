"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    qtd = 0
    for num in lista:
        if num < 0:
            qtd += 1
    return qtd


def media(lista):
    if len(lista) == 0:
        return 0
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)


def sem_o_maior(lista):
    if len(lista) == 0:
        return []
    
    maior = lista[0]
    idx_maior = 0
    i = 1
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
            idx_maior = i
        i += 1
        
    resultado = []
    i = 0
    while i < len(lista):
        if i != idx_maior:
            resultado.append(lista[i])
        i += 1
    return resultado


def acumulada(lista):
    resultado = []
    soma = 0
    for num in lista:
        soma += num
        resultado.append(soma)
    return resultado


def achata(lista_de_listas):
    resultado = []
    for sublista in lista_de_listas:
        for item in sublista:
            resultado.append(item)
    return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    pos = -1
    i = 0
    while i < len(lista):
        if lista[i] == alvo:
            pos = i
        i += 1
    return pos


def conta_ocorrencias(lista, alvo):
    qtd = 0
    for item in lista:
        if item == alvo:
            qtd += 1
    return qtd


def primeiro_maior_que(lista, limite):
    i = 0
    while i < len(lista):
        if lista[i] > limite:
            return i
        i += 1
    return -1


def busca_binaria_primeira(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    res = -1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            res = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return res


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    soma = 0
    operacoes = 0
    for num in lista:
        operacoes += 1
        if num % 2 == 0:
            soma += num
    return (soma, operacoes)


def maior_contando(lista):
    maior = lista[0]
    comparacoes = 0
    i = 1
    while i < len(lista):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
        i += 1
    return (maior, comparacoes)


def tem_soma_contando(lista, alvo):
    comparacoes = 0
    i = 0
    n = len(lista)
    while i < n:
        j = i + 1
        while j < n:
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return (True, comparacoes)
            j += 1
        i += 1
    return (False, comparacoes)


def ordenada_contando(lista):
    comparacoes = 0
    i = 0
    while i < len(lista) - 1:
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return (False, comparacoes)
        i += 1
    return (True, comparacoes)


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        troca = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = troca
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


def par_que_soma(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        soma = lista[inicio] + lista[fim]
        if soma == alvo:
            return (inicio, fim)
        elif soma < alvo:
            inicio += 1
        else:
            fim -= 1
    return (-1, -1)


def soma_maxima_janela(lista, k):
    if len(lista) < k or k == 0:
        return 0
    
    soma_atual = 0
    i = 0
    while i < k:
        soma_atual += lista[i]
        i += 1
        
    maior_soma = soma_atual
    i = k
    while i < len(lista):
        soma_atual = soma_atual + lista[i] - lista[i - k]
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        i += 1
        
    return maior_soma


def parenteses_balanceados(texto):
    pilha = []
    for char in texto:
        if char == '(' or char == '[':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0 or pilha.pop() != '(':
                return False
        elif char == ']':
            if len(pilha) == 0 or pilha.pop() != '[':
                return False
    return len(pilha) == 0