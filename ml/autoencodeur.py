import sys
import time

import yaml

import numpy as np

import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

from .base_model import BaseModelMl

from config import ConfigAutoEncodeur


class AutoEncodeur(BaseModelMl):
    def __init__(self):
        super().__init__()
        self.decoder = None
        self.timestamp = str(int(time.time()))
        self.config = ConfigAutoEncodeur()

    def train(self):
        data = np.array(self.data)
        # CREATION DE L'AUTOENCODEUR
        input_layer = Input(shape=(self.config.INPUT_DIM,))
        latent_space = self._create_encoder(input_layer)
        output_layer = self._create_decoder(latent_space)
        autoencoder = Model(input_layer, output_layer)
        autoencoder.compile(optimizer=self.config.OPTIMIZER(learning_rate=self.config.LEARNING_RATE),
                            loss=self.config.LOSS)

        # ENTRAINEMENT
        history = autoencoder.fit(data,
                                  data,
                                  epochs=self.config.EPOCHS,
                                  batch_size=self.config.BATCH_SIZE,
                                  shuffle=True,
                                  validation_split=self.config.VALIDATION_SPLIT)

        autoencoder.summary()

        # EXTRACTION DU DECODEUR
        self._extract_decoder(autoencoder)

        self._sauvegarder_donnees(autoencoder, input_layer, latent_space, data)
        self._sauvegarder_graphique(history)
        self._sauvegarder_config()

    def _create_encoder(self, encoded):
        for n_neurons in self.config.COUCHES:
            encoded = Dense(n_neurons, activation='relu')(encoded)

        latent_space = Dense(self.config.LATENT_SPACE_DIM, activation='relu')(encoded)  # Espace latent

        return latent_space

    def _create_decoder(self, decoded):
        for n_neurons in reversed(self.config.COUCHES):
            decoded = Dense(n_neurons, activation='relu')(decoded)

        output_layer = Dense(self.config.INPUT_DIM, activation='sigmoid')(
            decoded)  # Utilisation de 'sigmoid' car les valeurs sont entre 0 et 1

        return output_layer

    def _extract_decoder(self, autoencoder):
        latent_input = Input(shape=(self.config.LATENT_SPACE_DIM,))
        n_couches_decoded = len(self.config.COUCHES) + 1
        decoder_layer = latent_input
        for index_couche in reversed(range(1, n_couches_decoded + 1)):
            decoder_layer = autoencoder.layers[-index_couche](decoder_layer)

        self.decoder = Model(latent_input, decoder_layer)

    def _sauvegarder_donnees(self, autoencoder, input_layer, latent_space, data):
        nom_fichier = f"{self.REPORT_DIR}/{self.config.NOM_MODELE}_{self.timestamp}.txt"

        with open(nom_fichier, 'w') as fichier:
            sys.stdout = fichier
            autoencoder.summary()
            self._sauvegarder_valeurs_min_max_espace_latent(input_layer, latent_space, data)

            print(f"Modele entrainé sur {len(self.data)} ranges")

        sys.stdout = sys.__stdout__

    def _sauvegarder_valeurs_min_max_espace_latent(self, input_layer, latent_space, data):
        # Obtenir l'encodeur à partir de l'autoencodeur
        encoder = Model(input_layer, latent_space)

        # Prédire les valeurs de l'espace latent pour les données d'entraînement
        latent_representation = encoder.predict(data)

        # Trouver les valeurs min et max pour chaque paramètre de l'espace latent
        min_values = np.min(latent_representation, axis=0)
        max_values = np.max(latent_representation, axis=0)

        self.config.ajouter_min_max_espace_latent(min_values.tolist(), max_values.tolist())

        print(f"Valeurs minimales de l'espace latent: {min_values}")
        print(f"Valeurs maximales de l'espace latent: {max_values}")

    def _sauvegarder_config(self):
        # Chemin vers le fichier YAML
        fichier_yaml = f"{self.DIR_SAVE}/{self.config.NOM_MODELE}_{self.timestamp}.yaml"

        self.config.save(len(self.data), fichier_yaml)
        self.config.save(len(self.data), 'model-config.yaml')

    def _sauvegarder_graphique(self, history):
        plt.title(f"{self.config.NOM_MODELE}, "
                  f"COUCHES: {self.config.COUCHES}, "
                  f"PARAM_LATENT: {self.config.LATENT_SPACE_DIM}")
        plt.plot(history.history['loss'], label='loss')
        plt.plot(history.history['val_loss'], label='val_loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(f'{self.REPORT_DIR}/{self.config.NOM_MODELE}_{self.timestamp}.png')

    def save_model(self):
        self.decoder.save(f'{self.DIR_SAVE}/{self.config.NOM_MODELE}_{self.timestamp}.keras')
        self.decoder.save('model.keras')
