pares = 0

for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        pares += 1

print(f"{pares} valores pares")