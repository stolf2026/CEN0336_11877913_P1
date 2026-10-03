#!/usr/bin/env python3
import sys
a = sys.argv[1]
b = sys.argv[2]

#Indicação da formatação necessária ao usuário
print('______SCRIPT DE QUADRADO DA HIPOTENUSA (somente inteiros <500)________')
print('Utilizando os valores para o cálculo do quadrado da hipotenusa: a b (um espaço após o nome do script)')
print('___________________________________________')

# Checagem de valores fornecidos pelo usuário
print('________checando valores__________')
if a.isdigit() and b.isdigit() and int(a) < 500 and int(b) < 500:
    print('Os valores são números inteiros válidos')
else:
    print('Erro: o usuário forneceu um valor não numérico, não inteiro ou >= 500.')

#Conversão em inteiro
a = int(a)
b = int(b)

print('____________Calculando..._____________')

#Cálculos matemáticos
qa = a**2 #cálculo do quadrado de a
qb = b**2 #cálculo do quadrado de b
qc = qa + qb #cálculo do quadrado de c
c = qc**0.5 #cálculo da raiz qadrada do quadrado de c (hipotenusa)

#Impressão dos resultados dos cálculos, para o usuário
print(f'O quadrado da hipotenusa para o triangulo retângulo com lados a= {a} e b= {b}, é {qc}')
print(f'Já o valor da hipotenusa é: {c}')
print('_________Fim do script__________')

