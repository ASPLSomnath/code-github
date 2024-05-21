from flask import Flask

app = Flask(__name__)


items = [
    {'name': "fride rice",
     'price':70
    },
    {'name': "Biriyani",
     'price':170
    },
]

@app.route('/')
def hw():
    return 'hello'

@app.route('/get-items')
def get_items():
    return {"items":items}

if __name__ == "__main__":
    app.run(debug=True)