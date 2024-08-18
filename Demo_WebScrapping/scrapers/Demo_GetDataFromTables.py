from Demo_WebScrapping.utils.driver import DriverSeleniumChrome
from Demo_WebScrapping.config.settings import GetDataFromTable_CONFIG
from Demo_WebScrapping.scrapers.Base_scraper import BaseScraper
import datetime
import logging

logger = logging.getLogger('django')  

class DemoFillFormScrapper(BaseScraper):
    def __init__(self):
        # self.driver = DriverSeleniumChrome(GetDataFromTable_CONFIG['TARGET_URL'])        
        super().__init__(GetDataFromTable_CONFIG)

    def scrape(self):
        logger.debug(f"inicia self.driver.get { datetime.datetime.now()}")
        self.driver.get(GetDataFromTable_CONFIG['TARGET_URL'])  
        logger.debug(f"termina self.driver.get { datetime.datetime.now()}")        

        logger.debug(f"inicia self.close { datetime.datetime.now()}")
        logger.debug(f"termina self.close { datetime.datetime.now()}")
        
