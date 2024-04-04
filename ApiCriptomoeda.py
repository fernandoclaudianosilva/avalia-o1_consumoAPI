import requests
 
while True:
    print("=" * 30)
    print("Cotação de Moedas".center(30))
    print("-" * 30)
    print("1 - Moedas disponíveis")
    print("2 - Consultar moeda")
    print("3 - sair")
    print("=" * 30)
    resposta = int(input("Opção: "))
 
    match resposta:
        case 1:
            url = 'https://api.coincap.io/v2/assets'
            response = requests.get(url)
            data = response.json()
            for x in data['data']:
                print("Nome da Criptomoeda: ", x['name'])
                print(f'Valor em Dólar: R${float(x['priceUsd']):.2f}')
 
        case 2:
           
            resposta2 = str(input("qual o nome da moeda? \n")).strip().lower()
            url = f'https://api.coincap.io/v2/assets/{resposta2}'
            response = requests.get(url)
            data = response.json()
 
            if response.status_code ==200:
                print("Nome da moeda: " +data["data"]["name"])
                print(f'Valor em Dólar:$ {float(data['data']['priceUsd']):.2f}')
                print(f"variação em 24 horas:  {float(data["data"]["changePercent24Hr"]):.2f}","%")
                print(f"preço da moeda: $ {float(data["data"]["marketCapUsd"]):.2f}")
               
            else:
                print("moeda não encontrada")
 
        case 3:
            print("Saindo...")
            break
       
        case other:
            print("ERRO: Insira uma opção válida.")
   
    input("Pressione ENTER para continuar...")
[Ontem 19:49] FERNANDO CLAUDIANO DA SILVA
import requests
 
while True:
    print("=" * 30)
    print("Cotação de Moedas".center(30))
    print("-" * 30)
    print("1 - Moedas disponíveis")
    print("2 - Consultar moeda")
    print("3 - sair")
    print("=" * 30)
    resposta = int(input("Opção: "))
 
    match resposta:
        case 1:
            url = 'https://api.coincap.io/v2/assets'
            response = requests.get(url)
            data = response.json()
            for x in data['data']:
                print("Nome da Criptomoeda: ", x['name'])
                print(f'Valor em Dólar: R${float(x['priceUsd']):.2f}')
 
        case 2:
           
            resposta2 = str(input("qual o nome da moeda? \n")).strip().lower()
            url = f'https://api.coincap.io/v2/assets/{resposta2}'
            response = requests.get(url)
            data = response.json()
           
            if response.status_code ==200:
                print("=" * 30)
                print("Nome da moeda: " +data["data"]["name"])
                print("Abreviação: " +data["data"]["symbol"])
                print(f'Valor de um bitcoin em Dólar:$ {float(data['data']['priceUsd']):.2f}')
                print(f"Variação em 24 horas:  {float(data["data"]["changePercent24Hr"]):.2f}","%")
                print(f"Moedas disponiveis:  {float(data["data"]["maxSupply"]):.2f}")
                print(f"Valor da moeda: $ {float(data["data"]["marketCapUsd"]):.2f}")
               
            else:
                print("moeda não encontrada")
 
        case 3:
            print("Saindo...")
            break
       
        case other:
            print("ERRO: Insira uma opção válida.")
   
    input("Pressione ENTER para continuar...")