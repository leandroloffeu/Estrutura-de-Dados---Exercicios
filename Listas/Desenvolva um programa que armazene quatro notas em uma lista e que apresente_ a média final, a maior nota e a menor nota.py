#Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

notas = []  # cria uma lista vazia para armazenar as notas

# loop para inserir as notas na lista
#for i in range(4):
 #   nota = float(input(f"Informe a nota {i+1}: "))
  #  notas.append(nota)
nota1 = float (input(f'informe a 1º nota: '))
notas.append(nota1)
# calcula a média final
media = sum(notas) / len(notas)

# encontra a maior nota
maior_nota = max(notas)

# encontra a menor nota
menor_nota = min(notas)

# apresenta os resultados
print(f"Média final: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
