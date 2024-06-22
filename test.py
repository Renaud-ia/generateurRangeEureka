from persistence import Recuperateur, GestionnairePersistence
from poker import RangePoker

gen_data: list[Recuperateur] = []
gen_data.extend(GestionnairePersistence.recuperer_enregistreurs_json())
gen_data.extend(GestionnairePersistence.recuperer_enregistreurs_externe())

data_training: list[RangePoker] = []

for recuperateur in gen_data:
    print(f"RECUPERATION DU FORMAT: {recuperateur.get_format_poker()}")

    ranges: dict = recuperateur.get_ranges_enregistrees()
    print(f"NOMBRE DE RANGES: {len(ranges)}")

    max_index = 10

    index = 0

    for situation, range in ranges.items():
        if index > max_index:
            break
        index += 1

        print(situation)
        print(range)
        print(range.generer_input())