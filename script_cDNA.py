#!/usr/bin/env python3
import sys

print('IDENTIFICADOR DE CDS (gDNA EUCARIOTOS)')
print('Uso: script_CDS.py [sequencia] [n1] [n2] [n3] [n4] [n5] [n6]')

# Conferir quantidade de argumentos (script + 7 argumentos = 8)

if len(sys.argv) == 8:
    pass
else:
    print('Erro: forneça exatamente 7 argumentos: sequência + 6 números.')
    sys.exit(1)

sequencia = sys.argv[1]
numeros = sys.argv[2:8]

# Conferir se a sequência não está vazia

if len(sequencia) > 0:
    pass
else:
    print('Erro: a sequência está vazia.')
    sys.exit(1)

# Padronizar para maiúsculas
sequencia = sequencia.upper()

# Conferir que a sequência só contém A, C, T, G

for base in sequencia:
    if base in 'ACTG':
        pass
    else:
        print(f'Erro: caractere inválido na sequência: {base}')
        sys.exit(1)

# Conferir que cada argumento numérico é inteiro (isdigit)

for valor in numeros:
    if valor.isdigit():
        pass
    else:
        print(f'Erro: "{valor}" não é um número inteiro válido.')
        sys.exit(1)

# Converter para int
n1 = int(numeros[0])
n2 = int(numeros[1])
n3 = int(numeros[2])
n4 = int(numeros[3])
n5 = int(numeros[4])
n6 = int(numeros[5])

# Conferir que nenhum índice é maior que o tamanho da sequência

tamanho = len(sequencia)

if n1 > tamanho or n2 > tamanho or n3 > tamanho or n4 > tamanho or n5 > tamanho or n6 > tamanho:
    print(f'Erro: algum índice é maior que o tamanho da sequência ({tamanho}).')
    sys.exit(1)

if n1 >= n2 or n3 >= n4 or n5 >= n6:
    print('Erro: em cada par, o início deve ser menor que o fim.')
    sys.exit(1)

print('Dados válidos.')

# Extração das três CDS com coordenadas biológicas

cds1 = sequencia[n1-1:n2]
cds2 = sequencia[n3-1:n4]
cds3 = sequencia[n5-1:n6]

print('CDS1:', cds1)
print('CDS2:', cds2)
print('CDS3:', cds3)

# Conferir códon de início em CDS1 e códon de parada em CDS3

inicio_ok = cds1.startswith('ATG')
parada_ok = cds3.endswith(('TAG', 'TAA', 'TGA'))

if inicio_ok and parada_ok:
    cds_completa = cds1 + cds2 + cds3
    print('Sequência codante (CDS completa):', cds_completa)
else:
    if inicio_ok:
        pass
    else:
        print('CDS1 não inicia com o códon de início ATG.')
    if parada_ok:
        pass
    else:
        print('CDS3 não termina com um códon de parada (TAG, TAA ou TGA).')
    print('Os índices fornecidos não permitem a remoção de íntrons.')
