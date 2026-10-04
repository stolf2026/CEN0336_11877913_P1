#!/usr/bin/env python3

print('Script de conversão de temperaturas em Celsius pra Fahrenheit')
print() #Espaço para estética

#Solicitação de entrada ao usuário
string_celsius = input('Digite as temperatura em °Celsius separadas por espaço')

#Converter string em lista
lista_celsius = string_celsius.split()

temp_dict={} #Criar dicionário para armazenar valores em ambas escalas de temperatura

#Cálculo da temperatura em °Fahrenheit
count = 0 #Adicionado para contar quantos valores não numéricos o usuário forneceu e usar para obter contagem correta das temperaturas fornecidas
for temp in lista_celsius:
	if temp.replace('.', '', 1).replace('-', '', 1).isdigit() and temp not in ('.', '-', '-.'): #Ajuste do número para testar se o valor é numérico

		#Conversão em número flutuante
		temp_num = float(temp)
		fahrenheit = (9/5*temp_num)+32 #Conversão na outra escala

		#Guadar no dicionário
		temp_dict[temp] = fahrenheit
	else: #Indicar ao usuário no caso de valores não numéricos, onde estão.
		for i, valor in enumerate(lista_celsius):
			if valor == temp:
				count+=1
				print(f'O valor de índice python {i} ("{temp}") não é numérico, reexecute a análise somente com valores numéricos!')

tamanho = len(lista_celsius)-count #Leitura do tamanho de temperaturadas imputadas, desconsiderando valores não numéricos
print(f'A seguir está a tabela com as {tamanho} temperaturas em celsius e fahrenheit')
print() #Espaço para estética

#Apresentação da tabela ao usuário em ambas escalas
print('Tabela de temperaturas em ambas escalas') #Titulo da tabela
print('°C = Celsius; °F = Fahrenheit')
for Celsius, Fahrenheit in temp_dict.items(): #Uso da função que pega pares chave valor do dicionário para plotar a tabela
    print(f' {Celsius} °C      {Fahrenheit} °F') #Legenda para o usuário
print() #Espaço para estética
print('__________________________________________')
print('______________Fim do script_______________')


