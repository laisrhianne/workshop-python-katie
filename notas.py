print('Informe as 3 notas recebidas:')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print('Aprovado.')
if media >= 5 & media < 7:
    print('Recuperação.')
else:
    print('Reprovado.')