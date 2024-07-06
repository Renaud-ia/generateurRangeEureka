import argparse

from ml import BaseModelMl, AutoEncodeur
from persistence import GestionnairePersistence, Recuperateur
from poker import FormatPoker, SituationPoker, RangePoker, TypeJeuPoker

# Création du parseur d'arguments
parser = argparse.ArgumentParser(description='Script d\'entrainement pour un modèle de ML avec options de filtrage.')

# Ajout des arguments de filtrage
parser.add_argument('--max_all_in', type=int, help='Ne pas prendre en compte les all-in supérieur')

# Analyse des arguments
args = parser.parse_args()


# REGLES DE FILTRAGE

def format_passe_filtrage(format_poker: FormatPoker):
    if format_poker.type_jeu == TypeJeuPoker.MTT:
        return False

    return True


def situation_passe_filtrage(situation: SituationPoker):
    max_all_in = 30

    if args.max_all_in:
        max_all_in = int(args.max_all_in)

    if situation.get_all_in_more_than(max_all_in):
        return False

    return True


# RECUPERATION DE DONNEES

gen_data: list[Recuperateur] = []
gen_data.extend(GestionnairePersistence.recuperer_enregistreurs_json())
gen_data.extend(GestionnairePersistence.recuperer_enregistreurs_externe())

data_training: list[RangePoker] = []

for recuperateur in gen_data:
    if not format_passe_filtrage(recuperateur.get_format_poker()):
        continue

    for situation, range in recuperateur.get_ranges_enregistrees().items():
        if not situation_passe_filtrage(situation):
            print(f"Situation exclue des données: {situation}")
            continue

        data_training.append(range)

# ENTRAINEMENT

model: BaseModelMl = AutoEncodeur()

model.add_data(data_training)

model.train()

model.save_model()

