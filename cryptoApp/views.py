from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
import csv

# Create your views here.
def index(request):
    import requests
    import json
    #getting price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,DOGE,BNB,UNI,XMR,SUSHI,AVA&tsyms=USD") 
    #taking that data and making it into json data
    price = json.loads(price_request.content)
    
    #getting all news data from call
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN") 
    #taking that data and making it into json data
    news = json.loads(news_request.content)

    context = {
        'news': news,
        'price': price
    }
    return render(request, "index.html", context)

def moneyMaker(request):
    import requests
    import json

    coin_request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1000000&page=1&sparkline=false") 
    
    moneyMaker = []
    coins = json.loads(coin_request.content)
    
    dataToInsert = []
    
    for x in coins:
        
        
        for key, value in x.items():
            x["current_price"]
            if key == "market_cap":
                MarketCap = value
                print("this is marketcap",MarketCap)
            # print("this is marketcap after the if",MarketCap)
            if key == "circulating_supply":
                circulatingCoins = value
                print("this is circulating",circulatingCoins)
                expectedPrice = MarketCap/circulatingCoins
                print("expeted price right now", expectedPrice)
                moneyMaker.append({x["id"]: [x["current_price"], expectedPrice, ((x["current_price"] - expectedPrice) / x["current_price"]) * 100]})

    print(moneyMaker)
    context = {
        "coins": coins,
        "moneyMaker": moneyMaker
    }
    return render(request, "moneyMaker.html", context)

