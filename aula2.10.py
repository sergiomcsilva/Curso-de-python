''' 10 - Faça um programa que recebaa altura e o sexo de uma pessoa e calcule e
mostre seu peso ideal, utilizando as seguntes fŕmulas (onde h coresponde à altura):

Homens: (72.7*h)-58
Mulheres (62.1*h)-44.7'''

altura = float(input('Digite a altura: '))
sexo = input('insira o seu sexo: M para masculino ou F para feminino: ')

if sexo == 'm':
    pesoideal = (72.7 * altura) - 58
    print(f'O peso ideal para o homen com altura de {altura}m é: {pesoideal:.2f}Kg')
else:
    pesoideal = (62.1 * altura) - 44.7
    print(f'O peso ideal para a mulher com altura de {altura}m é: {pesoideal:.2f}Kg')

