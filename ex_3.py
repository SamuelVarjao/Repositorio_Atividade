import json

def calcular_valor(json_file):
    # Carrega os dados do arquivo JSON
    with open(json_file, 'r') as file:
        dados = json.load(file)

    # Filtra os dias que tiveram valor
    valor = [dia['valor'] for dia in dados if dia['valor'] > 0]

    # Calcula o menor e o maior valor de valor
    menor_valor = min(valor)
    maior_valor = max(valor)

    # Calcula a média mensal, ignorando os dias sem valor
    media_mensal = sum(valor) / len(valor)

    # Conta os dias com valor acima da média
    dias_acima_da_media = len([valor for valor in valor if valor > media_mensal])

    return menor_valor, maior_valor, dias_acima_da_media

menor, maior, dias_acima_media = calcular_valor('dados.json')
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")
