class BaseController:
    def __init__(self, scraper):
        self.scraper = scraper

    def run(self):
        self.scraper.scrape()
        
