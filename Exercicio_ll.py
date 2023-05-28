from time import sleep


def validar_inteiro():
    while True:
        try:
            numero = int(input('Informe um número inteiro ou 0 (zero) para '
                               'encerrar a entrada de números: '))
        except (ValueError, TypeError):
            print('\nERRO: por favor, digite um número inteiro válido.\n')
            sleep(1)
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            sleep(1)
            return 0
        else:
            break
    return numero


def validar_opcao():
    opcao = str(input('Quer continuar? [Sim/Não] ')).upper().strip()[0]
    sleep(1)
    print()
    while opcao not in 'SN':
        print('\nERRO: por favor, informe somente \'Sim\' ou \'Não\'.\n')
        sleep(1)
        opcao = str(input('Quer continuar? [Sim/Não] ')).upper().strip()[0]
        sleep(1)
    return opcao


def menor_diferenca(lista_numeros):
    lista_resultados = list()
    menor = max(lista_numeros)
    for numero in lista_numeros:
        for indice, numero_atual in enumerate(lista_numeros):
            if numero != lista_numeros[indice]:
                if 0 < numero - numero_atual <= menor:
                    menor = numero - numero_atual
                    lista_resultados.append((numero, lista_numeros[indice]))
    return lista_resultados


# Programa principal
while True:
    numeros = list()
    while True:
        numero = validar_inteiro()
        if numero == 0:
            break
        numeros.append(numero)
    if len(numeros) >= 2:
        resultado = menor_diferenca(numeros)
        print('\nResultado: ', end='')
        for indice, n in enumerate(resultado):
            if indice < len(resultado) - 1:
                sleep(1)
                print(f'{n},', end=' ')
            else:
                sleep(1)
                print(f'{n}.', end='')
        print('\n')
    elif len(numeros) == 1:
        print('\nERRO: por favor, informe no mínimo 2 números.\n')
        sleep(1)
    opcao = validar_opcao()
    if opcao == 'N':
        break
print('\nPrograma Finalizado!')
