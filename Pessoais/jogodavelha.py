#jogo da velha
import random

# Cria o tabuleiro
tabuleiro = [" "] * 9

def mostrar_tabuleiro():
    print(f"""
     {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
    ---+---+---
     {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
    ---+---+---
     {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
    """)

def verificar_vitoria(simbolo):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],  # Linhas
        [0,3,6], [1,4,7], [2,5,8],  # Colunas
        [0,4,8], [2,4,6]            # Diagonais
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == simbolo:
            return True
    return False

def posicoes_livres():
    return [i for i, v in enumerate(tabuleiro) if v == " "]

# Loop principal
print("🎮 Bem-vindo ao Jogo da Velha!")
print("Você é o X e joga primeiro.")
jogador = "X"
computador = "O"

for rodada in range(9):
    mostrar_tabuleiro()
    
    # Vez do jogador
    if jogador == "X":
        try:
            pos = int(input("Escolha uma posição (1-9): ")) - 1
            if pos not in range(9) or tabuleiro[pos] != " ":
                print("Posição inválida! Tente novamente.")
                continue
        except:
            print("Entrada inválida! Digite um número de 1 a 9.")
            continue
        tabuleiro[pos] = "X"
    else:
        # IA escolhe posição aleatória livre
        pos = random.choice(posicoes_livres())
        tabuleiro[pos] = "O"
        print(f"\n🤖 O computador jogou na posição {pos + 1}")

    # Verifica vitória
    if verificar_vitoria(jogador):
        mostrar_tabuleiro()
        if jogador == "X":
            print("🎉 Parabéns! Você venceu!")
        else:
            print("💻 O computador venceu!")
        break

    # Troca de turno
    jogador = "O" if jogador == "X" else "X"

else:
    mostrar_tabuleiro()
    print("😐 Empate!")
