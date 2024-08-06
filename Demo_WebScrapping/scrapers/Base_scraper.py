from Demo_WebScrapping.utils.driver import  DriverSeleniumChrome

class BaseScraper:
    def __init__(self, config):
        self.config = config
        self.driver = DriverSeleniumChrome()

    def scrape(self):
        raise NotImplementedError("Scrape method must be implemented by subclasses")

    def get_data(self, url):
        return self.driver.get(url)
        return self.driver.get_page_source()

    def close(self):
        self.driver.quit()
