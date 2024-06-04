import logging
from typing import Optional

from .gtowizard import FormatGtoWizard, SituationPokerGtoWizard, ScrapingTaskGtoWizard, TokenManagerGtoWizard
from .scraping_exceptions import BearerNotValid

logger = logging.getLogger(__name__)


class ScraperGtoWizard:
    def __init__(self, format_a_scraper: FormatGtoWizard):
        self.format_gto_wizard = format_a_scraper
        self.scraping_tasks: list[ScrapingTaskGtoWizard] = []
        self.token_getter = TokenManagerGtoWizard()
        self.bearer = self.token_getter.get_token()

        self.initialiser_tasks()

    def initialiser_tasks(self):
        for stack in self.format_gto_wizard.possibles_stack_sizes():
            situation_initiale: SituationPokerGtoWizard = SituationPokerGtoWizard(stack)
            tache_initiale = ScrapingTaskGtoWizard(self.format_gto_wizard, situation_initiale)

            self.scraping_tasks.append(tache_initiale)

    def scrap(self):
        # TODO : vérifier qu'on a pas déjà fait cette tâche et marquer la tâche comme enregistrée à la fin
        while len(self.scraping_tasks) > 0:
            scraping_task = self.scraping_tasks.pop()

            try:
                self.scraping_tasks.extend(scraping_task.execute(self.bearer))

            except BearerNotValid:
                logger.info("Le bearer n'est pas valide")
                self.bearer = self.token_getter.refresh_token()
                self.scraping_tasks.append(scraping_task)
                continue

            except Exception as e:
                logger.critical("Une erreur critique est survenue durant le scraping", e)
                break
