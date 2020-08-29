''' 6 - Escreva um programa que receba dois número inteiro,
   mostre na tela o maior deles assim como a difereça existente
   enter ambos.'''

num1 = int(input('Digite o primero número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número maior é: {num1}\n')
else:
    print(f'O número maior é: {num2}\n')

if num1 > num2:
    resultado = num1 - num2
else:
    resultado = num2 - num1

if num1 > num2:
    print(f'A diferença entre o número {num1} e o número {num2} é: {resultado}')
else:
    print(f'A diferença entre o número {num2} e o número {num1} é: {resultado}')
