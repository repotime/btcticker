import requests
import time

def fetch_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        return bitcoin_price
    else:
        return print('Probably sending too many requests. Try again in a few minutes.')

def main():
    while True:
        bitcoin_price = fetch_bitcoin_price()
        if bitcoin_price:
            print(f"Bitcoin price: ${bitcoin_price}")
        else:
            print("Failed to fetch Bitcoin price.")
        time.sleep(10)

if __name__ == '__main__':
    main()
