import requests

# Lista de IPs
ips = [
     "142.132.228.37:8085"
]

# Função para obter a localização exata de um IP
def obter_localizacao(ip):
    try:
        ip_sem_porta = ip.split(":")[0]  # Separando o IP da porta
        resposta = requests.get(f"http://ip-api.com/json/{ip_sem_porta}")
        resposta.raise_for_status()  # Lança uma exceção para códigos de status diferentes de 200
        dados = resposta.json()
        if dados["status"] == "success":
            traducao = {
                "query": "IP",
                "country": "País",
                "countryCode": "Código do País",
                "region": "Região",
                "regionName": "Nome da Região",
                "city": "Cidade",
                "zip": "CEP",
                "lat": "Latitude",
                "lon": "Longitude",
                "timezone": "Fuso Horário",
                "isp": "Provedor de Internet",
                "org": "Organização",
                "as": "ASN",
                "status": "Status"
            }
            traduzido = {traducao[chave]: valor for chave, valor in dados.items()}
            return traduzido
        else:
            return f"Erro: {dados['message']}"
    except Exception as e:
        return f"Erro ao obter localização do IP {ip}: {str(e)}"

# Loop pelos IPs
for ip in ips:
    localizacao = obter_localizacao(ip)
    if isinstance(localizacao, dict):
        print(f"Informações para o IP: {ip}")
        for chave, valor in localizacao.items():
            print(f"{chave}: {valor}")
        print()
    else:
        print(localizacao)
