from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import token_key
import json

def getInfo(crypto, currency):
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': crypto,
        'convert': currency
        }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': token_key.API_KEY,
        }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        # info = json.loads(response.text)
        info = json.loads(response.text)['data'] #['1']['quote'][currency]['price']
        index = list(info)[0]
        # print(info[index])
        info = info[index]['quote'][currency]['price']
        print(info)
        return info
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return e
        
#getInfo("ripple","USD")