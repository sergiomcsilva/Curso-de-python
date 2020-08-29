''' 1 - Faça um programa que receba dois números e mostre qual deles é o maior.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número : '))

maior = num1

if (num2 > maior):
    maior = num2

print(f'O número maior é : {maior}')

