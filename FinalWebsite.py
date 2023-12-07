from flask import Flask, render_template
from image_info import image_info
import random
from flask_bootstrap import Bootstrap
from PIL import Image
from forex_python.converter import CurrencyRates

app = Flask(__name__)

def getrate(currency):
    c = CurrencyRates()
    conversion = float(c.get_rate('USD', currency))
    return conversion
    
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/conversion/<select>')
def conversion(select):
    num = getrate(select)
    return render_template('conversion.html', vals=num, select=select)
    
if __name__ == '__main__':
    app.run(debug=True)

Bootstrap(app)

