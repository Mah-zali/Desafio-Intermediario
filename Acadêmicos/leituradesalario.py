# Leitura do salário
salario = float(input())

if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        # Se está entre 2000.01 e 3000.00 → só paga 8% do que passar de 2000
        imposto = (salario - 2000.00) * 0.08
        print(f"R$ {imposto:.2f}")
    else:
        if salario <= 4500.00:
            # Se está entre 3000.01 e 4500.00
            # paga 8% de 1000 + 18% do que passar de 3000
            imposto = (1000.00 * 0.08) + (salario - 3000.00) * 0.18
            print(f"R$ {imposto:.2f}")
        else:
            # Se está acima de 4500.00
            # paga 8% de 1000 + 18% de 1500 + 28% do que passar de 4500
            imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + (salario - 4500.00) * 0.28
            print(f"R$ {imposto:.2f}")
