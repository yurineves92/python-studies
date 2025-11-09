# Módulo Math
import math

print(f"Pi: {math.pi}")
print(f"Raiz quadrada de 16: {math.sqrt(16)}")
print(f"Seno de 90. {math.sin(math.radians(90))}")

import random

# Módulo random
print(f"Número aleatório: {random.randint(1, 100)}")
print(f"Escolha aleatória: {random.choice(['pedra', 'papel', 'tesoura'])}")

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista embaralhada: {numeros}")

from datetime import datetime, timedelta

agora = datetime.now()
print(f"Data e hora atual: {agora}")
print(f"Apenas a data: {agora.date()}")
print(f"Apenas a hora: {agora.time()}")

amanha = agora + timedelta(days=1)
print(f"Amanhã: {amanha.date()}")

import os

print(f"Diretório atual: {os.getcwd()}")
print(f"Arquivos no diretório: {os.listdir('.')}")