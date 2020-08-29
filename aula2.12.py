'''12. Ler um número inteiro. Se o número lido for negarivo, escveva a mensagem 'Número
invalido'. Se o numero for positivo, calcule o logaritmo desse número. '''
import math

num = int(input('Digite um numero: '))
if num > 0:
    print(math.log(num))
else:
    print('Numero invalido!')
