''' 7 - Faça um programa que receba dois números e mostre o maior. Se por acaso
   os dois números forem iguais, imprima a  mensagem "Números iguais"'''

num1 = int(input('Digite o primero número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número maior é: {num1}\n')
elif num1 < num2:
    print(f'O número maior é: {num2}')
else:
    print(f'Números iguais.')
