from persistence import GestionnairePersistence
from poker import FormatPoker


class ScrapingTask:
    def __init__(self, format_poker: FormatPoker):
        self.enregistreur = GestionnairePersistence.recuperer_enregistreur(format_poker)

