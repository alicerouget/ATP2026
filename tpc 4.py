import random

lista = []
opcao = -1

while opcao != 0:
    print("Menu")
    print("(1) Criar lista")
    print("(2) Ler lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Ordenar por ordem crescente")
    print("(8) Ordenar por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        tamanho = int(input("Digite o tamanho da lista: "))
        lista = []
        i = 0
        while i < tamanho:
            numero = random.randint(1, 100)
            lista.append(numero)
            i = i + 1
        print("Lista criada com sucesso!", lista)

    elif opcao == 2:
        tamanho = int(input("Digite o tamanho da lista: "))
        lista = []
        i = 0
        while i < tamanho:
            numero = int(input("Digite um número: "))
            lista.append(numero)
            i = i + 1
        print("Lista criada com sucesso!", lista)

    elif opcao == 3:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            soma = 0
            i = 0
            while i < len(lista):
                soma = soma + lista[i]
                i = i + 1
            print("A soma dos elementos da lista é:", soma) 

    elif opcao == 4:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            soma = 0
            i = 0
            while i < len(lista):
                soma = soma + lista[i]
                i = i + 1
            media = soma / len(lista)
            print("A média dos elementos da lista é:", media)

    elif opcao == 5:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            maior = lista[0]
            i = 1
            while i < len(lista):
                if lista[i] > maior:
                    maior = lista[i]
                i = i + 1
            print("O maior elemento da lista é:", maior)
    elif opcao == 6:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            menor = lista[0]
            i = 1
            while i < len(lista):
                if lista[i] < menor:
                    menor = lista[i]
                i = i + 1
            print("O menor elemento da lista é:", menor)

    elif opcao == 7:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            crescente = True
            i = 0
            while i < len(lista) - 1:
                if lista[i] > lista[i + 1]:
                    crescente = False
                i = i + 1
            if crescente:
                print("A lista já está em ordem crescente.")    
            else:
                print("A lista não está em ordem crescente.")

    elif opcao == 8:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            decrescente = True
            i = 0
            while i < len(lista) - 1:
                if lista[i] < lista[i + 1]:
                    decrescente = False
                i = i + 1
            if decrescente:
                print("A lista já está em ordem decrescente.")    
            else:
                print("A lista não está em ordem decrescente.")

    elif opcao == 9:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            elemento = int(input("Digite o elemento que deseja procurar: "))
            posicao = -1
            i = 0
            while i < len(lista) and posicao == -1:
                if lista[i] == elemento:
                    posicao = i
                i = i + 1

            if posicao != -1:
                print("Elemento encontrado na lista, na posição:", posicao)
            else:
                print("Resultado: posição -1; Elemento não encontrado na lista.")

    elif opcao == 0:
        print("Saindo do programa...")  
        print("Lista final:", lista)

