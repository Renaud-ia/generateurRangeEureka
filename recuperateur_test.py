from persistence.recuperateur_dir import RecuperateurDir
from scraping.gtowizard import BuilderFormatGtoWizard

dossier_format = "Cash6m50z50bbGeneral"
poker_format = BuilderFormatGtoWizard.from_str(dossier_format)

recuperateur = RecuperateurDir(dossier_format, poker_format)

ranges: dict = recuperateur.get_ranges_enregistrees()
print(f"Nombre de ranges : {len(ranges)}")

for situation, range in ranges.items():
    print(f"\n\n #######SITUATION: {situation}######")
    for combo, valeur in range.to_dict().items():
        print(f"{combo}:{valeur}")