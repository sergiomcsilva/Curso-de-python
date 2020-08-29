'''11. Escreva um programa que leia um número inteiro do que zero e devolva, na tela, a
soma de todos os seus algarsmo.Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o nùmero lido não for maior de que zero, o programa terminará com a
mensagem 'Número inválido'. '''

num = int(input('Digite um numero: '))
if num > 0:
    num0 = num // 1 % 10
    num1 = num // 10 % 10
    num2 = num // 100 % 10
    num3 = num // 1000 % 10
    soma = num0 + num1 + num2 + num3
    print('O valor da soma dos algarismos é: ' + str(soma))
else:
    print('Numero Invalido!')