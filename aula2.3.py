''' 3 - Leia um número real. Se o número for positivo imprima a raiz quadrada.
    do contrário, imprima o número ao quadrado.'''

numReal = float(input('Digite um número: '))

resultado = numReal % 2

if resultado == 0:
    raiz = sqrt(numReal)
    print(f'A raiz quadrada de {numReal} é: {raiz:.4f}')
elif numReal > 0:
    numReal **= 2
    print(f'O quadrado é: {numReal:.2f}\n')