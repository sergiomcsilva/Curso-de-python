''' 9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior a 20% do salário imprima: "Empréstimo não concedido",
caso contrário imprima: "Empréstimo comcedido".'''

salario = float(input('Digite o valor do salário: '))
prestacao = float(input('Digite o valor da prestação: '))

calculo = salario * 0.20

if prestacao > calculo:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')