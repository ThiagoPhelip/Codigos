import ccxt
import pandas as pd

# Criar uma lista de corretoras que deseja monitorar
exchanges = [ccxt.binance(), ccxt.bitmex(), ccxt.bittrex()]

# Inicializar um dataframe vazio para armazenar os dados de preços
prices = pd.DataFrame()

# Iterar através das corretoras
for exchange in exchanges:
    # Obter dados de preços de cada criptomoeda
    exchange.load_markets()
    tickers = exchange.fetch_tickers()
    exchange_prices = pd.DataFrame(tickers).T
    # Adicionar a coluna "exchange" para identificar a corretora
    exchange_prices["exchange"] = exchange.id
    # Adicionar os dados de preços ao dataframe
    prices = prices.append(exchange_prices)

# Imprimir os dados de preços
print(prices)


#Este exemplo usa a biblioteca "ccxt" para obter dados de preços de criptomoedas a partir de diferentes corretoras e a biblioteca "pandas" para armazenar e manipular os dados.
#Este código irá imprimir um dataframe com os dados de preços de todas as criptomoedas disponíveis nas corretoras especificadas (Binance, Bitmex, Bittrex). Ele pode ser modificado e adaptado de acordo com suas necessidades específicas, por exemplo, adicionando uma funcionalidade de alerta de preço ou gravando os dados em um banco de dados para análise posterior.
