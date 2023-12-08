import requests
#Oil API
api_key = 'OjA6ZtTt34XW29iJVpe6gIAGZI8eyNn404pQpNKJ'

api_endpoint = 'https://api.eia.gov/v2/petroleum/pri/fut/data/'

headers = {
    'X-Api-Key': api_key,
    'X-Params': '{"frequency": "daily", "data": ["value"], "facets": {}, "start": null, "end": null, "sort": [{"column": "period", "direction": "desc"}], "offset": 0, "length": 5000}'
}

response = requests.get(api_endpoint, headers=headers)

# Process the response
if response.status_code == 200:
    data = response.json()
    for index, key in enumerate(data):
        if(data['response']['data'][0]['product-name'] == 'Crude Oil'):
            print(data['response']['data'][index]['product-name'], 'price:', data['response']['data'][index]['value'], "on", data['response']['data'][index]['period'])
            break
else:
    print(f"Error: {response.status_code} - {response.text}")