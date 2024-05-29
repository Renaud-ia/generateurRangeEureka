from persistence import Enregistreur, GestionnairePersistence
from poker import VariantePoker

variante = VariantePoker()
enregistreur = GestionnairePersistence.recuperer_enregistreur(variante)
enregistreur.sauvegarder()