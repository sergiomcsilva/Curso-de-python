''' 8 - Faça um programa que leia duas notas de um aluno, verifique se as notas são
válidas e exiba na tela a média destas notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
onde caso a nota não passua um valor válido, este fato deve ser informado ao
usuário e o programa termina.'''

nota1 = float(input('Digite a primera nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

if 10 >= nota1 >= 0 and 10 >= nota2 >= 0:
    media = (nota1 + nota2) / 2
    print(f'A média do aluno é: {media:.2f}')
else:
    print('Nota não válida, por favor, digite uma nota valida ente 0.0 e 10.0')
