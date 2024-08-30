import json

def analisar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamento = dados['faturamento']
    
    valores = [item['valor'] for item in faturamento if item['valor'] > 0]
    
    if not valores:
        return "Não há dados de faturamento disponíveis."
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = len([valor for valor in valores if valor > media_mensal])
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

arquivo_json = 'faturamento.json'

resultado = analisar_faturamento(arquivo_json)
print(f"Menor valor de faturamento: {resultado['menor_faturamento']}")
print(f"Maior valor de faturamento: {resultado['maior_faturamento']}")
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")
