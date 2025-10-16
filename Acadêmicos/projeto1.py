# RPG: A Jornada em Godsgrave - Capítulo 1
# Rodar no terminal: python rpg_godsgrave.py
# Autor: (seu nome aqui)
# Observações:
# - Sistema simples de atributos/nível/XP/ouro.
# - Regras da Hydra implementadas conforme o enredo fornecido.
# - Estilo narrativo: mistura de tom épico (medieval) com linguagem leve de aventura.

import time
import random

# ---------------------------
# Utilitários de apresentação
# ---------------------------
def pausa(segundos=1.0):
    time.sleep(segundos)

def linha():
    print("-" * 60)

def estilo(texto):
    # Pequeno "embeleza" com quebras e pausa
    print(texto)
    pausa(0.9)

# ---------------------------
# Dados e configurações iniciais
# ---------------------------
MAX_LEVEL = 100
XP_POR_NIVEL = 150  # conforme especificado: 150 xp por nível

# Artefatos iniciais e seus bônus (decisão do projeto)
# Esses bônus são modestos e servem para diferenciar as classes ao início.
ARTEFATOS = {
    "mago": {
        "cajado": {"ataque": 10, "descrição": "Um cajado antigo que pulsa com energia arcana (+10 ataque)."},
        "livro": {"ataque": 8, "agilidade": 5, "descrição": "Um tomo de feitiços: sabedoria enraizada (+8 ataque, +5 agilidade)."}
    },
    "guerreiro": {
        "espada": {"ataque": 12, "descrição": "Uma espada afiada, forjada para combater (+12 ataque)."},
        "lanca": {"ataque": 10, "velocidade": 5, "descrição": "Uma lança longa que permite ataques precisos (+10 ataque, +5 velocidade)."}
    },
    "curandeiro": {
        "poção": {"defesa": 10, "descrição": "Uma poção antiga que fortalece sua resistência (+10 defesa)."},
        "amuleto": {"defesa": 8, "agilidade": 5, "descrição": "Amuleto de proteção em grupo, sussurra proteção (+8 defesa, +5 agilidade)."}
    },
    "explorador": {
        "mapa": {"agilidade": 10, "descrição": "Mapa com atalhos: encontra caminhos mais rápidos (+10 agilidade)."},
        "botas": {"velocidade": 15, "descrição": "Botas leves que aumentam sua velocidade (+15 velocidade)."}
    }
}

# Habilidades especiais por classe e descrição
HABILIDADES = {
    "mago": {"nome": "Bola de Fogo", "descrição": "Libera uma esfera flamejante que explode no alvo."},
    "guerreiro": {"nome": "Golpe Fatal", "descrição": "Um ataque bruto mirando um ponto vital."},
    "curandeiro": {"nome": "Regeneração Completa", "descrição": "Restaura forças e cura ferimentos (uso em batalha)."},
    "explorador": {"nome": "Invisibilidade", "descrição": "Suma dos olhos do inimigo e desfere um ataque surpresa."}
}

# ---------------------------
# Funções de criação de personagem
# ---------------------------
def criar_personagem():
    linha()
    estilo("🌆 Godsgrave — a cidade das mil histórias e banquetes inesquecíveis.")
    estilo("Entre nessa praça cheia de viajantes e escolha seu destino...")
    nome = input("Escolha o nome do seu herói: ").strip() or "Herói sem Nome"
    linha()
    estilo(f"Bem-vindo, {nome}. Antes de seguir, escolha sua classe:")
    classes = ["Mago", "Guerreiro", "Curandeiro", "Explorador"]
    for i, c in enumerate(classes, 1):
        print(f"{i} - {c.title()}")
    escolha = input("Digite o número da classe desejada: ").strip()
    if escolha not in ["1", "2", "3", "4"]:
        estilo("Escolha inválida. Vou definir você como Explorador por padrão.")
        classe = "Explorador"
    else:
        classe = classes[int(escolha) - 1]

    estilo(f"Você escolheu: {classe.title()}. Agora selecione um artefato inicial:")
    itens = ARTEFATOS[classe]
    chaves = list(itens.keys())
    for i, key in enumerate(chaves, 1):
        desc = itens[key]["descrição"]
        print(f"{i} - {key.title()}: {desc}")
    escolha_item = input("Digite o número do artefato desejado: ").strip()
    if escolha_item not in ["1", "2"]:
        estilo("Escolha inválida. Recebeu o primeiro item por padrão.")
        artefato = chaves[0]
    else:
        artefato = chaves[int(escolha_item) - 1]

    # Atributos base
    atributos = {
        "defesa": 30,
        "ataque": 30,
        "velocidade": 30,
        "agilidade": 30,
        "hp": 100  # HP usado para receber dano (adicionado para controle de batalha)
    }

    # Aplicar bônus do artefato escolhido
    bonus = ARTEFATOS[classe][artefato]
    for k, v in bonus.items():
        if k in atributos:
            atributos[k] += v

    personagem = {
        "nome": nome,
        "classe": classe,
        "artefato": artefato,
        "atributos": atributos,
        "nivel": 1,
        "xp": 0,
        "ouro": 0,
        "habilidade_usada": False  # controla uso único por batalha
    }

    estilo(f"\n{nome}, {classe.title()} armado com {artefato.title()}.")
    linha()
    mostrar_status_bravo(personagem)
    return personagem

def mostrar_status_bravo(p):
    a = p["atributos"]
    print(f"— {p['nome']} Lvl {p['nivel']} — Classe: {p['classe'].title()} — Artefato: {p['artefato'].title()}")
    print(f"HP: {a['hp']} | Ataque: {a['ataque']} | Defesa: {a['defesa']} | Velocidade: {a['velocidade']} | Agilidade: {a['agilidade']}")
    print(f"XP: {p['xp']} / {XP_POR_NIVEL}  | Ouro: {p['ouro']}")
    linha()

# ---------------------------
# Level up
# ---------------------------
def tentar_subir_nivel(personagem):
    while personagem["xp"] >= XP_POR_NIVEL and personagem["nivel"] < MAX_LEVEL:
        personagem["xp"] -= XP_POR_NIVEL
        personagem["nivel"] += 1
        # aumento de 10 pontos em cada atributo por nível, conforme especificado
        for stat in ["defesa", "ataque", "velocidade", "agilidade"]:
            personagem["atributos"][stat] += 10
        # opcional: aumentar HP ao subir de nível
        personagem["atributos"]["hp"] += 10
        estilo(f"✨ Parabéns! Você subiu para o nível {personagem['nivel']} — seus atributos aumentaram!")
    if personagem["nivel"] >= MAX_LEVEL:
        estilo(f"⚑ Você alcançou o nível máximo ({MAX_LEVEL}).")

# ---------------------------
# Batalha scriptada: Hydra
# ---------------------------
def capitulo_hydra(personagem):
    estilo("\n— Capítulo 1: A Caverna e a Hydra —")
    estilo("Após percorrer as ruelas e as tavernas de Godsgrave, você segue rumo à floresta.")
    estilo("Depois de alguma caminhada, entre troncos e neblina, uma boca escura se abre: uma caverna.")
    estilo("Você entra. O ar cheira a enxofre. Esconderijos e ossos quebrados no chão... algo se move nas sombras.")
    estilo("E então: três cabeças, olhos amarelos e um rugido que estremece as paredes. A HYDRA!")

    # Preparação do encontro conforme o enredo
    estilo("\nA Hydra ergue a cabeça e solta um jorro de veneno — seu ataque inicial!")
    estilo("O veneno faz com que você perca 15 pontos de defesa (por enquanto).")
    personagem["atributos"]["defesa"] -= 15
    if personagem["atributos"]["defesa"] < 0:
        personagem["atributos"]["defesa"] = 0
    mostrar_status_bravo(personagem)

    estilo("Você pode (1) Fugir para Godsgrave ou (2) Enfrentar a Hydra aqui e agora.")
    escolha = input("Escolha 1 (Fugir) ou 2 (Lutar): ").strip()
    if escolha == "1":
        estilo("\nVocê opta pela prudência: retorna a Godsgrave para descansar. Missão abortada.")
        estilo("Nenhuma recompensa ganha. Volte quando estiver mais preparado.")
        return  # fim da missão sem recompensas

    estilo("\nVocê se firma e escolhe lutar. A Hydra ruge e desfere um ataque: 'veneno cortante' — você recebe 10 de dano.")
    personagem["atributos"]["hp"] -= 10
    if personagem["atributos"]["hp"] <= 0:
        estilo("Você caiu sob o golpe mortal. Fim de jogo neste capítulo.")
        return

    # Hydra HP (scriptado para que a narrativa siga)
    hydra_hp = 100

    # Turno do jogador: especial ou normal
    estilo("\nÉ seu turno. Deseja usar (1) ataque normal (10 de dano) ou (2) sua habilidade especial (50 + 2*nivel) ?")
    escolha = input("Escolha 1 (Normal) ou 2 (Especial): ").strip()
    if escolha == "1":
        dano = 10
        hydra_hp -= dano
        estilo(f"Você desferiu um ataque normal e causou {dano} pontos de dano na Hydra.")
    elif escolha == "2":
        if personagem["habilidade_usada"]:
            estilo("Sua habilidade especial já foi usada (não pode ser usada novamente nesta batalha). Você acaba atacando normalmente.")
            dano = 10
            hydra_hp -= dano
            estilo(f"Você causou {dano} pontos de dano na Hydra.")
        else:
            dano = 50 + 2 * personagem["nivel"]
            hydra_hp -= dano
            personagem["habilidade_usada"] = True
            estilo(f"Você utilizou sua habilidade especial ({HABILIDADES[personagem['classe']]['nome']}) e causou {dano} de dano!")
    mostrar_status_bravo(personagem)
    estilo(f"Vida restante da Hydra (estimada): {hydra_hp}")

    # Depois do primeiro turno do jogador, a Hydra usa 'abraço da morte' (cinematizado)
    estilo("\nA Hydra recua e, com um movimento horrendo, usa 'Abraço da Morte' — todas as cabeças se aproximam para esmagar você.")
    estilo("Você pode (1) Desviar do abraço (contra-ataque) ou (2) Atacar diretamente (apontando para um ponto vital).")
    escolha = input("Escolha 1 (Desviar) ou 2 (Atacar): ").strip()

    if escolha == "2":
        # O jogador acerta ponto vital e vence a batalha de forma cinematográfica
        estilo("\nVocê reúne coragem e mira num ponto cego entre as cabeças. Um golpe perfeito... a Hydra cai!")
        estilo("A batalha terminou com sua ousadia. Vitória conquistada.")
        recompensa_final_escolha(personagem, escolha_final="atacar")
        return

    # Se desviar
    estilo("\nVocê escapa do abraço no último segundo e desfere um contra-ataque, causando 20 de dano (bônus de contra-ataque).")
    hydra_hp -= 20
    estilo(f"Vida restante da Hydra (estimada): {hydra_hp}")
    mostrar_status_bravo(personagem)

    # Hydra lança outro ataque de veneno
    estilo("\nA Hydra solta outro jato de veneno — você sofre mais 10 de dano.")
    personagem["atributos"]["hp"] -= 10
    if personagem["atributos"]["hp"] <= 0:
        estilo("O veneno foi demais. Você não resistiu. Fim do capítulo.")
        return
    mostrar_status_bravo(personagem)

    # Último turno: escolher entre atacar repetidamente ou achar brecha
    estilo("\nÚltima chance! Você pode (1) atacar repetidamente com tudo o que tem ou (2) procurar a brecha para um ataque certeiro.")
    escolha = input("Escolha 1 (Atacar repetidamente) ou 2 (Procurar brecha): ").strip()
    if escolha == "1":
        estilo("\nVocê avança em fúria, golpe após golpe. Finalmente a Hydra sucumbe aos seus ataques!")
        # Recompensa: 150 ouro, armadura de escamas de dragão (+50 defesa) e 200 xp
        personagem["ouro"] += 150
        personagem["atributos"]["defesa"] += 50  # armadura de escamas
        personagem["xp"] += 200
        estilo("🏆 Recompensa: 150 de ouro, Armadura de Escamas de Dragão (+50 defesa) e 200 XP.")
        personagem["habilidade_usada"] = False  # reset para próximas batalhas
        tentar_subir_nivel(personagem)
        mostrar_status_bravo(personagem)
        estilo("Missão finalizada. Sua lenda em Godsgrave começa a crescer. A próxima missão aguarda...")
        return
    else:
        estilo("\nVocê observa, respira fundo e procura pela fresta entre as escamas. Encontra o ponto fraco!")
        estilo("Um ataque certeiro: a Hydra cai, derrotada por sua determinação e astúcia.")
        # Recompensa: 150 ouro, cajado mágico (+50 ataque) e 200 xp
        personagem["ouro"] += 150
        personagem["atributos"]["ataque"] += 50  # cajado mágico
        personagem["xp"] += 200
        estilo("🏆 Recompensa: 150 de ouro, Cajado Mágico (+50 ataque) e 200 XP.")
        personagem["habilidade_usada"] = False
        tentar_subir_nivel(personagem)
        mostrar_status_bravo(personagem)
        estilo("Missão finalizada. Há sussurros sobre novas ameaças além da caverna...")
        return

# ---------------------------
# Recompensas alternativas (quando o jogador acertou vital com 'atacar' na fase abraço)
# ---------------------------
def recompensa_final_escolha(personagem, escolha_final):
    # Quando o jogador derrotou a Hydra atacando no abraço (final cinematográfico),
    # damos as mesmas recompensas que os finais principais (vamos oferecer uma escolha simbólica)
    estilo("\nAo derrotar a Hydra, você recolhe tesouros e troféus do monstro.")
    estilo("Escolha sua recompensa entre as opções disponíveis:")
    print("1 - Armadura de Escamas de Dragão (+50 defesa)  —  +150 ouro, +200 XP")
    print("2 - Cajado Mágico (+50 ataque)                 —  +150 ouro, +200 XP")
    escolha = input("Digite 1 ou 2 para escolher sua recompensa: ").strip()
    if escolha == "1":
        personagem["ouro"] += 150
        personagem["atributos"]["defesa"] += 50
        personagem["xp"] += 200
        estilo("Você escolheu a Armadura de Escamas. Força e resistência agora vestem suas costas.")
    else:
        personagem["ouro"] += 150
        personagem["atributos"]["ataque"] += 50
        personagem["xp"] += 200
        estilo("Você escolheu o Cajado Mágico. As runas brilham em suas mãos.")
    personagem["habilidade_usada"] = False
    tentar_subir_nivel(personagem)
    mostrar_status_bravo(personagem)
    estilo("Missão finalizada. A cidade de Godsgrave aguarda as notícias da sua vitória.")

# ---------------------------
# Fluxo principal do jogo
# ---------------------------
def main():
    personagem = criar_personagem()
    estilo("\nVocê decide partir para a aventura: rumo à floresta fora de Godsgrave.")
    pausa(1.2)
    capitulo_hydra(personagem)
    estilo("\nObrigado por jogar o Capítulo 1 — A Jornada em Godsgrave")
    linha()

if __name__ == "__main__":
    main()
