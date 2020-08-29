''' 5 - Faça um programa que receba um número inteiro e verifique
    se este número é par ou impar.'''

num = int(input('Digite um número: '))

resultado = num % 2

if resultado == 0:
    print(f'O número digitado {num} é Par.')
else:
    print(f'O númeor digitado {num} é Impar.')

