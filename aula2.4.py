''' 4 - Faça um programa que leia um número e, caso seja possitivo, calcule e mostre:
    O número digitado ao quadrado.
    A rais quadrada do número digitado.'''
from math import sqrt

num = float(input('Digite um numero: '))

resultado = num % 2
quadrado = num ** 2
raiz = sqrt(num)

if resultado > 0:
    print('Por favor, digite um numero positivo!')
elif resultado == 0:
    print(f'O número quadrado de {num} é: {quadrado}')
    print(f'A raiz quadrada de {num} é: {raiz:.4f}')

