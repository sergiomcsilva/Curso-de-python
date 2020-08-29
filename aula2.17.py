'''17. Faça um programa que calcule e mostre a area de um trapezio. sabe-se que:
A = (basemaior + basemenor) * altura / 2
lembre-se a base maior e abase menor deve ser numero maior que zero. '''

base_menor = float(input('Digite o valor da base menor: '))
base_maior = float(input('Digite o valor da base maior: '))
altura = float(input('Digite o valor da altura: '))

print('')

if 0 < base_menor and base_menor > 0 and 0 < base_maior and base_maior > 0 and 0 < altura and altura > 0:
    area = (((base_maior + base_menor) * altura) / 2)
    print(f'A area do trapezio é: {area:.2f}')
else:
    print('Nenhum valor pode ser igual ou menor que 0')
