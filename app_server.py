from flask import Flask

from ml.autoencodeur import AutoEncodeur

app = Flask(__name__)

model = AutoEncodeur()


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/generate')
def predict():
    return model.predict([0])


if __name__ == '__main__':
    model.load_model()
    app.run(host='0.0.0.0', debug=True, port=5000)
