import time
import random

# Funções auxiliares de estilo

def pausa(segundos=1.0):
    time.sleep(segundos)

def linha():
    print("-" * 60)

def estilo(texto):
    print(texto)
    pausa(0.8)

# Configurações gerais

MAX_LEVEL = 100
XP_POR_NIVEL = 150

ARTEFATOS = {
    "Mago": {
        "cajado": {"ataque": 10, "descricao": "Um cajado antigo que pulsa com energia arcana (+10 ataque)."},
        "livro": {"ataque": 8, "agilidade": 5, "descricao": "Um tomo de feitiços: sabedoria enraizada (+8 ataque, +5 agilidade)."}
    },
    "Guerreiro": {
        "espada": {"ataque": 12, "descricao": "Uma espada afiada, forjada para combater (+12 ataque)."},
        "lança": {"ataque": 10, "velocidade": 5, "descricao": "Uma lança longa que permite ataques precisos (+10 ataque, +5 velocidade)."}
    },
    "Curandeiro": {
        "poção": {"defesa": 10, "descricao": "Poção antiga que reforça sua resistência (+10 defesa)."},
        "amuleto": {"defesa": 8, "agilidade": 5, "descricao": "Amuleto de proteção em grupo, sussurra proteção (+8 defesa, +5 agilidade)."}
    },
    "Explorador": {
        "mapa": {"agilidade": 10, "descricao": "Mapa com atalhos: encontra caminhos mais rápidos e secretos (+10 agilidade)."},
        "botas": {"velocidade": 15, "descricao": "Botas leves de couro que aumentam sua velocidade (+15 velocidade)."}
    }
}

HABILIDADES = {
    "Mago": {"nome": "Bola de Fogo", "descricao": "Lança uma esfera flamejante devastadora que atinge o alvo."},
    "Guerreiro": {"nome": "Golpe Fatal", "descricao": "Ataque brutal mirando um ponto vital."},
    "Curandeiro": {"nome": "Regeneração Completa", "descricao": "Restaura forças e cura ferimentos (uso em batalha)."},
    "Explorador": {"nome": "Invisibilidade", "descricao": "Suma dos olhos do inimigo e desfere um ataque surpresa."}
}

# Funções principais

def criar_personagem():
    linha()
    estilo("🌆 Godsgrave — a cidade das mil histórias e tavernas iluminadas por velas.")
    estilo("Entre nessa praça cheia de viajantes e escolha seu destino...")

    nome = input("Escolha o nome do seu herói: ").strip() or "Herói sem Nome"
    linha()

    classes = ["Mago", "Guerreiro", "Curandeiro", "Explorador"]
    estilo("Escolha sua classe:")
    for i, c in enumerate(classes, 1):
        print(f"{i} - {c.title()}")
    escolha = input("Classe: ").strip()
    classe = classes[int(escolha) - 1] if escolha in ["1", "2", "3", "4"] else "Explorador"

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
        "ouro": 200,  # começa com 200 
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

# Mercadinho

import random

def mostrar_inventario(personagem):
    """Mostra os itens que o jogador possui"""
    linha()
    estilo(f"🎒 Inventário de {personagem['nome']}:")
    if "inventario" not in personagem or len(personagem["inventario"]) == 0:
        print("   (vazio)")
    else:
        for i, item in enumerate(personagem["inventario"], 1):
            print(f"   {i}. {item}")
    linha()


def mercado(personagem):
    estilo("🏪 Você chega à Loja Mística de Godsgrave...")
    print("O som de sinos mágicos ecoa enquanto você entra. Um velho elfo sorri por trás do balcão, polindo uma lâmina antiga.")
    estilo("'Bem-vindo, viajante... trago artefatos para todas as classes. Mas cuidado: alguns têm vontade própria.'")

    # Garante que o personagem tenha um inventário
    if "inventario" not in personagem:
        personagem["inventario"] = []

    # Itens por classe
    itens_por_classe = {
        "Mago": {
            "1": {"nome": "📜 Grimório das Chamas Eternas", "preco": 200, "efeito": ("ataque", 40),
                  "descricao": "Um livro proibido que ensina o feitiço ancestral de fogo (+40 ataque)."},
            "2": {"nome": "🔮 Orbe do Caos", "preco": 300, "efeito": ("ataque", 60),
                  "descricao": "Um artefato instável, pulsando energia arcana (+60 ataque)."},
            "3": {"nome": "🧪 Poção de Vitalidade Dracônica", "preco": 80, "efeito": ("hp", 50),
                  "descricao": "Restaura 50 pontos de vida com essência da Hydra."}
        },
        "Guerreiro": {
            "1": {"nome": "⚔️ Espada Rúnica da Lua", "preco": 200, "efeito": ("ataque", 25),
                  "descricao": "Forjada por guerreiros lunares, aumenta ataque em +25."},
            "2": {"nome": "🛡️ Escudo de Hydra", "preco": 180, "efeito": ("defesa", 30),
                  "descricao": "Feito das escamas da Hydra, concede +30 defesa."},
            "3": {"nome": "🩸 Elixir de Fúria", "preco": 250, "efeito": ("ataque", 50),
                  "descricao": "Infunde raiva em seu sangue, aumentando muito o ataque (+50)."}
        },
        "Curandeiro": {
            "1": {"nome": "💫 Amuleto de Luz Sagrada", "preco": 150, "efeito": ("defesa", 20),
                  "descricao": "Criação dos curandeiros do templo, concede +20 defesa."},
            "2": {"nome": "🌿 Bastão da Serenidade", "preco": 200, "efeito": ("hp", 80),
                  "descricao": "Emana energia curativa natural, restaurando 80 de vida."},
            "3": {"nome": "🌟 Elixir da Maestria", "preco": 300, "efeito": ("xp", 150),
                  "descricao": "Concede 150 de experiência instantânea."}
        },
        "Explorador": {
            "1": {"nome": "👢 Botas do Vento Prateado", "preco": 160, "efeito": ("velocidade", 20),
                  "descricao": "Aumenta sua velocidade e reflexos em +20."},
            "2": {"nome": "🏹 Arco das Sombras", "preco": 250, "efeito": ("ataque", 35),
                  "descricao": "Criado com madeira dos bosques antigos, concede +35 ataque."},
            "3": {"nome": "🧭 Relógio dos Caminhos", "preco": 180, "efeito": ("agilidade", 25),
                  "descricao": "Guia o usuário e aumenta +25 de agilidade."}
        }
    }

    # Itens raros do mercador misterioso
    raridades = [
        {"nome": "💎 Lâmina do Tempo", "preco": 400, "efeito": ("ataque", 80),
         "descricao": "Dizem que corta até o próprio destino (+80 ataque)."},
        {"nome": "🔥 Coração de Salamandra", "preco": 350, "efeito": ("hp", 120),
         "descricao": "Um fragmento ardente que concede 120 de vida."},
        {"nome": "🕯️ Véu do Crepúsculo", "preco": 300, "efeito": ("defesa", 50),
         "descricao": "Oculta o usuário nas sombras, concedendo +50 defesa."}
    ]
    raros_disponiveis = random.sample(raridades, 1)

    classe = personagem["classe"]
    itens = itens_por_classe[classe]

    while True:
        estilo(f"\n✨ Itens disponíveis para {classe}:")
        for chave, item in itens.items():
            print(f"[{chave}] {item['nome']} - {item['preco']} ouro\n   ➤ {item['descricao']}")
        print("\n[R] Falar com o mercador misterioso")
        print("[I] Ver inventário")
        print("[0] Sair da loja")

        escolha = input("\nO que deseja fazer? ").strip().upper()

        if escolha == "0":
            estilo("'Volte sempre, viajante... que os ventos de Godsgrave guiem sua jornada.'")
            break

        if escolha == "I":
            mostrar_inventario(personagem)
            continue

        if escolha == "R":
            estilo("🕯️ Uma figura encapuzada surge das sombras... 'Tenho algo que pode mudar o curso do seu destino...'")
            item = raros_disponiveis[0]
            print(f"\n💎 {item['nome']} - {item['preco']} ouro\n   ➤ {item['descricao']}")
            confirmar = input("\nDeseja comprá-lo? (s/n): ").strip().lower()
            if confirmar == "s":
                comprar_item(personagem, item)
            else:
                estilo("O mercador sorri em silêncio e desaparece...")
            continue

        if escolha not in itens:
            estilo("❌ Escolha inválida. Tente novamente.")
            continue

        item = itens[escolha]
        comprar_item(personagem, item)


def comprar_item(personagem, item):
    """Executa a compra e aplica o efeito do item"""
    # Garante inventário (caso a função seja chamada de fora do mercado)
    if "inventario" not in personagem:
        personagem["inventario"] = []

    if personagem["ouro"] < item["preco"]:
        estilo("💰 Você não tem ouro suficiente!")
        return

    personagem["ouro"] -= item["preco"]
    tipo, valor = item["efeito"]

    if tipo == "xp":
        personagem["xp"] += valor
        estilo(f"✨ Você sente o poder fluir! (+{valor} XP)")
    else:
        # Aplica o efeito dentro do dicionário de atributos
        if tipo not in personagem["atributos"]:
            personagem["atributos"][tipo] = 0
        personagem["atributos"][tipo] += valor
        estilo(f"✅ {item['nome']} adquirido! Seu {tipo} aumentou em +{valor}.")

    # Adiciona ao inventário
    personagem["inventario"].append(item["nome"])
    estilo(f"📦 {item['nome']} foi adicionado ao seu inventário!")
    estilo(f"💰 Ouro restante: {personagem['ouro']}")

# BATALHA: Hydra

def capitulo_hydra(personagem):
    estilo("\n— Capítulo 1: A Caverna e a Hydra —")
    estilo("Após percorrer as ruelas e as tavernas de Godsgrave, você segue rumo à floresta.")
    estilo("Depois de alguma caminhada, entre troncos e neblina, uma boca escura se abre: uma caverna.")
    estilo("Você entra. O ar cheira a enxofre. Esconderijos e ossos quebrados no chão... algo se move nas sombras.")
    estilo("E então: três cabeças, olhos amarelos e um rugido que estremece as paredes. A HYDRA!")

    # ataque inicial
    estilo("A Hydra ergue a cabeça e lança um jato de veneno! Sua defesa é reduzida em 15 pontos.")
    personagem["atributos"]["defesa"] = max(0, personagem["atributos"]["defesa"] - 15)
    mostrar_status(personagem)

    estilo("Deseja (1) Fugir para Godsgrave ou (2) Enfrentar a Hydra aqui e agora?")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        estilo("\nVocê opta pela prudência: retorna a Godsgrave para descansar. Missão abortada.")
        estilo("Nenhuma recompensa ganha. Volte quando estiver mais preparado.")
        return 

    estilo("Você decide lutar bravamente!")
    personagem["atributos"]["hp"] -= 10
    estilo("A Hydra ruge e desfere seu ataque: 'Veneno Cortante'! Você sofre 10 de dano.")
    if personagem["atributos"]["hp"] <= 0:
        estilo("Você caiu sob o golpe mortal. Fim de jornada.")
        return

    hydra_hp = 100
    dano_especial = 50 + 2 * personagem["nivel"]
    estilo(f"Seu turno! (1) Ataque normal (10 de dano) | (2) Habilidade especial ({dano_especial} de dano)")

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
    estilo("Com um movimento horrendo a Hydra tenta um 'Abraço da Morte'! - todas as cabeças se aproximam para esmagar você.")
    estilo("Você (1) Desvia para contra-atacar ou (2) Mira em um ponto vital?")
    escolha = input("Escolha: ").strip()

    if escolha == "2":
        estilo("Você reúne coragem e mira num ponto cego entre as cabeças. Um golpe perfeito... a Hydra ruge e desaba!")
        recompensa_final(personagem, "atacar")
        return
    else:
        estilo("Você escapa do abraço no último segundo e desfere um contra-ataque, causando +20 de dano!")
        hydra_hp -= 20
        personagem["atributos"]["hp"] -= 10
        estilo("A Hydra lança mais veneno! Você perde 10 de HP.")
        if personagem["atributos"]["hp"] <= 0:
            estilo("Você sucumbe ao veneno... Fim de jogo.")
            return

    # último turno
    estilo("Última chance! (1) Atacar repetidamente com tudo o que tem ou (2) Procurar brecha mortal?")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        estilo("Você golpeia furiosamente, golpe após golpe, até a Hydra cair!")
        personagem["ouro"] += 150
        personagem["atributos"]["defesa"] += 50
        personagem["xp"] += 200
        estilo("🏆 Recompensa: +150 ouro, Armadura de Escamas de Dragão (+50 defesa), +200 XP.")
    else:
        estilo("\nVocê observa, respira fundo e procura pela fresta entre as escamas. Encontra o ponto fraco!")
        estilo("Um ataque certeiro: a Hydra cai, derrotada por sua determinação e astúcia.")
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

# Fluxo Principal

def main():
    personagem = criar_personagem()
    mercado(personagem)
    capitulo_hydra(personagem)
    estilo("🏁 Fim do Capítulo 1 — A Jornada em Godsgrave")

if __name__ == "__main__":
    main()
