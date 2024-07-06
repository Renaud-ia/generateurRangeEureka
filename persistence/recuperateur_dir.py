import copy
import os
import re

from .recuperateur import Recuperateur
from poker import SituationPoker, RangePoker, FormatPoker, InitialStacks, InitialSymmetricStacks, ActionPoker, Move


class RecuperateurDir(Recuperateur):
    dossier_global: str = "GTOWizard_Scraped_Ranges"

    def __init__(self, dossier_format: str, format_poker: FormatPoker):
        self.nom_dossier: str = dossier_format
        self.dossier_root: str = os.path.join(self.dossier_global, dossier_format)
        self.format_poker: FormatPoker = format_poker
        self.player_names = self._player_names(self.format_poker.n_joueurs)
        self.ranges_stockees: dict[SituationPoker, RangePoker] = self._extract_ranges()

    def get_ranges_enregistrees(self) -> dict[SituationPoker, RangePoker]:
        return self.ranges_stockees

    def get_format_poker(self) -> FormatPoker:
        return self.format_poker

    def _extract_ranges(self):
        player_last_actions: dict[str, SituationPoker] = {name: None for name in self.player_names}
        initial_stacks: InitialStacks = self._create_initial_stack()

        root_situation: SituationPoker = SituationPoker(initial_stacks)

        ranges: dict[SituationPoker, RangePoker] = {}

        return self._next_dir(ranges, player_last_actions, root_situation, self.dossier_root)

    def _next_dir(self,
                  ranges: dict[SituationPoker, RangePoker],
                  player_last_actions: dict[str, SituationPoker],
                  situation: SituationPoker,
                  dossier: str) -> dict[SituationPoker, RangePoker]:
        stack_depart: float = situation.initial_stacks.get_common_stack()

        self._add_ranges(ranges, dossier, player_last_actions)

        dossiers_players: list[str] = self._find_players(dossier)

        for dossier_player in dossiers_players:
            sous_dossier_player: str = os.path.join(dossier, dossier_player)
            actions_dossiers: list[str] = self._find_actions(sous_dossier_player)

            for dossier_action in actions_dossiers:
                sous_dossier_action: str = os.path.join(sous_dossier_player, dossier_action)
                action_poker: ActionPoker = self._convert_action(dossier_action, stack_depart)

                situation_action: SituationPoker = copy.deepcopy(situation)
                player_actions_copy: dict[str, SituationPoker] = copy.deepcopy(player_last_actions)
                self._remplir_actions(situation_action, player_actions_copy, action_poker, dossier_player)

                self._next_dir(ranges, player_actions_copy, situation_action, sous_dossier_action)

        return ranges

    def _add_ranges(self,
                    ranges: dict[SituationPoker, RangePoker],
                    dossier: str,
                    players_last_actions) -> None:
        for file in os.listdir(dossier):
            complet_path: str = os.path.join(dossier, file)
            if not os.path.isfile(complet_path):
                continue

            if not file.endswith(".txt"):
                print(f"Fichier non txt trouvé: {file}")

            nom_joueur: str = file[:-4]
            range_poker: RangePoker = self._convert_file_in_range(complet_path)

            situation: SituationPoker = players_last_actions[nom_joueur]

            ranges[situation] = range_poker

    @staticmethod
    def _convert_file_in_range(file: str) -> RangePoker:
        with open(file, 'r') as fichier:
            donnees = fichier.read()

        range_as_dict: dict[str, float] = {}
        paires = donnees.split(',')

        for paire in paires:
            cle, valeur = paire.split(':')
            range_as_dict[cle] = float(valeur)

        range_poker: RangePoker = RangePoker.from_dict(range_as_dict)

        return range_poker

    @staticmethod
    def _find_players(dossier: str) -> list[str]:
        dossiers: list[str] = []

        for directory in os.listdir(dossier):
            complet_path: str = os.path.join(dossier, directory)
            if os.path.isdir(complet_path):
                dossiers.append(directory)

        return dossiers

    @staticmethod
    def _find_actions(dossier: str) -> list[str]:
        dossiers: list[str] = []

        for directory in os.listdir(dossier):
            complet_path: str = os.path.join(dossier, directory)
            if os.path.isdir(complet_path):
                dossiers.append(directory)

        return dossiers

    @staticmethod
    def _convert_action(dossier_action: str, stack_depart: float):
        dossier_action = dossier_action.replace("/", "")
        if dossier_action == "call" or dossier_action == "check":
            return ActionPoker(Move.CALL)

        elif dossier_action == "allin":
            return ActionPoker(Move.RAISE_ALL_IN, stack_depart)

        elif dossier_action == "fold":
            return ActionPoker(Move.FOLD)

        try:
            amount_raise: float = float(dossier_action[:-2])
            return ActionPoker(Move.RAISE, amount_raise)

        except Exception as e:
            raise ValueError(f"Ce n'est pas un raise: {dossier_action}", e)

    def _remplir_actions(self,
                         situation_action: SituationPoker,
                         player_last_actions: dict[str, SituationPoker],
                         action_poker: ActionPoker,
                         nom_player: str):
        # on vérifie que tous les joueurs ont joué avant
        players_not_played: list[str] = [player for player in self.player_names
                                         if self.player_names.index(player) < self.player_names.index(nom_player)
                                         and player_last_actions[player] is None]
        # pour les joueurs situés avant qui n'ont pas joué, c'est un fold
        for player_before in players_not_played:
            action_fold: ActionPoker = ActionPoker(Move.FOLD)
            situation_action.ajouter_action(action_fold)
            situation_joueur: SituationPoker = copy.deepcopy(situation_action)
            player_last_actions[player_before] = situation_joueur

        situation_action.ajouter_action(action_poker)
        player_last_actions[nom_player] = situation_action

    @staticmethod
    def _player_names(n_joueurs: int):
        if n_joueurs == 6:
            return ["UTG", "HJ", "CO", "BTN", "SB", "BB"]

        raise ValueError(f"Nombre de joueurs non pris en charge: {n_joueurs}")

    def _create_initial_stack(self):
        pattern = r'\d+(?=bb)'
        resultat = re.search(pattern, self.nom_dossier)
        if resultat:
            return InitialSymmetricStacks(int(resultat.group(0)))

        raise ValueError(f"Stack non trouvé dans: {self.nom_dossier}")








