from time import sleep


def validar_inteiro():
    while True:
        try:
            numero = int(input('Informe um número inteiro ou 0 (zero) '
                               'para encerrar: '))
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


def lista_asteriscos(numero):
    lista_resultado = list()
    for numero_atual in range(1, numero + 1, 1):
        lista_resultado.append('*' * numero_atual)
    return lista_resultado


# Programa principal
while True:
    numero = validar_inteiro()
    if numero == 0:
        break
    resultado = lista_asteriscos(numero)
    print('\nResultado: [', end='')
    for indice, asterisco in enumerate(resultado):
        if indice < len(resultado) - 1:
            sleep(1)
            print(f'{asterisco},', end=' ')
        else:
            sleep(1)
            print(f'{asterisco}', end='')
    print('].\n')
    sleep(1)
print('\nPrograma Finalizado!')
