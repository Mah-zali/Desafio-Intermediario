#entrada do salario
salario = float(input())

#calculo imposto
imposto1 = (salario - 2000.00) * 0.08
#paga 8% do que passar de 2000

imposto2 = (1000.00 * 0.08)+((salario-3000.00)*0.18)
#paga 8% do que passar de 2000 e mais 18% do que passar de 3000

imposto3 = (1000.00 * 0.08)+(1500.00*0.18)+((salario-3000.00)*0.18)
#paga 8% do que passar de 2000, mais 18% do que passar de 3000 e mais 28% do que passar de 4500

if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        print(f"R$ {imposto1:.2f}")
    if salario <= 4500.00:
        print(f"R$ {imposto2:.2f}")
    if salario > 4500.00:
        print(f"R$ {imposto3:.2f}")