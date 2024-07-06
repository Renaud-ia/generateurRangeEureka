import numpy as np
from flask import Flask, jsonify, request
import tensorflow as tf

from config import ConfigAutoEncodeur
from poker import RangePoker

app = Flask(__name__)

model = tf.keras.models.load_model('model.keras')
config: ConfigAutoEncodeur = ConfigAutoEncodeur.load_config('model-config.yaml')


def predict(input_data: list[list[float]]) -> dict[str, float]:
    latent_vector = np.array(input_data)
    generated_data = model.predict(latent_vector)[0]

    range_poker: dict[str, float] = {}

    for combo, value in zip(RangePoker.tous_les_combos_tries(), generated_data):
        range_poker[combo] = float(value)

    return range_poker


@app.route('/parameters')
def get_parameters():
    return jsonify(config.get_latent_parameters())


@app.route('/generate', methods=['POST'])
def generate_range():
    # Récupération des données JSON de la requête
    data = request.get_json()

    # Vérification que les données sont une liste
    if not isinstance(data, list):
        return jsonify({'error': 'Input should be a list of floats'}), 400

    # Vérification que tous les éléments de la liste sont des flottants
    for item in data:
        if not isinstance(item, float):
            return jsonify({'error': 'All elements in the list should be floats'}), 400

    return jsonify(predict([data]))


app.run(host='0.0.0.0', debug=True, port=5000)
