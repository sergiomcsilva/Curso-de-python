''' 2 - Leia um número fornecido pelo usuário. Se esse número for positivo,
    calcule a raiz quadrada do número. Se o número for negativo, mostre
    uma mensagem dizendo que o número é inválido.'''

from math import sqrt

num = int(input('Digite um número: '))

resultado = num % 2

if resultado == 0:
    raiz = sqrt(num)
    print(f'A raiz quadrada de {num} é: {raiz:.4f}\n')
else:
    print('Número é inválido.')

