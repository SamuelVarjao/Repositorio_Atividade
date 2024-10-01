import json

def calcular_faturamento(json_file):
    # Carrega os dados do arquivo JSON
    with open(json_file, 'r') as file:
        dados = json.load(file)

    # Filtra os dias que tiveram faturamento
    faturamentos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calcula a média mensal, ignorando os dias sem faturamento
    media_mensal = sum(faturamentos) / len(faturamentos)

    # Conta os dias com faturamento acima da média
    dias_acima_da_media = len([faturamento for faturamento in faturamentos if faturamento > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento('dados_ex_3.json')
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")
