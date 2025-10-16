# RPG: A Jornada em Godsgrave - Capítulo 1 + Mercado
# Autor: (seu nome aqui)
# Linguagem: Python
# Projeto de Introdução à Computação
# -------------------------------
# Recursos:
# - Criação de personagem com classes, artefatos e atributos
# - Sistema de XP / nível / ouro
# - Mercado com compras e bônus permanentes
# - Batalha com narrativa (Hydra)
# - Habilidade especial única por batalha
# -------------------------------

import time
import random

# --------------------------------
# Funções auxiliares de estilo
# --------------------------------
def pausa(segundos=1.0):
    time.sleep(segundos)

def linha():
    print("-" * 60)

def estilo(texto):
    print(texto)
    pausa(0.8)

# --------------------------------
# Configurações gerais
# --------------------------------
MAX_LEVEL = 100
XP_POR_NIVEL = 150

ARTEFATOS = {
    "mago": {
        "cajado": {"ataque": 10, "descricao": "Um cajado antigo que pulsa com energia arcana (+10 ataque)."},
        "livro": {"ataque": 8, "agilidade": 5, "descricao": "Um tomo de feitiços: sabedoria enraizada (+8 ataque, +5 agilidade)."}
    },
    "guerreiro": {
        "espada": {"ataque": 12, "descricao": "Uma espada afiada, forjada para combater (+12 ataque)."},
        "lanca": {"ataque": 10, "velocidade": 5, "descricao": "Uma lança longa e ágil (+10 ataque, +5 velocidade)."}
    },
    "curandeiro": {
        "poção": {"defesa": 10, "descricao": "Poção antiga que reforça sua resistência (+10 defesa)."},
        "amuleto": {"defesa": 8, "agilidade": 5, "descricao": "Amuleto de proteção em grupo (+8 defesa, +5 agilidade)."}
    },
    "explorador": {
        "mapa": {"agilidade": 10, "descricao": "Mapa com atalhos secretos (+10 agilidade)."},
        "botas": {"velocidade": 15, "descricao": "Botas leves de couro (+15 velocidade)."}
    }
}

HABILIDADES = {
    "mago": {"nome": "Bola de Fogo", "descricao": "Lança uma esfera flamejante devastadora."},
    "guerreiro": {"nome": "Golpe Fatal", "descricao": "Ataque brutal mirando um ponto vital."},
    "curandeiro": {"nome": "Regeneração Completa", "descricao": "Restaura grande parte da vida."},
    "explorador": {"nome": "Invisibilidade", "descricao": "Fica invisível por um instante e ataca furtivamente."}
}

# --------------------------------
# Funções principais
# --------------------------------
def criar_personagem():
    linha()
    estilo("🌆 Godsgrave — a cidade das mil histórias e tavernas iluminadas por velas.")
    estilo("Entre e escolha seu destino...")

    nome = input("Escolha o nome do seu herói: ").strip() or "Herói sem Nome"
    linha()

    classes = ["mago", "guerreiro", "curandeiro", "explorador"]
    estilo("Escolha sua classe:")
    for i, c in enumerate(classes, 1):
        print(f"{i} - {c.title()}")
    escolha = input("Classe: ").strip()
    classe = classes[int(escolha) - 1] if escolha in ["1", "2", "3", "4"] else "explorador"

    estilo(f"Você escolheu {classe.title()}. Agora selecione um artefato inicial:")
    itens = ARTEFATOS[classe]
    chaves = list(itens.keys())
    for i, key in enumerate(chaves, 1):
        print(f"{i} - {key.title()}: {itens[key]['descricao']}")
    escolha_item = input("Artefato: ").strip()
    artefato = chaves[int(escolha_item) - 1] if escolha_item in ["1", "2"] else chaves[0]

    atributos = {"defesa": 30, "ataque": 30, "velocidade": 30, "agilidade": 30, "hp": 100}

    # aplica bônus do artefato
    for k, v in ARTEFATOS[classe][artefato].items():
        if k in atributos:
            atributos[k] += v

    personagem = {
        "nome": nome,
        "classe": classe,
        "artefato": artefato,
        "atributos": atributos,
        "nivel": 1,
        "xp": 0,
        "ouro": 200,  # começa com 200 moedas
        "habilidade_usada": False
    }

    estilo(f"\n{nome}, {classe.title()} empunhando seu {artefato.title()}, inicia sua jornada!")
    mostrar_status(personagem)
    return personagem

def mostrar_status(p):
    a = p["atributos"]
    print(f"\n— {p['nome']} | Nível {p['nivel']} | Classe: {p['classe'].title()} | Ouro: {p['ouro']}")
    print(f"HP: {a['hp']} | Ataque: {a['ataque']} | Defesa: {a['defesa']} | Velocidade: {a['velocidade']} | Agilidade: {a['agilidade']}")
    print(f"XP: {p['xp']} / {XP_POR_NIVEL}")
    linha()

def tentar_subir_nivel(p):
    while p["xp"] >= XP_POR_NIVEL and p["nivel"] < MAX_LEVEL:
        p["xp"] -= XP_POR_NIVEL
        p["nivel"] += 1
        for stat in ["defesa", "ataque", "velocidade", "agilidade"]:
            p["atributos"][stat] += 10
        p["atributos"]["hp"] += 10
        estilo(f"✨ {p['nome']} subiu para o nível {p['nivel']}! A força cresce em suas veias.")

# --------------------------------
# MERCADO
# --------------------------------
def mercado(personagem):
    linha()
    estilo("🏪 Bem-vindo ao Mercado de Godsgrave!")
    estilo("O comerciante gorducho sorri: 'Tenho o que você precisa, aventureiro!'")
    itens = {
        "1": {"nome": "Poção de Vida", "preco": 50, "efeito": ("hp", 30)},
        "2": {"nome": "Aprimorar Ataque (+10)", "preco": 100, "efeito": ("ataque", 10)},
        "3": {"nome": "Aprimorar Defesa (+10)", "preco": 100, "efeito": ("defesa", 10)},
        "4": {"nome": "Aprimorar Agilidade (+10)", "preco": 100, "efeito": ("agilidade", 10)},
        "5": {"nome": "Sair do mercado", "preco": 0, "efeito": None}
    }

    while True:
        mostrar_status(personagem)
        for i, item in itens.items():
            print(f"{i} - {item['nome']} (💰 {item['preco']})")
        escolha = input("O que deseja comprar? ").strip()
        if escolha == "5":
            estilo("Você se despede do comerciante e volta à jornada.")
            break
        if escolha not in itens:
            estilo("Escolha inválida.")
            continue

        item = itens[escolha]
        if personagem["ouro"] < item["preco"]:
            estilo("Você não tem ouro suficiente!")
            continue

        personagem["ouro"] -= item["preco"]
        atributo, valor = item["efeito"]
        personagem["atributos"][atributo] += valor
        estilo(f"Você comprou {item['nome']}! (+{valor} em {atributo.upper()})")

# --------------------------------
# BATALHA: Hydra
# --------------------------------
def capitulo_hydra(personagem):
    estilo("\n🌫️ Capítulo 1: A Caverna e a Hydra 🌫️")
    estilo("Você caminha pela floresta sombria até encontrar uma caverna coberta por névoa.")
    estilo("Três olhos brilhantes o encaram no escuro... A HYDRA desperta!")

    # ataque inicial
    estilo("A Hydra lança um jato de veneno! Sua defesa é reduzida em 15 pontos.")
    personagem["atributos"]["defesa"] = max(0, personagem["atributos"]["defesa"] - 15)
    mostrar_status(personagem)

    estilo("Deseja (1) Fugir para Godsgrave ou (2) Lutar?")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        estilo("Você recua para a cidade. Missão abortada.")
        return

    estilo("Você decide lutar bravamente!")
    personagem["atributos"]["hp"] -= 10
    estilo("A Hydra usa 'Veneno Cortante'! Você sofre 10 de dano.")
    if personagem["atributos"]["hp"] <= 0:
        estilo("Você caiu. Fim de jornada.")
        return

    hydra_hp = 100
    estilo("Seu turno! (1) Ataque normal (10 dano) | (2) Habilidade especial (50 + 2*Nível de dano)")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        dano = 10
    else:
        if personagem["habilidade_usada"]:
            estilo("Sua habilidade já foi usada nesta batalha! Você ataca normalmente.")
            dano = 10
        else:
            dano = 50 + 2 * personagem["nivel"]
            personagem["habilidade_usada"] = True
            estilo(f"Você usou {HABILIDADES[personagem['classe']]['nome']} causando {dano} de dano!")

    hydra_hp -= dano
    estilo(f"A Hydra agora tem cerca de {hydra_hp} de HP restante.")
    mostrar_status(personagem)

    # fase do abraço da morte
    estilo("A Hydra tenta um 'Abraço da Morte'!")
    estilo("Você (1) Desvia para contra-atacar ou (2) Mira em um ponto vital?")
    escolha = input("Escolha: ").strip()

    if escolha == "2":
        estilo("Você encontra o ponto vital e golpeia — a Hydra ruge e desaba!")
        recompensa_final(personagem, "atacar")
        return
    else:
        estilo("Você desvia e desfere um contra-ataque causando +20 de dano!")
        hydra_hp -= 20
        personagem["atributos"]["hp"] -= 10
        estilo("A Hydra lança mais veneno! Você perde 10 de HP.")
        if personagem["atributos"]["hp"] <= 0:
            estilo("Você sucumbe ao veneno... Fim de jogo.")
            return

    # último turno
    estilo("Última chance! (1) Ataques repetidos ou (2) Procurar brecha mortal?")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        estilo("Você golpeia furiosamente até a Hydra cair!")
        personagem["ouro"] += 150
        personagem["atributos"]["defesa"] += 50
        personagem["xp"] += 200
        estilo("🏆 Recompensa: +150 ouro, Armadura de Escamas (+50 defesa), +200 XP.")
    else:
        estilo("Você acha a brecha e atinge o coração da criatura!")
        personagem["ouro"] += 150
        personagem["atributos"]["ataque"] += 50
        personagem["xp"] += 200
        estilo("🏆 Recompensa: +150 ouro, Cajado Mágico (+50 ataque), +200 XP.")

    personagem["habilidade_usada"] = False
    tentar_subir_nivel(personagem)
    mostrar_status(personagem)
    estilo("Missão concluída! A cidade ouvirá sobre seu feito.")

def recompensa_final(personagem, tipo):
    personagem["ouro"] += 150
    personagem["xp"] += 200
    if tipo == "atacar":
        personagem["atributos"]["ataque"] += 50
    else:
        personagem["atributos"]["defesa"] += 50
    tentar_subir_nivel(personagem)
    mostrar_status(personagem)

# --------------------------------
# Fluxo Principal
# --------------------------------
def main():
    personagem = criar_personagem()
    mercado(personagem)
    capitulo_hydra(personagem)
    estilo("🏁 Fim do Capítulo 1 — A Jornada em Godsgrave")

if __name__ == "__main__":
    main()
