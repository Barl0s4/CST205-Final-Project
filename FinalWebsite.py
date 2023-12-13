from flask import Flask, render_template, request
import requests
from forex_python.converter import CurrencyRates
from flask_bootstrap import Bootstrap5
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Takes the USD value, currency name to be compaired, currency value vs. USD, and the price of barrel to generate a bar graph. The graph is saved for use.
def graph(usdval, currency, curval, oil_price):
    # creating the dataset
    crbarrel = currency + " barrel"
    data = {'USD': usdval, currency:curval, 'UDS barrel':oil_price, crbarrel:(curval*oil_price)}
    courses = list(data.keys())
    values = list(data.values())
  
    fig = plt.figure(figsize = (10, 4))
 
    # creating the bar plot
    plt.bar(courses, values, color ='blue', width = 0.4)
 
    plt.xlabel("Types")
    plt.ylabel("Values")
    plt.title("Comparison of currency and barrel prices")
    plt.savefig('barrel_graph.png')

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