import yaml
from keras.src.optimizers import Adam


class LatentParam:
    def __init__(self, nom: str = "Inconnu", min_value: float = None, max_value: float = None):
        self.nom: str = nom
        self.min_value: float = min_value
        self.max_value: float = max_value

    def to_dict(self) -> dict:
        desc_params: dict = {
            "nom": self.nom,
            "min": self.min_value,
            "max": self.max_value
        }

        return desc_params

    @classmethod
    def from_dict(cls, desc_params: dict) -> 'LatentParam':
        return cls(desc_params["nom"], desc_params["min"], desc_params["max"])

    def set_minimum(self, value):
        self.min_value = value

    def set_maximum(self, value):
        self.max_value = value


class ConfigAutoEncodeur:
    NOM_MODELE = "dense_couche"
    INPUT_DIM = 169
    COUCHES = [100, 50, 25]
    LATENT_SPACE_DIM = 3
    EPOCHS = 100
    OPTIMIZER = Adam
    LEARNING_RATE = 0.001
    BATCH_SIZE = 32
    VALIDATION_SPLIT = 0.2
    LOSS = "mse"

    def __init__(self, latent_params: list[LatentParam] = None):
        self.latent_params: list[LatentParam] = latent_params

        if self.latent_params is None:
            self.latent_params = []
            for _ in range(self.LATENT_SPACE_DIM):
                latent_par: LatentParam = LatentParam()
                self.latent_params.append(latent_par)

    def ajouter_min_max_espace_latent(self, min_values: list[float], max_values: list[float]):
        if len(min_values) != len(max_values):
            raise ValueError("Les valeurs min et max ne correspondent pas")

        if len(min_values) != len(self.latent_params):
            raise ValueError("Pas autant de valeurs que de paramètres")

        for index, param in enumerate(self.latent_params):
            param.set_minimum(min_values[index])
            param.set_maximum(max_values[index])

    def save(self, n_data: int, fichier_yaml: str) -> None:
        config: dict = {
            "modele": self.NOM_MODELE,
            "input_dim": self.INPUT_DIM,
            "couches": self.COUCHES,
            "latent_dim": self.LATENT_SPACE_DIM,
            "epochs": self.EPOCHS,
            "optimizer": str(self.OPTIMIZER),
            "learning_rate": self.LEARNING_RATE,
            "batch": self.BATCH_SIZE,
            "split": self.VALIDATION_SPLIT,
            "loss": self.LOSS,
            "n_data": n_data,
            "parameters": []
        }

        for param in self.latent_params:
            config["parameters"].append(param.to_dict())

        # Écriture du dictionnaire en YAML dans le fichier
        with open(fichier_yaml, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

    @classmethod
    def load_config(cls, nom_fichier: str):
        with open(nom_fichier, 'r') as file:
            config: dict = yaml.safe_load(file)

        latent_params: list[LatentParam] = []

        for params in config["parameters"]:
            param: LatentParam = LatentParam.from_dict(params)
            latent_params.append(param)

        return cls(latent_params)

    def get_latent_parameters(self):
        latent_parameters: list[dict] = []

        for param in self.latent_params:
            latent_parameters.append(param.to_dict())

        return latent_parameters
