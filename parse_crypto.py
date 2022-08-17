import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from tqdm import tqdm, trange

# new string
print('')

for i in trange(100, colour='#66ff00', desc='Parsing'):
    sleep(.06)

def parse_btc():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    btc = soup.find('div', class_='priceValue')
    print(btc.text)

def parse_eth():
    url = 'https://coinmarketcap.com/currencies/ethereum/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    eth = soup.find('div', class_='priceValue')
    print(eth.text)

def parse_ltc():
    url = 'https://coinmarketcap.com/currencies/litecoin/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    ltc = soup.find('div', class_='priceValue')
    print(ltc.text)

def parse_trx():
    url = 'https://coinmarketcap.com/currencies/tron/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    trx = soup.find('div', class_='priceValue')
    print(trx.text)

def parse_bnb():
    url = 'https://coinmarketcap.com/currencies/bnb/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    bnb = soup.find('div', class_='priceValue')
    print(bnb.text)

def parse_xrp():
    url = 'https://coinmarketcap.com/currencies/xrp/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    xrp = soup.find('div', class_='priceValue')
    print(xrp.text)

def parse_sol():
    url = 'https://coinmarketcap.com/currencies/solana/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    sol = soup.find('div', class_='priceValue')
    print(sol.text)

def parse_doge():
    url = 'https://coinmarketcap.com/currencies/dogecoin/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    doge = soup.find('div', class_='priceValue')
    print(doge.text)

def parse_ada():
    url = 'https://coinmarketcap.com/currencies/cardano/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    ada = soup.find('div', class_='priceValue')
    print(ada.text)

def parse_dot():
    url = 'https://coinmarketcap.com/currencies/polkadot-new/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    dot = soup.find('div', class_='priceValue')
    print(dot.text)


def output():
    print('BTC:') 
    parse_btc()

    print('\nETH:') 
    parse_eth()

    print('\nLTC:')
    parse_ltc()

    print('\nTRX:')
    parse_trx()

    print('\nBNB:')
    parse_bnb()

    print('\nXRP:')
    parse_xrp()

    print('\nSOL:')
    parse_sol()

    print('\nDOGE:')
    parse_doge()

    print('\nADA:')
    parse_ada()

    print('\nDOT:')
    parse_dot()
    
    # new str 
    print('')

output() 