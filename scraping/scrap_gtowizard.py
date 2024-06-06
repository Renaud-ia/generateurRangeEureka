import logging

from persistence import GestionnairePersistence
from .gtowizard import FormatGtoWizard, SituationPokerGtoWizard, ScrapingTaskGtoWizard, TokenManagerGtoWizard
from .gtowizard.situation_gto_wizard import BuilderSituationGtoWizard
from .scraping_exceptions import BearerNotValid

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ScraperGtoWizard:
    def __init__(self, format_a_scraper: FormatGtoWizard):
        logger.info(f"Initialisation du format à scraper: {format_a_scraper}")
        self.format_gto_wizard = format_a_scraper
        self.scraping_tasks: list[ScrapingTaskGtoWizard] = []
        self.token_getter = TokenManagerGtoWizard()
        self.bearer = self.token_getter.get_token()
        self.enregistreur = GestionnairePersistence.recuperer_enregistreur(format_a_scraper)

        self.initialiser_tasks()

    def initialiser_tasks(self):
        for stack in self.format_gto_wizard.possibles_stack_sizes():
            situation_initiale: SituationPokerGtoWizard = BuilderSituationGtoWizard.get(self.format_gto_wizard, stack)
            tache_initiale = ScrapingTaskGtoWizard(self.format_gto_wizard, situation_initiale)

            self.scraping_tasks.append(tache_initiale)

    def scrap(self):
        if self.enregistreur.enregistrement_termine():
            logger.info(f"Les ranges ont déjà été scrapées pour {format}")

        while len(self.scraping_tasks) > 0:
            scraping_task = self.scraping_tasks.pop()

            try:
                self.scraping_tasks.extend(scraping_task.execute(self.bearer, self.enregistreur))
                self.enregistreur.sauvegarder()

                logger.info(f"Situation scrapée avec succès: {scraping_task}")

            except BearerNotValid:
                logger.info(f"Le bearer n'est pas valide pour: {scraping_task}")
                self.bearer = self.token_getter.refresh_token()
                self.scraping_tasks.append(scraping_task)
                continue

            except Exception as e:
                logger.critical(f"Une erreur critique est survenue durant le scraping: {e}")
                break

        self.enregistreur.terminer_enregistrement()

