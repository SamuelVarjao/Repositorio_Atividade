faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcula e imprime o percentual de cada estado
print("Percentual de representação por estado:")
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")