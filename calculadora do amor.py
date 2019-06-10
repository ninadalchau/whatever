from random import randint
import time

print("Calculadora do Amor")

nome1 = input("Digite o seu nome:")
nome1 = input("Digite o outro nome:")
resultado = randint(0,100)

print("Consultando o horóscopo...")
time.sleep(1)
print("Consultando as estrelas...")
time.sleep(1)
print("Consultando o culpido...")
time.sleep(1)

if resultado <=25:
    print("Pouca probabilidade", resultado, "%")

elif resultado <=50:
    print("Pode ser que dê certo, mas talvez só amizade", resultado, "%")

elif resultado <=75:
    print("Vai dar namoro", resultado, "%")

elif resultado  <=100:
    print("É amor verdadeiro", resultado, "%")


