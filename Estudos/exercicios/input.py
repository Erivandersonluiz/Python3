"""     
Exercicio

crie um algoritmo que solicite o ano de 
nascimento do usuario e com base no ano imprima a idade 
""" 

ano_nascimento = int(input("Digite o ano que você nasceu: "))
ano_atual = 2024  # Substitua pelo ano atual desejado

idade = ano_atual - ano_nascimento

print(f"Você nasceu em {ano_nascimento} e tem {idade} anos.")