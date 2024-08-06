from Demo_WebScrapping.utils.driver import DriverSeleniumChrome
from Demo_WebScrapping.config.settings import FillForm_CONFIG
from Demo_WebScrapping.scrapers.Base_scraper import BaseScraper

class DemoFillFormScrapper(BaseScraper):
    def __init__(self):
        self.driver = DriverSeleniumChrome(FillForm_CONFIG['TARGET_URL'])        
        super().__init__(FillForm_CONFIG)

    def scrape(self):
        self.driver.get(FillForm_CONFIG['TARGET_URL'])
        
        obj = self.driver.find_element_by_text_xpath('span','Account')
        obj.click()

        obj = self.driver.find_element_by_text_xpath('a','Register')
        obj.click()

        input = self.driver.find_element_by_id_xpath('input','firstname')
        input.send_keys('Leandro')

        input = self.driver.find_element_by_id_xpath('input','middlename')
        input.send_keys('Javier')

        input = self.driver.find_element_by_id_xpath('input','lastname')
        input.send_keys('Russo')

        input = self.driver.find_element_by_id_xpath('input','email_address')
        input.send_keys('russo_leandro28@hotmail.com')

        input = self.driver.find_element_by_id_xpath('input','password')
        input.send_keys('pass123')

        input = self.driver.find_element_by_id_xpath('input','confirmation')
        input.send_keys('pass123')

        obj = self.driver.find_element_by_id_xpath('input','is_subscribed')
        obj.click()

        obj = self.driver.find_element_by_text_xpath('span','Register')
        obj.click()

        self.close()
        
