import numpy as np
from flask import Flask
from tensorflow.keras.model import load_model

from config import ConfigAutoEncodeur

app = Flask(__name__)

model = load_model('model.keras')
config = ConfigAutoEncodeur.load_config('model_config.yaml')


def predict(self, input_data: list[float]) -> list[float]:
    latent_vector = np.array(input_data)
    generated_data = self.decoder.predict(latent_vector)

    return list(generated_data)


@app.route('/parameters')
def get_parameters():
    return "Hello, Flask!"


@app.route('/generate')
def predict():
    return predict([0])


app.run(host='0.0.0.0', debug=True, port=5000)
