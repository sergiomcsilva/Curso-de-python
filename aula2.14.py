'''14. A nota final de um estudante e calculada a partir de tres notas atribuidas enter o intervalo
de 0 ate 10, respectivamente, a um trabalho de laboratorio a uma avaliaçao semestral
e a um exame final. A medida das tres notas mencionandas anteriormente obedec aos
pesos. Trabalho de Laboratorio, 2, Avaliaçao Semestral, 3. Exame final 5. De acordo
com o resulado, mosre a tela se o aluno esta reprovado (media entre 0 e 2.9) de
recuperaçao(entre 3 e 4.9) ou se foi aprovado. Faça todas as verificaçôes necessarias.
'''

notalab = float(input('Digite a nota do trabalho de laboratório: '))
notasem = float(input('Digite a nota da avaliação semestral: '))
notafim = float(input('Digite a nota da avaliação final: '))

media = (((notalab * 2) + (notasem * 3) + (notafim * 5)) / 10)

if media <= 2.9:
    print('O aluno foi reprovado!')
elif media <= 4.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno está aprovado!')

print(f'A media do aluno é: {media:.1f}')
