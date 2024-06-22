import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

from ml.base_model import BaseModelMl


class AutoEncodeur(BaseModelMl):
    def __init__(self):
        super().__init__()
        self.decoder = None

    def train(self):
        data = np.array(self.data)
        input_dim = 169  # Taille des listes de floats

        # Encoder
        input_layer = Input(shape=(input_dim,))
        encoded = Dense(128, activation='relu')(input_layer)
        encoded = Dense(64, activation='relu')(encoded)
        encoded = Dense(32, activation='relu')(encoded)
        latent_space = Dense(5, activation='relu')(encoded)  # Espace latent

        # Decoder
        decoded = Dense(32, activation='relu')(latent_space)
        decoded = Dense(64, activation='relu')(decoded)
        decoded = Dense(128, activation='relu')(decoded)
        output_layer = Dense(input_dim, activation='sigmoid')(
            decoded)  # Utilisation de 'sigmoid' car les valeurs sont entre 0 et 1

        # Autoencodeur complet
        autoencoder = Model(input_layer, output_layer)

        # Decoder Model
        latent_input = Input(shape=(5,))
        decoder_layer1 = autoencoder.layers[-4](latent_input)
        decoder_layer2 = autoencoder.layers[-3](decoder_layer1)
        decoder_layer3 = autoencoder.layers[-2](decoder_layer2)
        decoder_output = autoencoder.layers[-1](decoder_layer3)
        self.decoder = Model(latent_input, decoder_output)

        autoencoder.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

        autoencoder.summary()

        history = autoencoder.fit(data, data, epochs=100, batch_size=32, shuffle=True, validation_split=0.2)

        self.plot_loss(history)

    def plot_loss(self, history):
        plt.plot(history.history['loss'], label='loss')
        plt.plot(history.history['val_loss'], label='val_loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

    def predict(self, input_data: list[float]) -> list[float]:
        latent_vector = np.array(input_data)
        generated_data = self.decoder.predict(latent_vector)

        return list(generated_data)

    def save_model(self):
        self.decoder.save('saved_models/decoder_model.keras')

    def load_model(self):
        self.decoder = load_model('saved_models/decoder_model.keras')

