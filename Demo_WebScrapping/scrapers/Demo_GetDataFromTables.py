from Demo_WebScrapping.utils.driver import DriverSeleniumChrome
from Demo_WebScrapping.config.settings import GetDataFromTable_CONFIG
from Demo_WebScrapping.scrapers.Base_scraper import BaseScraper

class DemoFillFormScrapper(BaseScraper):
    def __init__(self):
        self.driver = DriverSeleniumChrome(GetDataFromTable_CONFIG['TARGET_URL'])        
        super().__init__(GetDataFromTable_CONFIG)

    def scrape(self):
        self.driver.get(GetDataFromTable_CONFIG['TARGET_URL'])  
              
        self.close()
        
