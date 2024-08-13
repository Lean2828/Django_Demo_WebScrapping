class BaseController:
    def __init__(self, scraper):
        self.scraper = scraper

    def run(self):
        with self.scraper as scraper:
            scraper.scrape()
        
