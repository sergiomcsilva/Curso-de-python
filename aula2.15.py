'''15. Usando switch, escreva um program que leia um interio entre 1 e 7 e imprima o dia
da semana correspondente a cada numero, isto e, domindo se 1, segunda-feira se 2, e
assim por diante. '''

numdia = int(input('Digite um numero para saber o dia da semana 1 a 7: '))

if numdia == 1:
    print('1-Domingo')
elif numdia == 2:
    print('2-Segunda-feira')
elif numdia == 3:
    print('3-Terça-feira')
elif numdia == 4:
    print('4-Quarta-feira')
elif numdia == 5:
    print('5-Quinta-feira')
elif numdia == 6:
    print('6-Sexta-feira')
elif numdia == 7:
    print('7-Sabado')
else:
    print('Numero Invalido! Digite um numero de 1 a 7')
