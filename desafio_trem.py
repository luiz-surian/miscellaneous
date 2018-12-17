#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Desafio Matemático do Trem"""

__author__ = 'Luiz Fernando Surian Filho'

import os
import random

passageiros = 0
estacoes = 0
entram = 0
saem = 0


def display_title():
    # Limpa a tela do terminal, e mostra o título.
    os.system('cls')
    print("""
╔══════════════════════════════════════════════════════╗
║              Desafio Matemático do Trem              ║
╚══════════════════════════════════════════════════════╝
""")


def calc_movement():
    saem = random.randint(0, 10)
    entram = saem + random.randint(1, 4)
    return (entram, saem)


def verifica_quantidade(value, verb=['single', 'plural']):
    if value == 0:
        return f'não {verb[0]} nenhum passageiro'
    if value == 1:
        return f'{verb[0]} apenas um passageiro'
    else:
        return f'{verb[1]} {value} passageiros'


# Início do desafio.
# Valores iniciais.
estacoes = random.randint(6, 14)
passageiros = random.randint(80, 200)

entram, saem = calc_movement()
display_title()
print(f"""
Um trem possui {passageiros} passageiros e está a caminho da próxima estação.
Em sua primeira parada, {verifica_quantidade(entram, ['entrou', 'entraram'])},
e {verifica_quantidade(saem, ['saiu', 'saíram'])}.
""")
passageiros += entram
passageiros -= saem
# print('DEBUG | Estações:', estacoes, '| Passageiros:', passageiros)
os.system('pause')

for estacao in range(1, estacoes):
    entram, saem = calc_movement()
    display_title()
    print(f"""
Na próxima estação, {verifica_quantidade(entram, ['entrou', 'entraram'])},
e {verifica_quantidade(saem, ['saiu', 'saíram'])}.
""")
    passageiros += entram
    passageiros -= saem
    # print('DEBUG | Estações:', estacoes, '| Passageiros:', passageiros)
    os.system('pause')

# Fim do loop.
display_title()
print(f"""
Agora a pergunta...
""")
os.system('pause')

display_title()
resposta = input('Em quantas estações o trem parou? ')

display_title()
if int(resposta) == estacoes:
    print(f"""
ACERTOU! O trem parou em {estacoes}.
Parabéns! Você realmente prestou atenção!
""")
else:
    print(f"""
ERROU! O trem parou em {estacoes}.
Não era bem essa a pergunta que esperava, não é mesmo?
""")
os.system('pause')
