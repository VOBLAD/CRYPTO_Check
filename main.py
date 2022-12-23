import time
from bs4 import BeautifulSoup
import requests
from art import tprint

def btc():
    url = f"https://coinmarketcap.com/currencies/bitcoin/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    data = soup.find_all("div", class_="priceValue")
    print("Цена BTC:" + data[0].text + ":USDT")



def eth():
    url = f"https://coinmarketcap.com/currencies/ethereum/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    data = soup.find_all("div", class_="priceValue")
    print("Цена ETH:" + data[0].text + ":USDT")



def bnb():
    url = f"https://coinmarketcap.com/currencies/bnb/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    data = soup.find_all("div", class_="priceValue")
    print("Цена BNB:" + data[0].text + ":USDT",)



def main():
    tprint("CRYPTO", font="dolor")
    while True:
       btc()
       eth()
       bnb()
       print('.' * 25)
       time.sleep(30)




if __name__ =='__main__':
    main()