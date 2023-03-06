#Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado com duas casas decimais

# lê um número inteiro do usuário
numero = int(input("Digite um número que seja inteiro: "))

# exibe o número informado com duas casas decimais
print("O número informado é: {:.2f}".format(numero)) 
#o formato "{:.2f}" indica que o número deve ser exibido com duas casas decimais.
#A função "format()" é utilizada para substituir o valor da variável na mensagem formatada