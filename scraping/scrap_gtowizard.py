import logging
from typing import Optional

from .gtowizard.format_gto_wizard import FormatGtoWizard
from .gtowizard.situation_gto_wizard import SituationPokerGtoWizard
from .scraping_exceptions import BearerNotValid
from .gtowizard.scraping_task_gto_wizard import ScrapingTaskGtoWizard

logger = logging.getLogger(__name__)


class ScraperGtoWizard:
    def __init__(self, format_a_scraper: FormatGtoWizard, initial_bearer: Optional[str] = None):
        self.format_gto_wizard = format_a_scraper
        self.scraping_tasks: list[ScrapingTaskGtoWizard] = []
        self.bearer = initial_bearer

        self.initialiser_tasks()

    def initialiser_tasks(self):
        for stack in self.format_gto_wizard.possibles_stack_sizes():
            situation_initiale: SituationPokerGtoWizard = SituationPokerGtoWizard(stack)
            tache_initiale = ScrapingTaskGtoWizard(self.format_gto_wizard, situation_initiale)

            self.scraping_tasks.append(tache_initiale)

    def scrap(self):
        while len(self.scraping_tasks) > 0:
            scraping_task = self.scraping_tasks.pop()

            try:
                self.scraping_tasks.extend(scraping_task.execute(self.bearer))

            except BearerNotValid:
                logger.info("Le bearer n'est pas valide")
                print("Le bearer n'est pas valide")
                self.bearer = self.ask_bearer()
                self.scraping_tasks.append(scraping_task)
                continue

            except Exception as e:
                logger.critical("Une erreur critique est survenue durant le scraping", e)
                break

    @staticmethod
    def ask_bearer() -> str:
        return input("Entrez un bearer pour le scraping")
