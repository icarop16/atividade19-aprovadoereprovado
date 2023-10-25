#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
nota1 = float(input("digite a nota 01: "))
nota2 = float(input("digite a nota 02: "))
media = (nota1+nota2) / 2
print(f"Sua nota foi {media}.")
if media < 5:
    print("Você foi REPROVADO")
elif media >=5 and media <= 6.9:
    print("Você ficou de RECUPERAÇÃO")
else:
    print("Você foi APROVADO")