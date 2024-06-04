class TokenManagerGtoWizard:
    def __init__(self):
        self.token: str = self._obtain_token()

    def get_token(self) -> str:
        return self.token

    def refresh_token(self):
        print("Le bearer doit être rafraichi")
        self.token = self._obtain_token()
        return self.token

    @staticmethod
    def _obtain_token():
        return input("Entrez un bearer pour le scraping")
