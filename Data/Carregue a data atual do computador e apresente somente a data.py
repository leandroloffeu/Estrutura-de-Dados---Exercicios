#Carregue a data atual do computador e apresente somente a data

import datetime

dataatual = datetime.date.today() #obtém a data atual usando a função today()
dataformatada = dataatual.strftime('%d') #strftime("%d/%m/%Y") converte a data futura em uma string formatada no formato dia/mês/ano.

print("A data atual é:", (dataformatada))
