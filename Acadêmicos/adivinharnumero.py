# Adivinhar o número (sem else/elif, sem laços, sem funções)
numero_secreto = 7
tentativas = 0

# Tentativa 1
palpite = int(input("Adivinhe o número (entre 1 e 10): "))
tentativas = tentativas + 1

if palpite < 1 or palpite > 10:
    print("Palpite inválido!")
if palpite >= 1:
    if palpite <= 10:
        if palpite == numero_secreto:
            print(f"Acertou! Você usou {tentativas} tentativa(s).")
        if palpite < numero_secreto:
            print("Muito baixo!")
        if palpite > numero_secreto:
            print("Muito alto!")

# Tentativa 2
palpite = int(input("Adivinhe o número (entre 1 e 10): "))
tentativas = tentativas + 1

if palpite < 1 or palpite > 10:
    print("Palpite inválido!")
if palpite >= 1:
    if palpite <= 10:
        if palpite == numero_secreto:
            print(f"Acertou! Você usou {tentativas} tentativa(s).")
        if palpite < numero_secreto:
            print("Muito baixo!")
        if palpite > numero_secreto:
            print("Muito alto!")

# Tentativa 3 (mais blocos iguais se quiser aumentar)
palpite = int(input("Adivinhe o número (entre 1 e 10): "))
tentativas = tentativas + 1

if palpite < 1 or palpite > 10:
    print("Palpite inválido!")
if palpite >= 1:
    if palpite <= 10:
        if palpite == numero_secreto:
            print(f"Acertou! Você usou {tentativas} tentativa(s).")
        if palpite < numero_secreto:
            print("Muito baixo!")
        if palpite > numero_secreto:
            print("Muito alto!")

