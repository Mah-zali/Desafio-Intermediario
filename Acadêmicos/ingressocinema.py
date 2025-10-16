# Controle de ingressos de cinema

preco_base = 20.0

idade = int(input("Digite a idade: "))

if idade < 0 or idade > 120:
    print("Erro: idade inválida!")
else:
    estudante = input("É estudante? (S/N): ")

    justificativa = "entrada inteira"
    valor = preco_base

    if idade < 12:
        valor = preco_base / 2
        justificativa = "meia entrada para criança"
    else:
        if idade >= 60:
            valor = preco_base / 2
            justificativa = "meia entrada para idoso"
        else:
            if estudante == "S" or estudante == "s":
                valor = preco_base / 2
                justificativa = "meia entrada para estudante"

    print(f"Valor do ingresso: R$ {valor:.2f} ({justificativa})")