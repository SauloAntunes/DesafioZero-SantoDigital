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


def subconjuntos(lista_numeros):
    resultado_subconjuntos = [[]]
    for numero in lista_numeros:
        novo_subconjunto = []
        for subconjunto in resultado_subconjuntos:
            novo_subconjunto.append(subconjunto + [numero])
        resultado_subconjuntos.extend(novo_subconjunto)
    return resultado_subconjuntos


# Programa principal
while True:
    lista_numeros = list()
    while True:
        numero = validar_inteiro()
        if numero == 0:
            break
        lista_numeros.append(numero)
    if len(lista_numeros) >= 1:
        resultado = subconjuntos(lista_numeros)
        print('\nResultado: [', end='')
        for indice, subconjunto in enumerate(resultado):
            if indice < len(resultado) - 1:
                sleep(1)
                print(f'{subconjunto},', end=' ')
            else:
                sleep(1)
                print(f'{subconjunto}', end='')
        print('].\n')
        sleep(1)
    opcao = validar_opcao()
    if opcao == 'N':
        break
print('\nPrograma Finalizado!')
