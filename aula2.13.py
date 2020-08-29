'''13. faça um algoritmo que calcula a media ponderada das notas de 3 provas. A primeira e
a segunda prova tem o peso 1 e a terceira tem peso 2. Ao final, mostre a media do aluno
e indica se o aluno foi aprovado ou reprovado. A nota para a aprovaçao deve ser igual ou
superior a 60 pontos.
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4)
print(f'A media ponderada do aluno é: {media:.2f}')

if media > 6:
    print('O aluno foi aprovado!')
else:
    media < 6
    print('O aluno foi reprovado!')
