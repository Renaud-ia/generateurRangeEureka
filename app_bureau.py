from scraping import ScraperGtoWizard
from scraping.gtowizard import BuilderFormatGtoWizard, FormatGtoWizard

if __name__ == "__main__":
    formats_a_scraper: list[FormatGtoWizard] = BuilderFormatGtoWizard.generate_all_formats()
    for format_en_cours in formats_a_scraper:
        scraper: ScraperGtoWizard = ScraperGtoWizard(format_en_cours)
        scraper.scrap()
