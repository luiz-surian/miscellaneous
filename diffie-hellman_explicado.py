#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Explicando Diffie-Hellman.

Este código tem o propósito de explicar o método Diffie-Hellman de
uma maneira simples, portanto não se preocupa com eficiência, velocidade,
segurança e/ou recursos computacionais. Não deve ser usado em aplicações reais.

Wikipedia:
"A troca de chaves de Diffie-Hellman é um método de criptografia específico
para troca de chaves desenvolvido por Whitfield Diffie e Martin Hellman
e publicado em 1976. Foi um dos primeiros exemplos práticos de métodos
de troca de chaves implementado dentro do campo da criptografia.
O método da troca de chaves de Diffie-Hellman permite que duas partes
que não possuem conhecimento a priori de cada uma,
compartilhem uma chave secreta sob um canal de comunicação inseguro.
Tal chave pode ser usada para encriptar mensagens posteriores usando
um esquema de cifra de chave simétrica."
[https://pt.wikipedia.org/wiki/Diffie-Hellman]
"""

__author__ = 'Luiz Fernando Surian Filho'

import hashlib
import time
import os

wait = time.sleep
timer = 1.8

print('Aline quer mandar o convite da sua festa de aniversário para Bruno.')
wait(timer)
print('Mas tem medo que Carlos roube a informação antes de chegar a Bruno.')
wait(timer)
print('Ela decide proteger sua comunicação usando uma chave privada que')
wait(timer)
print('apenas Aline e Bruno conheçam, assim ninguém mais poderá ler as')
wait(timer)
print('mensagens que forem trocadas entre os dois.\n')
wait(timer)
wait(timer)
print('Mas eles não possuem uma chave em comum...')
wait(timer)
print('Como enviar uma sem correr o mesmo risco de Carlos')
wait(timer)
print('ou outra pessoa roubar a chave?\n')
wait(timer)
wait(timer)
print('Para solucionar este problema, iremos utilizar o método Diffie-Hellman')
wait(timer)
print('Assim é possível gerar a mesma chave privada entre os dois')
wait(timer)
print('em um canal público e/ou inseguro.\n')
wait(timer)

os.system('pause')
print('\n')

print('Primeiro vamos definir dois números que serão públicos:')
wait(timer)

p = 7919
print(f'Um número primo, vamos chamá-lo de "p"')
wait(timer)
print(f'p = {p}')
wait(timer)

g = 251
print(f'E um número que será usado como base em uma potência,')
wait(timer)
print('vamos chama-lo de "g"')
wait(timer)
print(f'g = {g}\n')
wait(timer)

os.system('pause')
print('\n')

print('Agora cada um dos dois irá escolher um número, sem compartilhar.')
wait(timer)

print(f'Aline terá um número "a"')
wait(timer)
a = 5869
print(f'a = {a}')
wait(timer)

print(f'Bruno terá um número "b"')
wait(timer)
b = 4943
print(f'b = {b}\n')
wait(timer)

os.system('pause')
print('\n')

print('Aline utiliza a base pública, elevado ao seu número privado')
wait(timer)
print('e pega a sobra da divisão com o número primo público.')
wait(timer)
print('A = g^a mod p')
wait(timer)
print(f'A = {g}^{a} mod {p}')
wait(timer)
A = (g ** a) % p
print(f'A = {A}')
wait(timer)
print('Aline manda seu novo número (A) para Bruno\n')
wait(timer)

os.system('pause')
print('\n')

print('Bruno utiliza a base pública, elevado ao seu número privado')
wait(timer)
print('e pega a sobra da divisão com o número primo público.')
wait(timer)
print('B = g^b mod p')
wait(timer)
print(f'B = {g}^{b} mod {p}')
wait(timer)
B = (g ** b) % p
print(f'B = {B}')
wait(timer)
print('Bruno manda seu novo número (B) para Aline\n')
wait(timer)

os.system('pause')
print('\n')

print('Aline calcula o número secreto dos dois,')
wait(timer)
print('utilizando o número que recebeu de Bruno como base,')
wait(timer)
print('elevado a seu próprio número inicial,')
wait(timer)
print('e pega a sobra da divisão com o número primo público.')
wait(timer)
print('segredo_aline = B^a mod p')
wait(timer)
print(f'segredo_aline = {B}^{a} mod {p}')
wait(timer)
segredo_aline = (B ** a) % p
print(f'segredo_aline = {segredo_aline}\n')
wait(timer)

os.system('pause')
print('\n')

print('Bruno calcula o número secreto dos dois,')
wait(timer)
print('utilizando o número que recebeu de Aline como base,')
wait(timer)
print('elevado a seu próprio número inicial,')
wait(timer)
print('e pega a sobra da divisão com o número primo público.')
wait(timer)
print('Bruno deverá chegar ao mesmo resultado que Aline.')
wait(timer)
print('segredo_bruno = A^b mod p')
wait(timer)
print(f'segredo_bruno = {A}^{b} mod {p}')
wait(timer)
segredo_bruno = (A ** b) % p
print(f'segredo_bruno = {segredo_bruno}\n')
wait(timer)

os.system('pause')
print('\n')

print('Este número ou semente (seed) pode ser')
wait(timer)
print('utilizado para gerar uma chave criptográfica.\n')
wait(timer)
print('Vamos gerar um hash do número de Aline:')
wait(timer)
hash_aline = hashlib.sha256(
    str(segredo_aline).encode()
).hexdigest()
print(f'sha256(segredo_aline) =\n\t{hash_aline}\n')
wait(timer)
print('Agora vamos gerar o hash do número de Bruno:')
wait(timer)
hash_bruno = hashlib.sha256(
    str(segredo_bruno).encode()
).hexdigest()
print(f'sha256(segredo_bruno) =\n\t{hash_bruno}\n')
wait(timer)

os.system('pause')
print('\n')
print('Resolvido! Agora Aline e Bruno possuem a mesma chave')
wait(timer)
print('e podem trocar mensagens sem a interferência de Carlos.\n')
wait(timer)
os.system('pause')
