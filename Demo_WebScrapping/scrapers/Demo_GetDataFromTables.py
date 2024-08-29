from Demo_WebScrapping.config.settings import GetDataFromTable_CONFIG
from Demo_WebScrapping.scrapers.Base_scraper import BaseScraper
import logging
import time

logger = logging.getLogger('django')  

class DemoFillFormScrapper(BaseScraper):
    def __init__(self):
        # self.driver = DriverSeleniumChrome(GetDataFromTable_CONFIG['TARGET_URL'])        
        super().__init__(GetDataFromTable_CONFIG)

    def scrape(self):
        self.driver.get(GetDataFromTable_CONFIG['TARGET_URL'])  
        
        self.next_page()
        
        time.sleep(3)
        
    def next_page(self):
        obj = self.driver.find_element_by_id_xpath('a','table_id_next')
        obj.click()      
        
