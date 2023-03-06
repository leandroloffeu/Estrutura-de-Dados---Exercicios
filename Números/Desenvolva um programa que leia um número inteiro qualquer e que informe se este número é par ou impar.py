#Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar

numero = int(input("Digite um número que seja inteiro: "))

if numero % 2 == 0:
    print(numero, "é par")
else:
    print(numero, "é ímpar")
