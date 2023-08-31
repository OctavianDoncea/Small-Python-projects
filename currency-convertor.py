from requests import get
from pprint import PrettyPrinter

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ElRtJltIl3MkQeHC2CzzCffl8pFIZrGAJPmQCefk'
API_KEY = 'fca_live_ElRtJltIl3MkQeHC2CzzCffl8pFIZrGAJPmQCefk'

printer = PrettyPrinter()

def get_currencies():
    data = get(URL).json()['data']
    data = list(data.items())
    data.sort()

    return data

def ex_rate_USD(currencies):
    for currency in currencies:
        name = currency[0]
        exchange_rate = currency[1]
        print(f"{name} - {exchange_rate}")

def exchange_rate(currency1, currency2):
    exchange_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ElRtJltIl3MkQeHC2CzzCffl8pFIZrGAJPmQCefk&currencies={currency2}&base_currency={currency1}'
    response = get(exchange_URL)
    data = response.json()['data']
    data = list(data.items())

    rate = data[0][1]
    printer.pprint(f'1 {currency1} = {rate} {currency2}')
    
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print('Invalid amount.')
        return
    
    converted_amount = rate * amount
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount

def main():
    currencies = get_currencies()

    print('Welcome to the currency converter!')
    print('List the different currencies (type "list")')
    print('Convert from one currency to another (type "convert")')
    print('Get the exchange rate between two currencies (type "rate")')
    print()

    while True:
        command = input('Type a command (q to quit): ').lower()

        if command == 'q':
            break
        elif command == 'list':
            ex_rate_USD(currencies)
        elif command == 'convert':
            currency1 = input('Enter the base currency id: ').upper()
            amount = input('Enter how much you want to convert: ')
            currency2 = input('Enter the currency id you want to convert to: ').upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input('Enter the base currency id: ').upper()
            currency2 = input('Enter the currency id you want to convert to: ').upper()
            exchange_rate(currency1, currency2)
        else:
            print('Unrecognized command!')

#data = get_currencies()
#ex_rate_USD(data)
#exchange_rate('EUR', 'RON')
#convert('RON', 'EUR', 1000000)
main()