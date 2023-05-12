def menu():
    linha = '-' * 42
    titulo = 'Calculadora'
    print(linha)
    print(titulo.center(42))
    print(linha)
    print('[1] SOMAR')
    print('[2] SUBTRAIR')
    print('[3] MULTIPLICAR')
    print('[4] DIVIDIR')
    print('[5] SAIR')

def somar():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    resultado = x + y
    print('-' * 42)
    print(f'O Resultado da Soma é: {resultado}'.center(42))
    print('-' * 42)

def diminuir():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    resultado = x - y
    print('-' * 42)
    print(f'O Resultado da Subtração é: {resultado}'.center(42))
    print('-' * 42)

def multiplicar():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    resultado = x * y
    print('-' * 42)
    print(f'O Resultado da Mulltiplicação é: {resultado}'.center(42))
    print('-' * 42)

def dividir():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    resultado = x / y
    print('-' * 42)
    print(f'O Resultado da Divisão é: {resultado}'.center(42))
    print('-' * 42)

def main():
    while True:
        menu()
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            print('-' * 42)
            print('Somar'.center(42))
            print('-' * 42)
            somar()
        elif opcao == 2:
            print('-' * 42)
            print('Subtrção'.center(42))
            print('-' * 42)
            diminuir()
        elif opcao == 3:
            print('-' * 42)
            print('Multiplicação'.center(42))
            print('-' * 42)
            multiplicar()
        elif opcao == 4:
            print('-' * 42)
            print('Divisão'.center(42))
            print('-' * 42)
            dividir()
        elif opcao == 5:
            Exception
        else:
            print('-' * 42)
            print('Opção Inválida!'.center(42))
            print('-' * 42)
            main()


main()
