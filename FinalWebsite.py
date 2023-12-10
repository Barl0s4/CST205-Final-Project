# from flask import Flask, render_template
# import random
# from flask_bootstrap import Bootstrap
# from PIL import Image
# from forex_python.converter import CurrencyRates

# app = Flask(__name__)

# def getrate(currency):
#     c = CurrencyRates()
#     conversion = float(c.get_rate('USD', currency))
#     return conversion
    
# @app.route('/')
# def home():
#     return render_template('index.html')
    
# @app.route('/conversion/<select>')
# def conversion(select):
#     num = getrate(select)
#     return render_template('conversion.html', vals=num, select=select)
    
# if __name__ == '__main__':
#     app.run(debug=True)

# Bootstrap(app)

from flask import Flask, render_template, request
import requests
from forex_python.converter import CurrencyRates

app = Flask(__name__)

# Function to get the latest oil price
def get_latest_oil_price():
    api_key = 'OjA6ZtTt34XW29iJVpe6gIAGZI8eyNn404pQpNKJ'
    api_endpoint = 'https://api.eia.gov/v2/petroleum/pri/fut/data/'
    headers = {
        'X-Api-Key': api_key,
        'X-Params': '{"frequency": "daily", "data": ["value"], "facets": {}, "start": null, "end": null, "sort": [{"column": "period", "direction": "desc"}], "offset": 0, "length": 5000}'
    }

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data['response']['data']:
            if item['product-name'] == 'Crude Oil':
                return item['value']
        return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def get_all_currency_rates(base_currency='USD'):
    c = CurrencyRates()
    rates = c.get_rates(base_currency)
    return rates

@app.route('/', methods=['GET', 'POST'])
def home():
    oil_price = get_latest_oil_price()
    currencies = get_all_currency_rates()
    if request.method == 'POST':
        amount = request.form.get('amount', type=float)
        from_currency = request.form.get('startingCurrency')
        to_currency = request.form.get('desiredCurrency')
        if amount and from_currency and to_currency:
            c = CurrencyRates()
            conversion = c.convert(from_currency, to_currency, amount)
            oil_adjusted_conversion = conversion * oil_price if oil_price else conversion
            return render_template('conversion.html', result=oil_adjusted_conversion, from_currency=from_currency, to_currency=to_currency, amount=amount)
    return render_template('index.html', oil_price=oil_price, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
