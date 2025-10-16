#pedra papel e tesoura
import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    
    print("=== Jogo: Pedra, Papel e Tesoura ===")
    print("Digite sua escolha: pedra, papel ou tesoura")
    
    jogador = input("Sua escolha: ").lower()
    while jogador not in opcoes:
        jogador = input("Opção inválida! Escolha entre pedra, papel ou tesoura: ").lower()
    
    computador = random.choice(opcoes)
    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

#Executa o jogo
jogar()            