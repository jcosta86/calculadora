from calculadora.calculator import *


def menu() -> int:
    options = ['Soma dois numeros', 'Divide dois numeros', 'Subtrai dois numeros', 'Multiplica dois numeros', 'Sair']

    print('\n--------  olist  --------\n')

    for i, option in enumerate(options):
        print(f'[{i + 1}] - {option}')

    op_menu = int(input('\nSelecione uma opção: '))
    return op_menu


while True:
    try:
        op = menu()
        if op == 5:
            print('Até logo!')
            break
        else:
            number_1 = float(input('Informe o primeiro número: '))
            number_2 = float(input('Informe o segundo número: '))
            if op == 1:
                print(f'{number_1} + {number_2} = {addition(number_1, number_2)}')
            elif op == 2:
                print(f'{number_1} / {number_2} = {division(number_1, number_2)}')
            elif op == 3:

                print(f'{number_1} - {number_2} = {subtaction(number_1, number_2)}')
            elif op == 4:
                print(f'{number_1} x {number_2} = {multiplication(number_1, number_2)}')
            else:
                print('Opção inválida.')
    except Exception as e:
        print(e)
