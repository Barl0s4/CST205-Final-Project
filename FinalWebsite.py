from flask import Flask, render_template
from image_info import image_info
import random
from flask_bootstrap import Bootstrap
from PIL import Image


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

Bootstrap(app)

